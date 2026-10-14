"""Pinned public ONNX model download, then local-only embedding inference."""
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
from urllib.request import urlopen


MODEL = "BAAI/bge-small-en-v1.5"
REPOSITORY = "Qdrant/bge-small-en-v1.5-onnx-Q"
REVISION = "aa8f8b060edb00e03bfdd08813a2949946c8ba55"
ASSETS = ("config.json", "model_optimized.onnx", "ort_config.json", "special_tokens_map.json", "tokenizer.json", "tokenizer_config.json", "vocab.txt")
DEFAULT_MODEL_DIR = Path("data/models/bge-small-en-v1.5")


def file_hash(path, algorithm="sha256", prefix=b""):
    result = hashlib.new(algorithm)
    result.update(prefix)
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def prepare_model(directory: Path):
    if os.name == "nt":
        shell = shutil.which("pwsh")
        if shell is None:
            raise ValueError("Model preparation on Windows requires PowerShell 7 (pwsh)")
        result = subprocess.run([shell, "-NoProfile", "-File", str(Path(__file__).with_name("fetch_model.ps1")),
                                 "-ModelDirectory", str(directory.resolve())], capture_output=True, text=True,
                                encoding="utf-8", creationflags=subprocess.CREATE_NO_WINDOW)
        if result.returncode:
            raise ValueError("Model download failed: " + result.stderr[-1500:])
        return json.loads(result.stdout.lstrip("\ufeff"))
    directory.mkdir(parents=True, exist_ok=True)
    url = f"https://huggingface.co/api/models/{REPOSITORY}/revision/{REVISION}?blobs=true"
    with urlopen(url, timeout=60) as response:
        metadata = json.load(response)
    if metadata["sha"] != REVISION:
        raise ValueError("Unexpected model revision")
    entries = {entry["rfilename"]: entry for entry in metadata["siblings"]}
    hashes = {}
    for filename in ASSETS:
        entry = entries[filename]
        target = directory / filename
        if not target.exists():
            partial = target.with_suffix(target.suffix + ".partial")
            with urlopen(f"https://huggingface.co/{REPOSITORY}/resolve/{REVISION}/{filename}", timeout=120) as response, partial.open("wb") as stream:
                shutil.copyfileobj(response, stream, 1024 * 1024)
            if partial.stat().st_size != entry["size"]:
                raise ValueError(f"Download size mismatch: {filename}")
            partial.rename(target)
        if target.stat().st_size != entry["size"]:
            raise ValueError(f"Asset size mismatch: {filename}")
        if "lfs" in entry:
            expected, actual = entry["lfs"]["sha256"], file_hash(target)
        else:
            expected = entry["blobId"]
            actual = file_hash(target, "sha1", f"blob {entry['size']}\0".encode())
        if actual != expected:
            raise ValueError(f"Asset checksum mismatch: {filename}")
        hashes[filename] = file_hash(target)
    manifest = {"model": MODEL, "repository": REPOSITORY, "revision": REVISION, "assets": hashes}
    (directory / "nabu-model.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {"model": MODEL, "revision": REVISION, "model_dir": str(directory.resolve()), "verified_assets": len(hashes)}


class LocalEncoder:
    def __init__(self, directory=DEFAULT_MODEL_DIR):
        directory = Path(directory).resolve()
        manifest_path = directory / "nabu-model.json"
        if not manifest_path.exists():
            raise ValueError("Embedding model is not prepared; run: python -m nabu prepare-model")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("model") != MODEL or manifest.get("revision") != REVISION or set(manifest.get("assets", {})) != set(ASSETS):
            raise ValueError("Unsupported embedding model manifest")
        for filename, expected in manifest["assets"].items():
            if file_hash(directory / filename) != expected:
                raise ValueError(f"Embedding asset changed: {filename}")
        backend_version = importlib.metadata.version("fastembed")
        runtime_version = importlib.metadata.version("onnxruntime")
        tokenizer_version = importlib.metadata.version("tokenizers")
        fingerprint = hashlib.sha256(json.dumps({**manifest, "backend_version": backend_version,
            "runtime_version": runtime_version, "tokenizer_version": tokenizer_version}, sort_keys=True).encode()).hexdigest()
        self.fingerprint = fingerprint
        self.metadata = {"model": MODEL, "revision": REVISION, "fingerprint": fingerprint,
                         "backend": "fastembed", "backend_version": backend_version,
                         "runtime_version": runtime_version,
                         "tokenizer_version": tokenizer_version,
                         "model_dir": str(directory), "max_input_tokens": 512}
        from fastembed import TextEmbedding
        self.model = TextEmbedding(model_name=MODEL, specific_model_path=str(directory),
                                   cache_dir=str(directory / "runtime-cache"),
                                   local_files_only=True, providers=["CPUExecutionProvider"], threads=2)

    def documents(self, texts):
        return list(self.model.embed(texts, batch_size=32))

    def query(self, text):
        return list(self.model.query_embed(text))
