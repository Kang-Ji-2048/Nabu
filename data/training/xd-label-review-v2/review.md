# Version 2 label review

**60 candidate targets: 3 supported-risk candidates and 57 no-risk candidates. All are generated_unreviewed; none are human approved.**

Prepared development data: 58 train, 2 validation; latest 742 tickets remain held out. Maximum complete chat sequence: 6547 / 8192 tokens. Schema, exact citations and manifest input hashes pass.

The new version excludes 70 quarantined child identities. The absent XD-3272/Jira64868 endpoint is explicitly proven outside the imported/raw identity universe; unknown child scope was not invented. Default preparation policy remains strict. Frozen original candidates and audits were preserved.

Validation contains no positive risks and cannot assess recall. Review is required for both positives and no-risk targets; no-risk means insufficient supported evidence, not verified safety.

## Positive candidates

### XD-1260 (train)

```json
{
  "risks": [
    {
      "id": "XD-1260-partition-step-history",
      "risk_type": "validation_gap",
      "claim": "The planned partitioned jobs may run while their persisted step history cannot be listed if null StepExecution IDs are stored in the shared job repository.",
      "rationale": "XD-1127 introduces partitioning across XD nodes and XD-1146 wires partitioners and StepExecutionHandlers through the MessageBus. XD-1206 reports partitioned jobs storing null StepExecution IDs, causing the listing test and HATEOAS assembler to fail again after another partitioned run; it is To Do at the cutoff. XD-703 explicitly requires a persistent repository shared across jobs, linking the failed persistence/listing behavior to the planned distributed executions. The cause of the null IDs is unknown and is not attributed to MessageBus wiring or job-name registration.",
      "suggested_action": "Investigate XD-1206 in the planned partitioned execution path, retain the repository across repeated multi-node runs, and verify non-null persisted StepExecution IDs and successful REST/CLI step listing. Confirm whether existing members already own the fix and these checks.",
      "target_item_ids": [
        "tawos-v1.1:2680",
        "tawos-v1.1:2661"
      ],
      "citations": [
        {
          "item_id": "tawos-v1.1:2601",
          "field": "description",
          "quote": "For some reason, the partitioned batch jobs are storing  {{StepExecutions}}s in the DB with a null ID."
        },
        {
          "item_id": "tawos-v1.1:3097",
          "field": "description",
          "quote": "A single job repository that is backed by a file need to be shared across all jobs that are a launched."
        }
      ],
      "severity": "medium"
    }
  ],
  "limitations": [
    "XD-1206 does not establish why StepExecution IDs are null or whether a particular planned member already fixes that behavior.",
    "XD-1146 and XD-703 are Done; the risk concerns the explicit partitioned persistence/listing failure, not absent MessageBus or repository implementation. Unknown other member text prevents declaring validation work missing.",
    "Severity remains provisional without company impact criteria."
  ]
}
```

Supplied source: [XD-1260 input](/Users/phoebe/Nabu/data/training/xd-development-v2/train-drafts.jsonl:19)

### XD-1317 (train)

```json
{
  "risks": [
    {
      "id": "yarn-admin-database-readiness",
      "risk_type": "dependency_gap",
      "claim": "If YARN starts XD containers before the admin server has initialized the shared batch database, container startup may fail when the job-execution DAO connects.",
      "rationale": "The plan explicitly introduces YARN Client/AppMaster implementations and deployment scripts. XD-1318 documents this exact startup-order failure, and XD-703 independently specifies that the admin creates the shared repository schema. These establish a concrete runtime readiness condition for deployment, rather than a risk inferred from topic similarity. Both prior tickets are marked Done, so recurrence and an actual omission in the new scripts are not established.",
      "suggested_action": "Verify that the YARN AppMaster and deployment scripts preserve admin/database readiness before container DAO initialization, or that the existing fix makes startup order safe; exercise a container-first launch.",
      "target_item_ids": [
        "tawos-v1.1:2486",
        "tawos-v1.1:2485"
      ],
      "citations": [
        {
          "item_id": "tawos-v1.1:2489",
          "field": "description",
          "quote": "During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes)."
        },
        {
          "item_id": "tawos-v1.1:3097",
          "field": "description",
          "quote": "The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up"
        }
      ],
      "severity": "medium"
    }
  ],
  "limitations": [
    "XD-1318 and XD-703 are marked Done; their text establishes the historical startup mechanism but does not show that it recurs in the YARN implementation.",
    "XD-1314 has unknown title/description, and the visible YARN tasks do not specify launch readiness behavior; no missing implementation is asserted.",
    "Severity is provisional because company impact thresholds and deployment acceptance criteria were not supplied."
  ]
}
```

Supplied source: [XD-1317 input](/Users/phoebe/Nabu/data/training/xd-development-v2/train-drafts.jsonl:22)

### XD-1605 (train)

