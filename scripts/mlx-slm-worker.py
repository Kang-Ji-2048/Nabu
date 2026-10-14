"""MLX CLI entry point with explicit Qwen non-thinking chat rendering."""
from functools import partial
from mlx_lm import lora

_original_load = lora.load


def load_non_thinking(*args, **kwargs):
    model, tokenizer = _original_load(*args, **kwargs)
    # Preserve the checkpoint template and pass its documented mode switch.
    tokenizer.apply_chat_template = partial(tokenizer.apply_chat_template, enable_thinking=False)
    return model, tokenizer


if __name__ == '__main__':
    lora.load = load_non_thinking
    lora.main()