```json
{
  "risks": [
    {
      "id": "XD-1605-management-jolokia-access",
      "risk_type": "validation_gap",
      "claim": "The planned management/jolokia migration may leave monitoring inaccessible if the reported management-context access exception in XD-1496 still applies to that route.",
      "rationale": "XD-1497 explicitly moves JMX endpoints from /jolokia to management/jolokia. The supplied XD-1496 title reports an exception when accessing Jolokia via the management context path and is To Do, giving a direct planned-route failure to investigate. XD-1396 independently records container startup failure with JMX and management_port enabled, explicitly including endpoints_jolokia_enabled=true in its reproduction configuration. That completed incident establishes that access to this context also depends on successful configuration/lifecycle initialization; it is not asserted to recur or share XD-1496’s unknown cause.",
      "suggested_action": "Investigate the cutoff-visible XD-1496 management-path exception as part of XD-1497, and verify an actual request to the migrated Jolokia route after successful startup in the intended management configuration. Confirm the completed XD-1396 fix remains applicable if a separate management port is used.",
      "target_item_ids": [
        "tawos-v1.1:2310"
      ],
      "citations": [
        {
          "item_id": "tawos-v1.1:2311",
          "field": "title",
          "quote": "Exception thrown when accessing Jolokia via the management context path"
        },
        {
          "item_id": "tawos-v1.1:2411",
          "field": "description",
          "quote": "The container will not start with JMX enabled and the management_port set."
        }
      ],
      "severity": "medium"
    }
  ],
  "limitations": [
    "XD-1496 has no known description; its exact reproduction, cause and applicability to the new route require review.",
    "XD-1396 is Done and XD-1280 also records completed version-specific access work. No regression of those fixes or missing tests is asserted. Unknown members may already own the relevant access check.",
    "A separate management port is not explicitly selected in the plan, so no startup failure in that configuration is predicted. Severity is provisional without company policy."
  ]
}
```

Supplied source: [XD-1605 input](/Users/phoebe/Nabu/data/training/xd-development-v2/train-drafts.jsonl:27)

## Changed-evidence reassessment

| Case | Decision | Explanation |
| --- | --- | --- |
| XD-177 | revise | No supported risk: XD-180/XD-181 explicitly cover protocol selection and launcher imports. Done shutdown histories and unrelated placeholder, observability and Windows packaging requirements do not establish a two-ticket protocol-change failure mechanism. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-238 | retain | Retain no-risk target: packaging consistency and profile deployment are explicit; requirements/configuration examples do not supply two comparable failures. Unreviewed assistant candidate; no human approval is asserted. |
| XD-697 | retain | No supported risk: isolation/cross-transport testing and payload/content-type checks are explicit. XD-614/XD-689 strengthen the relevance of planned checks. XD-467/XD-476 support lifecycle review questions but the supplied test design does not exclude failure/retry or destroy/recreate paths. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-706 | retain | Retain no-risk target: supplied configuration and MBean incidents are addressed by observed scope; unknown transport-combination details cannot establish a gap. Unreviewed assistant candidate; no human approval is asserted. |
| XD-742 | retain | No supported risk: preservation of imported job reporting API style and dependency versions are explicit. XD-555 concerns a different response resource; XD-556 depends on a cross-origin deployment absent from supplied scope. These Done incidents and unrelated lifecycle histories do not establish a reporting-controller gap. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-895 | revise | Retain the no-risk outcome but revise limitations to remove a legacy reference absent from supplied evidence and assess XD-614/XD-827 conversion counterevidence. Unreviewed assistant candidate; no human approval is asserted. |
| XD-1267 | retain | No supported risk: XD-1045 explicitly covers a common client/server model project. XD-1198/XD-465 concern shell parsing/error display, while XD-1023 concerns deployment dispatch. No affected shared-model classes or incompatible wire-format change is supplied. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-1275 | retain | Retain no-risk target: old/new layout compatibility and packaging requirements do not establish failure of the small path change; DSL naming collision is a different mechanism. Unreviewed assistant candidate; no human approval is asserted. |
| XD-1317 | retain | Independent positive review retains the conditional dependency risk. YARN Client/AppMaster and deployment scripts control startup; XD-1318 directly documents container DAO initialization connecting to the admin-initialized database, and XD-703 independently specifies admin schema creation. Both are Done, so this is a readiness condition to verify, not an assertion of an unfixed defect or omitted implementation. Other histories do not justify additional risks. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-1473 | revise | Retain the no-risk outcome but revise limitations to remove an absent legacy incident and reassess the supplied classloader, initialization and ZooKeeper configuration evidence. Unreviewed assistant candidate; no human approval is asserted. |
| XD-1606 | revise | Retain no risks and revise a legacy limitation naming absent evidence. XD-1601 describes naming inconsistency and working aliases without a proposed breaking contract. Completed XD-1177/XD-810 concern module-label ambiguity/shared-channel teardown; supplied plan text does not establish removal of their protections. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-1607 | revise | Retain the no-risk outcome but revise limitations: differing lifecycle mechanisms and explicit stream-state scope are the reason for abstention; Done statuses do not establish successful fixes. Unreviewed assistant candidate; no human approval is asserted. |
| XD-1608 | revise | Retain no risks and revise a legacy limitation naming absent evidence. XD-1002 covers execution navigation and XD-1507 explicitly addresses undeployed-job submission. XD-1000/XD-1001/XD-1003, XD-703 and XD-817 explain existing UI/backend contracts but do not establish an uncovered new failure. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-1609 | retain | Retain no-risk target: external transport configuration and enum removal are explicit; database startup and Hadoop loading incidents do not establish two comparable transport-setting failures. Unreviewed assistant candidate; no human approval is asserted. |
| XD-1821 | reject | Independent positive review rejects the legacy risk: its tap-failure citation is absent from the new supplied input. XD-1601 supplies prefix identity rules and says both aliases work; XD-705 supplies job control-channel requirements but no independent prefix/tap failure. XD-1738 concerns deletion after module files are removed, a different mechanism. Combining these would infer risk from topic similarity. Parser separation and source/sink metadata are already explicit. Unreviewed assistant-generated candidate; no human approval is asserted. |
| XD-2134 | revise | Retain the no-risk outcome but revise limitations to remove an absent legacy incident and reassess supplied channel-resolution evidence against explicit error-routing scope. Unreviewed assistant candidate; no human approval is asserted. |
| XD-2978 | retain | Independent validation review retains no risks. XD-2979 explicitly includes remaining refactoring, documentation and CF incubation. XD-2916 supplies one directly relevant completed Receptor client implementation; remaining REST/security/module/Hadoop histories do not establish a second comparable Receptor or incubation failure mechanism. Unreviewed assistant-generated candidate; no human approval is asserted. |

## Review every target

Two full inputs are exact matches; 41 changes affect coverage metadata only, with identical supplied plan/prior text and allowed risk types. Those targets were explicitly reassessed against unchanged evidence rather than silently marked unchanged. Seventeen cases have changed supplied prior evidence and received fresh assistant review.

### XD-75 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:1)

- The redis packaging plan has no recoverable description, so runtime prerequisites and acceptance criteria cannot be compared with prior work.
- XD-41 concerns unavailable Redis in tests and XD-61 discusses bundling Redis, but these do not establish two independent historical examples of a delivery failure in adding Redis to a distribution.
- XD-76 is an analogous packaging task; the other Redis service titles do not demonstrate an omitted requirement or failure mechanism.

### XD-92 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:2)

- The supplied root has unknown title, description, type and estimate, and no observed members; there is no recoverable requirement to assess.
- No prior tickets were supplied. The historical To Do status alone cannot establish scope, dependency or validation risk.

### XD-177 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:3)

- XD-177 and eight of ten supplied members lack known title/description scope; statuses alone do not establish a delivery risk.
- XD-180 and XD-181 already specify protocol selection and launcher imports, including naming conventions and extensibility.
- XD-107 and XD-124 are Done Redis shutdown work. XD-142 concerns placeholder/FactoryBean initialization and XD-151 Windows Redis binaries; neither supplies a second directly applicable protocol-selection failure mechanism.

Review questions:
- What readiness/configuration checks exist for the pipeProtocol-selected infrastructure in XD-180/XD-181?

### XD-238 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:4)

- The root explicitly requires shipped and user-contributed modules to share packaging, while XD-132 explicitly covers deployment profiles; neither is an established missing-work gap.
- XD-245 supplies XML/custom-code and regular/Hadoop-job acceptance requirements, not evidence that this packaging strategy fails; the other retrieved configuration and documentation tasks do not independently establish such a failure.
- XD-194 has no recoverable title or description, so the visible two-member plan cannot establish the complete intended packaging scope.

Review questions:
- Does the supplied packaging requirement and XD-132 profile scope support any concrete two-ticket failure mechanism, rather than an inference from the unknown XD-194 text?

### XD-240 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:5)

- Title, description, type and estimate are unknown for the supplied root, with no observed child tickets.
- No prior evidence was retrieved. To Do status and missing historical fields are insufficient to support any allowed risk type.

### XD-241 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:6)

- The supplied plan explicitly includes XD-162 message conversion; its description and the root description are unknown, so further distribution requirements cannot be inferred from this excerpt.
- XD-164 requests channel declaration validation, but no second supplied ticket establishes the same failure mechanism. Completed architecture and module guides are scope precedents rather than evidence of a delivery risk.
- XD-180 and XD-181 already describe completed protocol and launcher support; their relationship to distribution does not establish an unresolved dependency or an omission in XD-241.

### XD-395 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:7)

- The root and most observed members have unknown titles and descriptions, and seven members are omitted from the supplied plan. The visible HTTP and Twitter section tasks already request conversion from curl to Shell commands.
- XD-223 and XD-202 document Twitter API retirement, but the supplied plan does not identify a Twitter-search example or an API version that remains incompatible; topical overlap cannot establish that this documentation change misses required work.
- Other prior tickets describe completed documentation and configuration work, not two comparable failures tied to the visible section edits.

### XD-468 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:8)

- The root and seven observed children lack recoverable title and description. The known work includes Hadoop-distribution startup selection (XD-473), Avro sink investigation (XD-475), and a Twitter-to-HDFS/HAWQ design document (XD-388).
- XD-207 identifies previously hardcoded HDFS configuration and XD-181 describes protocol-specific launcher imports, but these do not demonstrate an unresolved gap in the supplied distribution-selection task.
- XD-279 discusses LZO licensing and file-container choices, not an established Avro failure. Unknown child content prevents treating these topics as omitted requirements.

### XD-484 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:9)

- The only visible member, XD-485, explicitly plans use of Spring Shell testing facilities; it contradicts a blanket claim that shell testing work is absent.
- XD-122 describes an actual Spring Integration script/version mismatch, but the other supplied tickets do not establish a second comparable Spring Shell testing-facility failure.
- The root has no known title or description, and XD-485 has no known description, so the intended framework migration or test coverage cannot be inferred.

### XD-527 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:10)

- XD-527 and XD-528 through XD-530 have unknown historical titles and descriptions. The only known member title, XD-531, explicitly schedules a syslog-tcp-reactor integration test.
- XD-127, XD-128, XD-140 and XD-26 describe completed TCP, syslog configuration and performance work; they do not show two failures in the planned Reactor module.
- XD-10 concerns Reactor HTTP ingestion, while XD-198 describes an apparently benign transformer logging issue. Neither establishes a specific unmet requirement or failing dependency in this supplied plan.

### XD-697 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:11)

- The root explicitly includes isolation and cross-transport stream testing; XD-304 and XD-306 specify message/content-type assertions but do not restrict all tests to successful flows.
- XD-467 supplies an unresolved failed-create/retry mechanism and XD-476 supplies a completed Redis destroy/recreate fault, but no supplied plan text shows that the new test design excludes or mishandles either lifecycle.
- XD-203 and other child text is unknown, so lifecycle coverage remains an unresolved review question rather than a supported missing-work risk.

Review questions:
- Does the test framework exercise failed creation followed by corrected retry and destroy/recreate across transports, as described by XD-467/XD-476?

### XD-706 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:12)

- XD-645 identifies Redis/Rabbit property-loading conflicts and XD-544 identifies duplicate analytics repositories, but plan member XD-353 already requires separate Admin/Container contexts, shared parent beans and unit tests for correct implementations and redundant instances. Those incidents therefore do not establish omitted configuration or validation work.
- XD-711 explicitly removes the MBeanServer from module-common configuration, addressing the same broad isolation concern raised by the supplied duplicate-MBean error in XD-465.
- Unknown root text and several unknown member descriptions leave the intended breadth of transport-combination testing unverified; this is an evidence limitation rather than a demonstrated validation gap.

Review questions:
- Does any supplied incident identify an uncovered mechanism beyond the explicit XD-353 configuration tests and XD-711 MBean isolation work?

### XD-742 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:13)

- XD-555 concerns StreamDefinitionResource XML marshalling; the imported job-controller response types and representation mappings are not supplied, so applicability is unverified.
- XD-556 concerns a cross-origin Kodiak deployment, but no deployment origin for the intended UI is supplied. Both cited incidents are Done at this cutoff.
- Unknown XD-743/XD-745 text and the missing endpoint attachment do not establish that compatibility checks are omitted.

Review questions:
- What imported job response types and browser origin are intended, and are their representation/origin contracts already tested?

### XD-895 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:14)

- XD-896 explicitly proposes configurable message conversion using media types or Java class names; the root and XD-825/XD-861 have no known scope text, so their acceptance coverage cannot be established.
- XD-306 lists format-testing ideas without a demonstrated failure. XD-555 concerns REST response marshalling; XD-465 and XD-467 concern shell error display and failed-tap lifecycle/JMX cleanup. These do not jointly establish a failure of the planned configurable data channels.
- XD-614 explicitly describes preserving content-type information across transport serialization and XD-827 describes a twittersearch JSON/POJO output parameter. Their supplied Done statuses and stated capabilities are counterevidence to simply claiming conversion support is absent, but do not prove this new configuration work is validated.

Review questions:
- Can a comparable conversion failure be established from the supplied data-channel evidence, rather than REST marshalling or tap cleanup incidents?

### XD-965 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:15)

- XD-621 already proposes a default Hadoop NameNode and asks about persistence; unknown requirements prevent interpreting its open question as a missing dependency or validation task.
- XD-207 describes configurable HDFS sink properties and XD-245 describes Hadoop batch-job support, but neither establishes two comparable failures caused by the proposed shell NameNode default.
- Most root/member text is unrecoverable, while the other supplied incidents concern job repositories, module naming and Rabbit queue crosstalk without a demonstrated connection to the visible banner and NameNode work.

### XD-1257 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:16)

- The observed plan already includes stopping previous EC2 deployments, shutdown success/failure artifacts, deployment URL artifacts, single-node acceptance tests, a Rabbit distributed stage and a round-trip result-checking application. None can be labelled missing.
- XD-969, XD-970 and XD-972 describe provisioning/port checks, deployment verification and cleanup, and are Done; these are existing safeguards rather than evidence of an unresolved EC2 CI failure.
- The unknown root, XD-1241 and XD-1263 leave some scope unrecoverable, but the other classloading/job/routing examples do not establish two supported failures of this CI plan.

### XD-1258 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:17)

- The root and all three supplied members have unknown titles and descriptions; statuses and the single recoverable estimate do not identify a delivery failure mechanism.
- No prior tickets were supplied, so no risk can satisfy the required two independent historical citations.

### XD-1259 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:18)

- The visible children create single-node Hadoop AMIs for four named distributions; the root and each installation specification are unknown. It is not established that these images bundle XD or share its classpath.
- XD-634 documents an XD/Guava mismatch for Hadoop 2.0.5 and Pivotal HD 1.0, while XD-472 calls for distribution-specific transitive dependencies. These establish conditional integration concerns, not an actual dependency gap in the listed Hadoop-only image tasks or their different versions.
- XD-1041 and XD-978 explicitly require runtime checks in other work. Their testing requirements do not prove those checks are missing here; no sufficiently grounded two-ticket mechanism applies to the recoverable AMI scope.

### XD-1260 — risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:19)

Review questions:
- Assess severity and company-specific impact for the supported conditional risk.

### XD-1267 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:20)

- XD-1045 explicitly creates a model project common to client and server; sharing model work is already part of the visible plan.
- XD-1198 documents whitespace-sensitive shell parameter parsing and XD-465 documents lost server error detail, but neither shows a defect in the shared model project or a proposed incompatible API change. Both are Done.
- The root has no known title/description and XD-1045 has no known description, so affected classes, wire formats and compatibility promises cannot be established.

Review questions:
- Which common client/server model classes and serialization contracts are moved, and does this change behavior or only packaging?

### XD-1275 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:21)

- The root and XD-783 have unknown title and description. The only recoverable task, XD-780, removes duplicated module-name location usage.
- XD-238 explicitly requires simultaneous support for old and new module layouts, and XD-841 describes simplifying custom-module packaging. Neither establishes that this small path change violates compatibility or omits dependency packaging.
- XD-702 concerns a DSL stream/module name collision, not duplicated filesystem path segments. Combining it with module-layout work would conflate different mechanisms.

Review questions:
- Does the module path change have two comparable supplied incidents establishing a compatibility gap, rather than a DSL naming collision?

### XD-1317 — risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:22)

Review questions:
- Does the Done XD-1318 fix permit container-first YARN startup, or do the AppMaster/scripts enforce admin database readiness?

### XD-1391 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:23)

- The visible work is an Angular MVC spike, with no recoverable description defining release or test acceptance criteria. Missing production checks cannot be inferred from a prototype title.
- XD-1229 explicitly supplies Angular build and test automation, while XD-1316 records one E2E tooling warning; together they do not demonstrate two independent unresolved failures in the planned MVC spike.
- The Rabbit outputType, JMX conversion and Homebrew failures concern backend deployment paths, with no supplied evidence connecting them to this UI design-mapping work.

### XD-1392 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:24)

- XD-1126 specifies a property-name migration but provides no known description of aliases, binding changes or property-source precedence.
- The actual YAML-shadowing and command-line-default override defects in XD-1186 and XD-1194 are Done; the supplied plan does not establish that naming changes retain or reintroduce their mechanisms.
- The root and five other members have no known requirements, so the proposed restriction to name-only validation cannot be inferred.

### XD-1405 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:25)

- Neither XD-1405 nor its observed member XD-1406 has a recoverable title or description at the cutoff, so the proposed work cannot be characterized.
- No prior tickets are supplied; no risk can satisfy the required two distinct historical evidence citations. This is insufficient evidence, not a finding that the plan is safe.

### XD-1473 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:26)

- The plan already includes parser/descriptor refactoring in XD-1474, runtime documentation in XD-1476, repository consolidation in XD-1477 and module identity changes in XD-1480; those tasks must not be labelled missing.
- XD-1474 is truncated and XD-1475/XD-1478/XD-1479 have unknown scope text, so complete compatibility or validation coverage cannot be established from the supplied input.
- XD-716 reports Netty/Lettuce initialization blocking; XD-718 describes module classloader precedence. Neither provides a second comparable incident establishing a failure mechanism in the planned parser or ZooKeeper repository consolidation.
- XD-1393 describes explicit ZooKeeper client connect-string support and is supplied as Done. It is counterevidence to claiming that capability is absent, while its truncated description and status do not prove the new runtime changes are safe.

Review questions:
- Does the supplied parser/repository consolidation evidence establish a comparable failure mechanism beyond the planned refactoring?

### XD-1605 — risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:27)

Review questions:
- Assess severity and company-specific impact for the supported conditional risk.

### XD-1606 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:28)

- XD-1601 describes distinct job/named-channel identities and explicitly says both job aliases work; its truncated description does not establish alias removal or a failing deployment.
- XD-1177 specifies completed repeated-module/label disambiguation and XD-810 describes completed shared-channel teardown work. The plan does not establish a change that defeats those protections.
- XD-1606 and XD-1522 have unknown title/description, so the final naming contract and compatibility checks cannot be determined.

Review questions:
- Does the intended change only document existing aliases, or alter broker identities and named-channel resolution?

### XD-1607 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:29)

- XD-1270 explicitly distinguishes deploying, deployed and failed states, retains successfully deployed modules after partial failure, identifies failed modules and requires undeploy to stop all modules. Claiming that partial-failure handling or cleanup is absent would contradict the supplied plan.
- XD-1291 describes shutdown ordering between connection factories and ModuleDeployer; XD-1452 describes HTTP module thread leaks during create/use/undeploy. These show lifecycle failures, but their differing mechanisms do not establish a gap in the stated stream-state transition work. Their Done statuses alone do not establish successful fixes.
- XD-1270 explicitly leaves per-module state storage TBD and partial redeployment uncertain. The root and XD-1416 have unknown scope text. These uncertainties limit assessment but do not supply two-ticket evidence of an uncovered scope, dependency or validation failure.

Review questions:
- Do the shutdown-order and HTTP thread-leak reports support an uncovered stream-state mechanism despite the explicit undeploy and partial-failure semantics?

### XD-1608 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:30)

- XD-1002 explicitly covers deployed-job execution navigation and return navigation; XD-1507 explicitly identifies submission of undeployed jobs through the Admin UI.
- XD-703 specifies shared job-state persistence and XD-817 specifies last-execution fields on job listings. These backend requirements do not establish an uncovered navigation or state-validation failure.
- The root and XD-1004/XD-1006/XD-1007 lack known scope text. Completed XD-1000/XD-1001/XD-1003 describe definitions, deployments and launches but do not demonstrate a new missing-work mechanism.

Review questions:
- Which job definition/deployment/execution states and failure cases are covered by XD-1507 and navigation work?

### XD-1609 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:31)

- XD-1592 explicitly supplies extensible transport configuration and is Done at this cutoff. XD-1350 and XD-1336 also describe completed enum-removal work, contradicting a warning that extensibility is simply missing.
- The root and XD-1593 have no recoverable scope text; XD-1596 lists acknowledgement, transaction size, prefetch and concurrency without identifying the required semantics. This incompleteness is not itself a risk.
- XD-1356 documents Hadoop class/namespace loading errors and XD-1318 documents batch database startup order. The supplied sample does not connect two demonstrated failures to these particular transport settings or external transport jars.

Review questions:
- Does supplied evidence show a specific transport-setting or external-jar failure beyond the explicit extensibility work?

### XD-1647 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:32)

- The root explicitly promises test coverage for all batch jobs and source/sink/processors, so testing coverage cannot be labelled absent merely because no members are observed.
- The referenced test matrix is not supplied; the evidence cannot establish which scenarios or transport combinations it includes.
- XD-1066 documents a real cross-transport broadcasting failure, while XD-1082, XD-1083 and XD-1086 explicitly require controller tests; these Done examples suggest checks but do not demonstrate that the proposed matrix omits them.

### XD-1688 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:33)

- The only identifiable plan topics are ELK log analysis and Stream-lib analytics operators; neither has a recoverable description establishing interfaces, supported transports or acceptance criteria.
- XD-1066 documents topic-channel broadcasting failures and XD-1308 describes transform fallback behavior, but the supplied plan does not show that the proposed operators use those mechanisms. Their shared analytics/logging vocabulary is insufficient support.
- XD-1245 and XD-719 demonstrate existing acceptance-test and packaging checks, so their existence cannot establish that this plan omits validation.

### XD-1694 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:34)

- XD-1695 explicitly includes optional REST endpoint authentication and authorization using Spring Security; claiming endpoint security is absent would contradict the plan.
- The root title is unknown and its description is empty. The supplied prior tickets concern Windows configuration, JMX, stream/HDFS behavior, documentation and testing, without two applicable authentication or authorization incidents.
- References to generic module tests in XD-203 and XD-1228 establish test infrastructure, not a security failure or a demonstrated validation omission in XD-1695.

### XD-1821 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:35)

- XD-1474 explicitly includes separate parsing entry points, source/sink channel metadata and merging descriptors with deployment requests; these cannot be labelled omitted.
- XD-1601 describes job and named-channel identity rules and states both job aliases work. Its description is truncated and status unknown, so a breaking prefix-resolution change is not established.
- XD-705 documents job control channels, while XD-1738 documents deletion failure after underlying module files are removed. They do not independently corroborate a tap/prefix-identity failure caused by the planned parser representation change.
- XD-1151 has unknown title/description and XD-1474 is truncated; compatibility tests and the final representation are unresolved rather than proven absent.

Review questions:
- Does the merged parser result preserve job/queue/topic identities described by XD-1601, and what supplied evidence establishes a failure if it does not?

### XD-1832 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:36)

- The epic explicitly covers shell tab-completion issues. Both member titles and descriptions are unknown, so the command coverage and test design cannot be inferred.
- XD-1197 reports job-launch option completion differing from destroy, while XD-1493 reports missing HTTP completion. These are useful historical cases, but no supplied target requirement establishes that only one command family will be implemented or validated.
- XD-1493, entity completion XD-670, and command separation XD-796 are marked Done. A generic possibility that completed fixes regress is insufficient to label a new validation gap.

### XD-1875 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:37)

- The plan already requires equivalent tests; unknown member text does not establish that real source-to-transport coverage will be removed.
- XD-1228 describes optional isolated testing, but its use in XD-1875 is not supplied. XD-1675 and XD-1683 are Done, and XD-1245 provides external-input acceptance utilities.

### XD-2052 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:38)

- The root explicitly requires data-accuracy validation, required-attribute errors and exception logging; XD-2044 also explicitly raises SFTP test infrastructure. Those requirements must not be labelled missing.
- XD-1295 reports a JMX proxy/conversion failure and XD-1743 reports Rabbit deserialization of Twitter classes. The supplied XD-1746 text does not establish whether the HTTP content-type change uses those same paths or whether their Done work leaves an active defect.
- XD-1912 concerns Rabbit-to-JDBC sink interoperability and XD-1678 concerns a batch jobstore connection. Neither, together with another supplied ticket, establishes a specific failure mechanism in the planned native JDBC source.
- XD-1329 and XD-1933 lack scope text; linked PR text is not supplied and was not consulted. The bounded evidence does not establish further omissions in the new sources.

### XD-2053 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:39)

- XD-1912 does not identify the cause of the Rabbit-to-JDBC failure; a payload-encoding mechanism cannot be assumed.
- XD-1743 describes a completed Rabbit/Tweet class-resolution defect, but the new ElasticSearch/Redis source payloads, transports and adapter contracts are not supplied.
- The plan explicitly includes data accuracy and error validation; absent scenario detail does not establish omitted checks.

### XD-2054 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:40)

- The sole visible child, XD-2015, already identifies the missing chromedriver.exe dependency that prevents Protractor end-to-end tests from running, and explicitly offers configuration or dependency correction. It is not an omitted testing task.
- The prior tickets describe server classloading, job deployment, configuration and module-test utilities. None supplies a second comparable browser-test dependency failure to support an additional risk mechanism.
- The root is wholly unknown. Backend integration-test needs cannot be inferred as uncovered work from this narrow UI test-runner repair.

### XD-2089 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:41)

- XD-2090 explicitly investigates bundling/unbundling custom modules and best practices. XD-841 and XD-1863 describe packaging/distribution difficulties that are directly relevant to that existing investigation, not evidence that packaging research was omitted.
- XD-2034 supplies one configuration-location failure across local and Yarn deployment, but the other supplied tickets do not independently establish the same configuration-loading mechanism for the proposed packaging approach.
- No packaging approach is selected in the visible plan, and XD-2091 is unknown. Inferring a specific dependency, layout or validation defect before that decision would exceed the evidence.

### XD-2106 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:42)

- The root explicitly includes cluster topology visualization and XD-2093 includes listing streams/jobs with deployed modules. Unknown member descriptions do not establish that deployment-state handling is omitted.
- XD-1777 demonstrates orphaned partition deployment state, but the remaining supplied tickets do not provide a second comparable cluster-view failure. XD-1000 and XD-1001 are planned/completed UI precedents, not independent incidents.
- XD-1972 concerns an evolving job contract and XD-1695 concerns endpoint security; neither establishes that the topology view is blocked or will display incorrect data.

### XD-2134 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:43)

- The visible plan explicitly supplies configurable error channels and root-cause propagation across source/processor/sink failures in XD-2135, reserved-keyword restrictions in XD-2136 and partition-state preservation on restart in XD-2137. Those concerns are already planned work.
- XD-1675 reports failure to find errorChannel; XD-1707 reports failure to find queue:foo in a Rabbit dynamic-router example. These concern channel resolution, but do not demonstrate that the planned error-channel configuration omits a particular required mechanism or validation. The supplied excerpts are truncated.
- XD-1678 concerns jobstore reconnection rather than hash-based partition assignment. XD-1601 concerns named-channel syntax rather than custom-module reserved keywords. XD-1738 concerns stream destruction after module files are removed, not the error-payload routing described in XD-2135.
- The root has unknown scope text. XD-2052 explicitly requires ingestion accuracy validation and appropriate error logging, and XD-1228 describes stream-test support; these caution against inferring missing validation solely from the bounded membership sample. No independent two-ticket mechanism establishes an additional supported risk.

Review questions:
- Do the supplied channel-resolution incidents establish a specific additional risk beyond the explicit configurable error-channel work?

### XD-2204 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:44)

- XD-2206 explicitly calls for investigating an R processor approach using rJava or Renjin; runtime selection/design investigation is already planned.
- XD-100 discusses tuple terminology, while the source/sink, security and paging tickets concern different features; they do not provide two comparable R integration or computation failure mechanisms.
- The root and XD-2205 have no recoverable title/description, and the known R task does not specify a runtime choice, input representation or deployment contract from which to infer a compatibility gap.

### XD-2252 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:45)

- XD-2253 explicitly measures network transfer rates for every edge in the four-machine topology. A warning that the plan lacks network baseline work would contradict this member.
- XD-1870 and XD-1602 show XD Rabbit/JMS module configuration selecting unintended brokers, but the supplied plan does not show that standalone Rabbit PerfTest or iperf uses those module configuration paths.
- The scope of XD-2254 through XD-2257 is unknown. Prior Redis initialization, ZooKeeper recovery and Rabbit-to-JDBC failures do not jointly establish a failure in the planned raw RabbitMQ baseline measurements.

### XD-2263 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:46)

- XD-2264 explicitly includes RabbitMQ cluster infrastructure, configuration changes and tool-chain setup, while XD-2265 and XD-2266 vary consumers and producers. These tasks are not missing from the supplied plan.
- XD-2084, XD-978 and XD-1342 provide completed deployment/configuration precedents rather than two demonstrated failures in RabbitMQ benchmark execution.
- XD-1793 documents stale XD job/stream state after a permission failure; XD-1495 concerns ZooKeeper runtime metadata and XD-1683 concerns Redis input handling. The supplied text does not establish that the benchmark clients use these failing paths.
- The root scope and benchmark acceptance details are unknown; this does not establish incorrect measurements or an unfulfilled prerequisite.

### XD-2267 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:47)

- Neither XD-2267 nor its supplied member XD-2268 has a known historical title or description, so no intended technical behavior can be identified from this input.
- No prior tickets were supplied by lexical retrieval, despite 1,963 eligible prior items being reported. A two-ticket-supported risk cannot be constructed from the supplied evidence.
- XD-2268 being In Progress does not establish that the plan is blocked, delayed or missing work; this empty target reflects unavailable support rather than verified safety.

### XD-2292 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:48)

- The root only states support for message brokers, and both observed members have unknown titles/descriptions; the supplied plan does not identify brokers, versions or whether the work changes source/sink adapters or the internal MessageBus.
- XD-1564 documents Rabbit routing-expression failure and XD-1291 documents Redis shutdown ordering, but both are Done and no supplied plan text ties a proposed change to either mechanism.
- XD-162 explicitly placed transport-independent conversion in shared channel-registry logic, providing counterevidence to a blanket claim that message conversion is absent.

### XD-2297 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:49)

- XD-2298 already investigates gpfdist/gpload, native HAWQ format, PXF and a Sqoop Tasklet, and explicitly decides between a batch job and other mechanisms. The research and architecture choice are present in scope.
- XD-2124 and XD-2132 describe candidate ingestion capabilities, not observed failures that show those options are unavailable. XD-1985 records a concrete Guava/Hadoop compatibility failure, but no second supplied ticket supports the same failure mechanism for a selected approach here.
- No implementation or target runtime version is chosen in the supplied spike. Generic accuracy and error-handling criteria from XD-2052/2053 cannot establish that this design investigation will omit them.

### XD-2336 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:50)

- XD-2335 explicitly includes the Kafka executable and Kafka performance tools in the performance AMI and is Done; these items cannot be labelled missing.
- The supplied EC2 provisioning, acceptance-test and YARN packaging stories describe existing work rather than two observed Kafka/AMI/performance-testing failures. The REST testing tasks do not establish a Kafka-specific mechanism.
- The root and XD-2334 have no known title/description, so intended benchmarks, readiness checks and AMI acceptance criteria cannot be inferred.

### XD-2374 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:51)

- XD-2375 explicitly specifies time-window processing with min and avg, so those aggregation operations cannot be labelled missing. The micro-batch member has no recoverable description.
- XD-2233 concerns REST time-series representation ordering and XD-2232 concerns median approximation; the plan does not specify REST output or median calculation, so those examples do not establish a comparable defect in the Reactor window processor.
- The source/sink acceptance criteria and error-channel proposal describe desired checks, not two independent historical Reactor or micro-batch failure mechanisms.

### XD-2464 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:52)

- The visible plan already defines Spark Streaming developer interfaces, a MessageBus receiver, an XD module type and a controllable driver. These integration boundaries must not be reported as forgotten tasks.
- XD-1470 supplies a concrete Jackson classloader conflict and XD-718 describes parent-last classloading, but the supplied Spark tasks do not state their library layout or cross-classloader types. A new library conflict cannot be inferred from dependency similarity alone.
- XD-1783 concerns cleanup after a departing deployment target, and XD-1318 concerns batch-database initialization order. The visible Spark design does not establish those same dependencies or failure paths.
- The root, XD-2466 and all implementation descriptions are unknown, so current acceptance and lifecycle coverage cannot be determined.

### XD-2476 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:53)

- XD-2477 explicitly adds stopping existing Sqoop jobs; stopping support is already planned and must not be labelled absent.
- XD-1793 reports stale Jobstore records after failed creation/deletion, and XD-742 describes ordinary job-management APIs. Their text does not establish two comparable Sqoop cancellation failures or confirm that Sqoop uses the same cleanup mechanism.
- Unknown root and other member text prevent determining the intended stop/cancel contract; the available estimate and broad job topics do not establish delivery risk.

### XD-2500 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:54)

- XD-2501 already includes upgrading Boot 1.2.0 RELEASE and its dependencies; a warning that dependency updates are missing would contradict the plan.
- XD-1967 records broken distro-specific Hadoop jars and XD-1464 records an unexpected Groovy version from snapshots, but the supplied text does not show that the Boot RC-to-release change repeats those resolution mechanisms.
- XD-2270 shows the earlier Boot 1.2.0 RC1 upgrade marked Done, and multiple completed Hadoop upgrades include explicit compatibility tests; these counterexamples prevent inferring a validation gap from the short current title.

### XD-2540 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:55)

- XD-2541 already defines a developer-facing RxJava interface contract and XD-2542 already creates a flexible processor/sink handler. Unknown root text does not establish that a particular contract behavior is omitted.
- XD-2481 asks for Reactor error-handling considerations and XD-2487 assigns error handling to another ticket. These are design precedents, not two demonstrated RxJava failures or evidence that the planned contract cannot address errors.
- XD-2135 proposes explicit error-channel support, but the supplied input does not establish that RxJava modules depend on this uncompleted feature or that errors will be lost. No such dependency was inferred from current links.

### XD-2629 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:56)

- XD-2630 explicitly scopes a study of an Ambari plugin for provisioning, management and monitoring. The supplied plan does not yet specify plugin implementation or library choices.
- XD-1530 and XD-1857 demonstrate different Hadoop API/classpath failures, but their supplied descriptions do not establish that the proposed Ambari study or eventual plugin uses those same dependencies.
- XD-1695 and XD-2143 describe security research and Basic Auth work marked Done; XD-2288 is a port-discovery spike. These precedents do not establish an unmet Ambari dependency or an access-control failure.
- The unknown root scope and bounded prior sample cannot establish further deliverables, schedule effects or a missing implementation task.

### XD-2660 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:57)

- XD-2662 explicitly adds Windows test coverage, so Windows validation is planned rather than demonstrably missing. The root and XD-2661 descriptions are unknown.
- XD-2401 describes failing distributed tests excluded from CI, but no second supplied ticket establishes a comparable Windows failure or a requirement for this Windows plan to repair the distributed CI suite.
- Completed YARN, Gemfire, Kafka and analytics acceptance-test stories show existing scenario checks; their topic similarity cannot establish a gap in Windows coverage.

### XD-2692 — no supported risk (train)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:58)

- XD-2596 explicitly targets intermittent Kafka compression-test failures on Ubuntu and OS X, while XD-2693 already moves the Kafka server into a separate process and is historically marked Done. Neither is omitted work.
- XD-2104 describes a UI test/server single-process failure, but that mechanism is not established for the remaining Kafka compression failure. XD-2401 records failing distributed tests excluded from CI and only suggests high startup CPU as a possible cause. These do not jointly establish a new Kafka-specific gap.
- XD-2462 explicitly provides prior Kafka message-bus CI acceptance coverage. The unknown root, XD-2573 and XD-2698 prevent inferring which remaining checks or process-management changes are absent.

### XD-2963 — no supported risk (validation)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:59)

- Only the broad stateful-stream-processing title is recoverable; both observed children have unknown title and description. No state backend, consistency contract, restart behavior or implementation is supplied.
- XD-1338 describes partitioning to colocate messages with in-process state and XD-2232 describes an approximate streaming median. These are relevant designs, not evidence that this plan omits state locality or uses an incorrect algorithm.
- XD-1707 reports a Rabbit dynamic-router failure and XD-1742 reports unwanted String conversion. Neither is tied to the unspecified stateful-processing design, and they do not establish a common state-management failure mechanism.

### XD-2978 — no supported risk (validation)

[Full current input and candidate target](/Users/phoebe/Nabu/data/training/xd-label-review-v2/generated-labels.jsonl:60)

- XD-2979 explicitly includes remaining refactoring, documentation and CF incubation submission; none of those activities can be labelled missing.
- XD-2916 provides one directly relevant completed Receptor client implementation, but no second supplied ticket documents a comparable Receptor or incubation failure mechanism.
- The other REST, security, stream cleanup and Hadoop packaging examples concern different interfaces and lifecycles; they do not establish a dependency or validation gap for the Java Receptor client.

Review questions:
- What Receptor API compatibility and CF incubation acceptance criteria apply to XD-2979 remaining refactoring?

Human decision: approve, revise or reject targets. Record a real named reviewer only after explicit review. The approved exports must preserve each current input hash and manifest; do not approve or train the older frozen candidates.
