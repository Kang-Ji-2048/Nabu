# Nabu candidate supervised risk labels

## Pre-publication membership audit

These 70 targets remain frozen, machine-generated review candidates. A metadata-only audit after the original run found 70 tickets with unresolvable child Epic Links; 21 supplied development inputs contain one or more of these IDs, and 10 additional plans would be excluded by the strengthened grouping policy. Their presence does not prove a risk or a held-out overlap. The current preparation guard also stops regeneration on 1 unresolved held-out parent reference. No held-out cutoff plan, ticket text or outcome was reconstructed or reviewed for this audit.

The original inputs, fingerprints, proposed targets and historical provenance are preserved. The 4 risk / 66 evidence-insufficient / 0 failed counts describe Detection/citation validation; they do not establish complete partition safety. Resolve the metadata audit and prepare/review an explicit new version before training. See [pre-publication-check.json](pre-publication-check.json) for affected development IDs and unresolved grouping questions.

These assistant-generated targets are unreviewed. Mechanical validation checks the Detection schema, allowed risk types, plan targets and exact historical citations. It does not verify causal support, usefulness, severity or completeness. No human approval or reviewer is claimed. Held-out test examples are excluded.

Examples: 70. Valid risk examples: 4; valid evidence-insufficient/no-risk examples: 66; failed or missing examples: 0.

An empty risk list means that this supplied evidence did not support a risk; it does not certify a safe plan.

## Preparation and assistant review

Imported Spring XD from TAWOS v1.1: 3,707 tickets and 43,227 history events, with zero ETL rejections. Development-only preparation retained 68 training and 2 validation examples. Nineteen development plans were excluded because membership references were unresolved or crossed partitions. Held-out cutoff plans were not generated or reviewed; their root/member IDs were also excluded from supplied prior evidence. Historical reconstruction internally preloads source records, as disclosed in the split report.

All 70 candidate targets passed validate_detection, with original ID, split, cutoff, input and evidence fingerprint preserved. The first pass proposed 12 risk examples. An independent assistant challenge rejected 8, narrowed 3 and retained 1. Original targets and decision reasons are preserved in initial-proposals.jsonl and semantic-review.jsonl; these assistant judgments do not constitute human approval.

The validation split contains only two evidence-insufficient examples and no positive risk. It cannot assess risk recall or confidence calibration. No GPU inference or model training was run.

### Risk candidates requiring human review

- **XD-1260** (validation_gap, provisional medium): The planned partitioned jobs may run while their persisted step history cannot be listed if null StepExecution IDs are stored in the shared job repository.
- **XD-1317** (dependency_gap, provisional medium): If YARN starts XD containers before the admin server has initialized the shared batch database, container startup may fail when the job-execution DAO connects.
- **XD-1605** (validation_gap, provisional medium): The planned management/jolokia migration may leave monitoring inaccessible if the reported management-context access exception in XD-1496 still applies to that route.
- **XD-1821** (validation_gap, provisional medium): The planned parser-entry-point and descriptor merge has a channel-identity compatibility risk: job queues and named stream/tap references use distinct prefix-resolution rules, and changing their representation can select a different channel or make a previously valid tap reference fail.

## Case index

| Case | Split | Risk count | Status |
| --- | --- | ---: | --- |
| [XD-75](#xd-75-train) | train | 0 | generated_unreviewed |
| [XD-92](#xd-92-train) | train | 0 | generated_unreviewed |
| [XD-177](#xd-177-train) | train | 0 | generated_unreviewed |
| [XD-235](#xd-235-train) | train | 0 | generated_unreviewed |
| [XD-238](#xd-238-train) | train | 0 | generated_unreviewed |
| [XD-239](#xd-239-train) | train | 0 | generated_unreviewed |
| [XD-240](#xd-240-train) | train | 0 | generated_unreviewed |
| [XD-241](#xd-241-train) | train | 0 | generated_unreviewed |
| [XD-395](#xd-395-train) | train | 0 | generated_unreviewed |
| [XD-464](#xd-464-train) | train | 0 | generated_unreviewed |
| [XD-468](#xd-468-train) | train | 0 | generated_unreviewed |
| [XD-484](#xd-484-train) | train | 0 | generated_unreviewed |
| [XD-527](#xd-527-train) | train | 0 | generated_unreviewed |
| [XD-697](#xd-697-train) | train | 0 | generated_unreviewed |
| [XD-706](#xd-706-train) | train | 0 | generated_unreviewed |
| [XD-742](#xd-742-train) | train | 0 | generated_unreviewed |
| [XD-836](#xd-836-train) | train | 0 | generated_unreviewed |
| [XD-895](#xd-895-train) | train | 0 | generated_unreviewed |
| [XD-963](#xd-963-train) | train | 0 | generated_unreviewed |
| [XD-965](#xd-965-train) | train | 0 | generated_unreviewed |
| [XD-996](#xd-996-train) | train | 0 | generated_unreviewed |
| [XD-1141](#xd-1141-train) | train | 0 | generated_unreviewed |
| [XD-1257](#xd-1257-train) | train | 0 | generated_unreviewed |
| [XD-1258](#xd-1258-train) | train | 0 | generated_unreviewed |
| [XD-1259](#xd-1259-train) | train | 0 | generated_unreviewed |
| [XD-1260](#xd-1260-train) | train | 1 | generated_unreviewed |
| [XD-1267](#xd-1267-train) | train | 0 | generated_unreviewed |
| [XD-1275](#xd-1275-train) | train | 0 | generated_unreviewed |
| [XD-1317](#xd-1317-train) | train | 1 | generated_unreviewed |
| [XD-1391](#xd-1391-train) | train | 0 | generated_unreviewed |
| [XD-1392](#xd-1392-train) | train | 0 | generated_unreviewed |
| [XD-1405](#xd-1405-train) | train | 0 | generated_unreviewed |
| [XD-1473](#xd-1473-train) | train | 0 | generated_unreviewed |
| [XD-1605](#xd-1605-train) | train | 1 | generated_unreviewed |
| [XD-1606](#xd-1606-train) | train | 0 | generated_unreviewed |
| [XD-1607](#xd-1607-train) | train | 0 | generated_unreviewed |
| [XD-1608](#xd-1608-train) | train | 0 | generated_unreviewed |
| [XD-1609](#xd-1609-train) | train | 0 | generated_unreviewed |
| [XD-1610](#xd-1610-train) | train | 0 | generated_unreviewed |
| [XD-1647](#xd-1647-train) | train | 0 | generated_unreviewed |
| [XD-1688](#xd-1688-train) | train | 0 | generated_unreviewed |
| [XD-1694](#xd-1694-train) | train | 0 | generated_unreviewed |
| [XD-1820](#xd-1820-train) | train | 0 | generated_unreviewed |
| [XD-1821](#xd-1821-train) | train | 1 | generated_unreviewed |
| [XD-1832](#xd-1832-train) | train | 0 | generated_unreviewed |
| [XD-1875](#xd-1875-train) | train | 0 | generated_unreviewed |
| [XD-2052](#xd-2052-train) | train | 0 | generated_unreviewed |
| [XD-2053](#xd-2053-train) | train | 0 | generated_unreviewed |
| [XD-2054](#xd-2054-train) | train | 0 | generated_unreviewed |
| [XD-2089](#xd-2089-train) | train | 0 | generated_unreviewed |
| [XD-2106](#xd-2106-train) | train | 0 | generated_unreviewed |
| [XD-2134](#xd-2134-train) | train | 0 | generated_unreviewed |
| [XD-2204](#xd-2204-train) | train | 0 | generated_unreviewed |
| [XD-2252](#xd-2252-train) | train | 0 | generated_unreviewed |
| [XD-2263](#xd-2263-train) | train | 0 | generated_unreviewed |
| [XD-2267](#xd-2267-train) | train | 0 | generated_unreviewed |
| [XD-2292](#xd-2292-train) | train | 0 | generated_unreviewed |
| [XD-2297](#xd-2297-train) | train | 0 | generated_unreviewed |
| [XD-2336](#xd-2336-train) | train | 0 | generated_unreviewed |
| [XD-2374](#xd-2374-train) | train | 0 | generated_unreviewed |
| [XD-2399](#xd-2399-train) | train | 0 | generated_unreviewed |
| [XD-2464](#xd-2464-train) | train | 0 | generated_unreviewed |
| [XD-2476](#xd-2476-train) | train | 0 | generated_unreviewed |
| [XD-2500](#xd-2500-train) | train | 0 | generated_unreviewed |
| [XD-2540](#xd-2540-train) | train | 0 | generated_unreviewed |
| [XD-2629](#xd-2629-train) | train | 0 | generated_unreviewed |
| [XD-2660](#xd-2660-train) | train | 0 | generated_unreviewed |
| [XD-2692](#xd-2692-train) | train | 0 | generated_unreviewed |
| [XD-2963](#xd-2963-validation) | validation | 0 | generated_unreviewed |
| [XD-2978](#xd-2978-validation) | validation | 0 | generated_unreviewed |

## XD-75 (train)

Historical cutoff: 2013-05-21T10:43:19.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `360e628cd61c8805f31a7e1db3e6de0a4fff8e6092ec1e0a2618be10b66a1e9e`

Source input identity SHA-256: `16d44be178c314a35c7d4be8bdc5318f7732f78e6deb37f1ccc1b5d783f44916`

### Supplied historical plan

- **XD-75** (`tawos-v1.1:3706`)
  - Title: "Add redis executable to distribution zip file"
  - Description: null
  - Unknown fields: ["description", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The redis packaging plan has no recoverable description, so runtime prerequisites and acceptance criteria cannot be compared with prior work.",
    "XD-41 concerns unavailable Redis in tests and XD-61 discusses bundling Redis, but these do not establish two independent historical examples of a delivery failure in adding Redis to a distribution.",
    "XD-76 is an analogous packaging task; the other Redis service titles do not demonstrate an omitted requirement or failure mechanism."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-76** (`tawos-v1.1:3705`), created 2013-05-20T10:45:00.000000Z
  - Title: "Add gemfire-server application to the distribution zip"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-23** (`tawos-v1.1:3754`), created 2013-04-16T11:21:12.000000Z
  - Title: "add file source and sink modules"
  - Description: null
  - Unknown fields: ["description"]
  - Truncated fields: []
- **XD-41** (`tawos-v1.1:3738`), created 2013-05-02T11:18:14.000000Z
  - Title: "Add JUnit @Rule so Tests Fail Fast with Clear Messaging if Redis Not Available"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: null
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-2** (`tawos-v1.1:3770`), created 2013-04-12T06:38:02.000000Z
  - Title: "HDFS Core writing helper classes"
  - Description: "Simple file writer that has existed in the spring hadoop samples."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-20** (`tawos-v1.1:3757`), created 2013-04-16T10:55:11.000000Z
  - Title: "DIRT Runtime that deploys an application context across multiple nodes using redis."
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-28** (`tawos-v1.1:3750`), created 2013-04-17T08:48:08.000000Z
  - Title: null
  - Description: "A gauge just stores a number.  Implementations for in-memory and redis."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-29** (`tawos-v1.1:3749`), created 2013-04-17T08:49:16.000000Z
  - Title: "Create rich gauge service"
  - Description: "A rich gauge stores a number and also rmd, min, max. Implementations for in-memory and redis."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-30** (`tawos-v1.1:3748`), created 2013-04-17T08:50:14.000000Z
  - Title: "Create a simple counter service"
  - Description: "A simple counters can increment/decrement a number.  Implementations for in-memory and redis."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-31** (`tawos-v1.1:3747`), created 2013-04-17T08:51:18.000000Z
  - Title: null
  - Description: "A field-value counter is useful for bar chart graphs, Strings on x-axis and count on y-axis.  Maps well to zset in redis. Implementations for in-memory and redis."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-45** (`tawos-v1.1:3734`), created 2013-05-06T07:44:41.000000Z
  - Title: "Remove the expiry of keys in Redis based repositories"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-78** (`tawos-v1.1:3704`), created 2013-05-20T10:56:33.000000Z
  - Title: "Documentation for \"http | file\" processing"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Unresolved labelling questions

- What Redis versions and supported operating systems were intended for this distribution?
- Is redis availability validation already part of the packaging acceptance criteria outside the supplied plan?

## XD-92 (train)

Historical cutoff: 2013-05-21T11:14:56.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `1823e5801426715406a1c8d338e0c73e4f88a2e29cb17ddf33705cb94d6f87ef`

Source input identity SHA-256: `e238f93905bf40573429d7106f3b212173db3e6ebfacaea6e8653a851636b135`

### Supplied historical plan

- **XD-92** (`tawos-v1.1:3690`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The supplied root has unknown title, description, type and estimate, and no observed members; there is no recoverable requirement to assess.",
    "No prior tickets were supplied. The historical To Do status alone cannot establish scope, dependency or validation risk."
  ]
}
```

### Supplied prior evidence for support and counterexample review


### Unresolved labelling questions

- Can a cutoff-valid statement of the intended work and supporting historical evidence be recovered before assigning a risk label?

## XD-177 (train)

Historical cutoff: 2013-06-04T13:50:47.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `74ae88750a3c8fb72ae714501d05fb0b0a88f01b57e9e937ed54102964c491be`

Source input identity SHA-256: `26569875b5d3ac5ffe8d050f3e6502b5c21ac09f210f668463665523d02039ae`

### Supplied historical plan

- **XD-177** (`tawos-v1.1:3606`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-178** (`tawos-v1.1:3605`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-179** (`tawos-v1.1:3604`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-180** (`tawos-v1.1:3603`)
  - Title: "The command line for xd-admin and xd-container to support an additional option, pipeProtocol, that is used to determine the middleware for sending admin requests and data between processing steps"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-181** (`tawos-v1.1:3602`)
  - Title: null
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-182** (`tawos-v1.1:3601`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-183** (`tawos-v1.1:3600`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-184** (`tawos-v1.1:3599`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-185** (`tawos-v1.1:3598`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-186** (`tawos-v1.1:3597`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-177 has no known historical title or description, and most supplied members also lack recoverable scope text; their statuses do not establish a delivery risk.",
    "The known XD-180 title and XD-181 description already address protocol selection and launcher configuration. They do not establish an omitted implementation requirement.",
    "XD-107 and XD-124 concern Redis shutdown and are already Done at this cutoff; the other supplied startup, parsing and placeholder issues do not provide two comparable incidents supporting a specific defect in this plan."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: null
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-106** (`tawos-v1.1:3676`), created 2013-05-23T01:22:04.000000Z
  - Title: "Container server does not log a message that it has started or stopped successfully"
  - Description: "$ ./xd-container \nprocessing module 'Module [name=file, type=sink]' from group 'tailtest' with index: 1\nprocessing module 'Module [name=tail, type=source]' from group 'tailtest' with index: 0\n\n\nLogging of 'processing module' should have log level, time.."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: null
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-102** (`tawos-v1.1:3680`), created 2013-05-22T23:35:27.000000Z
  - Title: "Create XDContainer class to start stream server"
  - Description: "Provide optional command line arg to embed the container launcher, aka - xd-admin server. \n\n\nXDContainer.sh --embeddAdmin"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-107** (`tawos-v1.1:3675`), created 2013-05-23T01:23:50.000000Z
  - Title: "Clean shutdown of redis in xd-admin"
  - Description: "A ctrl-c of xd-admin results in exception messages about disconnecting from redis.\n\n14:16:07,327 ERROR task-scheduler-1 handler.LoggingHandler:136 - org.springframework.data.redis.RedisSystemException: Redis command interrupted; nested exception is com.lambdaworks.redis.RedisCommandInterruptedException: Command interrupted\n"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-142** (`tawos-v1.1:3641`), created 2013-05-28T15:11:05.000000Z
  - Title: null
  - Description: "The {{ModuleDeployer}} calls {{getBeansOfType}} before the context has had its {{PropertySourcesPlaceholderConfigurer}} attached. This can cause issues with {{FactoryBean}} s with placeholders in constructor args because the unresolved placeholder is used when the {{FactoryBean}} is pre-instantiated to determine the type of object it will serve up."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-143** (`tawos-v1.1:3640`), created 2013-05-28T16:26:55.000000Z
  - Title: "Create externalized property file to support connectivity to redis"
  - Description: null
  - Unknown fields: ["description", "estimate"]
  - Truncated fields: []
- **XD-159** (`tawos-v1.1:3624`), created 2013-05-30T12:46:59.000000Z
  - Title: "Improve Module Parameter Parsing"
  - Description: "Parameter parsing does not work if an argument contains '--'.\n\nFor example:\n\n{code}\n... | transform --expression=42 | transform --expression=--payload |...\n{code}\n\nAlso, I was surprised that this worked..\n\n{code}\n| transform --expression=new StringBuilder(payload).reverse() |\n{code}\n\n... but this didn't...\n\n{code}\n| transform --expression='new StringBuilder(payload).reverse()' |\n{code}\n\nI think we need to tokenize the argument (with ' if contains spaces) and remove any surrounding '...' from the result. This means if someone wants a SpEL literal they would have to use something like \n\n{code}--expression=''Hello, world!''{code}\n\nresulting in a SpEL literal 'Hello, world!'"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-41** (`tawos-v1.1:3738`), created 2013-05-02T11:18:14.000000Z
  - Title: "Add JUnit @Rule so Tests Fail Fast with Clear Messaging if Redis Not Available"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-97** (`tawos-v1.1:3685`), created 2013-05-20T12:23:20.000000Z
  - Title: null
  - Description: "A Flow or a processor component may require routing semantics. Currently the stream assumes a single input and output for each module. A Flow may support multiple outputs - Switch routing that is - Recipient list is not currently supported (another subtask?). We need to support semantics like:\n\na |[output.foo:c,output.bar:d,default:e]"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-124** (`tawos-v1.1:3659`), created 2013-05-28T07:58:40.000000Z
  - Title: "Clean shutdown of redis in xd-container"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-127** (`tawos-v1.1:3656`), created 2013-05-28T08:35:42.000000Z
  - Title: null
  - Description: "Based off SI tcp inbound adapter.  This will allow for event forwarding that can select among the existing SI serialized/deserializer options.\n"
  - Unknown fields: ["title", "type"]
  - Truncated fields: []

### Unresolved labelling questions

- Can the intended XD-177 scope be recovered from an additional source demonstrably available at this cutoff?
- Do two supplied historical tickets actually show a failure mechanism applicable to the protocol changes, rather than separate startup or Redis concerns?

## XD-235 (train)

Historical cutoff: 2013-06-18T09:45:35.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `a1a2dc29f38403e425e34849feef38de16cd7da49e50dd2afcc76211daca7b92`

Source input identity SHA-256: `1c2c2811e68dd94b53eb2c91f8e6bb6d35aad1717e35b69e8ddcbde39c8a8c5d`

### Supplied historical plan

- **XD-235** (`tawos-v1.1:3548`)
  - Title: "Stream should be able to be easily tested inside the IDE using JUnit "
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The plan explicitly requests JUnit testing in an IDE; its unknown description and absence of observed members do not establish that testing work is missing.",
    "The supplied launcher/classpath, distribution, shutdown and stream tickets do not provide two comparable examples of an IDE or JUnit failure mechanism."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-188** (`tawos-v1.1:3595`), created 2013-06-03T21:07:58.000000Z
  - Title: "\"Add  directory to classpath in server startup scripts so groovy based processors can be easily referenced by name without a resource uri prefix\""
  - Description: "\"a stream such as time | filter --script=oddMinuteFilter.groovy | file   would load the groovy script 'oddMinuteFilter.groovy' that is located in the directory modules/processor or perhaps in modules/processor/scripts.  Not sure the benefit of having a subdirectory below processor just for scripts.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-199** (`tawos-v1.1:3584`), created 2013-06-06T09:23:17.000000Z
  - Title: "\"Ensure the DELETE Operation can Delete a Tap\""
  - Description: "\"While deleting a stream doesn't remove any taps right now, we should be able to explicitly delete a tap.  Determine whether the current DELETE works and, if not, make it so.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-244** (`tawos-v1.1:3540`), created 2013-06-17T12:19:33.000000Z
  - Title: null
  - Description: "h2. Narrative\nAs the XD system, I need to be able to execute a job (or potentially a stream) based on a given condition (time, data existence, etc).  This story is intended is for a local trigger implementation but remote triggers will also need to exist.\n\nh2.  Acceptance Criteria\n# Provide an abstraction that XD will use to determine when to launch a given stream or job.\n# Provide the implementation for a local time based trigger.\n# Provide the implementation for a trigger that executes when a file exists."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-72** (`tawos-v1.1:3709`), created 2013-05-17T09:24:13.000000Z
  - Title: "\"Provide a http source\""
  - Description: "\"stream should be able to ingest data from http \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-102** (`tawos-v1.1:3680`), created 2013-05-22T23:35:27.000000Z
  - Title: "Create XDContainer class to start stream server"
  - Description: "Provide optional command line arg to embed the container launcher, aka - xd-admin server. \n\n\nXDContainer.sh --embeddAdmin"
  - Unknown fields: []
  - Truncated fields: []
- **XD-103** (`tawos-v1.1:3679`), created 2013-05-22T23:37:24.000000Z
  - Title: "\"Create XDAdmin server to start container launcher\""
  - Description: "\"This will launch the RedisContainerLauncher, in future will be able to select from a variety of middleware options.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-110** (`tawos-v1.1:3672`), created 2013-05-23T08:41:56.000000Z
  - Title: "\"Remove use of system property xd.home to define location for install location, rely on environment variable XD_HOME\""
  - Description: "\"This is in the AdminMain and ContainerMain.    Can get the environment property directly in java code unless provided explicitly on the command line using --xdHomeDir.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-111** (`tawos-v1.1:3671`), created 2013-05-23T09:39:54.000000Z
  - Title: "\"Create final distribution zip across multiple projects\""
  - Description: "\"The final directory structure should look like  <install-dir>/xd <install-dir>/redis <install-dir>/gemfire  inside the XD directory   /xd/bin - which has xd-container and xd-admin scripts /xd/lib  inside the gemfire directory /gemfire/bin - has the gemfire-server script /gemfire/lib   inside the redis directory is   /redis/redis-latest-v.x.y.z.tar /redis/README /readis/install-redis  - script that does the basic 4 commands to install redis.   There should be a gradle task that runs after the distZip task, that will take the contents of different project directories, script diretories and 'redis-binary' directories and creates the final layout for the distribution.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-122** (`tawos-v1.1:3661`), created 2013-05-24T17:20:00.000000Z
  - Title: "\"XD scripts need to have spring-integration milestone versions updated\""
  - Description: "\"Spring-integration version is changed to 3.0.0.M2 and since we manually create the XD scripts, they still point to the 3.0.0.BUILD-SNAPSHOT version.  As discussed, we also need to have a better strategy on updating the lib directory inside the XD scripts.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-124** (`tawos-v1.1:3659`), created 2013-05-28T07:58:40.000000Z
  - Title: "Clean shutdown of redis in xd-container"
  - Description: "\"Need to shutdown cleanly, no exception messages are shown.  Order of components in the stream should be shut down from 'first to last'  (opposite of creation)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-125** (`tawos-v1.1:3658`), created 2013-05-28T08:30:30.000000Z
  - Title: "\"Stream documentation review\""
  - Description: null
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Should the IDE test harness exercise Redis and local-channel implementations, or isolate modules from external middleware?
- What historical acceptance criteria, if any, existed for repeatable JUnit setup and teardown at this cutoff?

## XD-238 (train)

Historical cutoff: 2013-06-18T10:03:00.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `df2303e332cff0057761a951fca7f571f39d2778ba781d63be4f406d3d069f6c`

Source input identity SHA-256: `b6c11954205ab0c93c604a645ac1e56884f69079b08332ad70db449a0c0523ce`

### Supplied historical plan

- **XD-238** (`tawos-v1.1:3545`)
  - Title: "Provide a strategy in which custom code can be deployed into the DIRT runtime"
  - Description: "modules that are shipped with XD should be packaged in the same way that any user contributed modules are packaged."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-132** (`tawos-v1.1:3651`)
  - Title: null
  - Description: "To allow for groups of beans to be defined or not in the container that runs a module.\n\nWhen deploying a stream (e.g. via the REST API), it should be possible to also provide profile names. Then those would apply to any modules within that particular stream deployment."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-194** (`tawos-v1.1:3589`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root explicitly requires shipped and user-contributed modules to share packaging, while XD-132 explicitly covers deployment profiles; neither is an established missing-work gap.",
    "XD-245 supplies XML/custom-code and regular/Hadoop-job acceptance requirements, not evidence that this packaging strategy fails; the other retrieved configuration and documentation tasks do not independently establish such a failure.",
    "XD-194 has no recoverable title or description, so the visible two-member plan cannot establish the complete intended packaging scope."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: "\"Create distributable artifact that contains server application and start/stop scripts\""
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-159** (`tawos-v1.1:3624`), created 2013-05-30T12:46:59.000000Z
  - Title: "Improve Module Parameter Parsing"
  - Description: "Parameter parsing does not work if an argument contains '--'.\n\nFor example:\n\n{code}\n... | transform --expression=42 | transform --expression=--payload |...\n{code}\n\nAlso, I was surprised that this worked..\n\n{code}\n| transform --expression=new StringBuilder(payload).reverse() |\n{code}\n\n... but this didn't...\n\n{code}\n| transform --expression='new StringBuilder(payload).reverse()' |\n{code}\n\nI think we need to tokenize the argument (with ' if contains spaces) and remove any surrounding '...' from the result. This means if someone wants a SpEL literal they would have to use something like \n\n{code}--expression=''Hello, world!''{code}\n\nresulting in a SpEL literal 'Hello, world!'"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-166** (`tawos-v1.1:3617`), created 2013-05-31T15:58:00.000000Z
  - Title: "\"Create config support based on channel registry type\""
  - Description: "\"We need to have the XD container & admin reading the registry specific property based on the registry type selected.   From Mark F, on one of the code review comments:  Maybe rather than having redis, rabbit, etc. properties all within a container.properties we should rely upon naming conventions instead. Specifically, we could have a single configurable property for the type of channel registry (\"\"redis\"\", \"\"rabbit\"\", or \"\"local\"\" being possible values), and then we could use something like:  <import resource=\"\"config/${registry.type}.xml\"\"/>  <context:property-placeholder location=\"\"config/${registry.type}.properties\"\"/>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: null
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to package XML configurations with custom code and deploy it to XD\n# Provide the ability to package custom code (with annotation/java config definitions) and deploy it to XD\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-246** (`tawos-v1.1:3538`), created 2013-06-17T13:26:13.000000Z
  - Title: "Define API to manage job lifecycle"
  - Description: "h2. Narrative\nAs a developer, I need to be able to start, stop and restart batch jobs on XD.  This should be available via the REST API as well as the CLI\n\nh2.  Acceptance Criteria\n# Provide a way to start/stop/restart an already registered job on demand via the REST API.\n# Provide a way to start/stop/restart an already registered job on demand via the CLI."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-135** (`tawos-v1.1:3648`), created 2013-05-28T11:02:56.000000Z
  - Title: "\"Documentation on XD Architecture\""
  - Description: "\"Show overall flow of data in a stream, the server components 'admin' and 'container'.  How modules are deployed.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: null
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-173** (`tawos-v1.1:3610`), created 2013-06-03T11:02:50.000000Z
  - Title: "Document how to create a custom input/output module for existing SI channel adapters"
  - Description: "\"Document how to take an existing input/output channel adapters in spring integration and add them as a XD source/sink module.  Should be as end-user focused, step by step guide as possible.  Consider including a getting started gradle/pom.xml \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-179** (`tawos-v1.1:3604`), created 2013-06-03T13:57:56.000000Z
  - Title: "\"Have three startup scripts, xd-singlenode, xd-admin, and xd-container\""
  - Description: "\"The xd-singlenode script will launch a main application that creates both the admin node (to process http admin requests) and the container node (to execute modules for data processing) within in the same process   the xd-admin script will launch a main application that creates only the admin node (remove current embeddedContainer options)  the xd-container script will launch a main application that creates only the container node (as it is now)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-182** (`tawos-v1.1:3601`), created 2013-06-03T14:09:03.000000Z
  - Title: "\"Create redisProtocol.xml that will load all the Redis specific implementations to suppor the XD container runtime and administration\""
  - Description: "\"The redis specific beans that are defined in the current launcher.xml should move into this configuration file.   \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does the packaging strategy include the XML and Java/annotation configurations and regular/Hadoop jobs described in XD-245?
- What work did XD-194 describe at this cutoff, and did it address packaging or runtime integration?

## XD-239 (train)

Historical cutoff: 2013-06-18T10:10:41.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `eb54b9481d22feea7543c74db5f2b4c3a381abe06923cb93ac05fe2e6b1915ba`

Source input identity SHA-256: `345cd10a18b242082d8aa0f2101ceedc20f1279520d3b33349b4c735a599e9c6`

### Supplied historical plan

- **XD-239** (`tawos-v1.1:3544`)
  - Title: "Provide a way to view aqverage performance statistics for each module involved in my stream, aggregated across a cluste"
  - Description: null
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-158** (`tawos-v1.1:3625`)
  - Title: "Add jolokia configuration to export JMX managed shutdown bean over http"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The visible goal is cluster-aggregated module performance statistics, while the only observed child concerns exporting a JMX shutdown bean; their relationship is not explained.",
    "XD-157 also concerns clean shutdown, and XD-132 concerns deployment profiles. Neither establishes a failure mechanism for metrics aggregation, and the remaining prior tickets do not provide two comparable examples.",
    "The narrow observed scope and incomplete historical fields do not establish that metrics collection or aggregation work was omitted."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-157** (`tawos-v1.1:3626`), created 2013-05-30T11:48:07.000000Z
  - Title: "Add a JMX managed bean to shutdown cleanly the xd-admin and xd-container servers"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-132** (`tawos-v1.1:3651`), created 2013-05-28T10:47:40.000000Z
  - Title: null
  - Description: "To allow for groups of beans to be defined or not in the container that runs a module.\n\nWhen deploying a stream (e.g. via the REST API), it should be possible to also provide profile names. Then those would apply to any modules within that particular stream deployment."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-161** (`tawos-v1.1:3622`), created 2013-05-30T16:21:52.000000Z
  - Title: "Add HTTP Delete Stream Operation"
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-212** (`tawos-v1.1:3571`), created 2013-06-07T08:25:52.000000Z
  - Title: "\"Add http port command line option to AdminMain\""
  - Description: "\"Currently StreamServer has setPort, but no way for end user to set it. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-221** (`tawos-v1.1:3562`), created 2013-06-10T10:33:28.000000Z
  - Title: "Links in asciidoctor generated HTML+docbook documentation are broken"
  - Description: "The issue arises because the link:document[Label] asciidoc macro is meant for \"external documents\" and creates {{<ulink>}} in docbook / {{<a href=\"document\">}} in html, whereas we want {{<link linkend=\"anchor\">}} / {{<a href=\"doc#anchor>}} resp. We also want it to continue working in github live view.\n\nI guess what could work is to have the macro (either override the link macro or create our own if github supports that) that looks like :\n{{link:document#anchor[Label]}}  (the #anchor works out of the box in asciidoc and should work in github) but override it for the html and docbook backends to render to the correct form.\n\nThe thing is, there are several ways to create/override macros (and templates they render to), some of which make sense to our setup:\n- having asciidoc.conf in the directory of the processed document (http://asciidoc.org/userguide.html#X27)\n- having docbook.conf/html.conf in the directory of the processed document (http://asciidoc.org/userguide.html#X27)\n- defining macros using attributes (http://asciidoc.org/userguide.html#_setting_configuration_entries)\n\nI tried all of those, but to no avail. These DO WORK with plain asciidoc, but not with our toolchain. Don't k"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-222** (`tawos-v1.1:3561`), created 2013-06-10T10:37:54.000000Z
  - Title: "\"Add docs for Deleting a simple stream.\""
  - Description: "\"curl -X DELETE http://localhost:8080/streams/ticktock\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: "\"Create distributable artifact that contains server application and start/stop scripts\""
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-72** (`tawos-v1.1:3709`), created 2013-05-17T09:24:13.000000Z
  - Title: "\"Provide a http source\""
  - Description: "\"stream should be able to ingest data from http \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-97** (`tawos-v1.1:3685`), created 2013-05-20T12:23:20.000000Z
  - Title: null
  - Description: "A Flow or a processor component may require routing semantics. Currently the stream assumes a single input and output for each module. A Flow may support multiple outputs - Switch routing that is - Recipient list is not currently supported (another subtask?). We need to support semantics like:\n\na |[output.foo:c,output.bar:d,default:e]"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-98** (`tawos-v1.1:3684`), created 2013-05-20T17:08:21.000000Z
  - Title: "\"Documentation on the module system and how to contribute new modules\""
  - Description: "\"For people who are familiar with Spring/Spring Integration provide documents that show how to add additional input sources/sinks.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-102** (`tawos-v1.1:3680`), created 2013-05-22T23:35:27.000000Z
  - Title: "Create XDContainer class to start stream server"
  - Description: "Provide optional command line arg to embed the container launcher, aka - xd-admin server. \n\n\nXDContainer.sh --embeddAdmin"
  - Unknown fields: []
  - Truncated fields: []
- **XD-115** (`tawos-v1.1:3668`), created 2013-05-23T13:16:37.000000Z
  - Title: "\"add SpEL 'transform' processor\""
  - Description: "\"It should provide an 'expression' param for SpEL and have a default pass-thru of the payload.\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does XD-158 belong to the statistics implementation or a separate management concern, and which historical tickets establish an aggregation-specific risk?

## XD-240 (train)

Historical cutoff: 2013-06-18T10:56:09.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `46c89473d6625b3f57c537fabf4a3cf7652b930e3a8b63510217fe5bdffd6072`

Source input identity SHA-256: `0607a87d90338b77375770e54fd79dd44f96066dd70c78d75b41abbb0a29f72e`

### Supplied historical plan

- **XD-240** (`tawos-v1.1:3543`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "Title, description, type and estimate are unknown for the supplied root, with no observed child tickets.",
    "No prior evidence was retrieved. To Do status and missing historical fields are insufficient to support any allowed risk type."
  ]
}
```

### Supplied prior evidence for support and counterexample review


### Unresolved labelling questions

- Is there recoverable cutoff-valid plan text for XD-240 that identifies the feature being assessed?

## XD-241 (train)

Historical cutoff: 2013-06-18T11:11:11.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `8cca604fbea3db1aa96a7e1a82ee164bcaeb7be4de745003119959801cfc2e0a`

Source input identity SHA-256: `724ce5a041677a1d466236756b96779ace14c322d65bea4d2ac5b8daee3c72f9`

### Supplied historical plan

- **XD-241** (`tawos-v1.1:3542`)
  - Title: "Describe how processing modules are distributed/colocated across XDContainers"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-162** (`tawos-v1.1:3621`)
  - Title: "add support for message conversion in ChannelRegistry"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The supplied plan explicitly includes XD-162 message conversion; its description and the root description are unknown, so further distribution requirements cannot be inferred from this excerpt.",
    "XD-164 requests channel declaration validation, but no second supplied ticket establishes the same failure mechanism. Completed architecture and module guides are scope precedents rather than evidence of a delivery risk.",
    "XD-180 and XD-181 already describe completed protocol and launcher support; their relationship to distribution does not establish an unresolved dependency or an omission in XD-241."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-217** (`tawos-v1.1:3566`), created 2013-06-10T10:12:14.000000Z
  - Title: "\"Add config dir to classpath to support custom properties-locations\""
  - Description: "\"The transform, filter, and script processor modules support passing in a properties-location for script variables. We need a default location on the classpath for users to provide custom properties files.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-98** (`tawos-v1.1:3684`), created 2013-05-20T17:08:21.000000Z
  - Title: "\"Documentation on the module system and how to contribute new modules\""
  - Description: "\"For people who are familiar with Spring/Spring Integration provide documents that show how to add additional input sources/sinks.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-106** (`tawos-v1.1:3676`), created 2013-05-23T01:22:04.000000Z
  - Title: "Container server does not log a message that it has started or stopped successfully"
  - Description: "$ ./xd-container \nprocessing module 'Module [name=file, type=sink]' from group 'tailtest' with index: 1\nprocessing module 'Module [name=tail, type=source]' from group 'tailtest' with index: 0\n\n\nLogging of 'processing module' should have log level, time.."
  - Unknown fields: []
  - Truncated fields: []
- **XD-117** (`tawos-v1.1:3666`), created 2013-05-23T13:36:27.000000Z
  - Title: "\"add spring-integration-groovy to container dependencies\""
  - Description: "\"This will enable the use of groovy scripts within modules.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-135** (`tawos-v1.1:3648`), created 2013-05-28T11:02:56.000000Z
  - Title: "\"Documentation on XD Architecture\""
  - Description: "\"Show overall flow of data in a stream, the server components 'admin' and 'container'.  How modules are deployed.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-140** (`tawos-v1.1:3643`), created 2013-05-28T12:32:46.000000Z
  - Title: "\"Parameterize syslog Source; Add Support for TCP\""
  - Description: "\"The syslog source currently is hard-coded to use udp on port 11111.  Need to parameterize the port and provide an option to use TCP.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-164** (`tawos-v1.1:3619`), created 2013-05-31T08:46:30.000000Z
  - Title: "Validate processing modules declare the required channels"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-173** (`tawos-v1.1:3610`), created 2013-06-03T11:02:50.000000Z
  - Title: "Document how to create a custom input/output module for existing SI channel adapters"
  - Description: "\"Document how to take an existing input/output channel adapters in spring integration and add them as a XD source/sink module.  Should be as end-user focused, step by step guide as possible.  Consider including a getting started gradle/pom.xml \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-174** (`tawos-v1.1:3609`), created 2013-06-03T11:04:12.000000Z
  - Title: "\"Document how to create a custom processor module.\""
  - Description: "\"The use case is to write custom code that does processing on a specific domain class (perhaps from twitter adapter) or a tuple.  Need to package up this code so that it can be used inside XD. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-179** (`tawos-v1.1:3604`), created 2013-06-03T13:57:56.000000Z
  - Title: "\"Have three startup scripts, xd-singlenode, xd-admin, and xd-container\""
  - Description: "\"The xd-singlenode script will launch a main application that creates both the admin node (to process http admin requests) and the container node (to execute modules for data processing) within in the same process   the xd-admin script will launch a main application that creates only the admin node (remove current embeddedContainer options)  the xd-container script will launch a main application that creates only the container node (as it is now)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-180** (`tawos-v1.1:3603`), created 2013-06-03T14:04:10.000000Z
  - Title: "The command line for xd-admin and xd-container to support an additional option, pipeProtocol, that is used to determine the middleware for sending admin requests and data between processing steps"
  - Description: "\"The name 'pipeProtocol' is tentative.    1. The command line scripts for xd-admin and xd-container would support a --pipeProtocol option, with the default being to use Redis.  (Otherwise use xd-singlenode). 2. The xd-admin and xd-container scripts will use the value of pipeProtocol to set the java system property xd.pipeProtocol when launching the app. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Is there cutoff-available acceptance text explaining the intended distribution and colocation behavior beyond the root title?
- Is message conversion in XD-162 sufficient for the intended behavior, and is there actual two-ticket evidence of a specific unmet requirement?

## XD-395 (train)

Historical cutoff: 2013-07-09T09:47:02.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `5b60d23dee905038aed13eb9b85cb71a06fc1537d467dfae82750ed01d097803`

Source input identity SHA-256: `d0f5c284b8f0735b7eb369b42c40d4ffabfefad766818af4a7db6a363ac3755a`

### Supplied historical plan

- **XD-395** (`tawos-v1.1:3399`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-398** (`tawos-v1.1:3396`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-399** (`tawos-v1.1:3395`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-400** (`tawos-v1.1:3394`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-403** (`tawos-v1.1:3391`)
  - Title: "Update Sources HTTP section to use Shell commands instead of curl"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-405** (`tawos-v1.1:3389`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-406** (`tawos-v1.1:3388`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-407** (`tawos-v1.1:3387`)
  - Title: "Update Sources twitter Gemfire CQ section to use Shell commands instead of curl "
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-408** (`tawos-v1.1:3386`)
  - Title: "Update Sources twitter Syslog section to use Shell commands instead of curl "
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-409** (`tawos-v1.1:3385`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-410** (`tawos-v1.1:3384`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-411** (`tawos-v1.1:3383`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-412** (`tawos-v1.1:3382`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-413** (`tawos-v1.1:3381`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-414** (`tawos-v1.1:3380`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-415** (`tawos-v1.1:3379`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-416** (`tawos-v1.1:3378`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-417** (`tawos-v1.1:3377`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-418** (`tawos-v1.1:3376`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-419** (`tawos-v1.1:3375`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-421** (`tawos-v1.1:3373`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root and most observed members have unknown titles and descriptions, and seven members are omitted from the supplied plan. The visible HTTP and Twitter section tasks already request conversion from curl to Shell commands.",
    "XD-223 and XD-202 document Twitter API retirement, but the supplied plan does not identify a Twitter-search example or an API version that remains incompatible; topical overlap cannot establish that this documentation change misses required work.",
    "Other prior tickets describe completed documentation and configuration work, not two comparable failures tied to the visible section edits."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-223** (`tawos-v1.1:3560`), created 2013-06-10T10:51:48.000000Z
  - Title: "Update Creating a Custom Source Module doc with a different SI adapter due to Twitter issues"
  - Description: "\"https://github.com/SpringSource/spring-xd/wiki/Creating-a-Source-Module uses the SI twittersearch inbound channel adapter, which is no longer going to work once Twitter disallows anonymous searches.   Ideally we update the example to use a new version of SI-twitter that adds support for this (as opposed to the XD workaround.)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-78** (`tawos-v1.1:3704`), created 2013-05-20T10:56:33.000000Z
  - Title: "Documentation for \"http | file\" processing"
  - Description: "\"Put on the guide as a section in an 'input sources' wiki page.  https://github.com/springsource/spring-xd/wiki/GuideGettingStarted  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-84** (`tawos-v1.1:3698`), created 2013-05-20T11:00:23.000000Z
  - Title: "\"Documentation for \"\"http | gemfire\"\" processing\""
  - Description: "\"Put on the guide as a section in an 'input-stream' wiki page.   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-111** (`tawos-v1.1:3671`), created 2013-05-23T09:39:54.000000Z
  - Title: "\"Create final distribution zip across multiple projects\""
  - Description: "\"The final directory structure should look like  <install-dir>/xd <install-dir>/redis <install-dir>/gemfire  inside the XD directory   /xd/bin - which has xd-container and xd-admin scripts /xd/lib  inside the gemfire directory /gemfire/bin - has the gemfire-server script /gemfire/lib   inside the redis directory is   /redis/redis-latest-v.x.y.z.tar /redis/README /readis/install-redis  - script that does the basic 4 commands to install redis.   There should be a gradle task that runs after the distZip task, that will take the contents of different project directories, script diretories and 'redis-binary' directories and creates the final layout for the distribution.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-112** (`tawos-v1.1:3670`), created 2013-05-23T11:15:10.000000Z
  - Title: "\"Update XD to Use SI 3.0.0.M2\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-140** (`tawos-v1.1:3643`), created 2013-05-28T12:32:46.000000Z
  - Title: "\"Parameterize syslog Source; Add Support for TCP\""
  - Description: "\"The syslog source currently is hard-coded to use udp on port 11111.  Need to parameterize the port and provide an option to use TCP.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-166** (`tawos-v1.1:3617`), created 2013-05-31T15:58:00.000000Z
  - Title: "\"Create config support based on channel registry type\""
  - Description: "\"We need to have the XD container & admin reading the registry specific property based on the registry type selected.   From Mark F, on one of the code review comments:  Maybe rather than having redis, rabbit, etc. properties all within a container.properties we should rely upon naming conventions instead. Specifically, we could have a single configurable property for the type of channel registry (\"\"redis\"\", \"\"rabbit\"\", or \"\"local\"\" being possible values), and then we could use something like:  <import resource=\"\"config/${registry.type}.xml\"\"/>  <context:property-placeholder location=\"\"config/${registry.type}.properties\"\"/>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-174** (`tawos-v1.1:3609`), created 2013-06-03T11:04:12.000000Z
  - Title: "\"Document how to create a custom processor module.\""
  - Description: "\"The use case is to write custom code that does processing on a specific domain class (perhaps from twitter adapter) or a tuple.  Need to package up this code so that it can be used inside XD. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-192** (`tawos-v1.1:3591`), created 2013-06-04T20:18:58.000000Z
  - Title: "\"Update getting started documentation to use xd-singlenode start script.\""
  - Description: "\"With the new option of starting without requiring redis, the getting started documentation should reflect this easier way to start processing data.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-198** (`tawos-v1.1:3585`), created 2013-06-06T08:50:30.000000Z
  - Title: "DEBUG Stack Trace When Deploying Transformer"
  - Description: "{{curl -X POST -d \"time --interval=3 | transform | log\" http://localhost:8080/streams/test}}\n\nresults in the following stack trace in the DEBUG log. It's apparently benign, but ugly...\n\n{code}\n2013-06-06 10:43:36,875 [task-scheduler-1] DEBUG: org.springframework.scripting.support.ResourceScriptSource - class path resource [transform.groovy] could not be resolved in the file system - current timestamp not available for script modification check\njava.io.FileNotFoundException: class path resource [transform.groovy] cannot be resolved to URL because it does not exist\n\tat org.springframework.core.io.ClassPathResource.getURL(ClassPathResource.java:177)\n\tat org.springframework.core.io.AbstractFileResolvingResource.lastModified(AbstractFileResolvingResource.java:170)\n\tat org.springframework.scripting.support.ResourceScriptSource.retrieveLastModifiedTime(ResourceScriptSource.java:101)\n\tat org.springframework.scripting.support.ResourceScriptSource.getScriptAsString(ResourceScriptSource.java:79)\n\tat org.springframework.integration.scripting.RefreshableResourceScriptSource.<init>(RefreshableResourceScriptSource.java:46)\n\tat sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)\n"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-202** (`tawos-v1.1:3581`), created 2013-06-06T10:51:46.000000Z
  - Title: "\"Update twittersearch module for Twitter 1.0 API retirement\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Do the visible Twitter Gemfire CQ and Syslog sections use the retired Twitter-search API, or a different adapter?
- Are command execution checks and API-version review included in the documentation update acceptance criteria?

## XD-464 (train)

Historical cutoff: 2013-07-13T07:33:10.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `3907b1372c52078bf58716f8c78e9c2784747a2d1878152179e815288df9ce06`

Source input identity SHA-256: `8349a6765839222b7c11614a7aaca58b34becc293555b08e2fcd36be3056ec12`

### Supplied historical plan

- **XD-464** (`tawos-v1.1:3331`)
  - Title: "Spring XD on Hadoop Yarn"
  - Description: null
  - Unknown fields: ["description", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "Only the title Spring XD on Hadoop Yarn identifies the intended work; the historical description and estimate are unknown and no members are observed.",
    "XD-122 describes stale script library versions and XD-193 describes classpath configuration collisions, but the supplied plan does not establish that either mechanism applies to this Yarn implementation.",
    "XD-245 explicitly calls for confirming regular and Hadoop jobs can run, but a validation requirement in another ticket is not evidence that this plan lacks that work. No two supplied tickets establish a sufficiently specific common risk mechanism."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: null
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-108** (`tawos-v1.1:3674`), created 2013-05-23T01:27:49.000000Z
  - Title: "\"Build script should not package 'spring-xd-dirt' scripts \""
  - Description: "\"We are packaging separate scripts to start XDAdmin and XDContainer.  The Gradle application plugin will generate an unwanted 'spring-xd-dirt' scripts, this should be removed from the bin directory when creating a distribution zip.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-109** (`tawos-v1.1:3673`), created 2013-05-23T02:06:01.000000Z
  - Title: "Documentation for starting Spring XD servers"
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-122** (`tawos-v1.1:3661`), created 2013-05-24T17:20:00.000000Z
  - Title: "\"XD scripts need to have spring-integration milestone versions updated\""
  - Description: "\"Spring-integration version is changed to 3.0.0.M2 and since we manually create the XD scripts, they still point to the 3.0.0.BUILD-SNAPSHOT version.  As discussed, we also need to have a better strategy on updating the lib directory inside the XD scripts.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-150** (`tawos-v1.1:3633`), created 2013-05-30T00:06:37.000000Z
  - Title: "\"Publish Spring XD final distribution zip as part of Bamboo artifactory plugin\""
  - Description: "\"Currently, Bamboo's gradle artifactory plugin has the artifacts configured to projects target(build) directory 'archives'. We need to have a way to set the final distribution archive as one of the gradle 'configurations' in our build.gradle and refer it inside bamboo artifacts.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-151** (`tawos-v1.1:3632`), created 2013-05-30T08:17:45.000000Z
  - Title: null
  - Description: "Presently, Spring XD does not ship Windows binaries for Redis. However, Microsoft is actively working [1] on supporting Redis on Windows. You can download Windows Redis binaries from:\n\nhttps://github.com/MSOpenTech/redis/tree/2.6/bin/release \n\n[1] http://blogs.msdn.com/b/interoperability/archive/2013/04/22/redis-on-windows-stable-and-reliable.aspx"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: null
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-171** (`tawos-v1.1:3612`), created 2013-06-03T10:56:35.000000Z
  - Title: "\"Create project home page for SpringXD on springsource.org/spring-xd\""
  - Description: "\"A minimal project page of a 'top level project' page that has basic information of docs and links to the github wiki page.  No need to list maven coordinates.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-173** (`tawos-v1.1:3610`), created 2013-06-03T11:02:50.000000Z
  - Title: "Document how to create a custom input/output module for existing SI channel adapters"
  - Description: "\"Document how to take an existing input/output channel adapters in spring integration and add them as a XD source/sink module.  Should be as end-user focused, step by step guide as possible.  Consider including a getting started gradle/pom.xml \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-193** (`tawos-v1.1:3590`), created 2013-06-05T05:55:48.000000Z
  - Title: "\"Need more unique resource locations for XD internal configuration\""
  - Description: "\"Currently internal config files are in META-INF/spring with fairly generic names. To avoid potential collisions if users add their own configuration in the classpath, we should have a more unique location, e.g. META-INF/spring/xd\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2** (`tawos-v1.1:3770`), created 2013-04-12T06:38:02.000000Z
  - Title: "HDFS Core writing helper classes"
  - Description: "Simple file writer that has existed in the spring hadoop samples."
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What deployment approach and acceptance criteria were recorded for Yarn at this cutoff, and were packaging and runtime checks already included?

## XD-468 (train)

Historical cutoff: 2013-07-13T11:25:58.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `e3735749ec559917e9d19f763264788a2b4af0f8ce1fd8e563b6edc1cc7af895`

Source input identity SHA-256: `45e6d90845a40c06b19a42ab232b5013a1aa6ea03bf83651a30f10f47975d847`

### Supplied historical plan

- **XD-468** (`tawos-v1.1:3327`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-119** (`tawos-v1.1:3664`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-227** (`tawos-v1.1:3556`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-388** (`tawos-v1.1:3403`)
  - Title: "Create design document for implementation strategy for ingesting data from twitter into HDFS that can be analyzed by HAWQ"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-469** (`tawos-v1.1:3326`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-470** (`tawos-v1.1:3325`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-471** (`tawos-v1.1:3324`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-472** (`tawos-v1.1:3323`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-473** (`tawos-v1.1:3322`)
  - Title: "Modify startup script to allow specifying hadoop distro to use"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-474** (`tawos-v1.1:3321`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-475** (`tawos-v1.1:3320`)
  - Title: "Investigate what is needed for an Avro sink for HDFS"
  - Description: null
  - Unknown fields: ["description", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root and seven observed children lack recoverable title and description. The known work includes Hadoop-distribution startup selection (XD-473), Avro sink investigation (XD-475), and a Twitter-to-HDFS/HAWQ design document (XD-388).",
    "XD-207 identifies previously hardcoded HDFS configuration and XD-181 describes protocol-specific launcher imports, but these do not demonstrate an unresolved gap in the supplied distribution-selection task.",
    "XD-279 discusses LZO licensing and file-container choices, not an established Avro failure. Unknown child content prevents treating these topics as omitted requirements."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-162** (`tawos-v1.1:3621`), created 2013-05-31T08:40:14.000000Z
  - Title: "Create design document for implementation strategy to support message conversion in ChannelRegistry"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-174** (`tawos-v1.1:3609`), created 2013-06-03T11:04:12.000000Z
  - Title: "\"Document how to create a custom processor module.\""
  - Description: "\"The use case is to write custom code that does processing on a specific domain class (perhaps from twitter adapter) or a tuple.  Need to package up this code so that it can be used inside XD. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-175** (`tawos-v1.1:3608`), created 2013-06-03T11:06:12.000000Z
  - Title: "\"Create and document a syslog aggregation example\""
  - Description: "\"2-3 containers (separate processes) that the stream: syslog | tcp  1 container (separate process) that aggregates the data sent from those conainers, tcp | severityFilter | hdfs       \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-128** (`tawos-v1.1:3655`), created 2013-05-28T08:36:05.000000Z
  - Title: "\"Create TCP sink module\""
  - Description: "\"Based off SI tcp inbound adapter.  This will allow for event fowarding.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-173** (`tawos-v1.1:3610`), created 2013-06-03T11:02:50.000000Z
  - Title: "Document how to create a custom input/output module for existing SI channel adapters"
  - Description: "\"Document how to take an existing input/output channel adapters in spring integration and add them as a XD source/sink module.  Should be as end-user focused, step by step guide as possible.  Consider including a getting started gradle/pom.xml \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-179** (`tawos-v1.1:3604`), created 2013-06-03T13:57:56.000000Z
  - Title: "\"Have three startup scripts, xd-singlenode, xd-admin, and xd-container\""
  - Description: "\"The xd-singlenode script will launch a main application that creates both the admin node (to process http admin requests) and the container node (to execute modules for data processing) within in the same process   the xd-admin script will launch a main application that creates only the admin node (remove current embeddedContainer options)  the xd-container script will launch a main application that creates only the container node (as it is now)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-187** (`tawos-v1.1:3596`), created 2013-06-03T18:32:06.000000Z
  - Title: "\"Create XD script for xd-single node\""
  - Description: "\"This script will launch XD admin along with the module container.  As part of this implementation, we will also remove the embedded options for XD admin & container scripts.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-192** (`tawos-v1.1:3591`), created 2013-06-04T20:18:58.000000Z
  - Title: "\"Update getting started documentation to use xd-singlenode start script.\""
  - Description: "\"With the new option of starting without requiring redis, the getting started documentation should reflect this easier way to start processing data.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-207** (`tawos-v1.1:3576`), created 2013-06-06T17:17:09.000000Z
  - Title: "\"Provide configurable properties for hdfs sink.\""
  - Description: "\"The config file modules/sink/hdfs.xml has a hardcoded value to locate the namenode.   <hdp:configuration register-url-handler=\"\"false\"\">   fs.default.name=hdfs://localhost:9000  </hdp:configuration>  the fs.default.name proprety should be configurable and we should also support loading an external configuration file using      <hdp:configuration properties-location=\"\"${xd.home}/config/hadoop.properties\"\">     </hdp:configuration>  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-221** (`tawos-v1.1:3562`), created 2013-06-10T10:33:28.000000Z
  - Title: "Links in asciidoctor generated HTML+docbook documentation are broken"
  - Description: "The issue arises because the link:document[Label] asciidoc macro is meant for \"external documents\" and creates {{<ulink>}} in docbook / {{<a href=\"document\">}} in html, whereas we want {{<link linkend=\"anchor\">}} / {{<a href=\"doc#anchor>}} resp. We also want it to continue working in github live view.\n\nI guess what could work is to have the macro (either override the link macro or create our own if github supports that) that looks like :\n{{link:document#anchor[Label]}}  (the #anchor works out of the box in asciidoc and should work in github) but override it for the html and docbook backends to render to the correct form.\n\nThe thing is, there are several ways to create/override macros (and templates they render to), some of which make sense to our setup:\n- having asciidoc.conf in the directory of the processed document (http://asciidoc.org/userguide.html#X27)\n- having docbook.conf/html.conf in the directory of the processed document (http://asciidoc.org/userguide.html#X27)\n- defining macros using attributes (http://asciidoc.org/userguide.html#_setting_configuration_entries)\n\nI tried all of those, but to no avail. These DO WORK with plain asciidoc, but not with our toolchain. Don't k"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-279** (`tawos-v1.1:3508`), created 2013-06-19T09:16:24.000000Z
  - Title: "Support writing to HDFS using the LZO codec"
  - Description: "note, the LZO codes are GPL-licensed, so can't be included in the distribution.\nIt is splittable, which makes it a good candidate for writing without any additional data file container structure such as sequence or avro files."
  - Unknown fields: ["estimate"]
  - Truncated fields: []

### Unresolved labelling questions

- Which acceptance criteria in the unknown children cover Hadoop configuration and format compatibility, and does the visible startup task already cover those concerns?

## XD-484 (train)

Historical cutoff: 2013-07-16T09:30:36.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `71bd1c312db9e32da79a0e6d04fc63262c53aaa5a2667f4d178ccdf1335cadb9`

Source input identity SHA-256: `838f5576c8702632a5cb59c0aebd8173c45cde683952a5b27b7a0b540b11e3a0`

### Supplied historical plan

- **XD-484** (`tawos-v1.1:3311`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-485** (`tawos-v1.1:3310`)
  - Title: "Create stories to enable the use of Spirng Shell's 2.0 branch testing facilities "
  - Description: null
  - Unknown fields: ["description", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The only visible member, XD-485, explicitly plans use of Spring Shell testing facilities; it contradicts a blanket claim that shell testing work is absent.",
    "XD-122 describes an actual Spring Integration script/version mismatch, but the other supplied tickets do not establish a second comparable Spring Shell testing-facility failure.",
    "The root has no known title or description, and XD-485 has no known description, so the intended framework migration or test coverage cannot be inferred."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-467** (`tawos-v1.1:3328`), created 2013-07-12T10:17:45.000000Z
  - Title: null
  - Description: "There's a lifecycle problem when a tap creation fails (e.g. because the DSL syntax is wrong). Subsequence attempts to create the tap will fail with an error:\n\n [{\"links\":[],\"logref\":\"MessageHandlingException\",\"message\":\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"}]\n\nDisabling JMX solves the issue."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-112** (`tawos-v1.1:3670`), created 2013-05-23T11:15:10.000000Z
  - Title: "\"Update XD to Use SI 3.0.0.M2\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-117** (`tawos-v1.1:3666`), created 2013-05-23T13:36:27.000000Z
  - Title: "\"add spring-integration-groovy to container dependencies\""
  - Description: "\"This will enable the use of groovy scripts within modules.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-122** (`tawos-v1.1:3661`), created 2013-05-24T17:20:00.000000Z
  - Title: "\"XD scripts need to have spring-integration milestone versions updated\""
  - Description: "\"Spring-integration version is changed to 3.0.0.M2 and since we manually create the XD scripts, they still point to the 3.0.0.BUILD-SNAPSHOT version.  As discussed, we also need to have a better strategy on updating the lib directory inside the XD scripts.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-14** (`tawos-v1.1:3761`), created 2013-04-12T06:48:58.000000Z
  - Title: "Design for deploying DIRT Runtime on EC2"
  - Description: "create enough of a design to develop additional stories."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-143** (`tawos-v1.1:3640`), created 2013-05-28T16:26:55.000000Z
  - Title: "Create externalized property file to support connectivity to redis"
  - Description: "\"We need to have an externalized property file(under xd/conf/) for the xd-container & admin scripts to use as options. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-166** (`tawos-v1.1:3617`), created 2013-05-31T15:58:00.000000Z
  - Title: "\"Create config support based on channel registry type\""
  - Description: "\"We need to have the XD container & admin reading the registry specific property based on the registry type selected.   From Mark F, on one of the code review comments:  Maybe rather than having redis, rabbit, etc. properties all within a container.properties we should rely upon naming conventions instead. Specifically, we could have a single configurable property for the type of channel registry (\"\"redis\"\", \"\"rabbit\"\", or \"\"local\"\" being possible values), and then we could use something like:  <import resource=\"\"config/${registry.type}.xml\"\"/>  <context:property-placeholder location=\"\"config/${registry.type}.properties\"\"/>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-174** (`tawos-v1.1:3609`), created 2013-06-03T11:04:12.000000Z
  - Title: "\"Document how to create a custom processor module.\""
  - Description: "\"The use case is to write custom code that does processing on a specific domain class (perhaps from twitter adapter) or a tuple.  Need to package up this code so that it can be used inside XD. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-175** (`tawos-v1.1:3608`), created 2013-06-03T11:06:12.000000Z
  - Title: "\"Create and document a syslog aggregation example\""
  - Description: "\"2-3 containers (separate processes) that the stream: syslog | tcp  1 container (separate process) that aggregates the data sent from those conainers, tcp | severityFilter | hdfs       \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-180** (`tawos-v1.1:3603`), created 2013-06-03T14:04:10.000000Z
  - Title: "The command line for xd-admin and xd-container to support an additional option, pipeProtocol, that is used to determine the middleware for sending admin requests and data between processing steps"
  - Description: "\"The name 'pipeProtocol' is tentative.    1. The command line scripts for xd-admin and xd-container would support a --pipeProtocol option, with the default being to use Redis.  (Otherwise use xd-singlenode). 2. The xd-admin and xd-container scripts will use the value of pipeProtocol to set the java system property xd.pipeProtocol when launching the app. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-197** (`tawos-v1.1:3586`), created 2013-06-06T06:26:25.000000Z
  - Title: "\"Create a scriptProcessor module that allows the execution of a groovy (potentially jruby,jython) based SI Service Activator\""
  - Description: "\"This will enable arbitrary processing logic to be used in a processing step.  See http://blog.springsource.org/2011/12/08/spring-integration-scripting-support-part-1/  <int:service-activator ...>   <script:script lang=\"\"groovy\"\" location=\"\"file:scripts/groovy/myscript.groovy\"\"> </int:service-activator>  would be the essence of the module.  Probably 'lang' gets detected from the file extension.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-21** (`tawos-v1.1:3756`), created 2013-04-16T11:18:31.000000Z
  - Title: "\"Create syslog.xml file for module registry\""
  - Description: "\"Consider which properties of the syslog namespace need to use property placeholders\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What shell versions and release steps were intended by XD-485 at this cutoff?
- Did the missing historical descriptions define integration-test setup and coverage, rather than leave those tasks outside the plan?

## XD-527 (train)

Historical cutoff: 2013-07-23T09:57:18.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `b466c1ec87dc7490d8323f9e999a20aa6d2ffae3aa3b6590e43b6f6046f4ee73`

Source input identity SHA-256: `6acff057dd3ba2335b98550cce1af0c322485083f7ee049b9b30a76af09e1dbf`

### Supplied historical plan

- **XD-527** (`tawos-v1.1:3268`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-528** (`tawos-v1.1:3267`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-529** (`tawos-v1.1:3266`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-530** (`tawos-v1.1:3265`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-531** (`tawos-v1.1:3264`)
  - Title: "Integration test for syslog-tcp-reactor module"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-527 and XD-528 through XD-530 have unknown historical titles and descriptions. The only known member title, XD-531, explicitly schedules a syslog-tcp-reactor integration test.",
    "XD-127, XD-128, XD-140 and XD-26 describe completed TCP, syslog configuration and performance work; they do not show two failures in the planned Reactor module.",
    "XD-10 concerns Reactor HTTP ingestion, while XD-198 describes an apparently benign transformer logging issue. Neither establishes a specific unmet requirement or failing dependency in this supplied plan."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-10** (`tawos-v1.1:3765`), created 2013-04-12T06:44:57.000000Z
  - Title: "Reactor based http ingestion"
  - Description: "When there is support for boostrapping a http server in the reactor project, and inbound SI adapter and associated XD source module should be created."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-127** (`tawos-v1.1:3656`), created 2013-05-28T08:35:42.000000Z
  - Title: "\"Create TCP source module\""
  - Description: "Based off SI tcp inbound adapter.  This will allow for event forwarding that can select among the existing SI serialized/deserializer options.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-128** (`tawos-v1.1:3655`), created 2013-05-28T08:36:05.000000Z
  - Title: "\"Create TCP sink module\""
  - Description: "\"Based off SI tcp inbound adapter.  This will allow for event fowarding.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-140** (`tawos-v1.1:3643`), created 2013-05-28T12:32:46.000000Z
  - Title: "\"Parameterize syslog Source; Add Support for TCP\""
  - Description: "\"The syslog source currently is hard-coded to use udp on port 11111.  Need to parameterize the port and provide an option to use TCP.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-173** (`tawos-v1.1:3610`), created 2013-06-03T11:02:50.000000Z
  - Title: "Document how to create a custom input/output module for existing SI channel adapters"
  - Description: "\"Document how to take an existing input/output channel adapters in spring integration and add them as a XD source/sink module.  Should be as end-user focused, step by step guide as possible.  Consider including a getting started gradle/pom.xml \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-175** (`tawos-v1.1:3608`), created 2013-06-03T11:06:12.000000Z
  - Title: "\"Create and document a syslog aggregation example\""
  - Description: "\"2-3 containers (separate processes) that the stream: syslog | tcp  1 container (separate process) that aggregates the data sent from those conainers, tcp | severityFilter | hdfs       \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-197** (`tawos-v1.1:3586`), created 2013-06-06T06:26:25.000000Z
  - Title: "\"Create a scriptProcessor module that allows the execution of a groovy (potentially jruby,jython) based SI Service Activator\""
  - Description: "\"This will enable arbitrary processing logic to be used in a processing step.  See http://blog.springsource.org/2011/12/08/spring-integration-scripting-support-part-1/  <int:service-activator ...>   <script:script lang=\"\"groovy\"\" location=\"\"file:scripts/groovy/myscript.groovy\"\"> </int:service-activator>  would be the essence of the module.  Probably 'lang' gets detected from the file extension.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-198** (`tawos-v1.1:3585`), created 2013-06-06T08:50:30.000000Z
  - Title: "DEBUG Stack Trace When Deploying Transformer"
  - Description: "{{curl -X POST -d \"time --interval=3 | transform | log\" http://localhost:8080/streams/test}}\n\nresults in the following stack trace in the DEBUG log. It's apparently benign, but ugly...\n\n{code}\n2013-06-06 10:43:36,875 [task-scheduler-1] DEBUG: org.springframework.scripting.support.ResourceScriptSource - class path resource [transform.groovy] could not be resolved in the file system - current timestamp not available for script modification check\njava.io.FileNotFoundException: class path resource [transform.groovy] cannot be resolved to URL because it does not exist\n\tat org.springframework.core.io.ClassPathResource.getURL(ClassPathResource.java:177)\n\tat org.springframework.core.io.AbstractFileResolvingResource.lastModified(AbstractFileResolvingResource.java:170)\n\tat org.springframework.scripting.support.ResourceScriptSource.retrieveLastModifiedTime(ResourceScriptSource.java:101)\n\tat org.springframework.scripting.support.ResourceScriptSource.getScriptAsString(ResourceScriptSource.java:79)\n\tat org.springframework.integration.scripting.RefreshableResourceScriptSource.<init>(RefreshableResourceScriptSource.java:46)\n\tat sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)\n"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-21** (`tawos-v1.1:3756`), created 2013-04-16T11:18:31.000000Z
  - Title: "\"Create syslog.xml file for module registry\""
  - Description: "\"Consider which properties of the syslog namespace need to use property placeholders\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-26** (`tawos-v1.1:3752`), created 2013-04-16T11:30:13.000000Z
  - Title: "\"Basic Performance Test For syslog injestion\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-313** (`tawos-v1.1:3476`), created 2013-06-25T05:19:12.000000Z
  - Title: "Add Spring/Integration MBean Exporters to Module ApplicationContexts"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Unresolved labelling questions

- What cutoff-available acceptance criteria define the Reactor syslog work and XD-531 integration test?
- Are any of the supplied prior incidents demonstrably applicable to Reactor TCP ingestion, rather than merely sharing transport or module terminology?

## XD-697 (train)

Historical cutoff: 2013-08-15T11:50:47.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `d283971e0a5f628459d5fcb987c5f4063bb6d675601a72c08fbffbf567c01cf8`

Source input identity SHA-256: `aa9ff6857c8fa07e0a31ca969c29c2a7effd4eacde67c037c4b6f5dfe45269f1`

### Supplied historical plan

- **XD-697** (`tawos-v1.1:3103`)
  - Title: null
  - Description: "Should be simple to test in isolation but also across transports (stream testing)"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-203** (`tawos-v1.1:3580`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-304** (`tawos-v1.1:3484`)
  - Title: null
  - Description: "Be able to point to the processor xml file, e.g. modules/processors/transformer.xml, and have access to a source channel that drives messages into the processor and a output channel where output messages are send.  The outbound channel is queue backed.\n\nTest sending JSON to a processor module that uses Tuples.\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-305** (`tawos-v1.1:3483`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-306** (`tawos-v1.1:3482`)
  - Title: null
  - Description: "Examples:\n1. Be able to start the rabbitmq source just by pointing to modules/source/rabbit.xml, pass in some property file for parameters to be replaced, and outgoing message is placed in a in-memory queue backed channel for use with assertions to verify functionality.  \n2. Test for as many source types as is 'reasonable', e.g. MQTT/TCP testing might be harder than say rabbitmq.\n3. Test that sending json, results in media-type header is set to json\n4. Test that sending POJO,   \"  POJO\n5. Test that sending Tuple, \"   Tuple\n6. Test that sending raw bytes, \" raw bytes\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-307** (`tawos-v1.1:3481`)
  - Title: "User to send a message directly to module and receive a message a module"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root explicitly includes isolation and cross-transport stream testing; XD-304 and XD-306 specify message/content-type assertions but do not restrict all tests to successful flows.",
    "XD-467 supplies an unresolved failed-create/retry mechanism and XD-476 supplies a completed Redis destroy/recreate fault, but no supplied plan text shows that the new test design excludes or mishandles either lifecycle.",
    "XD-203 and other child text is unknown, so lifecycle coverage remains an unresolved review question rather than a supported missing-work risk."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-592** (`tawos-v1.1:3205`), created 2013-08-01T12:44:18.000000Z
  - Title: "Problems with advanced tapping"
  - Description: "Start of a test program that can be placed in StreamCommandTests:\n\n{code}\n@Test\npublic void testTappingAndChannels() {\n  executeStreamCreate(\"myhttp\",\"http --port=9314 | transform --expression=payload.toUpperCase() | log\",true);\n  executeStreamCreate(\"tap\",\"tap @myhttp.1 | log\",true);\t\t\n  executeStreamCreate(\"tap_new\",\"tap myhttp.1 > log\",true);\t\t\t\t\n  executeCommand(\"http post --data Dracarys! --target http://localhost:9314\");\n  // TODO verify both logs output DRACARYS!\n}\n\n{code}\n\nIn the test program see two taps. One using the older style and one using the newer style and '>' so that there is no real tap module source, the log module just gets its input channel wired directly to myhttp.1 (the output of transform).  They should be doing the same thing.  However when run the output for tap_new is missing, all I see is:\n\n{code}\n11:39:36,055  WARN New I/O worker #28 logger.tap:141 - DRACARYS!\n11:39:36,059  WARN New I/O worker #28 logger.myhttp:141 - DRACARYS!\n{code}\n\nNo errors are reported, there is just no output for tap_new."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-614** (`tawos-v1.1:3184`), created 2013-08-06T12:14:45.000000Z
  - Title: "\"Conversion Enhancements\""
  - Description: "\"Content-Type during transport transit is not the same as the content-type within modules.  \"\"Real\"\" transports always use byte[] which may contain raw byte[] from a source, a byte[] converted from a String (which may or may not already contain JSON), or a byte[] containing JSON converted by the transport on the outbound side.  The transport needs to convey which of these was applied on the outbound side so it can properly reconstruct the message.  Retain any content-type header that already exists in the message, and restore it.  For Rabbit, use normal SI/Rabbit headers to convey this information.  For Redis, add the information to the byte[].\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-438** (`tawos-v1.1:3356`), created 2013-07-10T08:51:08.000000Z
  - Title: "\"More DSL work: exploiting source/sink channels\""
  - Description: "\"The DSL changes under XD-369 now build stream Ast objects that can include a source and sink channel:  {code} // Source Channel :mystream.foo > count | log  // Sink Channel http | count > :foo {code}  These new fields in the Ast object need to be copied into the module deployment request objects and then used at the destination as the channels for wiring things together.  Currently the only channels used are the .NNN numeric channels where NNN is the index of the module in the stream definition. The source/sink channels are 'extra' channels that need creating - the source channel acting as a real source for the next module in the chain whilst the sink channel acts as a sink output for the last channel in the chain.    I can think of two ways to handle the implementation: - In order to police the stream structure as \"\"source | processor* | sink\"\" maybe special SourceChannel and SinkChannel modules are created to represent these channels and when deployment happens the deployer understands that they don't represent a real request to deploy a module but simply the channels to wire up to the adjacent module.  - Carry source/sink channel info in the existing module definitions. But the"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-555** (`tawos-v1.1:3240`), created 2013-07-26T07:50:54.000000Z
  - Title: "\"make application/json the default output type for the REST API?\""
  - Description: "the top-level URL works via simple curl (without an Accept header) or the browser:\n\n{code}\n> curl http://localhost:8080\n\n{\"links\":[{\"rel\":\"streams\",\"href\":\"http://localhost:8080/streams\"},{\"rel\":\"triggers\",\"href\":\"http://localhost:8080/triggers\"},{\"rel\":\"jobs\",\"href\":\"http://localhost:8080/jobs\"},{\"rel\":\"taps\",\"href\":\"http://localhost:8080/taps\"},{\"rel\":\"counters\",\"href\":\"http://localhost:8080/metrics/counters\"}]}\n{code}\n\nHowever, trying any of those links then fails, e.g.:\n\n{code}\n> curl http://localhost:8080/streams\n\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><errors xmlns:ns2=\"http://www.w3.org/2005/Atom\"><error logref=\"HttpMessageNotWritableException\"><message>Could not marshal [PagedResource { content: [links: [&lt;http://localhost:8080/streams/mqttdemo&gt;;rel=&quot;self&quot;]], metadata: Metadata { number: 0, total pages: 1, total elements: 1, size: 20 }, links: [] }]: null; nested exception is javax.xml.bind.MarshalException\n - with linked exception:\n[com.sun.istack.internal.SAXException2: unable to marshal type &quot;org.springframework.xd.rest.client.domain.StreamDefinitionResource&quot; as an element because it is not known to this context.]</message></error"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-230** (`tawos-v1.1:3553`), created 2013-06-17T08:53:27.000000Z
  - Title: "Add RabbitMQ source module"
  - Description: "\"configurable parameters should include the queue-name(s) and optional binding key pattern  connection info, such as host and port, should also be configurable but with defaults (localhost and default port), and that should likely fallback to a rabbit.properties file in the $XD_HOME/config directory\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-467** (`tawos-v1.1:3328`), created 2013-07-12T10:17:45.000000Z
  - Title: null
  - Description: "There's a lifecycle problem when a tap creation fails (e.g. because the DSL syntax is wrong). Subsequent attempts to create the tap will fail with an error:\n\n [{\"links\":[],\"logref\":\"MessageHandlingException\",\"message\":\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"}]\n\nDisabling JMX solves the issue.\n\n\nreproduce\nCreate a bad stream definition name 'bad'\nTry to recreate with the same name, but correct stream definitions.  The system will report that the stream already exists."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-476** (`tawos-v1.1:3319`), created 2013-07-13T09:14:32.000000Z
  - Title: "The stream definition is not deleted in redis container when the stream is destroyed"
  - Description: "\"This only happened with distributed mode that uses redis as store. The single mode which uses in memory store works fine.  Step to reproduce:  Create stream: curl -X POST -d \"\"name=httptest\"\" -d \"\"definition=http|log\"\" http://localhost:8080/streams  redis 127.0.0.1:6379> keys *httptest* 1) \"\"modules:httptest\"\" 2) \"\"streams.httptest\"\" 3) \"\"stream.definitions.httptest\"\"  Delete Stream: curl -X DELETE http://localhost:8080/streams/httptest  redis 127.0.0.1:6379> keys *httptest* 1) \"\"streams.httptest\"\" 2) \"\"stream.definitions.httptest\"\"  stream still there not deleted  Recreate the stream curl -X POST -d \"\"name=httptest\"\" -d \"\"definition=http|log\"\" http://localhost:8080/streams  Got: <?xml version=\"\"1.0\"\" encoding=\"\"UTF-8\"\" standalone=\"\"yes\"\"?><errors xmlns:ns2=\"\"http://www.w3.org/2005/Atom\"\"><error logref=\"\"StreamAlreadyExistsException\"\"><message>There is already a stream with name 'httptest'</message></error>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-588** (`tawos-v1.1:3208`), created 2013-07-30T13:06:09.000000Z
  - Title: "\"RedisAggregateCounterRepository doesn't give proper results back\""
  - Description: "\"Both Luke's original code and my refactored PR[1] (which uses same code snippet) seem to behave strangely.  Stored values seem fine, but the getCounts() method seems phony.  To test: 1) stream create foo --definition \"\"time|log\"\" 2) tap create bar --definition \"\"tap@foo | aggregatecounter\"\" 3) curl -H \"\"application/json\"\" http://localhost:8080/metrics/aggregate-counters/bar  this gives default bucketing (hourly) but chances are that they are empty. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: "\"Create distributable artifact that contains server application and start/stop scripts\""
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-617** (`tawos-v1.1:3181`), created 2013-08-06T16:55:47.000000Z
  - Title: "\"Making an http post with json double quoted will hang the shell.\""
  - Description: "\"Was following the (now updated) directions for gemfire-cq source.  xd:> stream create --name stocks --definition \"\"http --port=9090 | gemfire-json-server --regionName=Stocks --keyExpression=payload.getField('symbol')\"\" xd:> stream create --name cqtest --definition \"\"gemfire-cq --query='Select * from /Stocks where symbol=''VMW''' | file\"\" xd:> http post --target http://localhost:9090 --data \"\"{\"\"symbol\"\":\"\"VMW\"\", \"\"price\"\":73}\"\"  The double quotes were causing a problem with xd-singlenode  Aug 06, 2013 5:38:15 PM org.jboss.netty.channel.SimpleChannelUpstreamHandler WARNING: EXCEPTION, please implement org.springframework.integration.x.http.NettyHttpInboundChannelAdapter$Handler.exceptionCaught() for proper handling. org.springframework.integration.transformer.MessageTransformationException: org.springframework.integration.MessageHandlingException: org.springframework.integration.transformer.MessageTransformationException: Expected a ':' after a key at 22 [character 23 line 1]  at org.springframework.integration.transformer.MessageTransformingHandler.handleRequestMessage(MessageTransformingHandler.java:73)  at org.springframework.integration.handler.AbstractReplyProducingMessageHand"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Do the cutoff-bound specifications include corrected-create and destroy/recreate lifecycle tests?
- Would the proposed harness actually invoke the JMX/Redis deployment paths in XD-467 and XD-476, or only isolated module contexts?

## XD-706 (train)

Historical cutoff: 2013-08-20T12:21:24.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `751c193701f1ec52291ddfdd6ac2b3032e4ca922c6698dc60122e7c7e1e01368`

Source input identity SHA-256: `63bb79371e7157d69ead5a5329a2c64bc05a91f2c003ed6102f69562133abe05`

### Supplied historical plan

- **XD-706** (`tawos-v1.1:3094`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-353** (`tawos-v1.1:3437`)
  - Title: "Clean up Spring Configuration"
  - Description: "- Container context should be separate from Admin Context in local mode (consistency across transports). Provide a LocalChannelRegistry to bridge deploy and undeploy channels to the ModuleDeployer\n\n- Verify Plugins are not in common module context. They are only needed by the ModuleDeployer not the Modules.\n\n- Add global-beans Config for beans to be shared among admin and container (and available to modules). This would be set as the parent context where needed. (Currently ‘analytics-context.xml’ and JobRepository shared by Admin and modules)\n\n- Fix ModuleDeployer sets parentContext twice\n- Rename common.xml to module-common.xml\n\nNOTE: Analytics parent only required in local mode\n\n- Write unit tests to verify configurations are as expected. Correct bean implementations and no stray beans or redundant instances where not needed\n\n- Decouple Command options from System properties (in general XD property names), this gives us some flexibility in mapping to properties or profiles where appropriate\n"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-707** (`tawos-v1.1:3093`)
  - Title: "Support use of separate control and message transport in XD"
  - Description: null
  - Unknown fields: ["description"]
  - Truncated fields: []
- **XD-708** (`tawos-v1.1:3092`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-709** (`tawos-v1.1:3091`)
  - Title: null
  - Description: "Remove unnecessary code that adds beans to shared context after refresh\nScheduler should not be in common.xml - register it in TriggerPlugin.postProcessSharedContext()"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-710** (`tawos-v1.1:3090`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-711** (`tawos-v1.1:3089`)
  - Title: "MBeanServer should not be declared in module common configuration"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-712** (`tawos-v1.1:3088`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-713** (`tawos-v1.1:3087`)
  - Title: "Consider replacing XML with @Configuration classes where appropriate"
  - Description: "\n"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-714** (`tawos-v1.1:3086`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-645 identifies Redis/Rabbit property-loading conflicts and XD-544 identifies duplicate analytics repositories, but plan member XD-353 already requires separate Admin/Container contexts, shared parent beans and unit tests for correct implementations and redundant instances. Those incidents therefore do not establish omitted configuration or validation work.",
    "XD-711 explicitly removes the MBeanServer from module-common configuration, addressing the same broad isolation concern raised by the supplied duplicate-MBean error in XD-465.",
    "Unknown root text and several unknown member descriptions leave the intended breadth of transport-combination testing unverified; this is an evidence limitation rather than a demonstrated validation gap."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: null
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: ["title", "type"]
  - Truncated fields: ["description"]
- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-166** (`tawos-v1.1:3617`), created 2013-05-31T15:58:00.000000Z
  - Title: "\"Create config support based on channel registry type\""
  - Description: "\"We need to have the XD container & admin reading the registry specific property based on the registry type selected.   From Mark F, on one of the code review comments:  Maybe rather than having redis, rabbit, etc. properties all within a container.properties we should rely upon naming conventions instead. Specifically, we could have a single configurable property for the type of channel registry (\"\"redis\"\", \"\"rabbit\"\", or \"\"local\"\" being possible values), and then we could use something like:  <import resource=\"\"config/${registry.type}.xml\"\"/>  <context:property-placeholder location=\"\"config/${registry.type}.properties\"\"/>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-645** (`tawos-v1.1:3153`), created 2013-08-08T20:56:37.000000Z
  - Title: null
  - Description: "Need to undo the recent add of rabbit.properties to xd-common.xml. Tried to work around this by configuring rabbit-container with only the PPC it needs (pointing to only rabbit.properties), but this caused issues with redis-analytics later requiring redis.properties. Would be nice to have a way for redis-analytics to contribute redis.properties or something similar...\n\n\nAlso, strictly speaking, the local admin server does not even need redis.properties, let alone rabbit.properties, so we should find a cleaner way to configure this."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-438** (`tawos-v1.1:3356`), created 2013-07-10T08:51:08.000000Z
  - Title: "\"More DSL work: exploiting source/sink channels\""
  - Description: "\"The DSL changes under XD-369 now build stream Ast objects that can include a source and sink channel:  {code} // Source Channel :mystream.foo > count | log  // Sink Channel http | count > :foo {code}  These new fields in the Ast object need to be copied into the module deployment request objects and then used at the destination as the channels for wiring things together.  Currently the only channels used are the .NNN numeric channels where NNN is the index of the module in the stream definition. The source/sink channels are 'extra' channels that need creating - the source channel acting as a real source for the next module in the chain whilst the sink channel acts as a sink output for the last channel in the chain.    I can think of two ways to handle the implementation: - In order to police the stream structure as \"\"source | processor* | sink\"\" maybe special SourceChannel and SinkChannel modules are created to represent these channels and when deployment happens the deployer understands that they don't represent a real request to deploy a module but simply the channels to wire up to the adjacent module.  - Carry source/sink channel info in the existing module definitions. But the"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-544** (`tawos-v1.1:3251`), created 2013-07-25T04:34:09.000000Z
  - Title: "\"Fix In-Memory Analytics\""
  - Description: "\"Most of the infrastructure and code cleanup has been done for In-Memory Analytics. The only remaining issue is that, by including memory-analytics.xml from common.xml, we're actually creating e.g. a new InMemoryCounterRepository that is different from the one present in the Admin process space.  This story involves fixing that. It may actually be done as part of XD-353, handling the \"\"local\"\" transport as a special case (context inheritance) rather than import based on xd.transport\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-180** (`tawos-v1.1:3603`), created 2013-06-03T14:04:10.000000Z
  - Title: "The command line for xd-admin and xd-container to support an additional option, pipeProtocol, that is used to determine the middleware for sending admin requests and data between processing steps"
  - Description: "\"The name 'pipeProtocol' is tentative.    1. The command line scripts for xd-admin and xd-container would support a --pipeProtocol option, with the default being to use Redis.  (Otherwise use xd-singlenode). 2. The xd-admin and xd-container scripts will use the value of pipeProtocol to set the java system property xd.pipeProtocol when launching the app. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-537** (`tawos-v1.1:3258`), created 2013-07-23T09:39:59.000000Z
  - Title: "Refactor analytics to get rid of Services"
  - Description: "\"This story corresponds to 3) & 4) in discussion below.     Currently, sink xml files define the Repository (hardcoded to be redis) and the services (tied to Redis as well!)   I want to:   1) Move those definitions out of the sink files, to somewhere shared by both admin and container   2) Make them aware of some configuration parameter (similar to the --store command line option)    3) Get rid of so-called Service layer (doesn't do much right now, and logic would better live in the 'Handler' IMO)   4) Have REST controllers depend on XRepository in all cases\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Do XD-353 configuration tests cover Redis, Rabbit and local mode with different control/message transport combinations introduced by XD-707?
- Does the existing configuration test plan explicitly assert analytics repository sharing and MBean isolation?

## XD-742 (train)

Historical cutoff: 2013-08-23T14:18:55.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `defdfced3ee82859d098f17460ac238bfaa6140cfe874d927368ba5147589388`

Source input identity SHA-256: `0a0bb2080064bcee264c40de9fbd77d9e01176431786053775b64e90bc8888bb`

### Supplied historical plan

- **XD-742** (`tawos-v1.1:3058`)
  - Title: null
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-743** (`tawos-v1.1:3057`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-744** (`tawos-v1.1:3056`)
  - Title: null
  - Description: "We should depend on\n\n\t\t<dependency>\n\t\t\t<groupId>org.springframework.batch</groupId>\n\t\t\t<artifactId>spring-batch-admin-manager</artifactId>\n\t\t\t<version>${project.parent.version}</version>\n\t\t</dependency>\n\t\t<dependency>\n\t\t\t<groupId>org.springframework.batch</groupId>\n\t\t\t<artifactId>spring-batch-admin-resources</artifactId>\n\t\t\t<version>${project.parent.version}</version>\n\t\t</dependency>\n\nwe are using spring batch 2.2.0.RELEASE. \n\nWe need to depend on spring-batch-admin version 1.3.0.BUILD-SNAPSHOT\n\n "
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-745** (`tawos-v1.1:3055`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-555 concerns StreamDefinitionResource XML marshalling; the imported job-controller response types and representation mappings are not supplied, so applicability is unverified.",
    "XD-556 concerns a cross-origin Kodiak deployment, but no deployment origin for the intended UI is supplied. Both cited incidents are Done at this cutoff.",
    "Unknown XD-743/XD-745 text and the missing endpoint attachment do not establish that compatibility checks are omitted."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: null
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: ["title", "type"]
  - Truncated fields: ["description"]
- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-438** (`tawos-v1.1:3356`), created 2013-07-10T08:51:08.000000Z
  - Title: "\"More DSL work: exploiting source/sink channels\""
  - Description: "\"The DSL changes under XD-369 now build stream Ast objects that can include a source and sink channel:  {code} // Source Channel :mystream.foo > count | log  // Sink Channel http | count > :foo {code}  These new fields in the Ast object need to be copied into the module deployment request objects and then used at the destination as the channels for wiring things together.  Currently the only channels used are the .NNN numeric channels where NNN is the index of the module in the stream definition. The source/sink channels are 'extra' channels that need creating - the source channel acting as a real source for the next module in the chain whilst the sink channel acts as a sink output for the last channel in the chain.    I can think of two ways to handle the implementation: - In order to police the stream structure as \"\"source | processor* | sink\"\" maybe special SourceChannel and SinkChannel modules are created to represent these channels and when deployment happens the deployer understands that they don't represent a real request to deploy a module but simply the channels to wire up to the adjacent module.  - Carry source/sink channel info in the existing module definitions. But the"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-476** (`tawos-v1.1:3319`), created 2013-07-13T09:14:32.000000Z
  - Title: "The stream definition is not deleted in redis container when the stream is destroyed"
  - Description: "\"This only happened with distributed mode that uses redis as store. The single mode which uses in memory store works fine.  Step to reproduce:  Create stream: curl -X POST -d \"\"name=httptest\"\" -d \"\"definition=http|log\"\" http://localhost:8080/streams  redis 127.0.0.1:6379> keys *httptest* 1) \"\"modules:httptest\"\" 2) \"\"streams.httptest\"\" 3) \"\"stream.definitions.httptest\"\"  Delete Stream: curl -X DELETE http://localhost:8080/streams/httptest  redis 127.0.0.1:6379> keys *httptest* 1) \"\"streams.httptest\"\" 2) \"\"stream.definitions.httptest\"\"  stream still there not deleted  Recreate the stream curl -X POST -d \"\"name=httptest\"\" -d \"\"definition=http|log\"\" http://localhost:8080/streams  Got: <?xml version=\"\"1.0\"\" encoding=\"\"UTF-8\"\" standalone=\"\"yes\"\"?><errors xmlns:ns2=\"\"http://www.w3.org/2005/Atom\"\"><error logref=\"\"StreamAlreadyExistsException\"\"><message>There is already a stream with name 'httptest'</message></error>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-485** (`tawos-v1.1:3310`), created 2013-07-15T09:34:37.000000Z
  - Title: "Create stories to enable the use of Spring Shell's 2.0 branch testing facilities "
  - Description: "\"We need a few steps 1. Investigate if we need to move off Spring Shell 1.0 dependency, e.g. need to use code in Spring Shell 2.0 branch 2. If we need to use code in Spring Shell 2.0 branch, we need to release a Spring Shell 1.1 M1 release with appropriate code changes.  Create stories related to Shell release. 3. Determine and document the basic recipe for doing integration tests. 4. Create stories to provide integration tests for each existing command\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-555** (`tawos-v1.1:3240`), created 2013-07-26T07:50:54.000000Z
  - Title: "\"make application/json the default output type for the REST API?\""
  - Description: "the top-level URL works via simple curl (without an Accept header) or the browser:\n\n{code}\n> curl http://localhost:8080\n\n{\"links\":[{\"rel\":\"streams\",\"href\":\"http://localhost:8080/streams\"},{\"rel\":\"triggers\",\"href\":\"http://localhost:8080/triggers\"},{\"rel\":\"jobs\",\"href\":\"http://localhost:8080/jobs\"},{\"rel\":\"taps\",\"href\":\"http://localhost:8080/taps\"},{\"rel\":\"counters\",\"href\":\"http://localhost:8080/metrics/counters\"}]}\n{code}\n\nHowever, trying any of those links then fails, e.g.:\n\n{code}\n> curl http://localhost:8080/streams\n\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><errors xmlns:ns2=\"http://www.w3.org/2005/Atom\"><error logref=\"HttpMessageNotWritableException\"><message>Could not marshal [PagedResource { content: [links: [&lt;http://localhost:8080/streams/mqttdemo&gt;;rel=&quot;self&quot;]], metadata: Metadata { number: 0, total pages: 1, total elements: 1, size: 20 }, links: [] }]: null; nested exception is javax.xml.bind.MarshalException\n - with linked exception:\n[com.sun.istack.internal.SAXException2: unable to marshal type &quot;org.springframework.xd.rest.client.domain.StreamDefinitionResource&quot; as an element because it is not known to this context.]</message></error"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-556** (`tawos-v1.1:3239`), created 2013-07-26T10:52:10.000000Z
  - Title: "\"CORS support\""
  - Description: "\"XD instances will not accept xhr requests from browsers whose page origin does not match the XD instance.    As an example, the Kodiak UI is served from a different process (and url) than the XD instance.  When users open the Kodiak UI in a browser, requests from the browser to the XD instance, but these requests will fail due to cross-site scripting limitations.  CORS (Cross-Origin Resource Sharing) is a way to get around this.  We can configure the server to accept requests from browsers whose origins are not the XD instance.  I have this working in a local branch and will submit a pull request.   More information: CORS Spec: http://www.w3.org/TR/cors/ SPR-9278 CORS support for SpringFramework \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-588** (`tawos-v1.1:3208`), created 2013-07-30T13:06:09.000000Z
  - Title: "\"RedisAggregateCounterRepository doesn't give proper results back\""
  - Description: "\"Both Luke's original code and my refactored PR[1] (which uses same code snippet) seem to behave strangely.  Stored values seem fine, but the getCounts() method seems phony.  To test: 1) stream create foo --definition \"\"time|log\"\" 2) tap create bar --definition \"\"tap@foo | aggregatecounter\"\" 3) curl -H \"\"application/json\"\" http://localhost:8080/metrics/aggregate-counters/bar  this gives default bucketing (hourly) but chances are that they are empty. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: "\"Create distributable artifact that contains server application and start/stop scripts\""
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: null
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Unresolved labelling questions

- Which exact job-controller resource types and content-negotiation mappings will be imported into XD?
- Will the intended UI use a different origin, and what existing CORS/serialization coverage applies to those endpoints?

## XD-836 (train)

Historical cutoff: 2013-09-11T09:54:43.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `a0378bc1be91fb3f3091d0897b4ead99170c4d03a7cadcc7f70d2f39bb0a553e`

Source input identity SHA-256: `f752f36e095428be5d3c2665ac94a4ecef8421a9a343e2ccb69542d328605708`

### Supplied historical plan

- **XD-836** (`tawos-v1.1:2964`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The supplied root has neither a recoverable title nor description and contains no observed members, so the delivery objective cannot be identified.",
    "No prior tickets were supplied; the two-distinct-ticket evidence requirement cannot be met. The reported eligible corpus size was not used to infer evidence."
  ]
}
```

### Supplied prior evidence for support and counterexample review


### Unresolved labelling questions

- Can a cutoff-bound title or description be recovered for this plan?
- Was any work scope observable at the review cutoff that is absent from this supplied example?

## XD-895 (train)

Historical cutoff: 2013-09-25T07:42:10.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `cf5a8e894aaffda3ae9416e84442764053b064654e7df53de73fe1569afc2fd1`

Source input identity SHA-256: `e4ed875b55eca08eb33b48e7c94329894ab04e32da6b2b3130507aaf8563b946`

### Supplied historical plan

- **XD-895** (`tawos-v1.1:2907`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-825** (`tawos-v1.1:2975`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-861** (`tawos-v1.1:2941`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-896** (`tawos-v1.1:2906`)
  - Title: null
  - Description: "The ability to configure message conversion via parameters. Consider programatic configuration of data type channels. Values can be media type, e.g., application/json or a java class name."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-896 explicitly proposes configurable message conversion using media types or Java class names; the root and other two supplied members have no known scope text.",
    "XD-306 lists format-testing ideas without a demonstrated failure. XD-555 reports REST response marshalling and XD-467 reports failed-tap cleanup; these are different mechanisms and do not jointly establish a defect in configurable data channels.",
    "XD-653 and XD-827 describe completed JSON conversion and output-selection capabilities. Their presence cautions against claiming these features are absent from XD-895 solely because acceptance text is incomplete."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-306** (`tawos-v1.1:3482`), created 2013-06-24T14:10:49.000000Z
  - Title: null
  - Description: "Examples:\n1. Be able to start the rabbitmq source just by pointing to modules/source/rabbit.xml, pass in some property file for parameters to be replaced, and outgoing message is placed in a in-memory queue backed channel for use with assertions to verify functionality.  \n2. Test for as many source types as is 'reasonable', e.g. MQTT/TCP testing might be harder than say rabbitmq.\n3. Test that sending json, results in media-type header is set to json\n4. Test that sending POJO,   \"  POJO\n5. Test that sending Tuple, \"   Tuple\n6. Test that sending raw bytes, \" raw bytes\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-555** (`tawos-v1.1:3240`), created 2013-07-26T07:50:54.000000Z
  - Title: "\"make application/json the default output type for the REST API?\""
  - Description: "the top-level URL works via simple curl (without an Accept header) or the browser:\n\n{code}\n> curl http://localhost:8080\n\n{\"links\":[{\"rel\":\"streams\",\"href\":\"http://localhost:8080/streams\"},{\"rel\":\"triggers\",\"href\":\"http://localhost:8080/triggers\"},{\"rel\":\"jobs\",\"href\":\"http://localhost:8080/jobs\"},{\"rel\":\"taps\",\"href\":\"http://localhost:8080/taps\"},{\"rel\":\"counters\",\"href\":\"http://localhost:8080/metrics/counters\"}]}\n{code}\n\nHowever, trying any of those links then fails, e.g.:\n\n{code}\n> curl http://localhost:8080/streams\n\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><errors xmlns:ns2=\"http://www.w3.org/2005/Atom\"><error logref=\"HttpMessageNotWritableException\"><message>Could not marshal [PagedResource { content: [links: [&lt;http://localhost:8080/streams/mqttdemo&gt;;rel=&quot;self&quot;]], metadata: Metadata { number: 0, total pages: 1, total elements: 1, size: 20 }, links: [] }]: null; nested exception is javax.xml.bind.MarshalException\n - with linked exception:\n[com.sun.istack.internal.SAXException2: unable to marshal type &quot;org.springframework.xd.rest.client.domain.StreamDefinitionResource&quot; as an element because it is not known to this context.]</message></error"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-467** (`tawos-v1.1:3328`), created 2013-07-12T10:17:45.000000Z
  - Title: null
  - Description: "There's a lifecycle problem when a tap creation fails (e.g. because the DSL syntax is wrong). Subsequent attempts to create the tap will fail with an error:\n\n [{\"links\":[],\"logref\":\"MessageHandlingException\",\"message\":\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"}]\n\nDisabling JMX solves the issue.\n\n\nreproduce\nCreate a bad stream definition name 'bad'\nTry to recreate with the same name, but correct stream definitions.  The system will report that the stream already exists."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-632** (`tawos-v1.1:3166`), created 2013-08-08T07:23:59.000000Z
  - Title: "\"Shell: HTTP Post - Allow posting of local file contents\""
  - Description: "\"E.g. allow for posting of JSON data stored in local files.  * Allow users to specify the *content-type*. * Ensure that Unicode data (UTF) posts correctly.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-653** (`tawos-v1.1:3145`), created 2013-08-09T10:39:48.000000Z
  - Title: "\"Configure Jackson ObjectMappers to Allow Single Quotes \""
  - Description: "\"Allow Json payloads from external sources, e.g., http post to contain single quoted field names and values. This is required where XD uses Jackson to convert payloads from Json to object or Tuples.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-827** (`tawos-v1.1:2973`), created 2013-09-07T15:18:43.000000Z
  - Title: "provide a property on twittersearch to enable the object-to-json transformer"
  - Description: "Twitter search source should produce JSON or Pojo. The Pojo requires a custom wrapper class that is JSON friendly (e.g., zero arg constructor). The twittersearch module should have a parameter --json true/false (default true) to control the output type."
  - Unknown fields: []
  - Truncated fields: []
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-244** (`tawos-v1.1:3540`), created 2013-06-17T12:19:33.000000Z
  - Title: "\"Create a Trigger\""
  - Description: "h2. Narrative\nAs the XD system, I need to be able to execute a job (or potentially a stream) based on a given condition (time, data existence, etc).  This story is intended is for a local trigger implementation but remote triggers will also need to exist.\n\nh2.  Acceptance Criteria\n# Implement the ability to register a time based trigger {{trigger <CRON_STRING>}} for example\n# Implement the ability to register a file existence based trigger {{trigger <PATH>}} for example\n# Implement the ability to execute a job via an anonymous trigger: {{job_name @ <CRON_STRING OR PATH>}}\n# Implement the ability to execute a job via a job via the previously registered trigger: {{job_name @ trigger_name}}\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-574** (`tawos-v1.1:3222`), created 2013-07-30T00:17:22.000000Z
  - Title: "\"Replace usage of 'raw' curl with shell command to post http data in documentation\""
  - Description: "\"e.g. http://localhost:8080:>post httpsource --target http://localhost:9090 --data 10  I believe this will also help to avoid ugly syntax to escaping quotes for json as in the gemfire example.\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Can historical acceptance text for XD-825, XD-861 or the root establish the converter behavior and validation already intended?
- Do two supplied tickets document the same failure mechanism in data-channel conversion, rather than separate REST, lifecycle or format requirements?

## XD-963 (train)

Historical cutoff: 2013-10-22T08:05:33.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `18a176c4a85c016a52b134a55e44d575e9834323c78003dc44cad267ed27908b`

Source input identity SHA-256: `eb2815d2295d864f03cfb88bbc12e2255a6e291917d9e95c628cd04599a7d741`

### Supplied historical plan

- **XD-963** (`tawos-v1.1:2841`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-654** (`tawos-v1.1:3144`)
  - Title: "Support explict named channel creation with configurable settings via the REST API and Shell"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-657** (`tawos-v1.1:3141`)
  - Title: "Support polling configuration for named channel queues"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-686** (`tawos-v1.1:3114`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-812** (`tawos-v1.1:2988`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-654 and XD-657 already include explicit named-channel creation and polling configuration. Their descriptions and the root scope are unknown, so a particular omitted behavior cannot be established.",
    "XD-582 documents a local-transport queue problem, but XD-571 already records completed named-channel shell tests; the supplied sample does not contain a second comparable configuration failure.",
    "XD-522 and XD-603 document completed tap/stream lifecycle fixes. The supplied text does not establish that the planned named-channel creation uses the same failing paths or that those fixes remain unresolved."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-132** (`tawos-v1.1:3651`), created 2013-05-28T10:47:40.000000Z
  - Title: "\"Profile support for modules\""
  - Description: "To allow for groups of beans to be defined or not in the container that runs a module.\n\nWhen deploying a stream (e.g. via the REST API), it should be possible to also provide profile names. Then those would apply to any modules within that particular stream deployment."
  - Unknown fields: []
  - Truncated fields: []
- **XD-248** (`tawos-v1.1:3536`), created 2013-06-18T06:28:29.000000Z
  - Title: "\"Provide a Spring Shell implementation for XD\""
  - Description: "\"Need to create a basic Spring Shell implementation to provide easier access to the XD REST API via an XD REST API Client library. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-734** (`tawos-v1.1:3066`), created 2013-08-21T14:01:12.000000Z
  - Title: "\"A job will be associated with a named channel when the job is created.  \""
  - Description: "When creating a job, a named channel will be created with a name of job.<your job name>  i.e. job.foo.\n========\nRequired components:\n- A Transform See XD-733\n- JobPlugin needs to create the NamedChannel for the job and associate the transform.\n   > Registrar.xml will need an input channel?\n   > Name channel support will be required.\n- Add --channel to job rest apis to notify system that a named channel is requested.  \n*Unit Test\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-166** (`tawos-v1.1:3617`), created 2013-05-31T15:58:00.000000Z
  - Title: "\"Create config support based on channel registry type\""
  - Description: "\"We need to have the XD container & admin reading the registry specific property based on the registry type selected.   From Mark F, on one of the code review comments:  Maybe rather than having redis, rabbit, etc. properties all within a container.properties we should rely upon naming conventions instead. Specifically, we could have a single configurable property for the type of channel registry (\"\"redis\"\", \"\"rabbit\"\", or \"\"local\"\" being possible values), and then we could use something like:  <import resource=\"\"config/${registry.type}.xml\"\"/>  <context:property-placeholder location=\"\"config/${registry.type}.properties\"\"/>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-207** (`tawos-v1.1:3576`), created 2013-06-06T17:17:09.000000Z
  - Title: "\"Provide configurable properties for hdfs sink.\""
  - Description: "\"The config file modules/sink/hdfs.xml has a hardcoded value to locate the namenode.   <hdp:configuration register-url-handler=\"\"false\"\">   fs.default.name=hdfs://localhost:9000  </hdp:configuration>  the fs.default.name proprety should be configurable and we should also support loading an external configuration file using      <hdp:configuration properties-location=\"\"${xd.home}/config/hadoop.properties\"\">     </hdp:configuration>  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-266** (`tawos-v1.1:3521`), created 2013-06-18T09:45:18.000000Z
  - Title: "\"Create java client lib over REST API\""
  - Description: "\"So that clients (e.g. Shell or custom user program) are insulated from REST details (ala Cloud Foundry).  May go even further if we want a Java DSL for stream definitions (that may reuse Batch command POJOs btw): Difference between: xdClient.createStream(\"\"mystream\"\", \"\"http --port=9000 | file\"\") and  import static stuff.*;  StreamDef stream = http().port(9000).pipe(file()); xdClient.createStream(\"\"mystream\"\", stream);\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-522** (`tawos-v1.1:3273`), created 2013-07-19T21:31:49.000000Z
  - Title: "\"Cannot create tap if you have already tried to create an invalid one of same name\""
  - Description: "\"From the shell:  {code} > stream create --name aaa --definition \"\"time|log\"\" Created new stream 'aaa'  > tap create --name aa --definition \"\"tap aaa | log\"\" Command failed org.springframework.xd.rest.client.impl.SpringXDException: XD111E:(pos 8): Unexpected token.  Expected 'dot(.)' but was 'pipe(|)' tap aaa | log  >tap create --name aa --definition \"\"tap aaa . log\"\" Command failed org.springframework.xd.rest.client.impl.SpringXDException: There is already a tap named 'aa' {code}  Looks like the first tap was created even though there was a parse error.  And so the second attempt to create the tap failed due to an existing tap.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-555** (`tawos-v1.1:3240`), created 2013-07-26T07:50:54.000000Z
  - Title: "\"make application/json the default output type for the REST API?\""
  - Description: "the top-level URL works via simple curl (without an Accept header) or the browser:\n\n{code}\n> curl http://localhost:8080\n\n{\"links\":[{\"rel\":\"streams\",\"href\":\"http://localhost:8080/streams\"},{\"rel\":\"triggers\",\"href\":\"http://localhost:8080/triggers\"},{\"rel\":\"jobs\",\"href\":\"http://localhost:8080/jobs\"},{\"rel\":\"taps\",\"href\":\"http://localhost:8080/taps\"},{\"rel\":\"counters\",\"href\":\"http://localhost:8080/metrics/counters\"}]}\n{code}\n\nHowever, trying any of those links then fails, e.g.:\n\n{code}\n> curl http://localhost:8080/streams\n\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><errors xmlns:ns2=\"http://www.w3.org/2005/Atom\"><error logref=\"HttpMessageNotWritableException\"><message>Could not marshal [PagedResource { content: [links: [&lt;http://localhost:8080/streams/mqttdemo&gt;;rel=&quot;self&quot;]], metadata: Metadata { number: 0, total pages: 1, total elements: 1, size: 20 }, links: [] }]: null; nested exception is javax.xml.bind.MarshalException\n - with linked exception:\n[com.sun.istack.internal.SAXException2: unable to marshal type &quot;org.springframework.xd.rest.client.domain.StreamDefinitionResource&quot; as an element because it is not known to this context.]</message></error"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-571** (`tawos-v1.1:3224`), created 2013-07-29T11:36:35.000000Z
  - Title: "\"Create shell integration test for named chanels\""
  - Description: "\"Expected usage (ATM) would be  // sink channel called foo http | transform --expression=payload.toUppercase() > :foo // source channel called foo :foo > count | file\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-582** (`tawos-v1.1:3214`), created 2013-07-30T08:31:35.000000Z
  - Title: "\"Support named channels when using local transport\""
  - Description: "Sending data to an incomplete stream which is created using a named sink channel only works when using Redis (or Rabbit?, not tested). Since the in-memory version doesn't use a queue, it will fail if you are using xd-singlenode.\n\nWe should use a queue channel with unlimited capacity to allow messages to be sent before the full stream is created."
  - Unknown fields: []
  - Truncated fields: []
- **XD-603** (`tawos-v1.1:3194`), created 2013-08-05T16:48:37.000000Z
  - Title: "\"NPE on stream destroy\""
  - Description: "\"xd:>stream create ticktock --definition \"\"time | log\"\" --deploy true 18:45:13,310  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/streams\"\" resulted in 400 (Bad Request); invoking error handler Command failed org.springframework.xd.rest.client.impl.SpringXDException: There is already a stream named 'ticktock'  xd:>stream destroy ticktock 18:45:16,505  WARN Spring Shell client.RestTemplate:524 - DELETE request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.xd.rest.client.impl.SpringXDException: java.lang.NullPointerException   Caused by: java.lang.NullPointerException  at org.springframework.xd.dirt.module.ModuleDeployer.undeploy(ModuleDeployer.java:143)  at org.springframework.xd.dirt.module.ModuleDeployer.handleMessageInternal(ModuleDeployer.java:97)   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-671** (`tawos-v1.1:3128`), created 2013-08-12T07:41:19.000000Z
  - Title: "Add support for dynamic routing"
  - Description: "\"It should be possible to create streams like the following which rely upon named channel support and dynamic routing capabilities:  {code} http | somerouter :x > xtransformer | hdfs :y > ytransformer | hdfs {code}  The 'somerouter' processor could return \"\"x\"\" or \"\"y\"\" which determines the downstream path for each message.  This should be implemented in such a way that any developer adding a router module would only need to deal with existing Spring Integration semantics (in this case, only considering the return of \"\"x\"\" or \"\"y\"\" - whether it be SpEL or a POJO method invocation). Perhaps in the plugin that modifies a module context, we could simply add a new ChannelResolver implementation (by adding that ChannelResolver as a bean and/or a BeanPostProcessor that configures that as the resolver for any router, if necessary). That ChannelResolver would have a reference to the ChannelRegistry so that the router actually sends its messages to those shared channels. The shared channels themselves would have been created as long as a valid downstream flow has been defined.\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does cutoff-available design text show that explicit channel creation shares the resource-registration and cleanup code implicated by XD-522 or XD-603?
- What validation was already intended for channel settings and polling across local and distributed transports?

## XD-965 (train)

Historical cutoff: 2013-10-22T09:58:15.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `3bb92febcb66b1c94df63a610143765d7a08c604b120f5a8263e12fdea2f23fd`

Source input identity SHA-256: `14b6abc95faa4cf52137ca5fe962669a478da02a3a2fa63fc9eaf2209665db47`

### Supplied historical plan

- **XD-965** (`tawos-v1.1:2839`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-517** (`tawos-v1.1:3278`)
  - Title: "Admin Server Banner and Info"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-621** (`tawos-v1.1:3177`)
  - Title: null
  - Description: "Currently, you have to set the default name node every time your start the shell. We should do 2 things: \n\n- Provide a default Name node Set Default Hadoop Name Node for Shell: hdfs://localhost:8020\n- Should we provide some form of persistence? It kind of sucks that you have to re-specify the name node every time the shell starts up\n\n{code}\nxd:>hadoop fs ls /\nYou must set fs URL before run fs commands\n{code}\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-741** (`tawos-v1.1:3059`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description"]
  - Truncated fields: []
- **XD-842** (`tawos-v1.1:2958`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-959** (`tawos-v1.1:2844`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-621 already proposes a default Hadoop NameNode and asks about persistence; unknown requirements prevent interpreting its open question as a missing dependency or validation task.",
    "XD-207 describes configurable HDFS sink properties and XD-245 describes Hadoop batch-job support, but neither establishes two comparable failures caused by the proposed shell NameNode default.",
    "Most root/member text is unrecoverable, while the other supplied incidents concern job repositories, module naming and Rabbit queue crosstalk without a demonstrated connection to the visible banner and NameNode work."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-742** (`tawos-v1.1:3058`), created 2013-08-22T14:18:55.000000Z
  - Title: null
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-207** (`tawos-v1.1:3576`), created 2013-06-06T17:17:09.000000Z
  - Title: "\"Provide configurable properties for hdfs sink.\""
  - Description: "\"The config file modules/sink/hdfs.xml has a hardcoded value to locate the namenode.   <hdp:configuration register-url-handler=\"\"false\"\">   fs.default.name=hdfs://localhost:9000  </hdp:configuration>  the fs.default.name proprety should be configurable and we should also support loading an external configuration file using      <hdp:configuration properties-location=\"\"${xd.home}/config/hadoop.properties\"\">     </hdp:configuration>  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-702** (`tawos-v1.1:3098`), created 2013-08-16T06:56:27.000000Z
  - Title: "stack overflow when trying to create a stream with the same name as a module"
  - Description: "\"(NOTE: even if we do want to prevent the use of module names for stream names, we obviously need to avoid a StackOverflowError)  to reproduce:  start the xd-singlenode container  start the xd-shell, and type the following:  {code} xd:>stream create time --definition \"\"time | log\"\" {code}  that should produce an Internal Server Error output message  check the xd-singlenode console, and find:  {code} SEVERE: Servlet.service() for servlet [xd] in context with path [] threw exception [Handler processing failed; nested exception is java.lang.StackOverflowError] with root cause java.lang.StackOverflowError  at java.lang.StringValue.from(StringValue.java:24)  at java.lang.String.<init>(String.java:178)  at org.springframework.xd.dirt.stream.dsl.Token.<init>(Token.java:46)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.lexIdentifier(Tokenizer.java:195)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.process(Tokenizer.java:62)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.<init>(Tokenizer.java:41)  at org.springframework.xd.dirt.stream.dsl.StreamConfigParser.parse(StreamConfigParser.java:65)  at org.springframework.xd.dirt.stream.dsl.StreamConfigParser.parse(StreamConfigP"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: "\"Provided console output of started server\""
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: []
  - Truncated fields: []
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []
- **XD-656** (`tawos-v1.1:3142`), created 2013-08-09T12:27:58.000000Z
  - Title: "\"Intra-Module \"\"Pipe\"\" Naming\""
  - Description: "\"Consider 2 Admins/Containers that are using discrete Redis instances but a shared Rabbit instance for the transport.  If two different streams are deployed on each, but with the same stream name, the Rabbit queues will be common (e.g. foo.0), causing crosstalk.  Stream names must be unique across all container instances sharing Rabbit infrastructure.  I am not sure what the solution is; two instances of the *same* stream *do* need common queues but instances of different streams need a qualifier of some kind (container name?). I guess it's not *that* big of an issue because, if they're sharing infrastructure, they're likely to be sharing a stream repo too - in which case you'd need unique stream names.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-67** (`tawos-v1.1:3714`), created 2013-05-14T13:06:23.000000Z
  - Title: "Submit a brew-based install for Spring XD"
  - Description: "\"- Host the Spring XD distributable zip somewhere that is accessible by external http request. - Create brew formula for Spring XD install while specifying redis as dependency.  - starting up stream server upon successful brew install  couple of questions: - should we name the brew task springxd? (name not taken yet) - should we start the stream server as part of the brew install process? - should we specify redis as a recommended dependency? user can pass in 'brew install springxd --without-redis' to skip redis installation. by default, 'brew install springxd' will install redis as well.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Should XD-621 preserve a user-selected NameNode across shell restarts and override its local default?
- Are external Hadoop clusters and shell-to-sink configuration consistency covered by this plan, or outside its intended scope?

## XD-996 (train)

Historical cutoff: 2013-10-24T07:07:27.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `bc13853e3c4111b7f17a799abc698e2af2253a3dc694ccdb765a11696a7c2c1c`

Source input identity SHA-256: `cf38602ea539972da96b0ab0a3fca671fbe2bc15facc19a8e25e6a7812398dc3`

### Supplied historical plan

- **XD-996** (`tawos-v1.1:2810`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1000** (`tawos-v1.1:2806`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1001** (`tawos-v1.1:2805`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1002** (`tawos-v1.1:2804`)
  - Title: null
  - Description: "On clicking a specific job on the deployed jobs list, we need to redirect the user to show the list of all the job executions on that job.\n\nUser should be able to navigate back to the deployed jobs list."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1003** (`tawos-v1.1:2803`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1004** (`tawos-v1.1:2802`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1005** (`tawos-v1.1:2801`)
  - Title: "UI: User should be able to see the list of all job executions"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1006** (`tawos-v1.1:2800`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1007** (`tawos-v1.1:2799`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1008** (`tawos-v1.1:2798`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-999** (`tawos-v1.1:2807`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1002 explicitly plans navigation to a selected job execution list and XD-1005 explicitly plans listing all job executions; these capabilities cannot be labelled missing.",
    "XD-703 and XD-774 describe repository/registry sharing requirements and are Done, while XD-745 explicitly addressed controller coexistence; the supplied evidence does not establish that persistence or API integration remains absent.",
    "The root and eight members lack known title/description text, so false-success behaviour from XD-662 or other historical job issues cannot be tied to a specific contradictory UI design in this plan."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-742** (`tawos-v1.1:3058`), created 2013-08-22T14:18:55.000000Z
  - Title: null
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-817** (`tawos-v1.1:2983`), created 2013-09-06T13:04:38.000000Z
  - Title: "\"REST API for job listing should provide details on last execution \""
  - Description: "\"A user should be able to view some important details of the last execution of a job from a job list.  The {{/batch/jobs}} REST endpoint should provide extra fields not currently available in the {{JobInfo}} class.  At a minimum, I would like to see:  * startTime * startDate * last job parameters * duration * last job status\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-246** (`tawos-v1.1:3538`), created 2013-06-17T13:26:13.000000Z
  - Title: "MessageChannelItemWriter"
  - Description: "h2. Narrative\nAs a user of XD, I want to be able to use a job as a source.  To do so, we need the output of a job to be written to a message channel\n\nh2.  Acceptance Criteria\n# Create a new ItemWriter in the Spring Batch project to write to a Spring Integration message channel."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-597** (`tawos-v1.1:3200`), created 2013-08-02T13:08:55.000000Z
  - Title: "\"Ad-Hoc Job needs to have option for launch and forget\""
  - Description: "\"When running an ad-hoc job without the use of a trigger (adhoc or named).  The user has to wait for job to complete before receiving a success.  We need to launch a job and get a success back to the user letting them know the job has been launched.  for example --immediate\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-662** (`tawos-v1.1:3137`), created 2013-08-09T15:11:35.000000Z
  - Title: "\"No indication of failure in shell when deploying job referencing nonexistent trigger\""
  - Description: "\"I see the following output on the shell if I create a job and reference a non-existent trigger. There's a big stack trace in the server log, but nothing on the shell side indicating failure. A subsequent \"\"jobs list\"\" also shows the job. The same thing happens if I deploy an undeployed Job after deleting its associated Trigger.  $ job create --name helloWorldJob --definition \"\"myjob --trigger=nonexistenttrigger\"\" Successfully created and deployed job 'helloWorldJob'\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-774** (`tawos-v1.1:3026`), created 2013-08-28T13:53:52.000000Z
  - Title: "\"Need to create a Persistent-Job-Registry \""
  - Description: "\"In order to hook up the to get access to all the jobs available the job registry has to be shared.  currently the only implmentation is is the MapJobRegistry.   ==== Testability. ==== The admin will need to be see all jobs created by its containers.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-166** (`tawos-v1.1:3617`), created 2013-05-31T15:58:00.000000Z
  - Title: "\"Create config support based on channel registry type\""
  - Description: "\"We need to have the XD container & admin reading the registry specific property based on the registry type selected.   From Mark F, on one of the code review comments:  Maybe rather than having redis, rabbit, etc. properties all within a container.properties we should rely upon naming conventions instead. Specifically, we could have a single configurable property for the type of channel registry (\"\"redis\"\", \"\"rabbit\"\", or \"\"local\"\" being possible values), and then we could use something like:  <import resource=\"\"config/${registry.type}.xml\"\"/>  <context:property-placeholder location=\"\"config/${registry.type}.properties\"\"/>\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which execution-state and job-identity acceptance checks were included in the eight members with unknown text?
- Do the job lists distinguish registered/deployed jobs from actual executions, as suggested by XD-705 and XD-743?
- Does the UI use the completed shared repository and job registry described in XD-703 and XD-774?

## XD-1141 (train)

Historical cutoff: 2013-12-05T19:48:18.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `9e1210c576d5bc6ac9dcf5ffa07d95ef0caf2b3f558f8fe4496432bbab86a750`

Source input identity SHA-256: `84246d24de9e6844fc5e038912b648c52aeef7ff70d07e561b41ea8367cce84f`

### Supplied historical plan

- **XD-1141** (`tawos-v1.1:2666`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1142** (`tawos-v1.1:2665`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1143** (`tawos-v1.1:2664`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1144** (`tawos-v1.1:2663`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-947** (`tawos-v1.1:2855`)
  - Title: null
  - Description: "SPI for deployment on to YARN + Local 'dirt' cluster."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-947 explicitly covers a deployment SPI for YARN and local dirt clusters; the only known plan text does not specify which startup, job lifecycle or failure-reporting paths the SPI changes.",
    "XD-601 records a local transport/property startup failure, and XD-1023 records an overloaded deployment path bypassing common behaviour, but both are Done and neither supplied text shows that this SPI retains or reintroduces those mechanisms.",
    "The root and XD-1142 through XD-1144 have unknown titles/descriptions, preventing a supported claim that backend validation or exception handling is missing."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1018** (`tawos-v1.1:2788`), created 2013-10-28T11:06:30.000000Z
  - Title: "\"JobDeployer hides root exceptions on failure\""
  - Description: "\"When deploying jobs, the following code (line 103), hides the root cause of deployment failure:    if (exceptionClassName.equals(BEAN_CREATION_EXCEPTION) || exceptionClassName.equals(BEAN_DEFINITION_EXEPTION)) {     throw new MissingRequiredDefinitionException(definition.getName(), cause.getMessage());   }  For example:  org.springframework.xd.dirt.stream.MissingRequiredDefinitionException: Error creating bean with name 'dataSourceInitializer' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Cannot resolve reference to bean 'databasePopulator' while setting bean property 'databasePopulator'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'databasePopulator' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Initialization of bean failed; nested exception is java.lang.NullPointerException  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:103)  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:67)  at org.springframework.xd.dirt.rest.XDController.save(XD"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-144** (`tawos-v1.1:3639`), created 2013-05-29T10:12:30.000000Z
  - Title: "\"Remove Log4j Properties/XMLs from Projects\""
  - Description: "\"If, say, xd-dirt is ahead of a local config on the classpath, it's log4j.properties is found first.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-178** (`tawos-v1.1:3605`), created 2013-06-03T13:55:24.000000Z
  - Title: "\"DefaultContainer should have a default constructor that generates a UUID\""
  - Description: "\"The current incrementAndGet approach based off redis will not easily be applicable in local model deployment\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-601** (`tawos-v1.1:3196`), created 2013-08-05T13:23:44.000000Z
  - Title: "\"./xd-container  --transport local throws NumberFormatException\""
  - Description: "\"./xd-container [OK] ./xd-container --transport redis [OK] ./xd-container --transport rabbit [OK] ./xd-container --transport local [FAIL]  <USER>mbp:bin administrator$ ./xd-container --transport local Exception in thread \"\"main\"\" org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.jolokia.jvmagent.spring.SpringJolokiaAgent#0': Invocation of init method failed; nested exception is java.lang.NumberFormatException: For input string: \"\"${xd.jmx.port}\"\"  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1488)  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:524)  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:461)  at org.springframework.beans.factory.support.AbstractBeanFactory$1.getObject(AbstractBeanFactory.java:295)  at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:223)  at org.springframework.beans.factory.support.Abstract"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-958** (`tawos-v1.1:2845`), created 2013-10-16T08:45:51.000000Z
  - Title: "\"Build failure on Ubuntu\""
  - Description: "\"Build fails:  gradle clean build  ...  :spring-xd-dirt:test  org.springframework.xd.dirt.stream.FileSourceModuleTests > classMethod FAILED     java.io.IOException at FileSourceModuleTests.java:53  org.springframework.xd.dirt.stream.FileSourceModuleTests > classMethod FAILED     java.lang.IllegalArgumentException at FileSourceModuleTests.java:130  328 tests completed, 2 failed, 11 skipped :spring-xd-dirt:test FAILED  FAILURE: Build failed with an exception.   Looks like it is trying to create a directory under the local filesystem /  java.io.IOException: Unable to create directory /tmpfilesourcetests  at org.apache.commons.io.FileUtils.forceMkdir(FileUtils.java:2024)  at org.springframework.xd.dirt.stream.FileSourceModuleTests.createTempDir(FileSourceModuleTests.java:53)  at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)  at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  at java.lang.reflect.Method.invoke(Method.java:606)  at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:47)  at org.junit.internal.runners.model.Ref"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1023** (`tawos-v1.1:2783`), created 2013-10-29T08:01:17.000000Z
  - Title: "\"Refactor job deploy to go through XDController.deploy(name)\""
  - Description: "\"Job deployment currently goes through an overloaded version of deploy() that takes 4 parameters. This prohibits job handling code from benefiting from common behavior (and eg currently breaks deployAll)  Given that the 3 additional parameters are in fine handled as module parameters, let's push them to the job definition, known at creation time, rather than at deployment time (as it does not really make sense to change those between deploys)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-108** (`tawos-v1.1:3674`), created 2013-05-23T01:27:49.000000Z
  - Title: "\"Build script should not package 'spring-xd-dirt' scripts \""
  - Description: "\"We are packaging separate scripts to start XDAdmin and XDContainer.  The Gradle application plugin will generate an unwanted 'spring-xd-dirt' scripts, this should be removed from the bin directory when creating a distribution zip.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-11** (`tawos-v1.1:3764`), created 2013-04-12T06:45:19.000000Z
  - Title: "Initial work that uses the module architecture from DIRT "
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-132** (`tawos-v1.1:3651`), created 2013-05-28T10:47:40.000000Z
  - Title: "\"Profile support for modules\""
  - Description: "To allow for groups of beans to be defined or not in the container that runs a module.\n\nWhen deploying a stream (e.g. via the REST API), it should be possible to also provide profile names. Then those would apply to any modules within that particular stream deployment."
  - Unknown fields: []
  - Truncated fields: []
- **XD-14** (`tawos-v1.1:3761`), created 2013-04-12T06:48:58.000000Z
  - Title: "Design for deploying DIRT Runtime on EC2"
  - Description: "create enough of a design to develop additional stories."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-163** (`tawos-v1.1:3620`), created 2013-05-31T08:43:54.000000Z
  - Title: "Enable grouping of modules for co-located deployment"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Unresolved labelling questions

- What deployment paths and common lifecycle behaviour are defined by the SPI in XD-947?
- Did XD-1142 through XD-1144 include cross-backend startup/property and deployment-error tests?
- Were the fixes described in XD-601, XD-1018 and XD-1023 preserved by the proposed SPI?

## XD-1257 (train)

Historical cutoff: 2014-01-22T23:20:02.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `13036fb1f232a148cf71db6622de5aafb56a7aaa00ad307fde2d031e72ec2737`

Source input identity SHA-256: `c01989829dec15ccb0922c8c9c759f3b0b2a1cc732be658f92c24e79f15354dd`

### Supplied historical plan

- **XD-1257** (`tawos-v1.1:2550`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1237** (`tawos-v1.1:2570`)
  - Title: "\"Add option to stop all running XD EC2 instances that match a given naming pattern\""
  - Description: "\"This functionality should be added as a command line option to the main app in the spring-xd-ec2 project\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1238** (`tawos-v1.1:2569`)
  - Title: "Add to Acceptance Test EC2 CI build plan a stage that stops any existing CI EC2 deployments"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1239** (`tawos-v1.1:2568`)
  - Title: "Add stage to Acceptance Test EC2 build plan that runs a basic acceptance test application against the single-node deployment"
  - Description: "Run  basic_stream_tests\n\nThis will require some mods to pass in the location of the xd-admin process data via a build artifact from the EC2 deployment stage.\n\n"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1240** (`tawos-v1.1:2567`)
  - Title: "Add to Acceptance Test EC2 CI build plan a stage that uses XD distributed mode with rabbit"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1241** (`tawos-v1.1:2566`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1242** (`tawos-v1.1:2565`)
  - Title: "\"Optimize deployment of xd-admin and multiple nodes in spring-xd-ec2 to occur in parallel.\""
  - Description: "\"The deployment of nodes is sequential, we can reduce the time to deploy a cluster greatly by having these tasks execute in parallel.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1243** (`tawos-v1.1:2564`)
  - Title: "\"Create App for CI to Shutdown XD EC2 Cluster\""
  - Description: "Application will shutdown all servers with a specific name.  \nApplication will take a --cluster-name parameter.   \nGenerate artifact to state success or failure  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-1244** (`tawos-v1.1:2563`)
  - Title: null
  - Description: "* Use the cleanup app from XD-1243 to stop previous CI runs of XD on EC2.\n* Build XD-EC2 deployer from github.\n* Use XD-EC2 Deployer to deploy the CI XD-Instance\n* Should produce artifact that contains the URL \n   * admin server of the XD cluster.\n   * container servers of the XD cluster"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1245** (`tawos-v1.1:2562`)
  - Title: "Develop basic acceptance test application test to exercise based XD-EC2 deployment from CI"
  - Description: "Create a round trip test script that will push data to the XD EC2 cluster and get results back that can be checked.  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1263** (`tawos-v1.1:2544`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The observed plan already includes stopping previous EC2 deployments, shutdown success/failure artifacts, deployment URL artifacts, single-node acceptance tests, a Rabbit distributed stage and a round-trip result-checking application. None can be labelled missing.",
    "XD-969, XD-970 and XD-972 describe provisioning/port checks, deployment verification and cleanup, and are Done; these are existing safeguards rather than evidence of an unresolved EC2 CI failure.",
    "The unknown root, XD-1241 and XD-1263 leave some scope unrecoverable, but the other classloading/job/routing examples do not establish two supported failures of this CI plan."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-972** (`tawos-v1.1:2833`), created 2013-10-21T14:11:44.000000Z
  - Title: "Create CI for XD-EC2 project"
  - Description: "\"Automated test will use directly use the Deployer class * asserts on basic info of RunningInstance ** check that EBS was mounted ** that application was unzipped ** redis and rabbit are running via port checks  * http requests on admin port for  ** root path ** list of modules * @AfterClass that will look for the cluster name and terminate all instances Look at ‘live’ tag in JClouds tests for some additional tactics \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-970** (`tawos-v1.1:2834`), created 2013-10-21T14:04:34.000000Z
  - Title: "Install XD admin instance on EC2"
  - Description: "*Update the Deployer class to add the following methods *\n** RunningInstance  deployAdminServer\n\n* The install script steps:\n** Using XD-977 install distribution\n** Setup XD_HOME variable\n** start up redis and rabbit using ports as specified in xd-ec2.properties on admin server\n** Create configurator directory\n** Copy the configurator to containers\n** Use port watch to make sure they started\n** start admin server\n** use port watch to make sure the admin started on 9393\n** Report if admin server started.  If it didn't start abort install.\n** Report public DNS name of admin-server \n\n\n* Integration Testing\n** Verify XD admin has been started\n*** Create a basic stream (trigger>log)and make sure we get a success code from xd admin was received.\n*** Query the redis to see if the stream was created.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: "\"Create distributable artifact that contains server application and start/stop scripts\""
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-720** (`tawos-v1.1:3080`), created 2013-08-20T09:51:19.000000Z
  - Title: "\"Deploy a new source module *after* XD-singlenode container has started.\""
  - Description: "\"After the xd-singlenode process has started, create a new module that has dependencies not already in the parent application context, and then create a stream that uses the new module.  *Implementation Suggestions* Develop in the test tree, maybe of the xd-shell project, a new module.  the lib and config should be sititng around in a directory waiting to be copied into the appropriate spot.  Could try http://www.date4j.net/..The config file  would be similar to time.xml but use the date4j class.  *How to verify it works* In a JUnit test case copy in a new module that has new dependencies, ..copy the lib and config directories into the location where the ModuleRegisty will pick it up.  Deploy a new stream, date4j | file and see if there are contents in the file. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-799** (`tawos-v1.1:3001`), created 2013-09-02T23:31:17.000000Z
  - Title: "\"Change rabbitmq sink to use routing-key-expression instead of routing-key\""
  - Description: "\"The current rabbitmq sink uses the attribute routing-key, which defaults to the name of the stream.  This should be change to use the attribute routing-key-expression so that the routing-key can be determined using SpEL.  This will enable a dynamic evaluation of the routing-key based on message payload/header.  *Implementation Suggestions*  This hopefully should be changing the XML description of the sink to     routing-key-expression=\"\"${routingKey:'${xd.stream.name}'}  This way, the ${xd.stream.name} is surrounded by a single quote to indicate a string literal to SpEL in the default case.    *How to verify it works.*  One of the simple uses of this is to create a routing key based on payload.  In a distributed word-count example, the hashcode of a word would be sent to a certain number of processing modules that would perform the count. The idea is that the same word is sent to the same node over and over again, in particular if in-memory counters or state is computed - using centralized redis counters this wouldn't be necessary in the case of only counter state.  The stream   http | rabbit --routingKey=\"\"'word-' + payload.hashCode() % 3\"\"  is an example of a stream that can be "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1077** (`tawos-v1.1:2730`), created 2013-11-18T09:02:51.000000Z
  - Title: null
  - Description: "Develop out a Proof of concept for review that allows users to easily create a new module to Spring XD. Key features to be enabled:\n\n1. Allow existing modules to be included as a classpath dependency\n2. Consolidate shared libraries in existing modules (e.g. a shared lib for all gemfire modules)\n3. User develops a module as a normal Java project\n4. User's project can then be added to a runtime container in the same way (as a dependency)\n\nNice to have: \n\n1. at development time container can run continuously and pick up changes from user's module project.\n2. Java config for a module.\n3. command line functionality to create project scaffolding.\n\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Unresolved labelling questions

- What scenarios did XD-1241 and XD-1263 cover, and were they additional transport or failure-path tests?
- How will deployment URL artifacts and the shutdown success/failure artifact be consumed by the explicitly planned CI stages?
- Does the round-trip application exercise the Rabbit distributed stage as well as single-node deployment?

## XD-1258 (train)

Historical cutoff: 2014-01-22T23:26:45.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `daee7bfaae7f7723e5a56fe29d1f816e32e6c87bd1931819bf26958305d2b5db`

Source input identity SHA-256: `acbe78a45023167f57e98cef56bdb92fd8e8a4be2b8461feac6076390faf1e04`

### Supplied historical plan

- **XD-1258** (`tawos-v1.1:2549`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1229** (`tawos-v1.1:2578`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1230** (`tawos-v1.1:2577`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1231** (`tawos-v1.1:2576`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root and all three supplied members have unknown titles and descriptions; statuses and the single recoverable estimate do not identify a delivery failure mechanism.",
    "No prior tickets were supplied, so no risk can satisfy the required two independent historical citations."
  ]
}
```

### Supplied prior evidence for support and counterexample review


### Unresolved labelling questions

- Can cutoff-bound task text be recovered for XD-1258 and its three observed members?
- What plan objective would allow relevant historical comparisons without using later snapshots?

## XD-1259 (train)

Historical cutoff: 2014-01-22T23:29:49.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `e4a240e75c48118405561ec6a6468b9428cc4da3ae1f58b7abcafa7b59e3c7c8`

Source input identity SHA-256: `17e587ac07502fbac2111185c3f5b60bc8e6f7efa711662509f51816add64364`

### Supplied historical plan

- **XD-1259** (`tawos-v1.1:2548`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1232** (`tawos-v1.1:2575`)
  - Title: "Create EC2 AMI for single-node install of Apache Hadoop 1.2.1"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1233** (`tawos-v1.1:2574`)
  - Title: "Create EC2 AMI for single-node install of Apache Hadoop 2.2.0"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1234** (`tawos-v1.1:2573`)
  - Title: "Create EC2 AMI for single-node install of  Pivotal HD 1.1"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1235** (`tawos-v1.1:2572`)
  - Title: "Create EC2 AMI for single-node install of Cloudera CDH 4.3.1"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1236** (`tawos-v1.1:2571`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The visible children create single-node Hadoop AMIs for four named distributions; the root and each installation specification are unknown. It is not established that these images bundle XD or share its classpath.",
    "XD-634 documents an XD/Guava mismatch for Hadoop 2.0.5 and Pivotal HD 1.0, while XD-472 calls for distribution-specific transitive dependencies. These establish conditional integration concerns, not an actual dependency gap in the listed Hadoop-only image tasks or their different versions.",
    "XD-1041 and XD-978 explicitly require runtime checks in other work. Their testing requirements do not prove those checks are missing here; no sufficiently grounded two-ticket mechanism applies to the recoverable AMI scope."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1041** (`tawos-v1.1:2765`), created 2013-11-08T09:12:37.000000Z
  - Title: "\"Upgrade to Spring for Apache Hadoop 1.0.2.RELEASE and Pivotal HD 1.1\""
  - Description: "\"Make sure the sinks and jobs work against Pivotal HD 1.1\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-799** (`tawos-v1.1:3001`), created 2013-09-02T23:31:17.000000Z
  - Title: "\"Change rabbitmq sink to use routing-key-expression instead of routing-key\""
  - Description: "\"The current rabbitmq sink uses the attribute routing-key, which defaults to the name of the stream.  This should be change to use the attribute routing-key-expression so that the routing-key can be determined using SpEL.  This will enable a dynamic evaluation of the routing-key based on message payload/header.  *Implementation Suggestions*  This hopefully should be changing the XML description of the sink to     routing-key-expression=\"\"${routingKey:'${xd.stream.name}'}  This way, the ${xd.stream.name} is surrounded by a single quote to indicate a string literal to SpEL in the default case.    *How to verify it works.*  One of the simple uses of this is to create a routing key based on payload.  In a distributed word-count example, the hashcode of a word would be sent to a certain number of processing modules that would perform the count. The idea is that the same word is sent to the same node over and over again, in particular if in-memory counters or state is computed - using centralized redis counters this wouldn't be necessary in the case of only counter state.  The stream   http | rabbit --routingKey=\"\"'word-' + payload.hashCode() % 3\"\"  is an example of a stream that can be "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-476** (`tawos-v1.1:3319`), created 2013-07-13T09:14:32.000000Z
  - Title: "The stream definition is not deleted in redis container when the stream is destroyed"
  - Description: "\"This only happened with distributed mode that uses redis as store. The single mode which uses in memory store works fine.  Step to reproduce:  Create stream: curl -X POST -d \"\"name=httptest\"\" -d \"\"definition=http|log\"\" http://localhost:8080/streams  redis 127.0.0.1:6379> keys *httptest* 1) \"\"modules:httptest\"\" 2) \"\"streams.httptest\"\" 3) \"\"stream.definitions.httptest\"\"  Delete Stream: curl -X DELETE http://localhost:8080/streams/httptest  redis 127.0.0.1:6379> keys *httptest* 1) \"\"streams.httptest\"\" 2) \"\"stream.definitions.httptest\"\"  stream still there not deleted  Recreate the stream curl -X POST -d \"\"name=httptest\"\" -d \"\"definition=http|log\"\" http://localhost:8080/streams  Got: <?xml version=\"\"1.0\"\" encoding=\"\"UTF-8\"\" standalone=\"\"yes\"\"?><errors xmlns:ns2=\"\"http://www.w3.org/2005/Atom\"\"><error logref=\"\"StreamAlreadyExistsException\"\"><message>There is already a stream with name 'httptest'</message></error>\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-485** (`tawos-v1.1:3310`), created 2013-07-15T09:34:37.000000Z
  - Title: "Create stories to enable the use of Spring Shell's 2.0 branch testing facilities "
  - Description: "\"We need a few steps 1. Investigate if we need to move off Spring Shell 1.0 dependency, e.g. need to use code in Spring Shell 2.0 branch 2. If we need to use code in Spring Shell 2.0 branch, we need to release a Spring Shell 1.1 M1 release with appropriate code changes.  Create stories related to Shell release. 3. Determine and document the basic recipe for doing integration tests. 4. Create stories to provide integration tests for each existing command\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-61** (`tawos-v1.1:3719`), created 2013-05-13T08:47:41.000000Z
  - Title: "\"Create distributable artifact that contains server application and start/stop scripts\""
  - Description: "The gradle application task should get us most of the way to create a distributable artifact akin to what you see when downloading tomcat/jetty etc.\n\nNow there is a launch task\n\ntask(launch, dependsOn: 'classes', type: JavaExec) {\n\t\tmain = 'org.springframework.xd.dirt.stream.StreamServer'\n\t\tclasspath = sourceSets.test.runtimeClasspath\n\t}\n\n\nThe same main should be referenced in the application plugin, a task to create a .zip distributable is needed.\n\nIdeally would be nice to \n1. download .zip\n2. unzip\n3. cd spring-xd/bin\n4. xdserver start\n\n\nand gracefully shutdown later with \n\n5. xdserver stop\n\nI don't know if we can/should bundle redis, I think we should bundle it.\n\nThe scripts can be for unix/linux and for windows.  \n\nDiscuss a brew based install as well.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-634** (`tawos-v1.1:3164`), created 2013-08-08T09:34:47.000000Z
  - Title: "\"Fix guava dependency for hadoop20 and phd1 \""
  - Description: "\"Spring Xd currently ships with Guava 12.0 while Hadoop 2.0.5 and Pivotal HD 1.0 depends on 11.0.2 - this could lead to classpath problems if we include both.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1077** (`tawos-v1.1:2730`), created 2013-11-18T09:02:51.000000Z
  - Title: null
  - Description: "Develop out a Proof of concept for review that allows users to easily create a new module to Spring XD. Key features to be enabled:\n\n1. Allow existing modules to be included as a classpath dependency\n2. Consolidate shared libraries in existing modules (e.g. a shared lib for all gemfire modules)\n3. User develops a module as a normal Java project\n4. User's project can then be added to a runtime container in the same way (as a dependency)\n\nNice to have: \n\n1. at development time container can run continuously and pick up changes from user's module project.\n2. Java config for a module.\n3. command line functionality to create project scaffolding.\n\n"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1144** (`tawos-v1.1:2663`), created 2013-12-04T20:12:57.000000Z
  - Title: "\"Spike for transformation of the parsed stream/job definition to a Physical Deployment Model taking into account a Deployment Manifest\""
  - Description: "\"The initial parsing of a stream/job definitions into a list of ModuleDeploymentRequests needs to be transformed into a Physical Deployment Model that takes into account   1) module co-location 2) partitioning 3) number of instances 4) node assignment  an potentially other data related to the runtime properties of a module (e.g. concurrency settings)   The an external DeploymentManifest will be used to capture this information.  A deployment of a stream or job will then need to optionally provide a reference to deployment manifest.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-472** (`tawos-v1.1:3323`), created 2013-07-12T11:58:59.000000Z
  - Title: "\"Add spring-xd-hadoop distro specific sub-projects\""
  - Description: "\"we need to modify build adding two sub-projects for spring-xd-hadoop: one for hadoop 1.1.2 and one for phd1 (Pivotal HD) to pull in transitive dependencies for correct Hadoop distro\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-978** (`tawos-v1.1:2828`), created 2013-10-21T15:21:31.000000Z
  - Title: "\"Installer needs to launch a single node XD instance\""
  - Description: "\"* Create a Deployer class has methods ** RunningInstance  deploySingleNode *** takes into account machine size as specified in properties file ** void  destroyAllInstances()   *** or whatever JClouds returns from the destroy call ** ctor gets passed in the root boostrapping credentials. * Install Script Steps ** Setup XD_HOME variable ** Make sure privileges are set to ubuntu not root. ** start up redis and rabbit using ports as specified in xd-ec2.properties ** Use port watch to make sure they started ** Start singlenode after configuration. ** Display hostname of singlenode server ** Report successful and failed startup ** Hit root of xd-admin to see if there is a response on 9393 * Integration Testing ** Verify that config files have been setup ** Verify XD has been started ** Verify XD can process a basic http post  \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Are these Hadoop-only base images or bundled XD environments, and where are their installation and runtime acceptance criteria recorded?

## XD-1260 (train)

Historical cutoff: 2014-01-22T23:35:08.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `25ecf9eba9e3ebadb6cb17f4058ced3b8d0852285b0231229270dd298512d1a0`

Source input identity SHA-256: `a170d5d7f390cc774210403f9434c118e0efd10fb997921a913c300b1942dfb3`

### Supplied historical plan

- **XD-1260** (`tawos-v1.1:2547`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1076** (`tawos-v1.1:2731`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1127** (`tawos-v1.1:2680`)
  - Title: "Add support for deploying a batch job with partitioning across multiple XD nodes."
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1139** (`tawos-v1.1:2668`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1140** (`tawos-v1.1:2667`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1146** (`tawos-v1.1:2661`)
  - Title: "\"With Partitioned Jobs, Wire Partitioner and StepExecutionHandlers with the MessageBus\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []

### Proposed target

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

#### Evidence for XD-1260-partition-step-history

- XD-1206 / `tawos-v1.1:2601` / description: "For some reason, the partitioned batch jobs are storing  {{StepExecutions}}s in the DB with a null ID."
- XD-703 / `tawos-v1.1:3097` / description: "A single job repository that is backed by a file need to be shared across all jobs that are a launched."

### Supplied prior evidence for support and counterexample review

- **XD-1206** (`tawos-v1.1:2601`), created 2014-01-07T15:28:42.000000Z
  - Title: null
  - Description: "For some reason, the partitioned batch jobs are storing  {{StepExecutions}}s in the DB with a null ID.\n\nThis causes {{JobCommandTests.testListStepExecutionsForSpecificJobExecution()}} to fail because the HATEOS code asserts not null...\n\n{code}\n18:25:26,185 ERROR http-nio-9393-exec-3 rest.RestControllerAdvice:186 - Caught exception while handling a request\njava.lang.IllegalArgumentException: [Assertion failed] - this argument is required; it must not be null\n\tat org.springframework.util.Assert.notNull(Assert.java:112)\n\tat org.springframework.util.Assert.notNull(Assert.java:123)\n\tat org.springframework.hateoas.mvc.ResourceAssemblerSupport.createResourceWithId(ResourceAssemblerSupport.java:87)\n\tat org.springframework.xd.dirt.rest.StepExecutionInfoResourceAssembler.toResource(StepExecutionInfoResourceAssembler.java:39)\n\tat org.springframework.xd.dirt.rest.BatchStepExecutionsController.list(BatchStepExecutionsController.java:107)\n{code}\n\nFor some reason, the query for objects with the {{jobExecutionId}} also returned these two objects with null keys.\n\nBlowing away my data directory fixes the problem (until I run another partitioned batch job).\n\nI need to figure out why spring batch is c"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-1192** (`tawos-v1.1:2615`), created 2014-01-02T09:03:46.000000Z
  - Title: "\"Add documentation for JDBC to HDFS batch job\""
  - Description: "\"Add docs to section   https://github.com/spring-projects/spring-xd/wiki/Batch-Jobs#pre-packaged-batch-jobs\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-752** (`tawos-v1.1:3048`), created 2013-08-23T18:50:21.000000Z
  - Title: "\"Restrict Job launcher with more than one batch job configured in job module\""
  - Description: "\"Currently the Job launcher launches all the batch jobs configured in the job module.  Please refer, ModuleJobLauncher's executeBatchJob().  This makes the JobRegistry registers with multiple batch jobs under the same Spring XD job name (group name).  Also, it is understood that having multiple jobs configuration under the same config xml is uncommon.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1001** (`tawos-v1.1:2805`), created 2013-10-23T22:03:13.000000Z
  - Title: "\"User should be able to view the list of all Deployed Jobs\""
  - Description: "\"On clicking the “Deployed Jobs”, we can have a table view of all the deployed jobs. This is again a responsive table layout with all the job definitions with status “deployed”. The deployed XD job corresponds to a single batch Job Instance.   This story addresses the UI layout changes to display existing JobInstance information.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1018** (`tawos-v1.1:2788`), created 2013-10-28T11:06:30.000000Z
  - Title: "\"JobDeployer hides root exceptions on failure\""
  - Description: "\"When deploying jobs, the following code (line 103), hides the root cause of deployment failure:    if (exceptionClassName.equals(BEAN_CREATION_EXCEPTION) || exceptionClassName.equals(BEAN_DEFINITION_EXEPTION)) {     throw new MissingRequiredDefinitionException(definition.getName(), cause.getMessage());   }  For example:  org.springframework.xd.dirt.stream.MissingRequiredDefinitionException: Error creating bean with name 'dataSourceInitializer' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Cannot resolve reference to bean 'databasePopulator' while setting bean property 'databasePopulator'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'databasePopulator' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Initialization of bean failed; nested exception is java.lang.NullPointerException  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:103)  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:67)  at org.springframework.xd.dirt.rest.XDController.save(XD"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1196** (`tawos-v1.1:2611`), created 2014-01-06T07:06:32.000000Z
  - Title: "Align filehdfs batch job defaults with those of corresponding hdfs sink"
  - Description: "The batch jobs use different defaults compared to some of the sink/source modules.\n\nfilehdfs puts data in a /data directory with files named after the stream using a .log file extension. The hdfs sink puts files in an /xd/<streamname> directory using .txt as the default file extension.\n\nfilehdfs needs a more descriptive naming"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1200** (`tawos-v1.1:2607`), created 2014-01-06T10:15:03.000000Z
  - Title: "\"Fix hdfsjdbc batch job\""
  - Description: "hdfsjdbc throws an exception:\n{code}\norg.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition with name 'itemReader' defined in URL [file:/Users/trisberg/Projects/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Could not resolve placeholder 'columns' in string value \"${columns}\"\n{code}\n\nThe hdfsjdbc job uses 'columns' instead of 'names' as the parameter for the column-names. Should we make this usage consistent between jobs?\n\nThere is a comment in the docs - \"there is also a limitation in that the database table must be created manually. This is due to a bug in Spring Hadoop and will be fixed in the future.\" Think this is this solved in Spring Hadoop now?\n\ninitializeDatabase should default to false now to be consistent with jdbc sink\n\nRename batch-jdbc/mongo-import.properties to batch-jdbc/mongo.properties since these aren't just for import"
  - Unknown fields: []
  - Truncated fields: []
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which member owns the still-To-Do null-StepExecution-ID problem in XD-1206?
- Can repeated multi-node partitioned runs list step history correctly without resetting the persistent repository?
- What company impact threshold applies when work executes but execution history cannot be listed?

## XD-1267 (train)

Historical cutoff: 2014-01-25T15:33:07.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `956009d69eb1e1a3171a59bf26d323c243cc11b51e151767b8a056102beced93`

Source input identity SHA-256: `25ce9b52b114bae3edcb5a30ba218bff9d04f2c8e0780560d6651c8c226a0e5e`

### Supplied historical plan

- **XD-1267** (`tawos-v1.1:2540`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1045** (`tawos-v1.1:2761`)
  - Title: "Create project for model that is common between client and server"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1045 explicitly creates a model project common to client and server; sharing model work is already part of the visible plan.",
    "XD-1198 documents whitespace-sensitive shell parameter parsing and XD-465 documents lost server error detail, but neither shows a defect in the shared model project or a proposed incompatible API change. Both are Done.",
    "The root has no known title/description and XD-1045 has no known description, so affected classes, wire formats and compatibility promises cannot be established."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1048** (`tawos-v1.1:2758`), created 2013-11-10T13:19:29.000000Z
  - Title: null
  - Description: "This would be a combination of the existing aggregate counter and field value counter functionality.\n\nFor example if the stream data was for car purchases some fields might be colour, make and model. \nWhen analysing the aggregate data I dont just want to know how many were sold on Monday, but how many of each make or how many of each colour, \nor how many of a particular colour, make AND model. This would allow a dashboard type client to 'drill down' into each dimension or combination of dimensions (in real time without executing batch queries against the raw data)\n\nIdeally the aggregate counter would be specified as \n\nstream create --name mytap --definition \"tap:mystream > aggregatecounter --name=mycount --fieldNames=colour,make,model\"\n\nThe keys would be dynamically created according to the field values in each record (ie in a similar way to the field value counter you would not need to predefine field values) and keys would be created for all combinations of the fields specified eg the record \n\n{ \"colour\":\"silver\" , \"make\":\"VW\" , \"model\" : \"Golf\" } \n\nwould increment the following key counters (in addtion to the existing time buckets)\n\n<existing base counter - ie all fields for thi"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]
- **XD-111** (`tawos-v1.1:3671`), created 2013-05-23T09:39:54.000000Z
  - Title: "\"Create final distribution zip across multiple projects\""
  - Description: "\"The final directory structure should look like  <install-dir>/xd <install-dir>/redis <install-dir>/gemfire  inside the XD directory   /xd/bin - which has xd-container and xd-admin scripts /xd/lib  inside the gemfire directory /gemfire/bin - has the gemfire-server script /gemfire/lib   inside the redis directory is   /redis/redis-latest-v.x.y.z.tar /redis/README /readis/install-redis  - script that does the basic 4 commands to install redis.   There should be a gradle task that runs after the distZip task, that will take the contents of different project directories, script diretories and 'redis-binary' directories and creates the final layout for the distribution.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1198** (`tawos-v1.1:2609`), created 2014-01-06T09:00:40.000000Z
  - Title: "\"Shell: Job Parameters are whitespace sensitive\""
  - Description: "\"This works:  {code} job launch helloSpringXD --params \"\"{\"\"myStringParameter\"\":\"\"foobar\"\",\"\"secondParam\"\":\"\"hello\"\"}\"\" {code}  This fails:  {code} job launch helloSpringXD --params \"\"{\"\"myStringParameter\"\":\"\"foobar\"\", \"\"secondParam\"\":\"\"hello\"\"}\"\" {code}  Notice the space between the parameters. This fails with:  {code} spring> job launch helloSpringXD --params \"\"{\"\"myStringParameter\"\":\"\"foobar\"\", \"\"secondParam\"\":\"\"hello\"\"}\"\" 14/01/06 12:00:07 WARN client.RestTemplate: PUT request for \"\"http://localhost:9393/jobs/helloSpringXD/launch\"\" resulted in 500 (Internal Server Error); invoking error handler  Command failed org.springframework.xd.rest.client.impl.SpringXDException: org.springframework.integration.MessageHandlingException: java.lang.IllegalArgumentException: Unable to convert provided JSON to Map<String, Object>  {code}  Internally the parameters are parsed to:  {code} {\"\"myStringParameter\"\":\"\"foobar\"\",secondParam\"\":\"\"hello\"\"} {code}  The curly brace is missing.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: "\"Provided console output of started server\""
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: []
  - Truncated fields: []
- **XD-266** (`tawos-v1.1:3521`), created 2013-06-18T09:45:18.000000Z
  - Title: "\"Create java client lib over REST API\""
  - Description: "\"So that clients (e.g. Shell or custom user program) are insulated from REST details (ala Cloud Foundry).  May go even further if we want a Java DSL for stream definitions (that may reuse Batch command POJOs btw): Difference between: xdClient.createStream(\"\"mystream\"\", \"\"http --port=9000 | file\"\") and  import static stuff.*;  StreamDef stream = http().port(9000).pipe(file()); xdClient.createStream(\"\"mystream\"\", stream);\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-446** (`tawos-v1.1:3348`), created 2013-07-11T06:39:25.000000Z
  - Title: "\"Investigate stream lifecycle issues with redis store\""
  - Description: "\"When running with \"\"./gradlew launch\"\" I get a 500 error when I try to re-deploy an undeployed stream. A subsequent create or destroy also fail  http://localhost:8080:>stream create --definition \"\"time | log\"\" --name ticktock Created new stream 'ticktock' http://localhost:8080:>stream undeploy --name ticktock Un-deployed stream 'ticktock' http://localhost:8080:>stream deploy --name ticktock 13:02:09,936  WARN Spring Shell client.RestTemplate:524 - PUT request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.web.client.HttpServerErrorException: 500 Internal Server Error http://localhost:8080:>stream deploy --name ticktock 13:03:11,453  WARN Spring Shell client.RestTemplate:524 - PUT request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.web.client.HttpServerErrorException: 500 Internal Server Error http://localhost:8080:>stream undeploy --name ticktock 13:03:54,576  WARN Spring Shell client.RestTemplate:524 - PUT request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Inter"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-603** (`tawos-v1.1:3194`), created 2013-08-05T16:48:37.000000Z
  - Title: "\"NPE on stream destroy\""
  - Description: "\"xd:>stream create ticktock --definition \"\"time | log\"\" --deploy true 18:45:13,310  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/streams\"\" resulted in 400 (Bad Request); invoking error handler Command failed org.springframework.xd.rest.client.impl.SpringXDException: There is already a stream named 'ticktock'  xd:>stream destroy ticktock 18:45:16,505  WARN Spring Shell client.RestTemplate:524 - DELETE request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.xd.rest.client.impl.SpringXDException: java.lang.NullPointerException   Caused by: java.lang.NullPointerException  at org.springframework.xd.dirt.module.ModuleDeployer.undeploy(ModuleDeployer.java:143)  at org.springframework.xd.dirt.module.ModuleDeployer.handleMessageInternal(ModuleDeployer.java:97)   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-687** (`tawos-v1.1:3113`), created 2013-08-12T17:24:36.000000Z
  - Title: "\"provide user friendly messages when dealing with invalid gemfire sink\""
  - Description: "\"xd:>stream create --name testgemfire --definition \"\"http --port=8887 | gemfire\"\"   16:20:28,503  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/streams\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.xd.rest.client.impl.SpringXDException: org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition with name 'region' defined in null: Could not resolve placeholder 'regionName' in string value \"\"${regionName}\"\"\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-10** (`tawos-v1.1:3765`), created 2013-04-12T06:44:57.000000Z
  - Title: "Reactor based http ingestion"
  - Description: "When there is support for boostrapping a http server in the reactor project, and inbound SI adapter and associated XD source module should be created."
  - Unknown fields: []
  - Truncated fields: []
- **XD-102** (`tawos-v1.1:3680`), created 2013-05-22T23:35:27.000000Z
  - Title: "Create XDContainer class to start stream server"
  - Description: "Provide optional command line arg to embed the container launcher, aka - xd-admin server. \n\n\nXDContainer.sh --embeddAdmin"
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which client/server model classes and wire contracts are being moved into XD-1045?
- Does the extraction alter JSON parsing or error representations relevant to XD-1198 and XD-465, or only code ownership?
- What existing consumer-compatibility checks accompanied the shared model project at this cutoff?

## XD-1275 (train)

Historical cutoff: 2014-01-29T17:37:13.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `5b86e87edd8fa5ee25a4721144d042c0707e7fc5667aefb7752be953072f303f`

Source input identity SHA-256: `dd03b1f0e935a1c61febd78106fc5d35b7cdc873067d20645831032eef244c23`

### Supplied historical plan

- **XD-1275** (`tawos-v1.1:2532`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-780** (`tawos-v1.1:3020`)
  - Title: "Avoid use of module name twice in location when using a custom modules"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-783** (`tawos-v1.1:3017`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root and XD-783 have unknown title and description. The only recoverable task, XD-780, removes duplicated module-name location usage.",
    "XD-238 explicitly requires simultaneous support for old and new module layouts, and XD-841 describes simplifying custom-module packaging. Neither establishes that this small path change violates compatibility or omits dependency packaging.",
    "XD-702 concerns a DSL stream/module name collision, not duplicated filesystem path segments. Combining it with module-layout work would conflate different mechanisms."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-702** (`tawos-v1.1:3098`), created 2013-08-16T06:56:27.000000Z
  - Title: "stack overflow when trying to create a stream with the same name as a module"
  - Description: "\"(NOTE: even if we do want to prevent the use of module names for stream names, we obviously need to avoid a StackOverflowError)  to reproduce:  start the xd-singlenode container  start the xd-shell, and type the following:  {code} xd:>stream create time --definition \"\"time | log\"\" {code}  that should produce an Internal Server Error output message  check the xd-singlenode console, and find:  {code} SEVERE: Servlet.service() for servlet [xd] in context with path [] threw exception [Handler processing failed; nested exception is java.lang.StackOverflowError] with root cause java.lang.StackOverflowError  at java.lang.StringValue.from(StringValue.java:24)  at java.lang.String.<init>(String.java:178)  at org.springframework.xd.dirt.stream.dsl.Token.<init>(Token.java:46)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.lexIdentifier(Tokenizer.java:195)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.process(Tokenizer.java:62)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.<init>(Tokenizer.java:41)  at org.springframework.xd.dirt.stream.dsl.StreamConfigParser.parse(StreamConfigParser.java:65)  at org.springframework.xd.dirt.stream.dsl.StreamConfigParser.parse(StreamConfigP"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1100** (`tawos-v1.1:2707`), created 2013-11-19T08:53:37.000000Z
  - Title: "\"Create aggregator module that uses redis as a message store\""
  - Description: "\"There is a need for a persistent store for messages so that they can survive the crash of a container node.  The redis implementation in SI is useful since users may already be using redis for other features such as analytics.  This module would sit alongside the current in-memory based aggregator.  It brings in redis as a dependency and there should be configuration options exposed so that one can use a different version of redis as compared to the one that maybe used for analytics.    Due to the need to have redis on the CP, and the large number of different options that each message store implementation provides and the different 3rd party library dependencies, I would like to avoid going down the path of using a profile here as it would seem to go beyond what we had discussed for profile support.  We can revisit as the module contribution story based on boot unfolds.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1175** (`tawos-v1.1:2632`), created 2013-12-18T04:49:09.000000Z
  - Title: "\"Support external defaults for PojoModuleOptions\""
  - Description: "\"The current behavior when there are \"\"global\"\" external defaults to module options is to set them in the placeholder construct: ${foo:${the_default}} where ${the_default} is sourced from some properties file.  The downside is that the module options infrastructure is unaware of them.  Provide support for such defaults (at least when using PojoModuleOptions) in the form of  * Annotate a field (or the setter?) with @Value(\"\"${the_default}\"\") * (maybe) Annotate the pojo with @PropertySource to indicate the location of the properties file * (maybe) come up with a general naming scheme for the properties file\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1222** (`tawos-v1.1:2585`), created 2014-01-13T11:12:11.000000Z
  - Title: "\"Duplicate MBean server definition by MBeanExportingPlugin\""
  - Description: "\"The MBeanServer is referred by XD admin/launcher when JMX is enabled (by setting --jmxEnabled option) and this is defined in xd-global-beans.xml.  The MBeans that are exposed by the modules also use the same MBeanServer define above and there is a duplicate MBeanServer definition (from jmx/common.xml) which the MBeanExportingPlugin adds as a component to the module which doesn't seem to be needed.  Also, currently the flag \"\"jmxEnabled\"\" is generic and used by adminserver/launcher as well as the module MBeanExportingPlugin. If we have a separate flag to enable the JMX *only* for modules then, a separate definition of MBeanServer could be necessary. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-207** (`tawos-v1.1:3576`), created 2013-06-06T17:17:09.000000Z
  - Title: "\"Provide configurable properties for hdfs sink.\""
  - Description: "\"The config file modules/sink/hdfs.xml has a hardcoded value to locate the namenode.   <hdp:configuration register-url-handler=\"\"false\"\">   fs.default.name=hdfs://localhost:9000  </hdp:configuration>  the fs.default.name proprety should be configurable and we should also support loading an external configuration file using      <hdp:configuration properties-location=\"\"${xd.home}/config/hadoop.properties\"\">     </hdp:configuration>  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-369** (`tawos-v1.1:3422`), created 2013-07-03T14:56:04.000000Z
  - Title: "\"Further DSL extensions\""
  - Description: "\"Extend the DSL in the following ways:  - stream naming, use <name>'=' {code} mystream = http | file {code}  - module aliasing (for later referencing) use <label>':' {code} mystream = http | t1: transform --expression=payload.toUpperCase() | t2: transform --expression=payload.toLowerCase() {code}  - sequence of job steps with '&' {code} mybigjobby = step1 --option=value & step2 --option=value {code}  - Channels for sources and sinks, use '>', channels references prefixed ':' {code} // sink channel called foo http | transform --expression=payload.toUppercase() > :foo // source channel called foo :foo > count | file {code}  - Qualify channels with a stream ':'<stream>'.'<channel> {code} mystream = http | transform --expression=payload.toUppercase() > :foo :mystream.foo > count | log {code}   - Reusable substreams, define then reuse {code} myIntricateFlow = transform --expression=payload.toUppercase() | transform --expression=payload.toLowercase()  http | myIntricateFlow | file {code}  - Parameterized substreams, use $XX or ${XX} to indicate parameters {code} obfuscateName = transform --expression=payload.replaceAll(\"\"${name}\"\",XXX)  twitter --query=Bieber | obfuscateName --name=Justi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-505** (`tawos-v1.1:3290`), created 2013-07-17T16:12:15.000000Z
  - Title: "\"Fix XD modules parameters with \"\"-\"\" to use camel case\""
  - Description: "\"XD-482 addresses the use of camel case in 'fixed-delay' job module parameter name. and, we need to fix the same for other module parameters wherever '-' is being used. \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which old/new package layouts does XD-780 change, and does XD-783 or the unknown root already specify compatibility checks?

## XD-1317 (train)

Historical cutoff: 2014-02-13T14:38:11.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `3a7bff8b71b73e177337c55b16635a9f9c9a3f1e6fbb882fddf71b700c2e5dcc`

Source input identity SHA-256: `62dbcc83661a75e8ad564daeb2a37574fd9064874ce777f7519a8d240aec015f`

### Supplied historical plan

- **XD-1317** (`tawos-v1.1:2490`)
  - Title: "All stories related to getting XD deployed and running on YARN"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1314** (`tawos-v1.1:2493`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1321** (`tawos-v1.1:2486`)
  - Title: "Add YARN Client and AppMaster implementations"
  - Description: "Add YARN specifci code based on Janne's prototyping"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1322** (`tawos-v1.1:2485`)
  - Title: "Create shell scripts to deploy XD to YARN"
  - Description: null
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []

### Proposed target

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

#### Evidence for yarn-admin-database-readiness

- XD-1318 / `tawos-v1.1:2489` / description: "During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes)."
- XD-703 / `tawos-v1.1:3097` / description: "The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up"

### Supplied prior evidence for support and counterexample review

- **XD-512** (`tawos-v1.1:3283`), created 2013-07-18T11:12:30.000000Z
  - Title: "\"Create XD shell integration test parser\""
  - Description: "Since most of the xd.shell.itests will do more then one thing (deploy a stream, start it, add a tap, add a job, stop, etc) we decided to decouple writing testcases with running it. Test cases will be written in spring-shell scriptlets. Scriptlets are json files with command and expectedResult as tokens.  Here's an example:\n\n{code}\n{ \"testscript\": \n [ {\"command\" : \"stream create --definition \"http | file\" --name http2file\",\n    \"result\" : \"Created new stream 'http2file'\"},\n   {\"command\" : \"stream list\",\n    \"result\" : \"...\"}\n ]\n}\n{code}\n\nA parser will parse scriptlets, executes it and asserts on expected results. \n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1000** (`tawos-v1.1:2806`), created 2013-10-23T21:49:05.000000Z
  - Title: "\"User should be able to view the list of all the job definitions\""
  - Description: "\"Create a tab view with tabs “Job Definitions”, “Runtime Jobs” (Deployed Jobs?, “Job Instances” (Is Runtime Jobs a better name here?) and “Job Executions”. On clicking “Job Definitions” tab, we can have a table view of job definitions. Since we bootstrap.js, we can have a responsive table layout to list all the available job definitions. At the REST layer, “/jobs” provides the list of job definitions. We can expand the JobsController list()’s QueryOptions to add more criteria (especially to list JobDefinition’s status (Deployed/Undeployed). Also, this is the UI implementation for the shell command “job list” \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1318** (`tawos-v1.1:2489`), created 2014-02-12T16:03:13.000000Z
  - Title: "\"XD container can not be started before the admin server\""
  - Description: "\"The job single partitioned step support (from singlestep-partitioner-support.xml) has the batch job DAOs (loaded from batch.xml).  During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes).   Here is the exception:  15:30:03,600  INFO main xml.XmlBeanDefinitionReader:316 - Loading XML bean definitions from class path resource [META-INF/spring-xd/batch/batch.xml] 15:30:06,154  WARN main annotation.ConfigurationClassEnhancer:318 - @Bean method StepScopeConfiguration.stepScope is non-static and returns an object assignable to Spring's BeanFactoryPostProcessor interface. This will result in a failure to process annotations such as @Autowired, @Resource and @PostConstruct within the method's declaring @Configuration class. Add the 'static' modifier to this method to avoid these container lifecycle issues; see @Bean Javadoc for complete details 15:30:06,705  INFO main support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker:309 - Bean 'org.springframework.xd.dirt.server.ParentConfiguration$JmxConfiguration' of type [class org.springframework.xd.dirt.server.ParentConfigurat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-162** (`tawos-v1.1:3621`), created 2013-05-31T08:40:14.000000Z
  - Title: "Create design document for implementation strategy to support message conversion in ChannelRegistry"
  - Description: "\"The conversion should be based on content-type headers, similar to the way Spring's HttpMessageConverters work (with mime types).  Also, the map of available converters should be extensible while including the most common defaults (for JSON, XML, etc). We most likely want to add a few of our own content types also (e.g. for Tuples).  Most likely, this logic and the configuration methods for extending the converter map, belong in AbstractChannelRegistry since it should be common across all implementations (i.e. the logic should be the same regardless of the transport used after-serialization/before-deserialization).\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []
- **XD-446** (`tawos-v1.1:3348`), created 2013-07-11T06:39:25.000000Z
  - Title: "\"Investigate stream lifecycle issues with redis store\""
  - Description: "\"When running with \"\"./gradlew launch\"\" I get a 500 error when I try to re-deploy an undeployed stream. A subsequent create or destroy also fail  http://localhost:8080:>stream create --definition \"\"time | log\"\" --name ticktock Created new stream 'ticktock' http://localhost:8080:>stream undeploy --name ticktock Un-deployed stream 'ticktock' http://localhost:8080:>stream deploy --name ticktock 13:02:09,936  WARN Spring Shell client.RestTemplate:524 - PUT request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.web.client.HttpServerErrorException: 500 Internal Server Error http://localhost:8080:>stream deploy --name ticktock 13:03:11,453  WARN Spring Shell client.RestTemplate:524 - PUT request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Internal Server Error); invoking error handler Command failed org.springframework.web.client.HttpServerErrorException: 500 Internal Server Error http://localhost:8080:>stream undeploy --name ticktock 13:03:54,576  WARN Spring Shell client.RestTemplate:524 - PUT request for \"\"http://localhost:8080/streams/ticktock\"\" resulted in 500 (Inter"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-485** (`tawos-v1.1:3310`), created 2013-07-15T09:34:37.000000Z
  - Title: "Create stories to enable the use of Spring Shell's 2.0 branch testing facilities "
  - Description: "\"We need a few steps 1. Investigate if we need to move off Spring Shell 1.0 dependency, e.g. need to use code in Spring Shell 2.0 branch 2. If we need to use code in Spring Shell 2.0 branch, we need to release a Spring Shell 1.1 M1 release with appropriate code changes.  Create stories related to Shell release. 3. Determine and document the basic recipe for doing integration tests. 4. Create stories to provide integration tests for each existing command\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-641** (`tawos-v1.1:3157`), created 2013-08-08T16:19:20.000000Z
  - Title: "\"Problem with tapping and > (source channels)\""
  - Description: "\"This is a follow on from XD-592. In that bug we fixed up the ability to use tap with pipe.  Tap when used as a source channel should also work (and should deploy in a more optimized fashion since source channels can be directly connected to the subsequent module, creation of a pass-through tap instance isn't necessary).  This test shows the syntax that should work and the current information about how it fails:  {code} public void testTapSourceChannel() throws IOException {   FileSink sink1 = newFileSink();   FileSink sink2 = newFileSink();    stream().create(\"\"myhttp\"\",     \"\"http --port=9314 | transform --expression=payload.toUpperCase() | filter --expression=true > :foo\"\");    // fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type   tap().create(\"\"wiretap1\"\", \"\"tap myhttp.transform > transform --expression=payload.replaceAll('a','.') | %s\"\", sink1);    // fails in TapDefinition ctor with: java.lang.IllegalArgumentException:   // streamName cannot be empty or null   tap().create(\"\"wiretap2\"\", \"\"tap :foo > transform --expression=payload.replaceAll('a','.') | %s\"\", sink2);    httpPostData(\"\"http://localhos"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-796** (`tawos-v1.1:3004`), created 2013-09-02T07:16:52.000000Z
  - Title: "Create separate commands for \"--all\" shell commands"
  - Description: "\"Commands like \"\"stream deploy\"\" have changed over time to allow passing a \"\"--all\"\" option.  So it's either {{stream deploy foo}} or {{stream deploy --all}}. This has a number of drawbacks, given that these are the only 2 alternatives: - Implementation code is cumbersome - None of the options can be marked mandatory, yet one of them is required. This has to be checked in the command code itself - TAB completion is less powerful as the shell doesn't know if we want the first or the second form.   Consider splitting those commands into two distinct commands, one as before and one literally named {{stream deploy all}}.\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does the completed XD-1318 fix make container-first launch safe in the YARN Client/AppMaster implementation, or must the new launch path preserve admin/database readiness?
- Does XD-1314 already settle this integration contract?
- What company-specific impact and severity apply if this prerequisite remains necessary?

## XD-1391 (train)

Historical cutoff: 2014-03-12T20:28:25.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `aac537e2d6df8655625a7873e45aa0bd8bd887d6ae7952430c58220b4b57afd1`

Source input identity SHA-256: `a1fb766058b265c3172295f09688de9d0797dd1c368d88994f92fc66f7911354`

### Supplied historical plan

- **XD-1391** (`tawos-v1.1:2416`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1328** (`tawos-v1.1:2479`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1375** (`tawos-v1.1:2432`)
  - Title: "Create spike of web app that maps UI design docs to MVC components in Angluar"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The visible work is an Angular MVC spike, with no recoverable description defining release or test acceptance criteria. Missing production checks cannot be inferred from a prototype title.",
    "XD-1229 explicitly supplies Angular build and test automation, while XD-1316 records one E2E tooling warning; together they do not demonstrate two independent unresolved failures in the planned MVC spike.",
    "The Rabbit outputType, JMX conversion and Homebrew failures concern backend deployment paths, with no supplied evidence connecting them to this UI design-mapping work."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1229** (`tawos-v1.1:2578`), created 2014-01-14T22:25:08.000000Z
  - Title: "\"Create build infrastructure for Angular based UI\""
  - Description: "\"Create a project that includes build and test automation for a new Angular based UI.  This work is independent of calling the UI build step from gradle.  A super minimal UI, just to have some basic code, is all that is required.   This should use   Grunt Jasmine Karma Bower YUIdoc (separate story?)  UI Components from backbone should be available in the base project.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1327** (`tawos-v1.1:2480`), created 2014-02-14T18:02:33.000000Z
  - Title: "\"Rabbit source module with outputType fails to deploy\""
  - Description: "\"To replicate the issue:  Create stream:  stream create rabbittest --definition \"\"rabbit --queues=test --outputType=text/plain | log\"\"  Stacktrace thrown:  17:59:56,436 ERROR http-nio-9393-exec-3 rest.RestControllerAdvice:191 - Caught exception while handling a request java.lang.IllegalArgumentException: Module option named outputType is already present  at org.springframework.xd.module.options.FlattenedCompositeModuleOptionsMetadata.<init>(FlattenedCompositeModuleOptionsMetadata.java:56)  at org.springframework.xd.module.options.DelegatingModuleOptionsMetadataResolver.resolve(DelegatingModuleOptionsMetadataResolver.java:49)  at org.springframework.xd.dirt.stream.XDStreamParser.parse(XDStreamParser.java:117)  at org.springframework.xd.dirt.stream.AbstractDeployer.save(AbstractDeployer.java:73)  at org.springframework.xd.dirt.rest.XDController.save(XDController.java:227)  at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)  at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  at java.lang.reflect.Method.invoke(Method.java:601)  at org.springframework.web."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1000** (`tawos-v1.1:2806`), created 2013-10-23T21:49:05.000000Z
  - Title: "\"User should be able to view the list of all the job definitions\""
  - Description: "\"Create a tab view with tabs “Job Definitions”, “Runtime Jobs” (Deployed Jobs?, “Job Instances” (Is Runtime Jobs a better name here?) and “Job Executions”. On clicking “Job Definitions” tab, we can have a table view of job definitions. Since we bootstrap.js, we can have a responsive table layout to list all the available job definitions. At the REST layer, “/jobs” provides the list of job definitions. We can expand the JobsController list()’s QueryOptions to add more criteria (especially to list JobDefinition’s status (Deployed/Undeployed). Also, this is the UI implementation for the shell command “job list” \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1015** (`tawos-v1.1:2791`), created 2013-10-25T10:14:41.000000Z
  - Title: "\"Create a reusable responsive UI layout to render the XD PagedResoures in tabular view\""
  - Description: "\"Create a reusable responsive UI layout to render the PagedResources returned from REST endpoint.   As part of this, try upgrading the bootstrap to 3.0.0 and use the responsive styles offered in it.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1026** (`tawos-v1.1:2780`), created 2013-10-31T13:46:04.000000Z
  - Title: "\"UI: Responsive layout for supported user agents(Mobile, Tablet and Desktop)\""
  - Description: "\"The current admin UI uses bootstrap 3.0.0 which provides responsive design. We need to expand our scope to support all supported user agents.  This requires changes to use user agent specific layout for the UI views.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1243** (`tawos-v1.1:2564`), created 2014-01-15T06:38:00.000000Z
  - Title: "\"Create App for CI to Shutdown XD EC2 Cluster\""
  - Description: "Application will shutdown all servers with a specific name.  \nApplication will take a --cluster-name parameter.   \nGenerate artifact to state success or failure  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-1244** (`tawos-v1.1:2563`), created 2014-01-15T06:49:16.000000Z
  - Title: "\"Create CI Plan for XD EC2 deployment\""
  - Description: "* Use the cleanup app from XD-1243 to stop previous CI runs of XD on EC2.\n* Build XD-EC2 deployer from github.\n* Use XD-EC2 Deployer to deploy the CI XD-Instance\n* Should produce artifact that contains the URL \n   * admin server of the XD cluster.\n   * container servers of the XD cluster"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1245** (`tawos-v1.1:2562`), created 2014-01-15T07:04:57.000000Z
  - Title: "Develop basic acceptance test application to exercise based XD-EC2 deployment from CI"
  - Description: "Create a first pass at an acceptance test app for a stream definition of http | log.  \n\nThis will involve creating two new projects in xd\n\n1. spring-xd-integration-test\n2. spring-xd-acceptance-tests\n\n#1 will contain generally useful utility methods for acceptance test, such as sending data over http, obtaining and asserting JMX values of specific modules.\n#2 will contain tests that use #1 to test the various out of the box modules provides in XD."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1295** (`tawos-v1.1:2512`), created 2014-02-10T00:54:04.000000Z
  - Title: "\"Module message conversion fails to work if JMX is enabled\""
  - Description: "\"If JMX is enabled for modules (enabling the IntegrationMBeanExporter), the ModuleTypeConversionPlugin fails to get the reference to input/output channel (for adding the ContentTypeHeaderInterceptor) and results in exception.  It seems like the IntegrationMBeanExporter (when JMX is enabled) creates JdkDynamicAopProxy for all the integration components and thereby the following check on ModuleTypeConversionPlugin to retrieve the AbstractMessageChannel fails.  AbstractMessageChannel channel = null;    if (isInput) {     channel = module.getComponent(\"\"input\"\", AbstractMessageChannel.class);    }    else {     channel = module.getComponent(\"\"output\"\", AbstractMessageChannel.class);    }  I see the reason why AbstractMessageChannel is used here (to use some of the methods in the implementing class that didn't exist in the interfaces) but IntegrationMBeanExporter creating JdkDynamicAopProxy for the channel fails to resolve as AbstractMessageChannel here.  Following is the full stack trace:  To replicate,  stream create testing --definition \"\"\"\"http --outputType=text/plain | log\"\" 3:45,238 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter1 handler.LoggingHandler:145 - org.spr"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1316** (`tawos-v1.1:2491`), created 2014-02-12T11:51:29.000000Z
  - Title: "UI:Fix E2E test warning"
  - Description: "\"When running E2E tests the following warning may be observed:  {code} Running \"\"karma:e2e\"\" (karma) task INFO [karma]: Karma v0.10.9 server started at http://localhost:7070/_karma_/ INFO [launcher]: Starting browser PhantomJS TypeError: Cannot read property 'verbose' of undefined     at enableWebsocket (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modules/grunt-connect-proxy/lib/utils.js:101:18)     at Object.utils.proxyRequest [as handle] (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modules/grunt-connect-proxy/lib/utils.js:109:5)     at next (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modules/grunt-contrib-connect/node_modules/connect/lib/proto.js:193:15)     at Object.livereload [as handle] (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modules/grunt-contrib-connect/node_modules/connect-livereload/index.js:147:5)     at next (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modules/grunt-contrib-connect/node_modules/connect/lib/proto.js:193:15)     at Function.app.handle (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modules/grunt-contrib-connect/node_modules/connect/lib/proto.js:201:3)     at Server.app (/Users/<USER>dev/git/spring-xd/spring-xd-ui/node_modu"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1323** (`tawos-v1.1:2484`), created 2014-02-14T14:12:36.000000Z
  - Title: "\"Create shell script to retrieve list of xd components running on YARN\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1361** (`tawos-v1.1:2446`), created 2014-03-02T07:08:12.000000Z
  - Title: "\"Classpath issue with homebrew version on MacOSX 10.9.1\""
  - Description: "I've installed spring xd for the first time today on my mac, using the homebrew distribution.\n\nI tried to create the following stream :\n\n{{xd> stream create --definition \"http --port=6666 | log\" --name httptest}}\n\nThis produced the following error : \n\norg.springframework.integration.MessageHandlingException: error occurred in message handler [moduleDeployer]\n\tat org.springframework.integration.handler.AbstractMessageHandler.handleMessage(AbstractMessageHandler.java:79)\n\tat org.springframework.integration.config.ServiceActivatorFactoryBean$1.handleRequestMessage(ServiceActivatorFactoryBean.java:83)\n\tat org.springframework.integration.handler.AbstractReplyProducingMessageHandler.handleMessageInternal(AbstractReplyProducingMessageHandler.java:142)\n\tat org.springframework.integration.handler.AbstractMessageHandler.handleMessage(AbstractMessageHandler.java:73)\n\tat org.springframework.integration.dispatcher.UnicastingDispatcher.doDispatch(UnicastingDispatcher.java:115)\n\tat org.springframework.integration.dispatcher.UnicastingDispatcher.dispatch(UnicastingDispatcher.java:102)\n\tat org.springframework.integration.channel.AbstractSubscribableChannel.doSend(AbstractSubscribableChannel.java:77"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What behavior must the Angular MVC spike demonstrate, and which existing build/test infrastructure from XD-1229 will it reuse?
- Is the resolved XD-1316 E2E tooling issue relevant to the toolchain used by this spike?

## XD-1392 (train)

Historical cutoff: 2014-03-12T20:41:29.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `54e73109eb543eb21984188c51f2aa7cab364a2fd93375398ccd51cab27cb959`

Source input identity SHA-256: `f9bd590a5190e97d73bfc942f57620c4d433c5c5e63b6b29707a46e54d18479e`

### Supplied historical plan

- **XD-1392** (`tawos-v1.1:2415`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1052** (`tawos-v1.1:2754`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1126** (`tawos-v1.1:2681`)
  - Title: "Switch CAPITAL_LETTERS to system.property style in application config"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1190** (`tawos-v1.1:2617`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1208** (`tawos-v1.1:2599`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1290** (`tawos-v1.1:2517`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1378** (`tawos-v1.1:2429`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1126 specifies a property-name migration but provides no known description of aliases, binding changes or property-source precedence.",
    "The actual YAML-shadowing and command-line-default override defects in XD-1186 and XD-1194 are Done; the supplied plan does not establish that naming changes retain or reintroduce their mechanisms.",
    "The root and five other members have no known requirements, so the proposed restriction to name-only validation cannot be inferred."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1186** (`tawos-v1.1:2621`), created 2013-12-23T11:14:15.000000Z
  - Title: "Support use of application.yml fragments"
  - Description: "\"Since spring boot (by default) looks for property sources from file:./config/application.yml and file:./application.yml  In XD bundles, the CLASSPATH of our XD startup scripts'(admin, container, singlenode startup scripts) set to use APP_HOME and APP_HOME/config.  But, if we have an application.yml fragment on $APP_HOME/config, then it is considered as classpath resource and the actual \"\"application.yml\"\" (from dirt lib/ classpath) is not loaded.   Also, we need to separate out the properties files we have inside $APP_HOME/config as by default, boot uses \"\"config\"\" directory as well.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-353** (`tawos-v1.1:3437`), created 2013-07-01T09:55:57.000000Z
  - Title: "Clean up Spring Configuration"
  - Description: "- Container context should be separate from Admin Context in local mode (consistency across transports). Provide a LocalChannelRegistry to bridge deploy and undeploy channels to the ModuleDeployer\n\n- Verify Plugins are not in common module context. They are only needed by the ModuleDeployer not the Modules.\n\n- Add global-beans Config for beans to be shared among admin and container (and available to modules). This would be set as the parent context where needed. (Currently ‘analytics-context.xml’ and JobRepository shared by Admin and modules)\n\n- Fix ModuleDeployer sets parentContext twice\n- Rename common.xml to module-common.xml\n\nNOTE: Analytics parent only required in local mode\n\n- Write unit tests to verify configurations are as expected. Correct bean implementations and no stray beans or redundant instances where not needed\n\n- Decouple Command options from System properties (in general XD property names), this gives us some flexibility in mapping to properties or profiles where appropriate\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1018** (`tawos-v1.1:2788`), created 2013-10-28T11:06:30.000000Z
  - Title: "\"JobDeployer hides root exceptions on failure\""
  - Description: "\"When deploying jobs, the following code (line 103), hides the root cause of deployment failure:    if (exceptionClassName.equals(BEAN_CREATION_EXCEPTION) || exceptionClassName.equals(BEAN_DEFINITION_EXEPTION)) {     throw new MissingRequiredDefinitionException(definition.getName(), cause.getMessage());   }  For example:  org.springframework.xd.dirt.stream.MissingRequiredDefinitionException: Error creating bean with name 'dataSourceInitializer' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Cannot resolve reference to bean 'databasePopulator' while setting bean property 'databasePopulator'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'databasePopulator' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Initialization of bean failed; nested exception is java.lang.NullPointerException  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:103)  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:67)  at org.springframework.xd.dirt.rest.XDController.save(XD"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-110** (`tawos-v1.1:3672`), created 2013-05-23T08:41:56.000000Z
  - Title: "\"Remove use of system property xd.home to define location for install location, rely on environment variable XD_HOME\""
  - Description: "\"This is in the AdminMain and ContainerMain.    Can get the environment property directly in java code unless provided explicitly on the command line using --xdHomeDir.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1130** (`tawos-v1.1:2677`), created 2013-11-26T11:08:46.000000Z
  - Title: "\"Update the EC2 deployer \""
  - Description: "\"EC2 Deployer  Needs to change its configuration behavior to use environment variables vs. the property files * Remove ConfigureSystem class, since we will use environment variables instead * Allow users to set environment variables via the xd-ec2 properties. * If properties are not present use those that are available in the application.yml * Utilize JClouds environment variable setup features to implement this behavior.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1171** (`tawos-v1.1:2636`), created 2013-12-16T16:24:44.000000Z
  - Title: "\"Container (Launcher) id is not unique\""
  - Description: "\"XD container's id is set to use its application context id which is derived from:  ${vcap.application.name:${spring.application.name:${spring.config.name:application}}}:${vcap.application.instance_index:${spring.application.index:${server.port:${PORT:null}}}}  With the *default* values[the PORT is not set and embedded tomcat uses local port], the launcher id is set to \"\"application:0\"\"  When I have multiple launchers then all the launchers have the same id as \"\"application:0\"\" which doesn't seem correct.  Do we need to use the Id that is generated at the XDContainer's constructor here?  public XDContainer() {   this.id = UUID.randomUUID().toString();  }  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1194** (`tawos-v1.1:2613`), created 2014-01-03T09:25:50.000000Z
  - Title: "\"CommandLine default values from container & admin options can not be overridden\""
  - Description: "\"If we have default values from Container/Admin options, then they can not be overridden by the system properties or system environment.   Currently, the only default we have for the Container/Admin options is for \"\"jmxEnabled\"\" option and since it is a boolean it can never be overridden by sys/env property XD_JMX_ENABLED.  I think we need to make sure there are no default values assigned for the non-boolean Container/Admin options and handle the boolean type option separately.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1220** (`tawos-v1.1:2587`), created 2014-01-10T12:30:46.000000Z
  - Title: "\"Batch jobs should use application.yml provided connection as default\""
  - Description: "\"Batch jobs should use application.yml provided connection as default. They now have their own configuration in batch-jdbc.properties. This config needs to account for any changes made to application.yml settings so the data is written to the batch metadata database by default.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1322** (`tawos-v1.1:2485`), created 2014-02-13T11:47:07.000000Z
  - Title: "Add way to provide module config options for XD on YARN"
  - Description: "There seems to be some intersection with the work for this issue and the rationalization of how module properties are handled.  There will be changes to configuration/property management support such that each module (source, sink, etc) will be able to also be overridden in spring-xd.yml (or wherever -Dspring.config.location points to.  The HDFS sink module for example, will have default values based on it's OptionsMetadata and will be of the form <type>.<module>.<option>\n\n\nThat means in the configuration for hdfs.xml sink, there would be a config section such as\n\n{code:xml}\n    <configuration>\n      fs.default.name=${sink.hdfs.hd.fs}\n      mapred.job.tracker=${sink.hdfs.hd.jt}\n      yarn.resourcemanager.address=${sink.hdfs.hd.rm}\n      mapreduce.framework.name=${sink.hdfs.mr.fw}\n    </configuration>\n{code}\n\nWith default values defined by a HdfsSinkOptionsMetadata class.  The hdfs.xml module file would not contain any references to a properties file.\n\nA file specified by -Dspring.config.location could override the values in a config section such as\n\nsink:\n  hdfs:\n    hd.fs : hdfs://foobarhost:8020\n    hd.jt : 10.123.123.123:9000\n\netc.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1349** (`tawos-v1.1:2458`), created 2014-02-25T08:18:42.000000Z
  - Title: "\"Make hdfs configurable via application.yml\""
  - Description: "\"We currently pull all hdfs config properties from hdfs.properties - change that to use application.yml\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What compatibility/alias mappings does the migration preserve between environment variables and system-property-style names?
- Does XD-1126 change property binding or precedence, or only declared names?
- Are effective-value checks already specified in the unknown members?

## XD-1405 (train)

Historical cutoff: 2014-03-18T08:30:20.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `76efdc66ae101ad6bb981a0e8e9f33cbb3e94e3b9f80da457b25b10ed672a302`

Source input identity SHA-256: `f9763f3c24b99e058d893112aebb7e7adff515969723d1c7812b5af242f01b7b`

### Supplied historical plan

- **XD-1405** (`tawos-v1.1:2402`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1406** (`tawos-v1.1:2401`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "Neither XD-1405 nor its observed member XD-1406 has a recoverable title or description at the cutoff, so the proposed work cannot be characterized.",
    "No prior tickets are supplied; no risk can satisfy the required two distinct historical evidence citations. This is insufficient evidence, not a finding that the plan is safe."
  ]
}
```

### Supplied prior evidence for support and counterexample review


### Unresolved labelling questions

- Is any additional cutoff-bound title or description evidence available for XD-1405 and XD-1406?
- Can eligible prior-ticket evidence be supplied once the historical plan topic is known?

## XD-1473 (train)

Historical cutoff: 2014-04-03T06:09:18.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `e1cf5a8e35aab5e2cae74e6e6635bc6e3335c6eb982a4ad2dc88faf5d00add20`

Source input identity SHA-256: `934e35139233d79605dd2280f3b9e0d6ec0e1dc71909505f7e4d66f513dc7e71`

### Supplied historical plan

- **XD-1473** (`tawos-v1.1:2334`)
  - Title: "issues to address after the initial merge of the ZooKeeper runtime"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1474** (`tawos-v1.1:2333`)
  - Title: null
  - Description: "{code}\nStreamDefinition sd = streamParser.parse(name, dslText);\n{code}\n\nWe should also consider explicit methods such as parseStream (so that parseJob and parseComposedModule are at least separate methods, if not separate parser classes that share the common parser support class that is the core of today's parser). The parsing for \"completion providers\" should probably be spun off to its own class as well. In the end, there should be no need for a ParsingContext enum but rather, more explicitly named methods and dedicated classes if that seems like the right approach.\n\nthe StreamDefinition should be composed of \"ModuleDescriptors\" (that name is not set in stone) and other Stream-level metadata like source/sink channels\n\nconsider merging some of StreamFactory code there, and the rest into StreamDeployer\n\nmerge ModuleDescriptor and ModuleDeploymentRequest as part of this effort (again, a new name could be considered, but ModuleDescriptor should take precedence over ModuleDeploymentRequest), and note in the process that ModuleDescriptor was originally designed to be immutable (taking constructor args), but as we migrated the prototype code into XD itself, this was violated. We may wan"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]
- **XD-1475** (`tawos-v1.1:2332`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1476** (`tawos-v1.1:2331`)
  - Title: "Create an under-the-hood document for the distributed runtime"
  - Description: null
  - Unknown fields: ["description"]
  - Truncated fields: []
- **XD-1477** (`tawos-v1.1:2330`)
  - Title: "Consider merging Container and ContainerMetadata as well as their \"repositories\""
  - Description: "The two classes in question are:\n* org.springframework.xd.dirt.cluster.Container\n* org.springframework.xd.dirt.container.ContainerMetadata\n\nThe former is currently used by the Admin when making decisions about Module deployment. That latter was a replacement for RuntimeContainerInforEntity as we migrated the various Redis/InMemory Repositories to use the data that is now available in ZooKeeper instead.\n\nThe ContainerRepository is currently used by the Admin leader, and the ContainerMetadataRepository is used by the REST endpoint that supports the xd-shell's 'runtime containers' command. Perhaps those can also be merged.\n\nIn any case, if not addressed by a larger refactoring, the ContainerRepository should probably support an Iterable return rather than an Iterator. Having finders (e.g. for attribute key/values such as \"group\"==\"foo\") might be convenient for various Module deployment strategies."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1478** (`tawos-v1.1:2329`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "estimate"]
  - Truncated fields: []
- **XD-1479** (`tawos-v1.1:2328`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1480** (`tawos-v1.1:2327`)
  - Title: null
  - Description: "Also likely rename, remove, or replace that Module (maybe can be supplanted by ModuleDescriptor when used in the refactored parser).\n\nAlso, considering the \"url\" property is not necessary (vestige of the prototype), all we'd be left with here is the Module name and type, which are used to identify a Module uniquely. Therefore this Module could be renamed to ModuleKey or something. It could be used within the StreamDefinition itself (e.g. getDescriptor(moduleKey))."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The plan already includes parser/descriptor refactoring in XD-1474, runtime documentation in XD-1476, repository consolidation in XD-1477 and module identity changes in XD-1480; those tasks must not be labelled missing.",
    "XD-1474 is truncated and several member scopes are unknown, so the supplied input cannot establish the complete compatibility or validation work intended.",
    "XD-641 records a completed tap/source-channel failure, while XD-716 concerns Netty and Redis connection initialization. They do not jointly demonstrate the same failure in the planned parser or ZooKeeper repository changes.",
    "XD-1393 already records completed ZooKeeper client configuration support; its presence does not establish an unresolved dependency on that feature."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-953** (`tawos-v1.1:2850`), created 2013-10-14T08:25:02.000000Z
  - Title: "\"Richer module options metadata\""
  - Description: "\"Module options are currently implemented using PropertySourcesPlaceholderConfigurer, doing simple \"\"text\"\" replacements.  This story proposes to introduce a richer model for module options, which could take the following xml representation (keeping in mind that there would be an underlying set of classes that could also apply to e.g. @Configuration approach):  {code:xml} <xd:params>   <xd:param name=\"\"port\"\" help=\"\"the http port to listen on\"\" /> </xd:params> {code}  So, the very first obvious benefit is providing help metadata. The second one is an easy way to list available option names, without resorting to brittle PropertySourcesPlaceholderConfigurer hacks (we wouldn't for example detect xd.stream.name or XD_TRANSPORT as a valid option)  One could also specify defaults/computations, this time benefiting from SpEL everywhere: {code:xml} <xd:params>   <xd:param name=\"\"directory\"\" default=\"\"headers.directory\"\" /> </xd:params> {code}  Lastly, this opens the door to better type checking / combinations / optionality support: {code:xml} <xd:params valid=\"\"fixedDelay || cron\"\">   <xd:param name=\"\"fixedDelay\"\" type=\"\"int\"\" />   <xd:param name=\"\"cron\"\" type=\"\"string\"\" /> </xd:params> {c"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1048** (`tawos-v1.1:2758`), created 2013-11-10T13:19:29.000000Z
  - Title: null
  - Description: "This would be a combination of the existing aggregate counter and field value counter functionality.\n\nFor example if the stream data was for car purchases some fields might be colour, make and model. \nWhen analysing the aggregate data I dont just want to know how many were sold on Monday, but how many of each make or how many of each colour, \nor how many of a particular colour, make AND model. This would allow a dashboard type client to 'drill down' into each dimension or combination of dimensions (in real time without executing batch queries against the raw data)\n\nIdeally the aggregate counter would be specified as \n\nstream create --name mytap --definition \"tap:mystream > aggregatecounter --name=mycount --fieldNames=colour,make,model\"\n\nThe keys would be dynamically created according to the field values in each record (ie in a similar way to the field value counter you would not need to predefine field values) and keys would be created for all combinations of the fields specified eg the record \n\n{ \"colour\":\"silver\" , \"make\":\"VW\" , \"model\" : \"Golf\" } \n\nwould increment the following key counters (in addtion to the existing time buckets)\n\n<existing base counter - ie all fields for thi"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]
- **XD-1418** (`tawos-v1.1:2389`), created 2014-03-19T03:37:45.000000Z
  - Title: "\"Create subproject spring-xd-machine-learning-analytics\""
  - Description: "\"This project contains core abstractions that will allow for multiple implementations of a machine learning algorithm to be implemented via integration with various existing libraries or custom code implementations.    The initial code for this has been developed in a separate github repo and is located here   https://github.com/thomasdarimont/spring-xd/tree/feature/advanced-analytics-support/spring-xd-analytics/src/main/java/org/springframework/xd/analytics/model  The model can assume its use in evaluation of the model inside a stream where the data structure is a Tuple.  Note, it maybe useful to consider Message<Tuple> in case any metadata outside the core 'input data' is required to help guide the evaluation.  The build.gradle file should be updated such that there is a new build artifact spring-xd-machine-learning-analytics.jar along the lines of our other build artifacts.  Open to other naming suggestions.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-641** (`tawos-v1.1:3157`), created 2013-08-08T16:19:20.000000Z
  - Title: "\"Problem with tapping and > (source channels)\""
  - Description: "\"This is a follow on from XD-592. In that bug we fixed up the ability to use tap with pipe.  Tap when used as a source channel should also work (and should deploy in a more optimized fashion since source channels can be directly connected to the subsequent module, creation of a pass-through tap instance isn't necessary).  This test shows the syntax that should work and the current information about how it fails:  {code} public void testTapSourceChannel() throws IOException {   FileSink sink1 = newFileSink();   FileSink sink2 = newFileSink();    stream().create(\"\"myhttp\"\",     \"\"http --port=9314 | transform --expression=payload.toUpperCase() | filter --expression=true > :foo\"\");    // fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type   tap().create(\"\"wiretap1\"\", \"\"tap myhttp.transform > transform --expression=payload.replaceAll('a','.') | %s\"\", sink1);    // fails in TapDefinition ctor with: java.lang.IllegalArgumentException:   // streamName cannot be empty or null   tap().create(\"\"wiretap2\"\", \"\"tap :foo > transform --expression=payload.replaceAll('a','.') | %s\"\", sink2);    httpPostData(\"\"http://localhos"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-716** (`tawos-v1.1:3084`), created 2013-08-19T19:54:19.000000Z
  - Title: "\"TapCommandTests hangs when using a lazily instantiated Lettuce connection\""
  - Description: "\"A change was made in spring-data-redis to instantiate the shared Lettuce connection lazily instead of when the context is initialized. This caused TapCommandTests to hang due to a Netty worker thread trying to initialize the Lettuce connection (Lettuce uses Netty). The change was temporarily backed out of SDR, but we need to consider using a NettyExecutionHandler in NettyHttpInboundChannelAdapter or making the HTTP module's \"\"input\"\" channel an ExecutorChannel to avoid potentially long operations like from happening in an I/O thread.  Also, we need to address why this failure simply hangs the shell. Shell was hung waiting on IO here:  at org.springframework.http.client.SimpleClientHttpResponse.getRawStatusCode(SimpleClientHttpResponse.java:47)  at org.springframework.http.client.AbstractClientHttpResponse.getStatusCode(AbstractClientHttpResponse.java:32)  at org.springframework.xd.shell.command.HttpCommands$1.hasError(HttpCommands.java:93)  at org.springframework.web.client.RestTemplate.doExecute(RestTemplate.java:484)  at org.springframework.web.client.RestTemplate.execute(RestTemplate.java:460)  at org.springframework.web.client.RestTemplate.postForEntity(RestTemplate.java:335) "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1393** (`tawos-v1.1:2414`), created 2014-03-12T07:29:44.000000Z
  - Title: "\"Support explicit client connect string for ZooKeeper\""
  - Description: "\"This will have an effect on both singlenode and distributed mode as  described below...  *singlenode:*  Currently, when running in singlenode mode, an embedded ZooKeeper server is started, and it discovers an available port for client connections and exposes it via a getClientPort() method.  With this change, IF a client connect string is provided explicitly, the embedded ZooKeeper server should not be started, but instead the client connection should be established using that explicitly provided connect string. SEE the \"\"todo\"\" comment above the `SpringApplicationBuilder admin` line within `SingleNodeApplication`.  *distributed:*  Currently, when running in distributed mode, the client connect string is hardcoded to `localhost:2181`. Obviously that is only a short term solution since a real-world distributed runtime would span multiple machines (including the ZooKeeper ensemble itself). That is also why the connect string must support a comma-delimited list of `host:port` values (for redundancy), but the constructor for `ZooKeeperConnection` that accepts a client connect string already supports that via the underlying `CuratorFramework` builder.  With this change, a command-line "
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Which cutoff-available acceptance criteria preserve existing stream, job and composed-module behavior during the parser refactor?
- Is there a second supplied historical incident with the same parser/descriptor failure mechanism as a proposed regression, rather than a separate transport initialization issue?

## XD-1605 (train)

Historical cutoff: 2014-04-23T09:58:12.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `51b3fa490445b19974898219f19d06e03bb9965ffd7f5580575555c4f7487e0a`

Source input identity SHA-256: `22890b0a1146b8cad994dba5943240e8ccb9301cef496ad7d2d48dfa16402bf2`

### Supplied historical plan

- **XD-1605** (`tawos-v1.1:2204`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1255** (`tawos-v1.1:2552`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1430** (`tawos-v1.1:2377`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1466** (`tawos-v1.1:2341`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1497** (`tawos-v1.1:2310`)
  - Title: "Move JMX Endpoints from /jolokia to management/jolokia"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

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

#### Evidence for XD-1605-management-jolokia-access

- XD-1496 / `tawos-v1.1:2311` / title: "Exception thrown when accessing Jolokia via the management context path"
- XD-1396 / `tawos-v1.1:2411` / description: "The container will not start with JMX enabled and the management_port set."

### Supplied prior evidence for support and counterexample review

- **XD-1396** (`tawos-v1.1:2411`), created 2014-03-13T10:29:38.000000Z
  - Title: "\"Container fails to start if JMX is enabled and manage_port is set\""
  - Description: "\"   The container will not start with JMX enabled and the management_port set.  The stacktrace is attached and the settings for the container are enumerated below:      export endpoints_jmx_enabled=true     export endpoints_jmx_uniqueNames=true     export endpoints_jolokia_enabled=true     export XD_JMX_ENABLED=true     export management_port=15005\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1280** (`tawos-v1.1:2527`), created 2014-01-29T14:10:16.000000Z
  - Title: "JMX endpoints not functioning "
  - Description: "I cannot access the JMX/Jolokia endpoints using the Spring Boot RC1 and Snapshot.  Works with XD-M5 and Boot-M7"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1184** (`tawos-v1.1:2623`), created 2013-12-20T17:38:48.000000Z
  - Title: "\"Admin & Launcher startup fails when XD_JMX_ENABLED is set to true\""
  - Description: "\"When exporting of MBeans are enabled via XD_JMX_ENABLED (also, jmxEnabled as in application.yml), the Admin and Lancher server application fail to start.  Since the admin applications has the same 'integrationMbeanExporter' bean name for IntegrationMBeanExporter as that its ParentConfiguration, there is a naming conflicts and the exception thrown as:  (Same is the case for launcher and its parent configuration)  Exception in thread \"\"main\"\" org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'mbeanExporter' defined in class org.springframework.context.annotation.MBeanExportConfiguration: Invocation of init method failed; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [org.springframework.integration.monitor.IntegrationMBeanExporter@1de40d3e] with key 'integrationMBeanExporter'; nested exception is javax.management.InstanceAlreadyExistsException: org.springframework.integration.monitor:name=integrationMBeanExporter,type=IntegrationMBeanExporter  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1553)  at"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1496** (`tawos-v1.1:2311`), created 2014-04-07T09:38:28.000000Z
  - Title: "Exception thrown when accessing Jolokia via the management context path"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1524** (`tawos-v1.1:2283`), created 2014-04-09T12:19:54.000000Z
  - Title: "\"Create small documentation section on jmx/monitoring functionalty\""
  - Description: "\"Should mention jolokia, how to turn on/off boot/jolokia http metric/monitoring and jmx.  Mention the naming strategy to identify modules running in a stream.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1532** (`tawos-v1.1:2275`), created 2014-04-10T13:19:16.000000Z
  - Title: "\"Clean up MBean registration for failed module deployments\""
  - Description: "\"When a module fails to deploy (for instance an http module configured with a port that is already bound) subsequent attempts to deploy the module fail due to a JMX exception:  {noformat} java.lang.RuntimeException: org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#beafb1fc-4423-4e4f-a88c-1655ea0fdcc5'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=output, sends=0]] with key 'org.springframework.integration:type=MessageChannel,name=output'; nested exception is javax.management.InstanceAlreadyExistsException: xd.foo:module=http.0,component=MessageChannel,name=output  at org.springframework.xd.dirt.server.ContainerRegistrar.deployStreamModule(ContainerRegistrar.java:447)  at org.springframework.xd.dirt.server.ContainerRegistrar.onChildAdded(ContainerRegistrar.java:346)  at org.springframework.xd.dirt.server.ContainerRegistrar.access$700(ContainerRegistrar.java:92)  at org.springframework.xd.dirt.server.ContainerRegistrar$DeploymentListener.childEvent(ContainerRegistrar.java:655)  at org.apache.curat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-467** (`tawos-v1.1:3328`), created 2013-07-12T10:17:45.000000Z
  - Title: null
  - Description: "There's a lifecycle problem when a tap creation fails (e.g. because the DSL syntax is wrong). Subsequent attempts to create the tap will fail with an error:\n\n [{\"links\":[],\"logref\":\"MessageHandlingException\",\"message\":\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"}]\n\nDisabling JMX solves the issue.\n\n\nreproduce\nCreate a bad stream definition name 'bad'\nTry to recreate with the same name, but correct stream definitions.  The system will report that the stream already exists."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-601** (`tawos-v1.1:3196`), created 2013-08-05T13:23:44.000000Z
  - Title: "\"./xd-container  --transport local throws NumberFormatException\""
  - Description: "\"./xd-container [OK] ./xd-container --transport redis [OK] ./xd-container --transport rabbit [OK] ./xd-container --transport local [FAIL]  <USER>mbp:bin administrator$ ./xd-container --transport local Exception in thread \"\"main\"\" org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.jolokia.jvmagent.spring.SpringJolokiaAgent#0': Invocation of init method failed; nested exception is java.lang.NumberFormatException: For input string: \"\"${xd.jmx.port}\"\"  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1488)  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:524)  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:461)  at org.springframework.beans.factory.support.AbstractBeanFactory$1.getObject(AbstractBeanFactory.java:295)  at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:223)  at org.springframework.beans.factory.support.Abstract"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-742** (`tawos-v1.1:3058`), created 2013-08-22T14:18:55.000000Z
  - Title: "\"REST API for Job Management\""
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: []
  - Truncated fields: []
- **XD-887** (`tawos-v1.1:2915`), created 2013-09-23T03:06:16.000000Z
  - Title: "\"Package modules with their support jars\""
  - Description: "\"Currently, a lot of jars that are on the classpath of xd-dirt are there to support modules. We should move those to the lib/ construct of a module and remove them from the CP of dirt.  But this should not be done by simple \"\"mv\"\", as we'd lose version tracking and dependency management offered by gradle.  Pending a \"\"dependency-aware\"\" ModuleRegistry, we should be able to alter the build.gradle file so that it - knows about individual modules (maybe handles them as project) - copies its libs into the appropriate directory - does not copy dependencies that are already legitimate dependencies of xd-dirt (this can be achieved by runtime introspection of the dependeny tree of both projects)  \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does the still-To-Do XD-1496 exception occur on the exact management/jolokia route introduced by XD-1497?
- Which existing member owns that access failure and verification of the migrated monitoring request?
- Is a separate management port part of the intended deployment, and if so does the completed XD-1396 fix apply?

## XD-1606 (train)

Historical cutoff: 2014-04-23T10:42:19.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `c0cca51eedc3ab2ef543e36e1f2cb91aa55375ec69456a20cedf8387a8f23312`

Source input identity SHA-256: `ddf335d27990120b2be13ad0dc7a0b4db5fd14d62a92fbb597b35b985973d132`

### Supplied historical plan

- **XD-1606** (`tawos-v1.1:2203`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1522** (`tawos-v1.1:2285`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1601** (`tawos-v1.1:2208`)
  - Title: null
  - Description: "There seems to be some inconsistency with the naming strategy for the named channels.\n\nFor example:\n\nIf we create a job \"j1\", the job launching request queue name in the message broker would \"job:j1\". To send a launching request, we can either use \"queue:job:j1\" or \"job:j1\" (both seems to work).\n\nIf we create a stream with the named p2p channel \"foo\" we expect to use the syntax \"queue:foo\" and the message broker will have the queue name \"queue:foo\"\n\nThe StreamConfigParser resolves the source/sink channel names for tap to deduce the module index from the channel component: ChannelNode.resolve(StreamLookupEnvironment env)\n\nBut, in case of the named channels that have prefix \"topic:\" or \"queue:\", their names are used as is the only exception in a case where (From StreamConfigParser's eatChannelReference(boolean tapAllowed)\n \n```\n// queue:XXX\n\t\t\t// topic:XXX\n\t\t\tif (firstToken.data.equalsIgnoreCase(\"queue\")) {\n\t\t\t\tchannelType = ChannelType.QUEUE;\n\t\t\t}\n\t\t\telse if (firstToken.data.equalsIgnoreCase(\"topic\")) {\n\t\t\t\tchannelType = ChannelType.TOPIC;\n\t\t\t}\n\t\t\t// TODO: DT not sure if this is the best way to handle\n\t\t\t// StreamConfigParserTests.substreamsWithSourceChannels()\n\t\t\tif (channelScopeCo"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: ["description"]

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1601 describes accepted job/channel forms and says both job aliases work; its truncated text does not specify a new naming contract or a failing deployment.",
    "XD-641 and XD-1177 describe completed tap resolution and repeated-module identity fixes, with no supplied evidence that XD-1601 removes their protections.",
    "Unknown root and XD-1522 text do not establish omitted compatibility tests or planned alias removal."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1295** (`tawos-v1.1:2512`), created 2014-02-10T00:54:04.000000Z
  - Title: "\"Module message conversion fails to work if JMX is enabled\""
  - Description: "\"If JMX is enabled for modules (enabling the IntegrationMBeanExporter), the ModuleTypeConversionPlugin fails to get the reference to input/output channel (for adding the ContentTypeHeaderInterceptor) and results in exception.  It seems like the IntegrationMBeanExporter (when JMX is enabled) creates JdkDynamicAopProxy for all the integration components and thereby the following check on ModuleTypeConversionPlugin to retrieve the AbstractMessageChannel fails.  AbstractMessageChannel channel = null;    if (isInput) {     channel = module.getComponent(\"\"input\"\", AbstractMessageChannel.class);    }    else {     channel = module.getComponent(\"\"output\"\", AbstractMessageChannel.class);    }  I see the reason why AbstractMessageChannel is used here (to use some of the methods in the implementing class that didn't exist in the interfaces) but IntegrationMBeanExporter creating JdkDynamicAopProxy for the channel fails to resolve as AbstractMessageChannel here.  Following is the full stack trace:  To replicate,  stream create testing --definition \"\"\"\"http --outputType=text/plain | log\"\" 3:45,238 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter1 handler.LoggingHandler:145 - org.spr"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-799** (`tawos-v1.1:3001`), created 2013-09-02T23:31:17.000000Z
  - Title: "\"Change rabbitmq sink to use routing-key-expression instead of routing-key\""
  - Description: "\"The current rabbitmq sink uses the attribute routing-key, which defaults to the name of the stream.  This should be change to use the attribute routing-key-expression so that the routing-key can be determined using SpEL.  This will enable a dynamic evaluation of the routing-key based on message payload/header.  *Implementation Suggestions*  This hopefully should be changing the XML description of the sink to     routing-key-expression=\"\"${routingKey:'${xd.stream.name}'}  This way, the ${xd.stream.name} is surrounded by a single quote to indicate a string literal to SpEL in the default case.    *How to verify it works.*  One of the simple uses of this is to create a routing key based on payload.  In a distributed word-count example, the hashcode of a word would be sent to a certain number of processing modules that would perform the count. The idea is that the same word is sent to the same node over and over again, in particular if in-memory counters or state is computed - using centralized redis counters this wouldn't be necessary in the case of only counter state.  The stream   http | rabbit --routingKey=\"\"'word-' + payload.hashCode() % 3\"\"  is an example of a stream that can be "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-438** (`tawos-v1.1:3356`), created 2013-07-10T08:51:08.000000Z
  - Title: "\"More DSL work: exploiting source/sink channels\""
  - Description: "\"The DSL changes under XD-369 now build stream Ast objects that can include a source and sink channel:  {code} // Source Channel :mystream.foo > count | log  // Sink Channel http | count > :foo {code}  These new fields in the Ast object need to be copied into the module deployment request objects and then used at the destination as the channels for wiring things together.  Currently the only channels used are the .NNN numeric channels where NNN is the index of the module in the stream definition. The source/sink channels are 'extra' channels that need creating - the source channel acting as a real source for the next module in the chain whilst the sink channel acts as a sink output for the last channel in the chain.    I can think of two ways to handle the implementation: - In order to police the stream structure as \"\"source | processor* | sink\"\" maybe special SourceChannel and SinkChannel modules are created to represent these channels and when deployment happens the deployer understands that they don't represent a real request to deploy a module but simply the channels to wire up to the adjacent module.  - Carry source/sink channel info in the existing module definitions. But the"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-874** (`tawos-v1.1:2928`), created 2013-09-19T21:33:03.000000Z
  - Title: "For file based item reader jobs, step/job completion message should have name of file sent on named channel"
  - Description: "\"It looks like we don't handle deletion of source files currently. We should provide some support for that - Maybe there is a way to into Spring Integration's PseudoTransactionManager support:  http://docs.spring.io/spring-integration/api/org/springframework/integration/transaction/PseudoTransactionManager.html  The *File Source* should possibly also support File archival functionality (But that might also be a dedicated processor?). Not sure where we want to set the semantic boundaries for the File Source. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1322** (`tawos-v1.1:2485`), created 2014-02-13T11:47:07.000000Z
  - Title: "Add way to provide module config options for XD on YARN"
  - Description: "There seems to be some intersection with the work for this issue and the rationalization of how module properties are handled.  There will be changes to configuration/property management support such that each module (source, sink, etc) will be able to also be overridden in spring-xd.yml (or wherever -Dspring.config.location points to.  The HDFS sink module for example, will have default values based on it's OptionsMetadata and will be of the form <type>.<module>.<option>\n\n\nThat means in the configuration for hdfs.xml sink, there would be a config section such as\n\n{code:xml}\n    <configuration>\n      fs.default.name=${sink.hdfs.hd.fs}\n      mapred.job.tracker=${sink.hdfs.hd.jt}\n      yarn.resourcemanager.address=${sink.hdfs.hd.rm}\n      mapreduce.framework.name=${sink.hdfs.mr.fw}\n    </configuration>\n{code}\n\nWith default values defined by a HdfsSinkOptionsMetadata class.  The hdfs.xml module file would not contain any references to a properties file.\n\nA file specified by -Dspring.config.location could override the values in a config section such as\n\nsink:\n  hdfs:\n    hd.fs : hdfs://foobarhost:8020\n    hd.jt : 10.123.123.123:9000\n\netc.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1363** (`tawos-v1.1:2444`), created 2014-03-03T08:16:18.000000Z
  - Title: "\"Tap XD batch Job output\""
  - Description: "\"Currently, job module only has an input channel that receives the job launching requests. If we have an output channel for the job module, we get the following benefits:  1) The output channel reflects the JobExecution from the job launching message handler's reply channel 2) This can be different from JobExecution listener's notification channel where we would get both the beforeJob() and afterJob() notification. 3) We can tap the output channel to send the job results to some other sinks.  Along with this improvement, planning to do some more refactoring on the Plugins so that some of the common implementation methods are handled in the base class. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-641** (`tawos-v1.1:3157`), created 2013-08-08T16:19:20.000000Z
  - Title: "\"Problem with tapping and > (source channels)\""
  - Description: "\"This is a follow on from XD-592. In that bug we fixed up the ability to use tap with pipe.  Tap when used as a source channel should also work (and should deploy in a more optimized fashion since source channels can be directly connected to the subsequent module, creation of a pass-through tap instance isn't necessary).  This test shows the syntax that should work and the current information about how it fails:  {code} public void testTapSourceChannel() throws IOException {   FileSink sink1 = newFileSink();   FileSink sink2 = newFileSink();    stream().create(\"\"myhttp\"\",     \"\"http --port=9314 | transform --expression=payload.toUpperCase() | filter --expression=true > :foo\"\");    // fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type   tap().create(\"\"wiretap1\"\", \"\"tap myhttp.transform > transform --expression=payload.replaceAll('a','.') | %s\"\", sink1);    // fails in TapDefinition ctor with: java.lang.IllegalArgumentException:   // streamName cannot be empty or null   tap().create(\"\"wiretap2\"\", \"\"tap :foo > transform --expression=payload.replaceAll('a','.') | %s\"\", sink2);    httpPostData(\"\"http://localhos"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1177** (`tawos-v1.1:2630`), created 2013-12-18T11:32:06.000000Z
  - Title: "\"Change module naming strategy in parser taking into account no duplicate labels and repeated modules\""
  - Description: "\"Labels should only be used help uniquely identify a module in a stream.  The stream definition a | x: b | x: c | d should throw an error since the label x is applied to two modules.  Also ambiguity exists with a stream definition such as   http | transform | transform | filter | hdfs  since a module with the name 'transform' will exist twice, meaning a tap on transform will result in message from both transform modules.  To make the naming unique and the usage with taps, the following naming strategy is proposed demonstrated by example.  http | transform | transform | filter | hdfs http, transform.0, transform.1, filter, hdfs  If a use tries to tap on transform, an error would be shown saying that  you could try to tap on transform.0 or transform.1 or alternatively use labels.  http | transform | filter | transform | hdfs http, transform.0, filter, transform.1, hdfs  http | x: transform | filter | transform | hdfs http, x, filter, transform, hdfs  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-369** (`tawos-v1.1:3422`), created 2013-07-03T14:56:04.000000Z
  - Title: "\"Further DSL extensions\""
  - Description: "\"Extend the DSL in the following ways:  - stream naming, use <name>'=' {code} mystream = http | file {code}  - module aliasing (for later referencing) use <label>':' {code} mystream = http | t1: transform --expression=payload.toUpperCase() | t2: transform --expression=payload.toLowerCase() {code}  - sequence of job steps with '&' {code} mybigjobby = step1 --option=value & step2 --option=value {code}  - Channels for sources and sinks, use '>', channels references prefixed ':' {code} // sink channel called foo http | transform --expression=payload.toUppercase() > :foo // source channel called foo :foo > count | file {code}  - Qualify channels with a stream ':'<stream>'.'<channel> {code} mystream = http | transform --expression=payload.toUppercase() > :foo :mystream.foo > count | log {code}   - Reusable substreams, define then reuse {code} myIntricateFlow = transform --expression=payload.toUppercase() | transform --expression=payload.toLowercase()  http | myIntricateFlow | file {code}  - Parameterized substreams, use $XX or ${XX} to indicate parameters {code} obfuscateName = transform --expression=payload.replaceAll(\"\"${name}\"\",XXX)  twitter --query=Bieber | obfuscateName --name=Justi"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Is XD-1601 intended to document existing naming behavior, change canonical broker names, or remove accepted aliases?
- What exact accepted syntax or parser rule will change, and is there a cutoff-visible reproduction demonstrating a resulting incompatibility?

## XD-1607 (train)

Historical cutoff: 2014-04-23T10:46:28.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `6a241d7657c0c5f2cfcf97bfe9872c62e395290c067d9615f5f199515bb2de17`

Source input identity SHA-256: `91bbb0dd45208c739aefb4903b1387450e1f999a953cf89ff2628d5fd87b2f70`

### Supplied historical plan

- **XD-1607** (`tawos-v1.1:2202`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1270** (`tawos-v1.1:2537`)
  - Title: null
  - Description: "1) Improve how the state of the stream is managed.\n\n\n\n\nA deploy command moves the stream from the undeployed state to the deploying state.\nIf all modules in the stream are successfully deployed, the stream state is ‘deployed’\nIf one or more module deployments failed, the stream state is failed.  Any modules that were successfully deployed, are still running.  \nSending an undeploy command will stop all modules of the stream and return the stream to the undeployed state.\n\nFor the individual modules that failed, we will be able to find out which ones failed.  Not yet sure if we can try to redeploy just those parts of the stream that failed.\n\nThe channel that will be used to update the state of the stream is xd.stream.status\n\nTBD: Details of how the state for each module in the stream will be stored."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-1416** (`tawos-v1.1:2391`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1270 explicitly distinguishes deploying, deployed and failed states, retains successfully deployed modules after partial failure, and requires undeploy to stop all modules; warning that partial-failure handling or cleanup is missing would contradict this plan.",
    "XD-1291 and XD-1452 document shutdown-order exceptions and HTTP thread leaks, but both are marked Done and do not establish that the new stream-state work repeats those mechanisms or omits cleanup.",
    "Per-module state storage is explicitly TBD, while the root and XD-1416 text are unknown. This design uncertainty does not establish a supported dependency or scope gap."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1384** (`tawos-v1.1:2423`), created 2014-03-10T15:20:24.000000Z
  - Title: "Improve job launch functionality with distributed nodes"
  - Description: "When sending a launch request, the message is not targeted to the container node that hosts the deployed job.  With RabbitMQ, the message is not ack'd so it will get picked up eventually by the container that hosts the deployed job.  This should change to a targeted message.\n\n-----\nOriginal description from Thomas below\n\nTried deploying some batch jobs and they all seem to fail when running admin and one container using redis as transport\n\nxd:>job create mongojob --definition \"hdfsmongodb --resources=/data/*.log --names=col1,col2,col3 --idField=col1 --collectionName=test\"\n\nfails with this:\n{quote}\n18:19:01,612  WARN redisInboundAdapter-redis:queue-inbound-channel-adapter6 boot.SpringApplication:635 - Error handling failed (Error creating bean with name 'integrationRequestMappingHandlerMapping': Initialization of bean failed; nested exception is java.lang.IllegalStateException: org.springframework.context.annotation.AnnotationConfigApplicationContext@25e7506f has not been refreshed yet)\n18:19:01,614 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter6 handler.LoggingHandler:145 - org.springframework.messaging.MessageHandlingException: error occurred in message handler [mod"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-799** (`tawos-v1.1:3001`), created 2013-09-02T23:31:17.000000Z
  - Title: "\"Change rabbitmq sink to use routing-key-expression instead of routing-key\""
  - Description: "\"The current rabbitmq sink uses the attribute routing-key, which defaults to the name of the stream.  This should be change to use the attribute routing-key-expression so that the routing-key can be determined using SpEL.  This will enable a dynamic evaluation of the routing-key based on message payload/header.  *Implementation Suggestions*  This hopefully should be changing the XML description of the sink to     routing-key-expression=\"\"${routingKey:'${xd.stream.name}'}  This way, the ${xd.stream.name} is surrounded by a single quote to indicate a string literal to SpEL in the default case.    *How to verify it works.*  One of the simple uses of this is to create a routing key based on payload.  In a distributed word-count example, the hashcode of a word would be sent to a certain number of processing modules that would perform the count. The idea is that the same word is sent to the same node over and over again, in particular if in-memory counters or state is computed - using centralized redis counters this wouldn't be necessary in the case of only counter state.  The stream   http | rabbit --routingKey=\"\"'word-' + payload.hashCode() % 3\"\"  is an example of a stream that can be "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1048** (`tawos-v1.1:2758`), created 2013-11-10T13:19:29.000000Z
  - Title: null
  - Description: "This would be a combination of the existing aggregate counter and field value counter functionality.\n\nFor example if the stream data was for car purchases some fields might be colour, make and model. \nWhen analysing the aggregate data I dont just want to know how many were sold on Monday, but how many of each make or how many of each colour, \nor how many of a particular colour, make AND model. This would allow a dashboard type client to 'drill down' into each dimension or combination of dimensions (in real time without executing batch queries against the raw data)\n\nIdeally the aggregate counter would be specified as \n\nstream create --name mytap --definition \"tap:mystream > aggregatecounter --name=mycount --fieldNames=colour,make,model\"\n\nThe keys would be dynamically created according to the field values in each record (ie in a similar way to the field value counter you would not need to predefine field values) and keys would be created for all combinations of the fields specified eg the record \n\n{ \"colour\":\"silver\" , \"make\":\"VW\" , \"model\" : \"Golf\" } \n\nwould increment the following key counters (in addtion to the existing time buckets)\n\n<existing base counter - ie all fields for thi"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]
- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-719** (`tawos-v1.1:3081`), created 2013-08-20T09:50:31.000000Z
  - Title: "\"Refactor the file source module to have lib/config directories\""
  - Description: "\"Convert a simple module, such as file, to further test that what was done in the previous story, “Use ParentLastClassLoader to create the Modules ApplicationContext.” works as expected.  *Implementation Suggestions*  Remove from build.gradle the dependency on spring-integration-file and place that jar inside a directory  ./modules/source/file/lib   place the current file.xml inside ./modules/source/file/config  *How to verify it works.*  1. Running tests that currently use the file source, e.g. in spring shell, should work as before 2. When deploying a stream file | log, we should be able to interrogate the channel registry and make sure it found the dependencies for the module, ModuleDescriptor should have a not-null URL[] property.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1291** (`tawos-v1.1:2516`), created 2014-01-31T14:53:24.000000Z
  - Title: "Handle container shutdown gracefully"
  - Description: "\"Currently, ModuleDeployer is a disposable bean. When the container context is closed, the ModuleDeployer bean is destroyed along with its associated common context and deployed modules. Issue arises, if the connectionfactory bean associated with the deployed modules' message bus bindings  is destroyed before the ModuleDeployer bean, there is exception stacktrace (at least in case of Redis MessageBus) saying \"\"Connection closed\"\".   Adding SmartLifecycle support to ModuleDeployer will make sure all the beans are destroyed during Lifecycle processor's stop() method before any of the singletonbeans are destroyed.  The stacktrace (when using Redis MessageBus is):  org.springframework.data.redis.RedisSystemException: Redis exception; nested exception is com.lambdaworks.redis.RedisException: Connection closed at org.springframework.data.redis.connection.lettuce.LettuceExceptionConverter.convert(LettuceExceptionConverter.java:45) at org.springframework.data.redis.connection.lettuce.LettuceExceptionConverter.convert(LettuceExceptionConverter.java:35) at org.springframework.data.redis.connection.lettuce.LettuceConverters.toDataAccessException(LettuceConverters.java:158) at org.springframew"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1452** (`tawos-v1.1:2355`), created 2014-03-27T07:19:08.000000Z
  - Title: "\"http module leaks threads\""
  - Description: "\"Attempts to create/use/undeploy a stream involving the http module will result in an OOME stating that VM could not create native thread.  Other modules should be checked as well. {noformat}  at java.lang.Thread.run(Thread.java:724) Caused by: org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.x.http.NettyHttpInboundChannelAdapter#0'; nested exception is java.lang.OutOfMemoryError: unable to create new native thread  at org.springframework.context.support.DefaultLifecycleProcessor.doStart(DefaultLifecycleProcessor.java:176)  at org.springframework.context.support.DefaultLifecycleProcessor.access$200(DefaultLifecycleProcessor.java:51)  at org.springframework.context.support.DefaultLifecycleProcessor$LifecycleGroup.start(DefaultLifecycleProcessor.java:346)  at org.springframework.context.support.DefaultLifecycleProcessor.startBeans(DefaultLifecycleProcessor.java:149)  at org.springframework.context.support.DefaultLifecycleProcessor.start(DefaultLifecycleProcessor.java:91)  at org.springframework.context.support.AbstractApplicationContext.start(AbstractApplicationContext.java:1180)  at org.springframework.xd.module.core.Simp"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What state-storage and acknowledgment rules will XD-1270 use for partial deployment and undeploy completion?
- Are the resolved shutdown-order and HTTP thread-leak fixes exercised by the existing lifecycle tests that this state-management work will reuse?

## XD-1608 (train)

Historical cutoff: 2014-04-23T10:51:31.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `d075344c133436aa767f501e1f352a6eddf2bcca33446b7431f2024e866f8fea`

Source input identity SHA-256: `bf1630d05ca5b41fd95770dabe09b27f902a87e91cfd0bf40b2362b4d6b7d094`

### Supplied historical plan

- **XD-1608** (`tawos-v1.1:2201`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1002** (`tawos-v1.1:2804`)
  - Title: null
  - Description: "On clicking a specific job name in the deployed jobs list, we need to redirect the user to show the list of all the job executions on that job.\n\nUser should be able to navigate back to the deployed jobs list."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1004** (`tawos-v1.1:2802`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1006** (`tawos-v1.1:2800`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1007** (`tawos-v1.1:2799`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1507** (`tawos-v1.1:2300`)
  - Title: "Able to submit jobs that are not currently deployed using Admin UI"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1002 explicitly includes navigation from a deployed job to its executions and back. XD-1507 explicitly identifies submission of undeployed jobs through the Admin UI, so that concern must not be presented as forgotten work.",
    "XD-1384 concerns distributed launch-message routing and XD-703 concerns shared persistence of job state. They are relevant backend context but do not establish an uncovered UI-state or navigation failure in the visible tasks.",
    "The root and three other children lack recoverable requirements. Earlier UI specifications (XD-1000, XD-1001 and XD-1003) distinguish job definitions, deployments and launches, but do not demonstrate two supporting failure examples for a new gap here."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1000** (`tawos-v1.1:2806`), created 2013-10-23T21:49:05.000000Z
  - Title: "\"User should be able to view the list of all the job definitions\""
  - Description: "\"Create a tab view with tabs “Job Definitions”, “Runtime Jobs” (Deployed Jobs?, “Job Instances” (Is Runtime Jobs a better name here?) and “Job Executions”. On clicking “Job Definitions” tab, we can have a table view of job definitions. Since we bootstrap.js, we can have a responsive table layout to list all the available job definitions. At the REST layer, “/jobs” provides the list of job definitions. We can expand the JobsController list()’s QueryOptions to add more criteria (especially to list JobDefinition’s status (Deployed/Undeployed). Also, this is the UI implementation for the shell command “job list” \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1001** (`tawos-v1.1:2805`), created 2013-10-23T22:03:13.000000Z
  - Title: "\"User should be able to view the list of all Deployed Jobs\""
  - Description: "\"On clicking the “Deployed Jobs”, we can have a table view of all the deployed jobs. This is again a responsive table layout with all the job definitions with status “deployed”. The deployed XD job corresponds to a single batch Job Instance.   This story addresses the UI layout changes to display existing JobInstance information.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-742** (`tawos-v1.1:3058`), created 2013-08-22T14:18:55.000000Z
  - Title: "\"REST API for Job Management\""
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: []
  - Truncated fields: []
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1003** (`tawos-v1.1:2803`), created 2013-10-23T22:08:17.000000Z
  - Title: "\"UI: User should be able to launch a job from Deployed jobs page\""
  - Description: "\"From the Deployed jobs page, user should be able to click on the \"\"Launch\"\" button on a specific job and specify the Job parameters as key value pairs in the text box and we will convert that into JSON string as JobParameters into JobLaunch request.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1384** (`tawos-v1.1:2423`), created 2014-03-10T15:20:24.000000Z
  - Title: "Improve job launch functionality with distributed nodes"
  - Description: "When sending a launch request, the message is not targeted to the container node that hosts the deployed job.  With RabbitMQ, the message is not ack'd so it will get picked up eventually by the container that hosts the deployed job.  This should change to a targeted message.\n\n-----\nOriginal description from Thomas below\n\nTried deploying some batch jobs and they all seem to fail when running admin and one container using redis as transport\n\nxd:>job create mongojob --definition \"hdfsmongodb --resources=/data/*.log --names=col1,col2,col3 --idField=col1 --collectionName=test\"\n\nfails with this:\n{quote}\n18:19:01,612  WARN redisInboundAdapter-redis:queue-inbound-channel-adapter6 boot.SpringApplication:635 - Error handling failed (Error creating bean with name 'integrationRequestMappingHandlerMapping': Initialization of bean failed; nested exception is java.lang.IllegalStateException: org.springframework.context.annotation.AnnotationConfigApplicationContext@25e7506f has not been refreshed yet)\n18:19:01,614 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter6 handler.LoggingHandler:145 - org.springframework.messaging.MessageHandlingException: error occurred in message handler [mod"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1026** (`tawos-v1.1:2780`), created 2013-10-31T13:46:04.000000Z
  - Title: "\"UI: Responsive layout for supported user agents(Mobile, Tablet and Desktop)\""
  - Description: "\"The current admin UI uses bootstrap 3.0.0 which provides responsive design. We need to expand our scope to support all supported user agents.  This requires changes to use user agent specific layout for the UI views.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1544** (`tawos-v1.1:2263`), created 2014-04-11T07:45:59.000000Z
  - Title: "Need to be able setup environment to run jobs on Ec2"
  - Description: "Currently in order to deploy a job we copy the job to the containers and admin server, and then bounce the servers.  The tests will need the ability to copy these jobs to the containers, & admin and then bounce the servers.  "
  - Unknown fields: ["type", "status", "estimate"]
  - Truncated fields: []
- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What acceptance behavior and regression tests are already covered by XD-1507, including the deployed/undeployed state distinction?

## XD-1609 (train)

Historical cutoff: 2014-04-23T10:57:52.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `bf2ef0c688299885b390b92b4dd21f229e35c4c3f3407d4be09bba98f4d6f341`

Source input identity SHA-256: `06032d9f9a5c5119f9d9575d7ec3f146b40b0d5d5069e96683c4bffabdec7e23`

### Supplied historical plan

- **XD-1609** (`tawos-v1.1:2200`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1592** (`tawos-v1.1:2217`)
  - Title: "\"Make transport configuration extensible. \""
  - Description: "\"Change message-bus.xml to read   <import resource=\"\"classpath*:/META-INF/spring-xd/transports/${XD_TRANSPORT}-bus.xml\"\"/>  So new transports may be configured in external jars\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1593** (`tawos-v1.1:2216`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1596** (`tawos-v1.1:2213`)
  - Title: null
  - Description: "acknowlege-more, tx-size, prefetch-count, concurrency etc."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1592 explicitly supplies extensible transport configuration and is Done at this cutoff. XD-1350 and XD-1336 also describe completed enum-removal work, contradicting a warning that extensibility is simply missing.",
    "The root and XD-1593 have no recoverable scope text; XD-1596 lists acknowledgement, transaction size, prefetch and concurrency without identifying the required semantics. This incompleteness is not itself a risk.",
    "XD-1356 documents Hadoop class/namespace loading errors and XD-1318 documents batch database startup order. The supplied sample does not connect two demonstrated failures to these particular transport settings or external transport jars."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1343** (`tawos-v1.1:2464`), created 2014-02-24T07:33:09.000000Z
  - Title: "\"Provide a conventional way to extend XD Container configuration\""
  - Description: "\"Provide an easy way for users to add beans (e.g., Gemfire cache configuration) or modify default XD configuration such as serializers, and message converters. A simple approach is to add a well known resource selector such as classpath*:META-INF/spring/xd/extensions or include this path in an extensible @Configuration base class.  In addition, we should adopt conventional names for beans that are meant to be extended, e.g. use an xd. prefix.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1350** (`tawos-v1.1:2457`), created 2014-02-25T10:02:34.000000Z
  - Title: "\"Remove enum for transport options\""
  - Description: "\"The enum unnecessarily restricts the ability to add new transport (MessageBus implementations) whereas the config location path is open for extensions since it uses wildcards (in message-bus.xml):  {code} <import resource=\"\"../../transports/${XD_TRANSPORT}-bus.xml\"\"/> {code} \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1318** (`tawos-v1.1:2489`), created 2014-02-12T16:03:13.000000Z
  - Title: "\"XD container can not be started before the admin server\""
  - Description: "\"The job single partitioned step support (from singlestep-partitioner-support.xml) has the batch job DAOs (loaded from batch.xml).  During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes).   Here is the exception:  15:30:03,600  INFO main xml.XmlBeanDefinitionReader:316 - Loading XML bean definitions from class path resource [META-INF/spring-xd/batch/batch.xml] 15:30:06,154  WARN main annotation.ConfigurationClassEnhancer:318 - @Bean method StepScopeConfiguration.stepScope is non-static and returns an object assignable to Spring's BeanFactoryPostProcessor interface. This will result in a failure to process annotations such as @Autowired, @Resource and @PostConstruct within the method's declaring @Configuration class. Add the 'static' modifier to this method to avoid these container lifecycle issues; see @Bean Javadoc for complete details 15:30:06,705  INFO main support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker:309 - Bean 'org.springframework.xd.dirt.server.ParentConfiguration$JmxConfiguration' of type [class org.springframework.xd.dirt.server.ParentConfigurat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1336** (`tawos-v1.1:2471`), created 2014-02-20T09:53:01.000000Z
  - Title: "Allow easy integration with other types of message transports - remove enums for transport layers"
  - Description: "\"If a third party messaging solution wants to be the transport layer in SpringXD they must currently fork the SpringXD code base and change the enums.  Example: CommonDistributedOptions.ControlTransport currently limits to the following options (rabbit, redis).  So if a third party like messaging system, like ZeroMQ, wanted to plug-in they would have to add to the enum.  Here is another example where GemFire was used as the messaging system:   https://github.com/charliemblack/spring-xd/blob/master/spring-xd-dirt/src/main/java/org/springframework/xd/dirt/server/options/CommonDistributedOptions.java#L38  All messaging enums should be removed for an extensible model.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-181** (`tawos-v1.1:3602`), created 2013-06-03T14:07:38.000000Z
  - Title: "\"Update launcher.xml to have protocol independent beans defined and an import statement to load protocol specific defintiions from a system property defined location.\""
  - Description: "launcher.xml can make use of the system property xd.pipeProtocol inside an import statement.  This determines which version of the XD infrastructure to load, for example what ChannelRegistry implementation, Local or Redis based, or specific message listener containers. \n\nFile name conventions should be used, so if the option passed in from the command line is --pipeProtocol localChannel\n\nthen the XML filename looked for has the 'Protocol' suffix applied, e.g. localChannelProtocol, and is loaded via the classpath.\n\nRedis and Local will not be the only options, other implementations will be provided in the future, e.g. Rabbit, and the user may be able to provide their own implementations of these infrastructure classes (an advanced task).  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-193** (`tawos-v1.1:3590`), created 2013-06-05T05:55:48.000000Z
  - Title: "\"Need more unique resource locations for XD internal configuration\""
  - Description: "\"Currently internal config files are in META-INF/spring with fairly generic names. To avoid potential collisions if users add their own configuration in the classpath, we should have a more unique location, e.g. META-INF/spring/xd\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1356** (`tawos-v1.1:2451`), created 2014-02-27T11:58:50.000000Z
  - Title: "\"Hadoop distro option hdp20 is broken\""
  - Description: "\"Starting the shell with --hadoopDistro hdp20 causes this:  Exception in thread \"\"main\"\" org.springframework.beans.factory.parsing.BeanDefinitionParsingException: Configuration problem: Unable to locate Spring NamespaceHandler for XML schema namespace [http://www.springframework.org/schema/hadoop] Offending resource: URL [jar:file:/Users/trisberg/Demo/spring-xd-1.0.0.BUILD-SNAPSHOT/shell/lib/spring-xd-shell-1.0.0.BUILD-SNAPSHOT.jar!/META-INF/spring/spring-shell-plugin.xml]  Creating a stream \"\"time | hdfs\"\" in xd-singlenode started with --hadoopDistro hdp20 causes this:  java.lang.IllegalStateException: Can't find class used for type of option 'codec': org.springframework.data.hadoop.store.codec.Codecs \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-162** (`tawos-v1.1:3621`), created 2013-05-31T08:40:14.000000Z
  - Title: "Create design document for implementation strategy to support message conversion in ChannelRegistry"
  - Description: "\"The conversion should be based on content-type headers, similar to the way Spring's HttpMessageConverters work (with mime types).  Also, the map of available converters should be extensible while including the most common defaults (for JSON, XML, etc). We most likely want to add a few of our own content types also (e.g. for Tuples).  Most likely, this logic and the configuration methods for extending the converter map, belong in AbstractChannelRegistry since it should be common across all implementations (i.e. the logic should be the same regardless of the transport used after-serialization/before-deserialization).\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Which transport and acknowledgement or transaction guarantees were intended by XD-1596 at the cutoff?
- Does cutoff-available evidence identify two applicable failures in external transport configuration beyond the distinct Hadoop and batch-startup incidents?

## XD-1610 (train)

Historical cutoff: 2014-04-23T11:06:50.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `cfb655c557addd6c2a8edbc11c4e1b78f391914e74c03c9a75f45ad318a6d799`

Source input identity SHA-256: `858b5601b3657385100dcbaccba58eb4b0340a1c73c4010f81725c70ca98335d`

### Supplied historical plan

- **XD-1610** (`tawos-v1.1:2199`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1496** (`tawos-v1.1:2311`)
  - Title: "Exception thrown when accessing Jolokia via the management context path"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1600** (`tawos-v1.1:2209`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1496 explicitly identifies an exception accessing Jolokia through the management context path; the supplied plan therefore already includes work on this observable problem.",
    "XD-1465 records a management-path change and XD-158 describes Jolokia shutdown integration, but neither provides a second comparable failure proving an omitted requirement in XD-1496.",
    "The MBean name-collision and failed-deployment registration incidents demonstrate other JMX failure mechanisms; the unknown XD-1496 description does not establish that its exception shares those causes. Root and XD-1600 text are also unknown."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1184** (`tawos-v1.1:2623`), created 2013-12-20T17:38:48.000000Z
  - Title: "\"Admin & Launcher startup fails when XD_JMX_ENABLED is set to true\""
  - Description: "\"When exporting of MBeans are enabled via XD_JMX_ENABLED (also, jmxEnabled as in application.yml), the Admin and Lancher server application fail to start.  Since the admin applications has the same 'integrationMbeanExporter' bean name for IntegrationMBeanExporter as that its ParentConfiguration, there is a naming conflicts and the exception thrown as:  (Same is the case for launcher and its parent configuration)  Exception in thread \"\"main\"\" org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'mbeanExporter' defined in class org.springframework.context.annotation.MBeanExportConfiguration: Invocation of init method failed; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [org.springframework.integration.monitor.IntegrationMBeanExporter@1de40d3e] with key 'integrationMBeanExporter'; nested exception is javax.management.InstanceAlreadyExistsException: org.springframework.integration.monitor:name=integrationMBeanExporter,type=IntegrationMBeanExporter  at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1553)  at"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1318** (`tawos-v1.1:2489`), created 2014-02-12T16:03:13.000000Z
  - Title: "\"XD container can not be started before the admin server\""
  - Description: "\"The job single partitioned step support (from singlestep-partitioner-support.xml) has the batch job DAOs (loaded from batch.xml).  During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes).   Here is the exception:  15:30:03,600  INFO main xml.XmlBeanDefinitionReader:316 - Loading XML bean definitions from class path resource [META-INF/spring-xd/batch/batch.xml] 15:30:06,154  WARN main annotation.ConfigurationClassEnhancer:318 - @Bean method StepScopeConfiguration.stepScope is non-static and returns an object assignable to Spring's BeanFactoryPostProcessor interface. This will result in a failure to process annotations such as @Autowired, @Resource and @PostConstruct within the method's declaring @Configuration class. Add the 'static' modifier to this method to avoid these container lifecycle issues; see @Bean Javadoc for complete details 15:30:06,705  INFO main support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker:309 - Bean 'org.springframework.xd.dirt.server.ParentConfiguration$JmxConfiguration' of type [class org.springframework.xd.dirt.server.ParentConfigurat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-148** (`tawos-v1.1:3635`), created 2013-05-29T14:22:54.000000Z
  - Title: "\"Improve User Experience when Redis is not running\""
  - Description: "\"Redis is not running we get a nasty stacktrace:  {code} ~/dev/git/spring-xd/dist/spring-xd/xd/bin (master)] ➔ ./xd-container  13/05/29 16:17:15 INFO support.ClassPathXmlApplicationContext: Refreshing org.springframework.context.support.ClassPathXmlApplicationContext@851052d: startup date [Wed May 29 16:17:15 EDT 2013]; root of context hierarchy 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/launcher.xml] 13/05/29 16:17:16 INFO xml.XmlBeanDefinitionReader: Loading XML bean definitions from class path resource [META-INF/spring/redis.xml] 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Pre-instantiating singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0,redisConnectionFactory,org.springframework.xd.dirt.launcher.RedisContainerLauncher#0]; root of factory hierarchy 13/05/29 16:17:17 INFO support.DefaultListableBeanFactory: Destroying singletons in org.springframework.beans.factory.support.DefaultListableBeanFactory@4934ce4a: defining beans [org.springframework.context."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1532** (`tawos-v1.1:2275`), created 2014-04-10T13:19:16.000000Z
  - Title: "\"Clean up MBean registration for failed module deployments\""
  - Description: "\"When a module fails to deploy (for instance an http module configured with a port that is already bound) subsequent attempts to deploy the module fail due to a JMX exception:  {noformat} java.lang.RuntimeException: org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#beafb1fc-4423-4e4f-a88c-1655ea0fdcc5'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=output, sends=0]] with key 'org.springframework.integration:type=MessageChannel,name=output'; nested exception is javax.management.InstanceAlreadyExistsException: xd.foo:module=http.0,component=MessageChannel,name=output  at org.springframework.xd.dirt.server.ContainerRegistrar.deployStreamModule(ContainerRegistrar.java:447)  at org.springframework.xd.dirt.server.ContainerRegistrar.onChildAdded(ContainerRegistrar.java:346)  at org.springframework.xd.dirt.server.ContainerRegistrar.access$700(ContainerRegistrar.java:92)  at org.springframework.xd.dirt.server.ContainerRegistrar$DeploymentListener.childEvent(ContainerRegistrar.java:655)  at org.apache.curat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-467** (`tawos-v1.1:3328`), created 2013-07-12T10:17:45.000000Z
  - Title: null
  - Description: "There's a lifecycle problem when a tap creation fails (e.g. because the DSL syntax is wrong). Subsequent attempts to create the tap will fail with an error:\n\n [{\"links\":[],\"logref\":\"MessageHandlingException\",\"message\":\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"}]\n\nDisabling JMX solves the issue.\n\n\nreproduce\nCreate a bad stream definition name 'bad'\nTry to recreate with the same name, but correct stream definitions.  The system will report that the stream already exists."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-702** (`tawos-v1.1:3098`), created 2013-08-16T06:56:27.000000Z
  - Title: "stack overflow when trying to create a stream with the same name as a module"
  - Description: "\"(NOTE: even if we do want to prevent the use of module names for stream names, we obviously need to avoid a StackOverflowError)  to reproduce:  start the xd-singlenode container  start the xd-shell, and type the following:  {code} xd:>stream create time --definition \"\"time | log\"\" {code}  that should produce an Internal Server Error output message  check the xd-singlenode console, and find:  {code} SEVERE: Servlet.service() for servlet [xd] in context with path [] threw exception [Handler processing failed; nested exception is java.lang.StackOverflowError] with root cause java.lang.StackOverflowError  at java.lang.StringValue.from(StringValue.java:24)  at java.lang.String.<init>(String.java:178)  at org.springframework.xd.dirt.stream.dsl.Token.<init>(Token.java:46)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.lexIdentifier(Tokenizer.java:195)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.process(Tokenizer.java:62)  at org.springframework.xd.dirt.stream.dsl.Tokenizer.<init>(Tokenizer.java:41)  at org.springframework.xd.dirt.stream.dsl.StreamConfigParser.parse(StreamConfigParser.java:65)  at org.springframework.xd.dirt.stream.dsl.StreamConfigParser.parse(StreamConfigP"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1291** (`tawos-v1.1:2516`), created 2014-01-31T14:53:24.000000Z
  - Title: "Handle container shutdown gracefully"
  - Description: "\"Currently, ModuleDeployer is a disposable bean. When the container context is closed, the ModuleDeployer bean is destroyed along with its associated common context and deployed modules. Issue arises, if the connectionfactory bean associated with the deployed modules' message bus bindings  is destroyed before the ModuleDeployer bean, there is exception stacktrace (at least in case of Redis MessageBus) saying \"\"Connection closed\"\".   Adding SmartLifecycle support to ModuleDeployer will make sure all the beans are destroyed during Lifecycle processor's stop() method before any of the singletonbeans are destroyed.  The stacktrace (when using Redis MessageBus is):  org.springframework.data.redis.RedisSystemException: Redis exception; nested exception is com.lambdaworks.redis.RedisException: Connection closed at org.springframework.data.redis.connection.lettuce.LettuceExceptionConverter.convert(LettuceExceptionConverter.java:45) at org.springframework.data.redis.connection.lettuce.LettuceExceptionConverter.convert(LettuceExceptionConverter.java:35) at org.springframework.data.redis.connection.lettuce.LettuceConverters.toDataAccessException(LettuceConverters.java:158) at org.springframew"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1384** (`tawos-v1.1:2423`), created 2014-03-10T15:20:24.000000Z
  - Title: "Improve job launch functionality with distributed nodes"
  - Description: "When sending a launch request, the message is not targeted to the container node that hosts the deployed job.  With RabbitMQ, the message is not ack'd so it will get picked up eventually by the container that hosts the deployed job.  This should change to a targeted message.\n\n-----\nOriginal description from Thomas below\n\nTried deploying some batch jobs and they all seem to fail when running admin and one container using redis as transport\n\nxd:>job create mongojob --definition \"hdfsmongodb --resources=/data/*.log --names=col1,col2,col3 --idField=col1 --collectionName=test\"\n\nfails with this:\n{quote}\n18:19:01,612  WARN redisInboundAdapter-redis:queue-inbound-channel-adapter6 boot.SpringApplication:635 - Error handling failed (Error creating bean with name 'integrationRequestMappingHandlerMapping': Initialization of bean failed; nested exception is java.lang.IllegalStateException: org.springframework.context.annotation.AnnotationConfigApplicationContext@25e7506f has not been refreshed yet)\n18:19:01,614 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter6 handler.LoggingHandler:145 - org.springframework.messaging.MessageHandlingException: error occurred in message handler [mod"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1465** (`tawos-v1.1:2342`), created 2014-04-01T00:55:35.000000Z
  - Title: "\"Update management context path to <root>/management\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1526** (`tawos-v1.1:2281`), created 2014-04-09T15:04:45.000000Z
  - Title: "\"Exception when accessing CDH4 namenode\""
  - Description: "Get exception when accessing cdh4 from shell -\n\njava.lang.UnsupportedOperationException: This is supposed to be overridden by subclasses.\n\tat com.google.protobuf.GeneratedMessage.getUnknownFields\n\nmost likely due to protobuf-java-2.5.0.jar being on the main classpath now\n\n\nFull stack trace:\n{code}\ntrisberg@carbon:~/Test$ ./spring-xd-1.0.0.BUILD-SNAPSHOT/shell/bin/xd-shell --hadoopDistro cdh4\n16:55:22,680  WARN main conf.Configuration:824 - fs.default.name is deprecated. Instead, use fs.defaultFS\n _____                           __   _______\n/  ___|          (-)             \\ \\ / /  _  \\\n\\ `--. _ __  _ __ _ _ __   __ _   \\ V /| | | |\n `--. \\ '_ \\| '__| | '_ \\ / _` |  / ^ \\| | | |\n/\\__/ / |_) | |  | | | | | (_| | / / \\ \\ |/ /\n\\____/| .__/|_|  |_|_| |_|\\__, | \\/   \\/___/\n      | |                  __/ |\n      |_|                 |___/\neXtreme Data\n1.0.0.BUILD-SNAPSHOT | Admin Server Target: http://localhost:9393\nWelcome to the Spring XD shell. For assistance hit TAB or type \"help\".\nxd:>hadoop config fs --namenode hdfs://cdh4:8020\nxd:>hadoop fs ls /\nHadoop configuration changed, re-initializing shell...\n16:55:28,853  WARN Spring Shell util.NativeCodeLoader:62 - Unable to load native-ha"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-158** (`tawos-v1.1:3625`), created 2013-05-30T11:53:23.000000Z
  - Title: "Expose shutdown operation over http"
  - Description: "\"This will allow for a simple way to shutdown the server via an HTTP call.  Support for security is a separate story. The end goal is to have some shell scripts distributed that can issue HTTP requests to shutdown the xd-admin and xd-container servers.  The newest version of Jolokia has the ability to boostrap itself inside an application context vs. requiring a java agent.  I suspect using the application context approach will provide us with more flexibility (e.g. property replacement etc) but not sure.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-316** (`tawos-v1.1:3473`), created 2013-06-25T08:30:23.000000Z
  - Title: "\"Create a common exception framework for XD\""
  - Description: "\"Need to capture exceptions from the various projects that make up XD and wrap them in XD Specific exceptions.  An example of this is when leaving out the channels in the module definitions, we see NoSuchBeanExceptions and IllegalArgumentExceptions thrown based on which module and what channel is missing. \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What exact exception and reproduction steps belong to XD-1496 at this cutoff?
- Does the proposed fix cover management-path routing, Jolokia context initialization, or MBean registration, and what regression tests already accompany it?

## XD-1647 (train)

Historical cutoff: 2014-04-30T09:46:58.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `b969589f7be72875e052e63ca666ef438a4184126c3de389a3dd502826710411`

Source input identity SHA-256: `6217b816fc2899cb4349d6b31969837c019fdf4d421f93cde40ecf5fc3a43eb2`

### Supplied historical plan

- **XD-1647** (`tawos-v1.1:2162`)
  - Title: null
  - Description: "Based off http://bit.ly/spring-xd-test-matrix\n\nProvide test coverage for all batch jobs and source/sink/processors"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root explicitly promises test coverage for all batch jobs and source/sink/processors, so testing coverage cannot be labelled absent merely because no members are observed.",
    "The referenced test matrix is not supplied; the evidence cannot establish which scenarios or transport combinations it includes.",
    "XD-1066 documents a real cross-transport broadcasting failure, while XD-1082, XD-1083 and XD-1086 explicitly require controller tests; these Done examples suggest checks but do not demonstrate that the proposed matrix omits them."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1322** (`tawos-v1.1:2485`), created 2014-02-13T11:47:07.000000Z
  - Title: "Add way to provide module config options for XD on YARN"
  - Description: "There seems to be some intersection with the work for this issue and the rationalization of how module properties are handled.  There will be changes to configuration/property management support such that each module (source, sink, etc) will be able to also be overridden in spring-xd.yml (or wherever -Dspring.config.location points to.  The HDFS sink module for example, will have default values based on it's OptionsMetadata and will be of the form <type>.<module>.<option>\n\n\nThat means in the configuration for hdfs.xml sink, there would be a config section such as\n\n{code:xml}\n    <configuration>\n      fs.default.name=${sink.hdfs.hd.fs}\n      mapred.job.tracker=${sink.hdfs.hd.jt}\n      yarn.resourcemanager.address=${sink.hdfs.hd.rm}\n      mapreduce.framework.name=${sink.hdfs.mr.fw}\n    </configuration>\n{code}\n\nWith default values defined by a HdfsSinkOptionsMetadata class.  The hdfs.xml module file would not contain any references to a properties file.\n\nA file specified by -Dspring.config.location could override the values in a config section such as\n\nsink:\n  hdfs:\n    hd.fs : hdfs://foobarhost:8020\n    hd.jt : 10.123.123.123:9000\n\netc.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-874** (`tawos-v1.1:2928`), created 2013-09-19T21:33:03.000000Z
  - Title: "For file based item reader jobs, step/job completion message should have name of file sent on named channel"
  - Description: "\"It looks like we don't handle deletion of source files currently. We should provide some support for that - Maybe there is a way to into Spring Integration's PseudoTransactionManager support:  http://docs.spring.io/spring-integration/api/org/springframework/integration/transaction/PseudoTransactionManager.html  The *File Source* should possibly also support File archival functionality (But that might also be a dedicated processor?). Not sure where we want to set the semantic boundaries for the File Source. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1066** (`tawos-v1.1:2740`), created 2013-11-14T03:37:18.000000Z
  - Title: "\"Topic channels are not broadcasting\""
  - Description: "\"This needs to work for all transports (local, rabbit, and redis), and we need to ensure that we have test coverage for each of those to avoid any regressions.  The incorrect behavior was observed with all three transports:  {code} xd:>stream create a --definition \"\"topic:foo > transform --expression=payload+'-a' | log\"\" Created new stream 'a'  xd:>stream create b --definition \"\"topic:foo > transform --expression=payload+'-b' | log\"\" Created new stream 'b'  xd:>stream create s --definition \"\"http > topic:foo\"\" Created new stream 's'  xd:>http post --data hi > POST (text/plain;Charset=UTF-8) http://localhost:9000 hi > 200 OK  // only one line in log! {code} \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1076** (`tawos-v1.1:2731`), created 2013-11-18T08:55:59.000000Z
  - Title: "\"Create an FTP tasklet to get remote files and put them in the local file system.\""
  - Description: "\"This is along the lines of what is in this blog post  http://coreyreil.wordpress.com/2012/12/21/spring-batch-creating-an-ftp-tasklet-to-get-remote-files/  Note that there have been some new developments in SI to get at the underlying stream for FTP.  The way to test this is to create a new batch job in XD that has this as it's tasklet.  Going forward the target file system will also be HDFS.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1082** (`tawos-v1.1:2725`), created 2013-11-18T20:43:11.000000Z
  - Title: "Create REST API for getting information on a job execution for a given execution id"
  - Description: "Adopted functionality from Spring Batch admin\nShould include springmvc test framework style tests\n\nGET /batch/jobs/executions/{executionId} - Get information on all executions of a given job name."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1083** (`tawos-v1.1:2724`), created 2013-11-18T20:44:08.000000Z
  - Title: "\"Create REST API for getting information on all steps of a given job execution\""
  - Description: "Adopted functionality from spring batch admin\nShould include springmvc test framework style tests\n\nGET /batch/jobs/executions/{executionId}/steps - Get information on all steps of a given job execution"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1086** (`tawos-v1.1:2721`), created 2013-11-18T20:47:03.000000Z
  - Title: "\"Create REST API for stopping all job executions\""
  - Description: "\"Adopted functionality from spring batch admin Should include SpringMVC test framework style tests.  DELETE /batch/jobs/executions/ - stop all job executions\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does the supplied historical test matrix include topic broadcasting on local, Rabbit and Redis transports, as required by XD-1066?
- How does the matrix verify job execution/step REST contracts and source/sink outcomes rather than only module creation?
- Can the cutoff-bound matrix contents be supplied for review without consulting later edits?

## XD-1688 (train)

Historical cutoff: 2014-05-13T09:34:40.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `a6c89947cca6b277c478dfb57d3dc09672e868fc5283d56adc9f23df359a1e89`

Source input identity SHA-256: `0419b7e7ee4902069b8653e25ae896e5701feb99310e429265d542ff9890eb15`

### Supplied historical plan

- **XD-1688** (`tawos-v1.1:2122`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1689** (`tawos-v1.1:2121`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1690** (`tawos-v1.1:2120`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1691** (`tawos-v1.1:2119`)
  - Title: "ELK - log analysis"
  - Description: null
  - Unknown fields: ["description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1692** (`tawos-v1.1:2118`)
  - Title: "Stream-lib - analytics operators"
  - Description: null
  - Unknown fields: ["description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1693** (`tawos-v1.1:2117`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The only identifiable plan topics are ELK log analysis and Stream-lib analytics operators; neither has a recoverable description establishing interfaces, supported transports or acceptance criteria.",
    "XD-1066 documents topic-channel broadcasting failures and XD-1308 describes transform fallback behavior, but the supplied plan does not show that the proposed operators use those mechanisms. Their shared analytics/logging vocabulary is insufficient support.",
    "XD-1245 and XD-719 demonstrate existing acceptance-test and packaging checks, so their existence cannot establish that this plan omits validation."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1060** (`tawos-v1.1:2746`), created 2013-11-12T08:28:43.000000Z
  - Title: "Add support for Hortonworks Data Platform 2.0"
  - Description: "\"(apologies if a ticket already exists for this, but I didn't see one)  I spun up the Hortonworks Data Platform 2.0 sandbox, but see it isn't supported by Spring XD yet.  How hard would it be to add these Distro's in?  Is it just a matter of dropping in a lib folder for hadoop22 and/or hdp20, and allowing those and options to be passed in via the --hadoopDistro option?  I'm currently trying to work through the following tutorial, but using the HDP 2.0 sandbox instead of the 1.3 sandbox  http://hortonworks.com/hadoop-tutorial/using-spring-xd-to-stream-tweets-to-hadoop-for-sentiment-analysis/  Thanks!\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-719** (`tawos-v1.1:3081`), created 2013-08-20T09:50:31.000000Z
  - Title: "\"Refactor the file source module to have lib/config directories\""
  - Description: "\"Convert a simple module, such as file, to further test that what was done in the previous story, “Use ParentLastClassLoader to create the Modules ApplicationContext.” works as expected.  *Implementation Suggestions*  Remove from build.gradle the dependency on spring-integration-file and place that jar inside a directory  ./modules/source/file/lib   place the current file.xml inside ./modules/source/file/config  *How to verify it works.*  1. Running tests that currently use the file source, e.g. in spring shell, should work as before 2. When deploying a stream file | log, we should be able to interrogate the channel registry and make sure it found the dependencies for the module, ModuleDescriptor should have a not-null URL[] property.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1034** (`tawos-v1.1:2772`), created 2013-11-05T07:39:35.000000Z
  - Title: null
  - Description: "This relates to XD-871 which provides a good scenario.\n\n >stream create s1 --definition \"http | log\"\n >stream create s2 --definition \"http | log\"\n\nThe second command results in an error message that the port is in use but the stream definition is still saved. Since create + deploy is a logical unit of work, it should follow transactional semantics. In other words if the deploy fails, the repository should be rolled back (or a compensating destroy should be performed).  Note this should not be handled the same way if create and deploy happen separately. In that case, the stream definition should remain."
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1064** (`tawos-v1.1:2742`), created 2013-11-14T02:51:48.000000Z
  - Title: "\"Update router sink logic to match new channel syntax\""
  - Description: "\"for example, the following should work:  {code} xd:>stream create a1 --definition \"\"queue:a > transform --expression=payload+'-a' | log\"\" Created new stream 'a1'  xd:>stream create b1 --definition \"\"queue:b > transform --expression=payload+'-b' | log\"\" Created new stream 'b1'  xd:>stream create s1 --definition \"\"http | router --expression=payload.contains('a')?'queue:a':'queue:b'\"\" Created new stream 's1'  xd:>http post --data \"\"ha\"\" > POST (text/plain;Charset=UTF-8) http://localhost:9000 ha > 200 OK  // log shows: \"\"ha-a\"\"  xd:>http post --data \"\"hi\"\" > POST (text/plain;Charset=UTF-8) http://localhost:9000 hi > 200 OK  // log shows: \"\"ha-b\"\" {code}  This needs to be tested against all transports (local, redis, and rabbit) \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1066** (`tawos-v1.1:2740`), created 2013-11-14T03:37:18.000000Z
  - Title: "\"Topic channels are not broadcasting\""
  - Description: "\"This needs to work for all transports (local, rabbit, and redis), and we need to ensure that we have test coverage for each of those to avoid any regressions.  The incorrect behavior was observed with all three transports:  {code} xd:>stream create a --definition \"\"topic:foo > transform --expression=payload+'-a' | log\"\" Created new stream 'a'  xd:>stream create b --definition \"\"topic:foo > transform --expression=payload+'-b' | log\"\" Created new stream 'b'  xd:>stream create s --definition \"\"http > topic:foo\"\" Created new stream 's'  xd:>http post --data hi > POST (text/plain;Charset=UTF-8) http://localhost:9000 hi > 200 OK  // only one line in log! {code} \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1196** (`tawos-v1.1:2611`), created 2014-01-06T07:06:32.000000Z
  - Title: "Align filehdfs batch job defaults with those of corresponding hdfs sink"
  - Description: "The batch jobs use different defaults compared to some of the sink/source modules.\n\nfilehdfs puts data in a /data directory with files named after the stream using a .log file extension. The hdfs sink puts files in an /xd/<streamname> directory using .txt as the default file extension.\n\nfilehdfs needs a more descriptive naming"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1245** (`tawos-v1.1:2562`), created 2014-01-15T07:04:57.000000Z
  - Title: "Develop basic acceptance test application to exercise based XD-EC2 deployment from CI"
  - Description: "Create a first pass at an acceptance test app for a stream definition of http | log.  \n\nThis will involve creating two new projects in xd\n\n1. spring-xd-integration-test\n2. spring-xd-acceptance-tests\n\n#1 will contain generally useful utility methods for acceptance test, such as sending data over http, obtaining and asserting JMX values of specific modules.\n#2 will contain tests that use #1 to test the various out of the box modules provides in XD."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1273** (`tawos-v1.1:2534`), created 2014-01-28T06:02:59.000000Z
  - Title: "\"The use of labelled modules and taps needs more explanation\""
  - Description: "\"https://github.com/spring-projects/spring-xd/wiki/Taps mentions this but the explanation needs more elaboration and example, e.g.  mystream ->  \"\"http | flibble: transform --expression=payload.toUpperCase() | file\"\"  \"\"tap:stream:mystream.flibble > transform --expression=payload.replaceAll('A','.') | log\"\");\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1277** (`tawos-v1.1:2530`), created 2014-01-29T04:32:27.000000Z
  - Title: "\"Default option values broken for composed modules\""
  - Description: "\"May want to fix \"\"properly\"\" when tackling the module options for composed modules, but this is currently broken (and wasn't at some point):  module compose upperHttp --definition \"\"http | transform --expression=payload.toUpperCase()\"\" stream create foo --definition \"\"upperHttp | log\"\"  This will fail saying that ${port} can't be resolved  This will work though: module compose upperHttp --definition \"\"http --port=9000 | transform --expression=payload.toUpperCase()\"\" stream create foo --definition \"\"upperHttp | log\"\"   Note that  stream create foo --definition \"\"upperHttp --port=xxx | log\"\" should work too wut won't, but that's another bug (will create after this one)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1295** (`tawos-v1.1:2512`), created 2014-02-10T00:54:04.000000Z
  - Title: "\"Module message conversion fails to work if JMX is enabled\""
  - Description: "\"If JMX is enabled for modules (enabling the IntegrationMBeanExporter), the ModuleTypeConversionPlugin fails to get the reference to input/output channel (for adding the ContentTypeHeaderInterceptor) and results in exception.  It seems like the IntegrationMBeanExporter (when JMX is enabled) creates JdkDynamicAopProxy for all the integration components and thereby the following check on ModuleTypeConversionPlugin to retrieve the AbstractMessageChannel fails.  AbstractMessageChannel channel = null;    if (isInput) {     channel = module.getComponent(\"\"input\"\", AbstractMessageChannel.class);    }    else {     channel = module.getComponent(\"\"output\"\", AbstractMessageChannel.class);    }  I see the reason why AbstractMessageChannel is used here (to use some of the methods in the implementing class that didn't exist in the interfaces) but IntegrationMBeanExporter creating JdkDynamicAopProxy for the channel fails to resolve as AbstractMessageChannel here.  Following is the full stack trace:  To replicate,  stream create testing --definition \"\"\"\"http --outputType=text/plain | log\"\" 3:45,238 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter1 handler.LoggingHandler:145 - org.spr"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1308** (`tawos-v1.1:2499`), created 2014-02-12T04:28:59.000000Z
  - Title: "\"Weird behavior of the transform module\""
  - Description: "\"When trying some of the examples of XD-159, came up with weird behavior of the transform module.  This boils down to: {noformat} stream create foo --definition \"\"http |transform --expression='new java.lang.Integer(payload)' |  transform --expression=payload.getClass() | log\"\" http post --data 42   ==> Integer (OK) http post --data WTH => WTH (!) {noformat}  Seems that when the expression can not be evaluated, the incoming payload is transmitted as is\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1327** (`tawos-v1.1:2480`), created 2014-02-14T18:02:33.000000Z
  - Title: "\"Rabbit source module with outputType fails to deploy\""
  - Description: "\"To replicate the issue:  Create stream:  stream create rabbittest --definition \"\"rabbit --queues=test --outputType=text/plain | log\"\"  Stacktrace thrown:  17:59:56,436 ERROR http-nio-9393-exec-3 rest.RestControllerAdvice:191 - Caught exception while handling a request java.lang.IllegalArgumentException: Module option named outputType is already present  at org.springframework.xd.module.options.FlattenedCompositeModuleOptionsMetadata.<init>(FlattenedCompositeModuleOptionsMetadata.java:56)  at org.springframework.xd.module.options.DelegatingModuleOptionsMetadataResolver.resolve(DelegatingModuleOptionsMetadataResolver.java:49)  at org.springframework.xd.dirt.stream.XDStreamParser.parse(XDStreamParser.java:117)  at org.springframework.xd.dirt.stream.AbstractDeployer.save(AbstractDeployer.java:73)  at org.springframework.xd.dirt.rest.XDController.save(XDController.java:227)  at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)  at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  at java.lang.reflect.Method.invoke(Method.java:601)  at org.springframework.web."
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What inputs, outputs and XD integration paths are intended for the Stream-lib operators and ELK analysis?
- Which existing module acceptance tests and supported transport combinations apply to these integrations?

## XD-1694 (train)

Historical cutoff: 2014-05-13T10:29:20.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `284fd2c551cc83f9fe24e19593873a324b1486a1d0faad827148b7e11e0c2e45`

Source input identity SHA-256: `ea0a6a62d003b2dcdd6816f9cf049d113d0bc5f7f6fcc74a286e06e4b3bdf8ac`

### Supplied historical plan

- **XD-1694** (`tawos-v1.1:2116`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1695** (`tawos-v1.1:2115`)
  - Title: "Add support for securing REST endpoints"
  - Description: "We would like to provide optional security configurations to secure REST endpoints of xd-admin. Spring security can be leveraged to provide authentication and authorization.\n\nGitHub -> https://github.com/spring-projects/spring-security"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1695 explicitly includes optional REST endpoint authentication and authorization using Spring Security; claiming endpoint security is absent would contradict the plan.",
    "The root title is unknown and its description is empty. The supplied prior tickets concern Windows configuration, JMX, stream/HDFS behavior, documentation and testing, without two applicable authentication or authorization incidents.",
    "References to generic module tests in XD-203 and XD-1228 establish test infrastructure, not a security failure or a demonstrated validation omission in XD-1695."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1333** (`tawos-v1.1:2474`), created 2014-02-19T23:58:15.000000Z
  - Title: "\"Add config file fragment support configuration in XD windows bat scripts\""
  - Description: "\"The external configuration fragment file support by setting spring.config.location in the XD startup scripts are not updated in xd-admin, xd-container and xd-singlenode .bat scripts.   Please refer: https://github.com/spring-projects/spring-xd/issues/582 \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-203** (`tawos-v1.1:3580`), created 2013-06-06T11:59:46.000000Z
  - Title: "\"Provided modules should be integration tested\""
  - Description: "\"I don't see that we have automated tests for the modules we provide out-of-the-box.  We could make the modules folder an Eclipse project (which would also help solve XD-198) and add some integration tests similar to those documented here:  https://github.com/SpringSource/spring-xd/wiki/Creating-Custom-Modules\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1168** (`tawos-v1.1:2639`), created 2013-12-16T11:33:00.000000Z
  - Title: "\"Tapping a stream with multiple labelled filters causes duplicate messages\""
  - Description: "\"Test case is here:  https://github.com/spring-projects/spring-xd/blob/master/src/test/scripts/basic_stream_tests#L49  We would expect one message in the counter, but get 3.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1336** (`tawos-v1.1:2471`), created 2014-02-20T09:53:01.000000Z
  - Title: "Allow easy integration with other types of message transports - remove enums for transport layers"
  - Description: "\"If a third party messaging solution wants to be the transport layer in SpringXD they must currently fork the SpringXD code base and change the enums.  Example: CommonDistributedOptions.ControlTransport currently limits to the following options (rabbit, redis).  So if a third party like messaging system, like ZeroMQ, wanted to plug-in they would have to add to the enum.  Here is another example where GemFire was used as the messaging system:   https://github.com/charliemblack/spring-xd/blob/master/spring-xd-dirt/src/main/java/org/springframework/xd/dirt/server/options/CommonDistributedOptions.java#L38  All messaging enums should be removed for an extensible model.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1544** (`tawos-v1.1:2263`), created 2014-04-11T07:45:59.000000Z
  - Title: "Need to be able setup ec2 env to test  job samples in spring-xd-samples repo"
  - Description: "Currently in order to deploy a user created job we copy the job to the containers and admin server, and then bounce the servers.  The tests will need the ability to copy these jobs to the containers, & admin and then bounce the servers.  \nThese sample jobs are located at https://github.com/spring-projects/spring-xd-samples"
  - Unknown fields: ["type", "status", "estimate"]
  - Truncated fields: []
- **XD-848** (`tawos-v1.1:2952`), created 2013-09-14T14:25:27.000000Z
  - Title: "\"ICLA website is missing Spring XD project option\""
  - Description: "The README.md at:\n\n  https://github.com/spring-projects/spring-xd/blob/master/README.md\n\n...says:\n\n\"Before we accept a non-trivial patch or pull request we will need you to sign the contributor's agreement\"\n\nNavigating to the <contributor's agreement> link takes the user to the ICLA web page at:\n\nhttps://support.springsource.com/spring_committer_signup\n\n//exp: The Project field's dropdown should have an option for \"Spring XD\"\n//act: There's no \"Spring XD\" option"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1040** (`tawos-v1.1:2766`), created 2013-11-07T11:05:37.000000Z
  - Title: "\"Remove \"\"legacy\"\" application code following Spring bootification\""
  - Description: "\"See the discussion in https://github.com/spring-projects/spring-xd/pull/370  There are now various superseded classes and tests which we no longer need.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1122** (`tawos-v1.1:2685`), created 2013-11-26T01:46:44.000000Z
  - Title: "\"Add jmxPort to list of coerced cmd line options\""
  - Description: "\"Following merge of XD-1109.  See discussion at https://github.com/spring-projects/spring-xd/commit/eaf886eab3b2ef07da55575029ccabb2c8a36af9#commitcomment-4701947\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1133** (`tawos-v1.1:2674`), created 2013-12-02T09:22:13.000000Z
  - Title: "\"Create test script that reproduces failure in writing to HDFS when undeploying and redeploying a stream\""
  - Description: "\"See https://github.com/spring-projects/spring-xd/pull/415#issuecomment-29024329  This test should be created so that it reproduces the failure and then turned off, so that when we switch to the new HDFS writing code  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1180** (`tawos-v1.1:2627`), created 2013-12-19T07:21:53.000000Z
  - Title: "Enabling of JMX support is broken"
  - Description: "\"However this is triggered (depending on whether https://github.com/spring-projects/spring-xd/pull/477/files is merged yet or not), jmx seems to be broken because of duplicate beans / mbeans names\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1192** (`tawos-v1.1:2615`), created 2014-01-02T09:03:46.000000Z
  - Title: "\"Add documentation for JDBC to HDFS batch job\""
  - Description: "\"Add docs to section   https://github.com/spring-projects/spring-xd/wiki/Batch-Jobs#pre-packaged-batch-jobs\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1228** (`tawos-v1.1:2579`), created 2014-01-14T22:07:43.000000Z
  - Title: "Provide a easy, prescriptive means to perform unit and basic stream integration tests."
  - Description: "\"AbstractSingleNodeStreamDeploymentIntegrationTests is the basis of 'state of the art' testing for a stream that allows you to get a reference to the input and output channel of the stream  http | filter | transform | file.  One can send messages to the channel after the http module, but before filter and one can retrieve the messages that were sent to the channel after the transform module but before file.  The current implementation inside AbstractSingleNodeStreamDeploymentIntegrationTests can be improved in terms of ease of use for end-users.    The issue is to create as simple a way as possible for a user to test their processing modules/stream definitions without having to actually do a real integration test by sending data to the input module.  Either as a separate issue or as part of this one, the documentation   https://github.com/spring-projects/spring-xd/wiki/Creating-a-Processor-Module  should be updated to explicitly show how to use this issue's test functionality. \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What cutoff-available security acceptance criteria define endpoint coverage, roles and behavior when optional security is disabled?
- Do any supplied prior tickets actually document a relevant REST access-control failure, rather than sharing Spring or configuration terminology?

## XD-1820 (train)

Historical cutoff: 2014-06-07T11:49:16.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `9c6ef0f87477d57a46ec940fb45c1344719b123b0fedefba02f1097ca627aab4`

Source input identity SHA-256: `c6508c4cbf96f87a8a846deee6434dd8e4a65b7cbc55cef1a81de956cf27ec0f`

### Supplied historical plan

- **XD-1820** (`tawos-v1.1:1992`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1270** (`tawos-v1.1:2537`)
  - Title: null
  - Description: "1) Improve how the state of the stream is managed.\n\n\n\n\nA deploy command moves the stream from the undeployed state to the deploying state.\nIf all modules in the stream are successfully deployed, the stream state is ‘deployed’\nIf one or more module deployments failed, the stream state is failed.  Any modules that were successfully deployed, are still running.  \nSending an undeploy command will stop all modules of the stream and return the stream to the undeployed state.\n\nFor the individual modules that failed, we will be able to find out which ones failed.  Not yet sure if we can try to redeploy just those parts of the stream that failed.\n\nThe channel that will be used to update the state of the stream is xd.stream.status\n\nTBD: Details of how the state for each module in the stream will be stored."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-1586** (`tawos-v1.1:2223`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1591** (`tawos-v1.1:2218`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1759** (`tawos-v1.1:2052`)
  - Title: "Status on Shell command prompt is inconsistent"
  - Description: "Deployment: xd-shell local, xd-singlenode (ec2)\nSHA: 942c7868e3e0d0cf7730b536170438a0291f5cab\n\n[Description]\n<Case 1>\nOnce successfully connected to a server, if you connect to a server that is not present.  The prompt still shows XD when it should show server-unknown.  Can be reproduced consistently.\nConversely:\n<Case 2>\nAttempted to connect to a xd-singlenode on ec2 using a local xd-shell.  \nThe xd-singlenode was not running.  After bringing up the xd-singlenode, I was able to connect however the status did not change from \"server-unknown\"  *This behavior, can not be consistently reproduced, but have seen it happen on multiple accounts.* \n\n[Steps to reproduce]\n<Case 1>\n1. Bring up shell while xd-singlenode is not running.\n2. Bring up xd-singlenode\n3. Connect to xd-singlenode\n* xd:>admin config server http://localhost:9393\n\n4. Connect to a fake address\n* xd:>admin config server http://foo.bar:9393\n\n<Case 2>\n1.  Attempt to connect to remote server that is not available\n* xd:>admin config server http://ec2-54-237-186-186.compute-1.amazonaws.com:9393\n* Unable to contact XD Admin Server at 'http://ec2-54-237-186-186.compute-1.amazonaws.com:9393'.\n\n2. Bring up xd-singlenode on remote\n*"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-1777** (`tawos-v1.1:2034`)
  - Title: "Handle redeployment of \"orphaned\" modules for a partitioned stream"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1270 already specifies stopping all stream modules on undeploy, and XD-1777 explicitly covers redeployment of orphaned partitioned modules. Neither recovery work nor physical stopping can be declared absent.",
    "XD-1738 records destroy failure after module files are manually removed, and XD-1754 records retained Gemfire connections after destroy. The supplied plan does not establish their applicability to its undeploy/redeployment paths or to a chosen module type.",
    "The acceptance design and two member descriptions are unknown. No supplied evidence shows the plan validates only logical state, so a missing-cleanup-test risk is unsupported."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: ["status", "estimate"]
  - Truncated fields: ["description"]
- **XD-1675** (`tawos-v1.1:2135`), created 2014-05-07T15:40:19.000000Z
  - Title: "\"FilePollHdfs is not writing results to hdfs\""
  - Description: "\"XD Deployment  Description:  XD Cluster (1 Container) Environment:  EC2 Type Of Test:  Manual Test Test Failed On  filepollhdfs (only test that was run) Build Used  Built May 7, 10:29 UTC  From the shell, attempted to create filepollhdfs however no results were written to hdfs (hadoop22).    The commands executed were the following: job create myjob --definition \"\"filepollhdfs  --names=forename,surname,address\"\" --deploy stream create mystream --definition \"\"file --dir=67fc27a6-224d-4c67-a02a-40730bcf8906 --pattern='*.out' > queue:job:myjob\"\" --deploy  No warnings nor exceptions were displayed till I changed the log4j.logger.org.springframework to INFO and restarted the container.  Then when I copied the sample file to the monitored directory the log reported: 21:30:07,605  INFO DeploymentsPathChildrenCache-0 module.ModuleDeployer:118 - deployed SimpleModule [name=file, type=source, group=mystream, index=0 @61612c7c] Exception in thread \"\"inbound.job:myjob-redis:queue-inbound-channel-adapter1\"\" org.springframework.messaging.core.DestinationResolutionException: failed to look up MessageChannel with name 'errorChannel' in the BeanFactory (and there is no HeaderChannelRegistry presen"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1577** (`tawos-v1.1:2231`), created 2014-04-15T01:44:34.000000Z
  - Title: "\"Changing externalized module config properties at runtime\""
  - Description: "\"Once the container starts up and the module is deployed, the externalized module configuration properties could not be changed for the subsequent modules of same type.  Here is the scenario for a stream \"\"http | transform | log\"\", with XD_MODULE_CONFIG_LOCATION and XD_MODULE_CONFIG_NAME using their default values.  In, ${xd.config.home}/modules/modules.yml, I have: processor:   transform:     expression: \"\"'Inside modules.yml'\"\"  and, in, ${xd.config.home}/modules/processor/transform/transform.properties, I have: expression: \"\"'First module: inside transform.properties'\"\"  Now, I deploy this stream: \"\"http | transform | log\"\".  Lets say, I have another stream that uses the transform module, but this time I want to change the expression in ${xd.config.home}/modules/processor/transform/transform.properties to, expression: \"\"'Second module'\"\"  Now, when the stream containing this transform module gets deployed, it uses the same transform.properties that is used by the previously deployed transform module.  What I understand from this behavior is that, the EnvironmentAwareModuleOptionsMetadataResolver caches the module environments for a given module type and name. When the same modul"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1602** (`tawos-v1.1:2207`), created 2014-04-22T07:53:03.000000Z
  - Title: "\"JMS Source on EC2 only uses localhost for activemq broker\""
  - Description: "\"[Problem] On a EC2 container jms-activemq.properties was configured to use a activemq broker on a different host, it still referred to localhost.   On my local mac, I was able to updated the jms-activemq.properties with an activemq on a different host and it worked.  [work-around] While not recommended you can set the amq.url in the jms-activemq-infrastructure-context.xml.  [Steps to reproduce] 1) Deploy a single admin/container using xd-ec2.   2) create a jms-activemq.properties file in the spring-xd-1.0.0.BUILD-SNAPSHOT/xd/ where it refers to a broker on another machine (ec2-54-221-32-82.compute-1.amazonaws.com).   3) Create a stream with JMS as its source.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1384** (`tawos-v1.1:2423`), created 2014-03-10T15:20:24.000000Z
  - Title: "Improve job launch functionality with distributed nodes"
  - Description: "When sending a launch request, the message is not targeted to the container node that hosts the deployed job.  With RabbitMQ, the message is not ack'd so it will get picked up eventually by the container that hosts the deployed job.  This should change to a targeted message.\n\n-----\nOriginal description from Thomas below\n\nTried deploying some batch jobs and they all seem to fail when running admin and one container using redis as transport\n\nxd:>job create mongojob --definition \"hdfsmongodb --resources=/data/*.log --names=col1,col2,col3 --idField=col1 --collectionName=test\"\n\nfails with this:\n{quote}\n18:19:01,612  WARN redisInboundAdapter-redis:queue-inbound-channel-adapter6 boot.SpringApplication:635 - Error handling failed (Error creating bean with name 'integrationRequestMappingHandlerMapping': Initialization of bean failed; nested exception is java.lang.IllegalStateException: org.springframework.context.annotation.AnnotationConfigApplicationContext@25e7506f has not been refreshed yet)\n18:19:01,614 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter6 handler.LoggingHandler:145 - org.springframework.messaging.MessageHandlingException: error occurred in message handler [mod"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1754** (`tawos-v1.1:2057`), created 2014-05-23T11:27:47.000000Z
  - Title: "GemfireJsonServer & gemfireServer sinks do not close connections"
  - Description: "* OS - Mac\n* XD Deployment Type - Singlenode\n* SHA - bb4dd58\n* Required Software - XD Gemfire Sample Server\n\n[Description]\nAfter creating and destroying 3 streams with gemfireJsonServer sink the 4th will fail with this error:  \n* 44707 refused connection: The number of clients, 4, exceeded the limit of 3 allowed by the default evaluation license.\n\n[Steps to reproduce]\n* From your shell execute the following 4 times:\n** stream create --name stocks --definition \"http --port=9090 | gemfire-json-server --regionName=Stocks --host=ec2-54-221-32-82.compute-1.amazonaws.com --port=40404 --keyExpression=payload.getField('symbol')\" --deploy\n** stream destroy stocks"
  - Unknown fields: []
  - Truncated fields: []
- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-641** (`tawos-v1.1:3157`), created 2013-08-08T16:19:20.000000Z
  - Title: "\"Problem with tapping and > (source channels)\""
  - Description: "\"This is a follow on from XD-592. In that bug we fixed up the ability to use tap with pipe.  Tap when used as a source channel should also work (and should deploy in a more optimized fashion since source channels can be directly connected to the subsequent module, creation of a pass-through tap instance isn't necessary).  This test shows the syntax that should work and the current information about how it fails:  {code} public void testTapSourceChannel() throws IOException {   FileSink sink1 = newFileSink();   FileSink sink2 = newFileSink();    stream().create(\"\"myhttp\"\",     \"\"http --port=9314 | transform --expression=payload.toUpperCase() | filter --expression=true > :foo\"\");    // fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type   tap().create(\"\"wiretap1\"\", \"\"tap myhttp.transform > transform --expression=payload.replaceAll('a','.') | %s\"\", sink1);    // fails in TapDefinition ctor with: java.lang.IllegalArgumentException:   // streamName cannot be empty or null   tap().create(\"\"wiretap2\"\", \"\"tap :foo > transform --expression=payload.replaceAll('a','.') | %s\"\", sink2);    httpPostData(\"\"http://localhos"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-716** (`tawos-v1.1:3084`), created 2013-08-19T19:54:19.000000Z
  - Title: "\"TapCommandTests hangs when using a lazily instantiated Lettuce connection\""
  - Description: "\"A change was made in spring-data-redis to instantiate the shared Lettuce connection lazily instead of when the context is initialized. This caused TapCommandTests to hang due to a Netty worker thread trying to initialize the Lettuce connection (Lettuce uses Netty). The change was temporarily backed out of SDR, but we need to consider using a NettyExecutionHandler in NettyHttpInboundChannelAdapter or making the HTTP module's \"\"input\"\" channel an ExecutorChannel to avoid potentially long operations like from happening in an I/O thread.  Also, we need to address why this failure simply hangs the shell. Shell was hung waiting on IO here:  at org.springframework.http.client.SimpleClientHttpResponse.getRawStatusCode(SimpleClientHttpResponse.java:47)  at org.springframework.http.client.AbstractClientHttpResponse.getStatusCode(AbstractClientHttpResponse.java:32)  at org.springframework.xd.shell.command.HttpCommands$1.hasError(HttpCommands.java:93)  at org.springframework.web.client.RestTemplate.doExecute(RestTemplate.java:484)  at org.springframework.web.client.RestTemplate.execute(RestTemplate.java:460)  at org.springframework.web.client.RestTemplate.postForEntity(RestTemplate.java:335) "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-799** (`tawos-v1.1:3001`), created 2013-09-02T23:31:17.000000Z
  - Title: "\"Change rabbitmq sink to use routing-key-expression instead of routing-key\""
  - Description: "\"The current rabbitmq sink uses the attribute routing-key, which defaults to the name of the stream.  This should be change to use the attribute routing-key-expression so that the routing-key can be determined using SpEL.  This will enable a dynamic evaluation of the routing-key based on message payload/header.  *Implementation Suggestions*  This hopefully should be changing the XML description of the sink to     routing-key-expression=\"\"${routingKey:'${xd.stream.name}'}  This way, the ${xd.stream.name} is surrounded by a single quote to indicate a string literal to SpEL in the default case.    *How to verify it works.*  One of the simple uses of this is to create a routing key based on payload.  In a distributed word-count example, the hashcode of a word would be sent to a certain number of processing modules that would perform the count. The idea is that the same word is sent to the same node over and over again, in particular if in-memory counters or state is computed - using centralized redis counters this wouldn't be necessary in the case of only counter state.  The stream   http | rabbit --routingKey=\"\"'word-' + payload.hashCode() % 3\"\"  is an example of a stream that can be "
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Is there cutoff-valid design evidence that the planned undeploy or orphan-redeployment path uses the destroy/connection-cleanup behavior implicated by XD-1738 or XD-1754?
- What recovery guarantees and acceptance scenarios are already specified in the unknown members?

## XD-1821 (train)

Historical cutoff: 2014-06-07T12:25:05.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `1724538ddb1323034f54528ea104a86dbb181aa927f92c7ddfe3ecfb2cfb953e`

Source input identity SHA-256: `209c93d6d568a91040cc93b30155e84c9b605f1fcbc09731fcd0b4cebd1350d8`

### Supplied historical plan

- **XD-1821** (`tawos-v1.1:1991`)
  - Title: "\"internal modeling of modules and streams.\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1043** (`tawos-v1.1:2763`)
  - Title: "Encapsulate list of ModuleDeploymentRequests within a parsed Stream result object"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1151** (`tawos-v1.1:2656`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1474** (`tawos-v1.1:2333`)
  - Title: null
  - Description: "{code}\nStreamDefinition sd = streamParser.parse(name, dslText);\n{code}\n\nWe should also consider explicit methods such as parseStream (so that parseJob and parseComposedModule are at least separate methods, if not separate parser classes that share the common parser support class that is the core of today's parser). The parsing for \"completion providers\" should probably be spun off to its own class as well. In the end, there should be no need for a ParsingContext enum but rather, more explicitly named methods and dedicated classes if that seems like the right approach.\n\nthe StreamDefinition should be composed of \"ModuleDescriptors\" (that name is not set in stone) and other Stream-level metadata like source/sink channels\n\nconsider merging some of StreamFactory code there, and the rest into StreamDeployer\n\nmerge ModuleDescriptor and ModuleDeploymentRequest as part of this effort (again, a new name could be considered, but ModuleDescriptor should take precedence over ModuleDeploymentRequest), and note in the process that ModuleDescriptor was originally designed to be immutable (taking constructor args), but as we migrated the prototype code into XD itself, this was violated. We may wan"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]

### Proposed target

```json
{
  "risks": [
    {
      "id": "XD-1821-channel-identity-compatibility",
      "risk_type": "validation_gap",
      "claim": "The planned parser-entry-point and descriptor merge has a channel-identity compatibility risk: job queues and named stream/tap references use distinct prefix-resolution rules, and changing their representation can select a different channel or make a previously valid tap reference fail.",
      "rationale": "XD-1474 explicitly separates stream/job/composed-module parsing, moves source/sink metadata into StreamDefinition and merges ModuleDescriptor with ModuleDeploymentRequest. XD-1601 names StreamConfigParser channel resolution and gives the explicit constraint that job:j1 and queue:job:j1 refer to a job request queue while queue:foo is itself a stream broker queue name. XD-641 independently documents tap-source forms failing through bean-identity/type registration and an empty stream name. The proposed refactor touches the parser/descriptor boundary carrying those identities, making this a specific compatibility concern rather than an assumed absence of regression tests. XD-641 is Done; the claim does not assert that its old defect persists. The status and final resolution of XD-1601 are unknown.",
      "suggested_action": "Preserve channel kind, scope and canonical broker identity explicitly through the parser result and merged descriptor. Verify job aliases, named queue/topic references and tap-source resolution from parsing through deployment, including the supplied XD-641 forms. Confirm whether existing planned work already provides these checks.",
      "target_item_ids": [
        "tawos-v1.1:2333"
      ],
      "citations": [
        {
          "item_id": "tawos-v1.1:2208",
          "field": "description",
          "quote": "If we create a job \"j1\", the job launching request queue name in the message broker would \"job:j1\". To send a launching request, we can either use \"queue:job:j1\" or \"job:j1\" (both seems to work)."
        },
        {
          "item_id": "tawos-v1.1:3157",
          "field": "description",
          "quote": "// fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type"
        }
      ],
      "severity": "medium"
    }
  ],
  "limitations": [
    "The plan already explicitly includes source/sink channel metadata and parser separation; neither is labelled missing.",
    "The supplied description is truncated and XD-1151 is unknown; the final representation and compatibility checks may already preserve these rules.",
    "XD-641 is Done and XD-1601 has unknown status; no current reproduced defect or definitive company severity is established."
  ]
}
```

#### Evidence for XD-1821-channel-identity-compatibility

- XD-1601 / `tawos-v1.1:2208` / description: "If we create a job \"j1\", the job launching request queue name in the message broker would \"job:j1\". To send a launching request, we can either use \"queue:job:j1\" or \"job:j1\" (both seems to work)."
- XD-641 / `tawos-v1.1:3157` / description: "// fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type"

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-953** (`tawos-v1.1:2850`), created 2013-10-14T08:25:02.000000Z
  - Title: "\"Richer module options metadata\""
  - Description: "\"Module options are currently implemented using PropertySourcesPlaceholderConfigurer, doing simple \"\"text\"\" replacements.  This story proposes to introduce a richer model for module options, which could take the following xml representation (keeping in mind that there would be an underlying set of classes that could also apply to e.g. @Configuration approach):  {code:xml} <xd:params>   <xd:param name=\"\"port\"\" help=\"\"the http port to listen on\"\" /> </xd:params> {code}  So, the very first obvious benefit is providing help metadata. The second one is an easy way to list available option names, without resorting to brittle PropertySourcesPlaceholderConfigurer hacks (we wouldn't for example detect xd.stream.name or XD_TRANSPORT as a valid option)  One could also specify defaults/computations, this time benefiting from SpEL everywhere: {code:xml} <xd:params>   <xd:param name=\"\"directory\"\" default=\"\"headers.directory\"\" /> </xd:params> {code}  Lastly, this opens the door to better type checking / combinations / optionality support: {code:xml} <xd:params valid=\"\"fixedDelay || cron\"\">   <xd:param name=\"\"fixedDelay\"\" type=\"\"int\"\" />   <xd:param name=\"\"cron\"\" type=\"\"string\"\" /> </xd:params> {c"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1477** (`tawos-v1.1:2330`), created 2014-04-02T06:40:12.000000Z
  - Title: "Consider merging Container and ContainerMetadata as well as their \"repositories\""
  - Description: "The two classes in question are:\n* org.springframework.xd.dirt.cluster.Container\n* org.springframework.xd.dirt.container.ContainerMetadata\n\nThe former is currently used by the Admin when making decisions about Module deployment. That latter was a replacement for RuntimeContainerInforEntity as we migrated the various Redis/InMemory Repositories to use the data that is now available in ZooKeeper instead.\n\nThe ContainerRepository is currently used by the Admin leader, and the ContainerMetadataRepository is used by the REST endpoint that supports the xd-shell's 'runtime containers' command. Perhaps those can also be merged.\n\nIn any case, if not addressed by a larger refactoring, the ContainerRepository should probably support an Iterable return rather than an Iterator. Having finders (e.g. for attribute key/values such as \"group\"==\"foo\") might be convenient for various Module deployment strategies."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1601** (`tawos-v1.1:2208`), created 2014-04-21T18:52:37.000000Z
  - Title: null
  - Description: "There seems to be some inconsistency with the naming strategy for the named channels.\n\nFor example:\n\nIf we create a job \"j1\", the job launching request queue name in the message broker would \"job:j1\". To send a launching request, we can either use \"queue:job:j1\" or \"job:j1\" (both seems to work).\n\nIf we create a stream with the named p2p channel \"foo\" we expect to use the syntax \"queue:foo\" and the message broker will have the queue name \"queue:foo\"\n\nThe StreamConfigParser resolves the source/sink channel names for tap to deduce the module index from the channel component: ChannelNode.resolve(StreamLookupEnvironment env)\n\nBut, in case of the named channels that have prefix \"topic:\" or \"queue:\", their names are used as is the only exception in a case where (From StreamConfigParser's eatChannelReference(boolean tapAllowed)\n \n```\n// queue:XXX\n\t\t\t// topic:XXX\n\t\t\tif (firstToken.data.equalsIgnoreCase(\"queue\")) {\n\t\t\t\tchannelType = ChannelType.QUEUE;\n\t\t\t}\n\t\t\telse if (firstToken.data.equalsIgnoreCase(\"topic\")) {\n\t\t\t\tchannelType = ChannelType.TOPIC;\n\t\t\t}\n\t\t\t// TODO: DT not sure if this is the best way to handle\n\t\t\t// StreamConfigParserTests.substreamsWithSourceChannels()\n\t\t\tif (channelScopeCo"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: ["description"]
- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: ["status", "estimate"]
  - Truncated fields: ["description"]
- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1322** (`tawos-v1.1:2485`), created 2014-02-13T11:47:07.000000Z
  - Title: "Add way to provide module config options for XD on YARN"
  - Description: "There seems to be some intersection with the work for this issue and the rationalization of how module properties are handled.  There will be changes to configuration/property management support such that each module (source, sink, etc) will be able to also be overridden in spring-xd.yml (or wherever -Dspring.config.location points to.  The HDFS sink module for example, will have default values based on it's OptionsMetadata and will be of the form <type>.<module>.<option>\n\n\nThat means in the configuration for hdfs.xml sink, there would be a config section such as\n\n{code:xml}\n    <configuration>\n      fs.default.name=${sink.hdfs.hd.fs}\n      mapred.job.tracker=${sink.hdfs.hd.jt}\n      yarn.resourcemanager.address=${sink.hdfs.hd.rm}\n      mapreduce.framework.name=${sink.hdfs.mr.fw}\n    </configuration>\n{code}\n\nWith default values defined by a HdfsSinkOptionsMetadata class.  The hdfs.xml module file would not contain any references to a properties file.\n\nA file specified by -Dspring.config.location could override the values in a config section such as\n\nsink:\n  hdfs:\n    hd.fs : hdfs://foobarhost:8020\n    hd.jt : 10.123.123.123:9000\n\netc.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-641** (`tawos-v1.1:3157`), created 2013-08-08T16:19:20.000000Z
  - Title: "\"Problem with tapping and > (source channels)\""
  - Description: "\"This is a follow on from XD-592. In that bug we fixed up the ability to use tap with pipe.  Tap when used as a source channel should also work (and should deploy in a more optimized fashion since source channels can be directly connected to the subsequent module, creation of a pass-through tap instance isn't necessary).  This test shows the syntax that should work and the current information about how it fails:  {code} public void testTapSourceChannel() throws IOException {   FileSink sink1 = newFileSink();   FileSink sink2 = newFileSink();    stream().create(\"\"myhttp\"\",     \"\"http --port=9314 | transform --expression=payload.toUpperCase() | filter --expression=true > :foo\"\");    // fails with: java.lang.IllegalArgumentException: bean 'myhttp.1' is already   // registered but does not match the required type   tap().create(\"\"wiretap1\"\", \"\"tap myhttp.transform > transform --expression=payload.replaceAll('a','.') | %s\"\", sink1);    // fails in TapDefinition ctor with: java.lang.IllegalArgumentException:   // streamName cannot be empty or null   tap().create(\"\"wiretap2\"\", \"\"tap :foo > transform --expression=payload.replaceAll('a','.') | %s\"\", sink2);    httpPostData(\"\"http://localhos"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- How does the merged descriptor preserve channel kind/scope and distinguish job aliases from stream broker names?
- Do the full cutoff-bound XD-1474 criteria or XD-1151 already verify these parser-to-deployment identities?
- What company severity policy applies to incorrect channel routing or an unusable supported tap reference?

## XD-1832 (train)

Historical cutoff: 2014-06-10T14:06:39.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `2915c79f68ea938ca422470d8ad9e265d192bd8c43cd8dc3b57cfca8eb91e0c4`

Source input identity SHA-256: `2770273cac495a5b240781ec37634a3d35e3cf0ef4e8e628fe816d5f31a14ab6`

### Supplied historical plan

- **XD-1832** (`tawos-v1.1:1980`)
  - Title: "\"Issues related to tab completion in the shell\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1585** (`tawos-v1.1:2224`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1706** (`tawos-v1.1:2104`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "status", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The epic explicitly covers shell tab-completion issues. Both member titles and descriptions are unknown, so the command coverage and test design cannot be inferred.",
    "XD-1197 reports job-launch option completion differing from destroy, while XD-1493 reports missing HTTP completion. These are useful historical cases, but no supplied target requirement establishes that only one command family will be implemented or validated.",
    "XD-1493, entity completion XD-670, and command separation XD-796 are marked Done. A generic possibility that completed fixes regress is insufficient to label a new validation gap."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1197** (`tawos-v1.1:2610`), created 2014-01-06T08:01:42.000000Z
  - Title: null
  - Description: "In the shell:\n\njob launch doesn't do completion of --name, this is different behavior compared to job destroy\n\ntyping 'job destroy' and hitting tab completes with '--name'\n\ntyping 'job launch' and hitting tab does nothing"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1493** (`tawos-v1.1:2314`), created 2014-04-06T17:48:51.000000Z
  - Title: "\"xd-shell tab completion missing for http post/get\""
  - Description: "\"xd-shell tab completion missing for 'http post' and 'http get' cli commands.  Typing \"\"xd:>http post\"\" <tab> <tab> gives no suggestions event though --file or --data are required.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-670** (`tawos-v1.1:3129`), created 2013-08-12T04:40:28.000000Z
  - Title: "\"TAB completion for existing entities\""
  - Description: "\"Provide Shell TAB completion when referencing an existing entity\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-796** (`tawos-v1.1:3004`), created 2013-09-02T07:16:52.000000Z
  - Title: "Create separate commands for \"--all\" shell commands"
  - Description: "\"Commands like \"\"stream deploy\"\" have changed over time to allow passing a \"\"--all\"\" option.  So it's either {{stream deploy foo}} or {{stream deploy --all}}. This has a number of drawbacks, given that these are the only 2 alternatives: - Implementation code is cumbersome - None of the options can be marked mandatory, yet one of them is required. This has to be checked in the command code itself - TAB completion is less powerful as the shell doesn't know if we want the first or the second form.   Consider splitting those commands into two distinct commands, one as before and one literally named {{stream deploy all}}.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1000** (`tawos-v1.1:2806`), created 2013-10-23T21:49:05.000000Z
  - Title: "\"User should be able to view the list of all the job definitions\""
  - Description: "\"Create a tab view with tabs “Job Definitions”, “Runtime Jobs” (Deployed Jobs?, “Job Instances” (Is Runtime Jobs a better name here?) and “Job Executions”. On clicking “Job Definitions” tab, we can have a table view of job definitions. Since we bootstrap.js, we can have a responsive table layout to list all the available job definitions. At the REST layer, “/jobs” provides the list of job definitions. We can expand the JobsController list()’s QueryOptions to add more criteria (especially to list JobDefinition’s status (Deployed/Undeployed). Also, this is the UI implementation for the shell command “job list” \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1011** (`tawos-v1.1:2795`), created 2013-10-25T08:37:27.000000Z
  - Title: "\"Spring Shell --host option does not work\""
  - Description: "\"When trying to use the --host command line parameter, spring shell reports the following error for this command, \"\"xd-shell --host localhost\"\" : Oct 25, 2013 10:35:25 AM org.springframework.shell.core.SimpleParser commandNotFound WARNING: Command '--host localhost' not found (for assistance press TAB) \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1104** (`tawos-v1.1:2703`), created 2013-11-21T04:01:12.000000Z
  - Title: "\"Create Shell Integration test fixture for jdbc related sink\""
  - Description: "\"Would be nice to have some kind of regression testing on the jdbc sink, as it becomes more prominent in XD.  Use of an in memory db where we expose eg a JdbcTemplate to assert state\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1155** (`tawos-v1.1:2652`), created 2013-12-11T12:21:11.000000Z
  - Title: "\"The lib directory for hadoop12 contains mix of hadoop versions\""
  - Description: "\"This causes issues depending on which version of the core/common jar gets loaded first - like:  xd:>hadoop fs ls -ls: Fatal internal error java.lang.UnsupportedOperationException: Not implemented by the DistributedFileSystem FileSystem implementation   at org.apache.hadoop.fs.FileSystem.getScheme(FileSystem.java:213)   at org.apache.hadoop.fs.FileSystem.loadFileSystems(FileSystem.java:2401)   at org.apache.hadoop.fs.FileSystem.getFileSystemClass(FileSystem.java:2411)   at org.apache.hadoop.fs.FileSystem.createFileSystem(FileSystem.java:2428)   at org.apache.hadoop.fs.FileSystem.access$200(FileSystem.java:88)   at org.apache.hadoop.fs.FileSystem$Cache.getInternal(FileSystem.java:2467)   at org.apache.hadoop.fs.FileSystem$Cache.get(FileSystem.java:2449)   at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:367)   at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:166)   at org.apache.hadoop.fs.FileSystem.get(FileSystem.java:351)   at org.apache.hadoop.fs.Path.getFileSystem(Path.java:287)   at org.apache.hadoop.fs.shell.PathData.expandAsGlob(PathData.java:325)   at org.apache.hadoop.fs.shell.Command.expandArgument(Command.java:224)   at org.apache.hadoop.fs.shell.Command.expan"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1227** (`tawos-v1.1:2580`), created 2014-01-14T21:59:45.000000Z
  - Title: "\"Investigate long running tests and create refactoring issues\""
  - Description: "\"https://sonar.springsource.org/dashboard/index/7173?did=3  Shows which of our current tests take the most time to execute.  xd.dirt.stream and xd.shell.command are where the most time is spent.  In xd.dirt.stream it seems likely that time can be reduced by not restarting a new single node server per test, but sharing it across tests, e.g.   RabbitSingleNodeStreamDeploymentIntegrationTests    LocalSingleNodeStreamDeploymentIntegrationTests  RedisSingleNodeStreamDeploymentIntegrationTests    As a first pass, the test that take longer than 15 seconds in that report should be investigated. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1272** (`tawos-v1.1:2535`), created 2014-01-28T05:13:17.000000Z
  - Title: "\"Remove job options that are handled at module level from shell\""
  - Description: "\"Since makeUnique, dateFormat and numberFormat now have their own module options now, they are nicely advertised as options to a job (and will benefit from code completion soon), so they can be removed from the shell (where they currently allow for a misconfiguration if set at both the job and shell level)\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1344** (`tawos-v1.1:2463`), created 2014-02-24T11:53:18.000000Z
  - Title: "\"Cannot undeploy stream that was created and deployed with a \"\".\"\" in the name\""
  - Description: "\"<USER>mbp:spring-xd-1.0.0.M5 <USER> ./shell/bin/xd-shell  _____                           __   _______ /  ___|          (-)             \\ \\ / /  _  \\ \\ `--. _ __  _ __ _ _ __   __ _   \\ V /| | | |  `--. \\ '_ \\| '__| | '_ \\ / _` |  / ^ \\| | | | /\\__/ / |_) | |  | | | | | (_| | / / \\ \\ |/ / \\____/| .__/|_|  |_|_| |_|\\__, | \\/   \\/___/       | |                  __/ |       |_|                 |___/ eXtreme Data 1.0.0.M5 | Admin Server Target: http://localhost:9393 Welcome to the Spring XD shell. For assistance hit TAB or type \"\"help\"\". xd:>stream list   Stream Name    Stream Definition                                          Status   -------------  ---------------------------------------------------------  --------   eesstream.log  http | transform --expression=payload.toUpperCase() | log  deployed   httptest       http | file   tictac         time | log  xd:>stream   stream all         stream create      stream deploy      stream destroy     stream list        stream undeploy      xd:>stream undeploy --name  stream undeploy --name  required --name: the name of the stream to un-deploy; no default value xd:>stream undeploy --name eesstream.log  Command failed org.springframework.xd."
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1512** (`tawos-v1.1:2295`), created 2014-04-08T10:14:19.000000Z
  - Title: "\"Create documentation for how to extend the XD containers\""
  - Description: "\"https://jira.spring.io/browse/XD-1343 and related issues.\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which concrete completion behaviors and regression cases are specified in the cutoff-valid XD-1585 and XD-1706 descriptions?
- Does any supplied design show that required-option handling is changing in a way that could exclude a command family?

## XD-1875 (train)

Historical cutoff: 2014-06-25T08:11:53.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `e819d362737d1946ec51c8c0fe9cfc167546022077ddc6690e35ed7e5483d7a0`

Source input identity SHA-256: `f186da3b304ce3b0e53679fe1ee7773dea7d8714d5557360e2c64b16227dfb1b`

### Supplied historical plan

- **XD-1875** (`tawos-v1.1:1937`)
  - Title: "Create equivalent tests in spring-xd-integration which are only present in the script based tests."
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-1876** (`tawos-v1.1:1936`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1877** (`tawos-v1.1:1935`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1878** (`tawos-v1.1:1934`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1879** (`tawos-v1.1:1933`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-1880** (`tawos-v1.1:1932`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The plan already requires equivalent tests; unknown member text does not establish that real source-to-transport coverage will be removed.",
    "XD-1228 describes optional isolated testing, but its use in XD-1875 is not supplied. XD-1675 and XD-1683 are Done, and XD-1245 provides external-input acceptance utilities."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1413** (`tawos-v1.1:2394`), created 2014-03-18T11:03:56.000000Z
  - Title: "Create spring-xd-test-fixtures project"
  - Description: "\"Acceptance tests has a direct library reference to spring-xd-shell.  This causes problems with eclipse.  It needs a intermediate main project to resolve the dependencies.  This is based on the conversation I had with <USER>  you cant depend on another projects' src/test what is needed is an intermediate project… some test support project that project would depend on spring-xd-shell (and others) … but then the spring-xd-integration-test project would depend on the intermediate one lib dependencies should only be under src/main src/test is intended to be scoped to the project it sits in… tests FOR that project - not reusable base classes, etc\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1245** (`tawos-v1.1:2562`), created 2014-01-15T07:04:57.000000Z
  - Title: "Develop basic acceptance test application to exercise based XD-EC2 deployment from CI"
  - Description: "Create a first pass at an acceptance test app for a stream definition of http | log.  \n\nThis will involve creating two new projects in xd\n\n1. spring-xd-integration-test\n2. spring-xd-acceptance-tests\n\n#1 will contain generally useful utility methods for acceptance test, such as sending data over http, obtaining and asserting JMX values of specific modules.\n#2 will contain tests that use #1 to test the various out of the box modules provides in XD."
  - Unknown fields: []
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-756** (`tawos-v1.1:3044`), created 2013-08-26T09:53:02.000000Z
  - Title: "\"Create a splitter module\""
  - Description: "\"The splitter functionality in Spring Integration should be exposed to XD as a processing module.  The splitter should use a SpEL expression to specify how to split the message up.    *Implementation Suggestions*  This should be a simple XML based module definition that has input/output channels and has the SpEL expression parameterized.  The default value of the SpEL expression should result in the message not being split.  *How to check it works*  The current file or tail input source can be used to split up the text in a file into words.  The tail module should be checked to see how many lines of text it will read into memory at once.  The file module node with the file-to-string transformer will only work for small files as it keep the whole file in memory.    If there is a big memory inefficiency in using the tail file input source, create a new story to investigate how to have a file based input source that creates a message per line of text or something that is will not result in excessive memory usage.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1228** (`tawos-v1.1:2579`), created 2014-01-14T22:07:43.000000Z
  - Title: "Provide a easy, prescriptive means to perform unit and basic stream integration tests."
  - Description: "\"AbstractSingleNodeStreamDeploymentIntegrationTests is the basis of 'state of the art' testing for a stream that allows you to get a reference to the input and output channel of the stream  http | filter | transform | file.  One can send messages to the channel after the http module, but before filter and one can retrieve the messages that were sent to the channel after the transform module but before file.  The current implementation inside AbstractSingleNodeStreamDeploymentIntegrationTests can be improved in terms of ease of use for end-users.    The issue is to create as simple a way as possible for a user to test their processing modules/stream definitions without having to actually do a real integration test by sending data to the input module.  Either as a separate issue or as part of this one, the documentation   https://github.com/spring-projects/spring-xd/wiki/Creating-a-Processor-Module  should be updated to explicitly show how to use this issue's test functionality. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1675** (`tawos-v1.1:2135`), created 2014-05-07T15:40:19.000000Z
  - Title: "\"FilePollHdfs is not writing results to hdfs\""
  - Description: "\"XD Deployment  Description:  XD Cluster (1 Container) Environment:  EC2 Type Of Test:  Manual Test Test Failed On  filepollhdfs (only test that was run) Build Used  Built May 7, 10:29 UTC  From the shell, attempted to create filepollhdfs however no results were written to hdfs (hadoop22).    The commands executed were the following: job create myjob --definition \"\"filepollhdfs  --names=forename,surname,address\"\" --deploy stream create mystream --definition \"\"file --dir=67fc27a6-224d-4c67-a02a-40730bcf8906 --pattern='*.out' > queue:job:myjob\"\" --deploy  No warnings nor exceptions were displayed till I changed the log4j.logger.org.springframework to INFO and restarted the container.  Then when I copied the sample file to the monitored directory the log reported: 21:30:07,605  INFO DeploymentsPathChildrenCache-0 module.ModuleDeployer:118 - deployed SimpleModule [name=file, type=source, group=mystream, index=0 @61612c7c] Exception in thread \"\"inbound.job:myjob-redis:queue-inbound-channel-adapter1\"\" org.springframework.messaging.core.DestinationResolutionException: failed to look up MessageChannel with name 'errorChannel' in the BeanFactory (and there is no HeaderChannelRegistry presen"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1681** (`tawos-v1.1:2129`), created 2014-05-09T12:33:52.000000Z
  - Title: "\"Need to support XD_admin_host and xd_containers in test properties\""
  - Description: "\"If a user wishes to run the acceptance tests from their local machine against an XD instance on EC2  the only way to establish container and admin server is via the artifact ec2servers.csv. And this has to be copied to the spring-xd-integration-test subdirectory.   The user should be able to set the xd_admin_host and xd_containers in the application-<profile>.properties file. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1683** (`tawos-v1.1:2127`), created 2014-05-09T15:51:29.000000Z
  - Title: "\"syslog-tcp throws exception when receiving syslog data\""
  - Description: "\"XD Deployment  Description XD Cluster (1 Container) Environment EC2 Type Of Test Manual test via shell Test Failed On syslog-tcp (only test that was run) Build Used Built May 7, 10:29 UTC  [Setting up the Environment] * Used the wiki instructions to setup the syslog on the ec2 instance.  * Deploy the stream below: stream create mystream --definition \"\"syslog-tcp | file --binary=true --mode=REPLACE\"\" --deploy  * On the EC2 Instance execute the line below: logger -p local3.info -t TESTING \"\"Test Syslog Message\"\"  [What occurred] Stream fails to process inbound syslog information and throws the exception below:   Exception in thread \"\"inbound.mystream.0-redis:queue-inbound-channel-adapter17\"\" org.springframework.messaging.core.DestinationResolutionException: failed to look up MessageChannel with name 'errorChannel' in the BeanFactory (and there is no HeaderChannelRegistry present).  at org.springframework.integration.support.channel.BeanFactoryChannelResolver.resolveDestination(BeanFactoryChannelResolver.java:108)  at org.springframework.integration.support.channel.BeanFactoryChannelResolver.resolveDestination(BeanFactoryChannelResolver.java:44)  at org.springframework.integration.ch"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1707** (`tawos-v1.1:2103`), created 2014-05-14T08:55:46.000000Z
  - Title: "\"The Dynamic Router example in the docs throws an exception with Rabbit Transport\""
  - Description: "\"The example in the M6 documentation for the Dynamic Router (here: http://docs.spring.io/spring-xd/docs/1.0.0.M6/reference/html/#dynamic-router) for the SpEL-Based Routing throws an exception when processing the message (from the HTTP post) saying \"\"No bean named 'queue:foo' is defined\"\", when using RabbitMQ as the transport.  I do not know a workaround.  Steps to reproduce: 1) Run RabbitMQ locally 2) Run xd-singlenode --transport rabbit 3) xd:>stream create f --definition \"\"queue:foo > transform --expression=payload+'-foo' | log\"\" --deploy  xd:>stream create b --definition \"\"queue:bar > transform --expression=payload+'-bar' | log\"\" --deploy  xd:>stream create r --definition \"\"http | router --expression=payload.contains('a')?'queue:foo':'queue:bar'\"\" --deploy  4) xd:>http post --data \"\"a\"\"  5) This should give a stacktrace: Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No bean named 'queue:foo' is defined  at org.springframework.beans.factory.support.DefaultListableBeanFactory.getBeanDefinition(DefaultListableBeanFactory.java:641)  at org.springframework.beans.factory.support.AbstractBeanFactory.getMergedLocalBeanDefinition(AbstractBeanFactory.java:115"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-197** (`tawos-v1.1:3586`), created 2013-06-06T06:26:25.000000Z
  - Title: "\"Create a scriptProcessor module that allows the execution of a groovy (potentially jruby,jython) based SI Service Activator\""
  - Description: "\"This will enable arbitrary processing logic to be used in a processing step.  See http://blog.springsource.org/2011/12/08/spring-integration-scripting-support-part-1/  <int:service-activator ...>   <script:script lang=\"\"groovy\"\" location=\"\"file:scripts/groovy/myscript.groovy\"\"> </int:service-activator>  would be the essence of the module.  Probably 'lang' gets detected from the file extension.\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What concrete script scenarios and behavioral equivalence criteria belong to XD-1875?
- Do the planned Java tests use the external-input harness in XD-1245, the isolated approach in XD-1228, or both?

## XD-2052 (train)

Historical cutoff: 2014-08-05T15:49:24.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `5a94c08b063ecb351fcc96212dfa2a3e9531b1a6d7a430759ae84b18a80ce42e`

Source input identity SHA-256: `c2132b4f7b9c37ed31a7238ccc2622ab140fc5c146a279927c6892add20afe57`

### Supplied historical plan

- **XD-2052** (`tawos-v1.1:1762`)
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1329** (`tawos-v1.1:2478`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-1746** (`tawos-v1.1:2065`)
  - Title: "Richer Support for Content-Type in the HTTP Source"
  - Description: "See [~jbrisbin] comments in https://github.com/spring-projects/spring-xd/pull/879."
  - Unknown fields: ["type", "status"]
  - Truncated fields: []
- **XD-1933** (`tawos-v1.1:1880`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2044** (`tawos-v1.1:1770`)
  - Title: "Create a SFTP source"
  - Description: "Use the SFTP adapter in SI as the basis.\n\nNeed to consider the infrastructure for testing."
  - Unknown fields: ["estimate"]
  - Truncated fields: []
- **XD-2060** (`tawos-v1.1:1755`)
  - Title: null
  - Description: "As an user, I'd like to have a native JDBC source module to ingest data directly from various databases. "
  - Unknown fields: ["title", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root explicitly requires data-accuracy validation, required-attribute errors and exception logging; XD-2044 also explicitly raises SFTP test infrastructure. Those requirements must not be labelled missing.",
    "XD-1295 reports a JMX proxy/conversion failure and XD-1743 reports Rabbit deserialization of Twitter classes. The supplied XD-1746 text does not establish whether the HTTP content-type change uses those same paths or whether their Done work leaves an active defect.",
    "XD-1912 concerns Rabbit-to-JDBC sink interoperability and XD-1678 concerns a batch jobstore connection. Neither, together with another supplied ticket, establishes a specific failure mechanism in the planned native JDBC source.",
    "XD-1329 and XD-1933 lack scope text; linked PR text is not supplied and was not consulted. The bounded evidence does not establish further omissions in the new sources."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1228** (`tawos-v1.1:2579`), created 2014-01-14T22:07:43.000000Z
  - Title: "Provide a easy, prescriptive means to perform unit and basic stream integration tests."
  - Description: "\"AbstractSingleNodeStreamDeploymentIntegrationTests is the basis of 'state of the art' testing for a stream that allows you to get a reference to the input and output channel of the stream  http | filter | transform | file.  One can send messages to the channel after the http module, but before filter and one can retrieve the messages that were sent to the channel after the transform module but before file.  The current implementation inside AbstractSingleNodeStreamDeploymentIntegrationTests can be improved in terms of ease of use for end-users.    The issue is to create as simple a way as possible for a user to test their processing modules/stream definitions without having to actually do a real integration test by sending data to the input module.  Either as a separate issue or as part of this one, the documentation   https://github.com/spring-projects/spring-xd/wiki/Creating-a-Processor-Module  should be updated to explicitly show how to use this issue's test functionality. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: ["status", "estimate"]
  - Truncated fields: ["description"]
- **XD-1912** (`tawos-v1.1:1901`), created 2014-07-02T01:06:54.000000Z
  - Title: "\"Rabbitmq source is not ingested the data into jdbc sink\""
  - Description: "\"I am using Spring XD to ingest the data into Pivotal HD.My source is log files which is coming from logstash through Rabbitmq. I could able to ingest the log files in HDFS (by using Rabbitmq source and HDFS sink) However when i try to ingest the data directly into Hawq by using JDBC sink,it's not working. Shall we directly load Rabbitmq source into any databases like Hawq?   stream create --name pivotalqueue --definition \"\"rabbit --host=<my host name>   | jdbc   --columns='colum list'\"\"      ---Not working  I configured jdbc in jdbc.properties. There was no issue with jdbc configuration(because i tested this with simple tail source it's working and load the data into HAWQ. stream create --name pivotalqueue --definition \"\"tail --name=/tmp/xd/output/test.out   | jdbc  --columns='columns list'\"\"  ) \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1975** (`tawos-v1.1:1839`), created 2014-07-15T06:41:28.000000Z
  - Title: "Undeploying twitterstream logs warning - MessageDeliveryException"
  - Description: "To reproduce - \n\nDownload recent snapshot - http://repo.spring.io/libs-snapshot-local/org/springframework/xd/spring-xd/1.0.0.BUILD-SNAPSHOT/spring-xd-1.0.0.BUILD-20140715.101224-1-dist.zip\n\nStart XD and shell -\nxd:>stream create --name tweets --definition \"twitterstream | file\" --deploy \nxd:>stream undeploy --name tweets \n\n(Note: the IllegalStateException has been fixed for RC1, still need to fix the MessageDeliveryException)\n\nThere is an error logged in the logs:\n\n{code}\n08:37:57,022  INFO DeploymentsPathChildrenCache-0 module.ModuleDeployer - deployed SimpleModule [name=twitterstream, type=source, group=tweets, index=0 @581a12b9]\n08:38:02,685  INFO main-EventThread server.ContainerRegistrar - Undeploying module [ModuleDescriptor@4807f3e2 moduleName = 'twitterstream', moduleLabel = 'twitterstream', group = 'tweets', sourceChannelName = [null], sinkChannelName = [null], sinkChannelName = [null], index = 0, type = source, parameters = map[[empty]], children = list[[empty]]]\n08:38:02,687  INFO main-EventThread module.ModuleDeployer - removed SimpleModule [name=twitterstream, type=source, group=tweets, index=0 @581a12b9]\n08:38:02,705  INFO DeploymentsPathChildrenCache-0 server.Contain"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1295** (`tawos-v1.1:2512`), created 2014-02-10T00:54:04.000000Z
  - Title: "\"Module message conversion fails to work if JMX is enabled\""
  - Description: "\"If JMX is enabled for modules (enabling the IntegrationMBeanExporter), the ModuleTypeConversionPlugin fails to get the reference to input/output channel (for adding the ContentTypeHeaderInterceptor) and results in exception.  It seems like the IntegrationMBeanExporter (when JMX is enabled) creates JdkDynamicAopProxy for all the integration components and thereby the following check on ModuleTypeConversionPlugin to retrieve the AbstractMessageChannel fails.  AbstractMessageChannel channel = null;    if (isInput) {     channel = module.getComponent(\"\"input\"\", AbstractMessageChannel.class);    }    else {     channel = module.getComponent(\"\"output\"\", AbstractMessageChannel.class);    }  I see the reason why AbstractMessageChannel is used here (to use some of the methods in the implementing class that didn't exist in the interfaces) but IntegrationMBeanExporter creating JdkDynamicAopProxy for the channel fails to resolve as AbstractMessageChannel here.  Following is the full stack trace:  To replicate,  stream create testing --definition \"\"\"\"http --outputType=text/plain | log\"\" 3:45,238 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter1 handler.LoggingHandler:145 - org.spr"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1418** (`tawos-v1.1:2389`), created 2014-03-19T03:37:45.000000Z
  - Title: "\"Create subproject spring-xd-machine-learning-analytics\""
  - Description: "\"This project contains core abstractions that will allow for multiple implementations of a machine learning algorithm to be implemented via integration with various existing libraries or custom code implementations.    The initial code for this has been developed in a separate github repo and is located here   https://github.com/thomasdarimont/spring-xd/tree/feature/advanced-analytics-support/spring-xd-analytics/src/main/java/org/springframework/xd/analytics/model  The model can assume its use in evaluation of the model inside a stream where the data structure is a Tuple.  Note, it maybe useful to consider Message<Tuple> in case any metadata outside the core 'input data' is required to help guide the evaluation.  The build.gradle file should be updated such that there is a new build artifact spring-xd-machine-learning-analytics.jar along the lines of our other build artifacts.  Open to other naming suggestions.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1678** (`tawos-v1.1:2132`), created 2014-05-08T09:59:25.000000Z
  - Title: "\"XD does not reconnect to jobstore if connection is  lost, leaving Jobs in inconsistent state.\""
  - Description: "\"XD Deployment Description XD Cluster (1 Container) Environment EC2 Type Of Test Shell Command Line Test Failed On hdfs (only test that was run) Build Used Built May 7, 10:29 PST  [Overall issue] XD Admin and container lost connectivity to the the jobstore (MySql on RDS) and did not reconnect.   Exception Displayed in log. Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: The last packet successfully received from the server was 54,321,927 milliseconds ago.  The last packet sent successfully to the server was 54,321,928 milliseconds ago. is longer than the server configured value of 'wait_timeout'. You should consider either expiring and/or testing connection validity before use in your application, increasing the server configured values for client timeouts, or using the Connector/J connection property 'autoReconnect=true' to avoid this problem.  at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)  at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:57)  at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)  at java.lang.reflect.Constructor.newInstance(C"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1299** (`tawos-v1.1:2508`), created 2014-02-10T12:26:26.000000Z
  - Title: "Move --deleteFiles out of ResourcesIntoJdbcJobModuleOptionsMetadata"
  - Description: "\"Currently, the fileDeletion listeners are added to filepollhdfs and filejdbc OOTB job modules so that the files are deleted after successful completion of jobs that write the file into hdfs/jdbc.  We have \"\"--deleteFiles\"\" option in ResourcesIntoJdbcJobModuleOptionsMetadata (from https://github.com/spring-projects/spring-xd/pull/562)  which makes it available for hdfsjdbc job module as well. But it is not supported yet as it involves deletion of HDFS files.  We need the file deletion listeners for the hdfsjdbc and hdfsmongodb job modules so that if opted to delete files, it can be supported.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1743** (`tawos-v1.1:2068`), created 2014-05-21T13:53:13.000000Z
  - Title: "\"ClassNotFoundException: o.s.social.twitter.api.Tweet with Rabbit-transport\""
  - Description: "Using Rabbit as a transport, I get the below error when creating the following stream:\n\n{code}\nstream create mytweets --definition \"twittersearch --query='spring' | log\" --deploy true\n{code}\n\nIn local mode, the stream executes just fine. Of course it works with *--outputType=application/json*. Nevertheless, I was not expecting that exception (see below)\n\nIssue was also verified by [~<USER>. \n\n{code}\norg.springframework.amqp.rabbit.listener.ListenerExecutionFailedException: Listener threw exception\n\tat org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer.wrapToListenerExecutionFailedExceptionIfNeeded(AbstractMessageListenerContainer.java:758)\n\tat org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer.doInvokeListener(AbstractMessageListenerContainer.java:653)\n\tat org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer.invokeListener(AbstractMessageListenerContainer.java:576)\n\tat org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer.access$001(SimpleMessageListenerContainer.java:75)\n\tat org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer$1.invokeListener(SimpleMessageListenerContainer.java"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What cutoff-available acceptance text defines incoming and outgoing content-type behavior for XD-1746 beyond its title and PR reference?
- Are actual transport/JMX or database compatibility cases applicable to these source implementations, and are they already covered by the explicit data-accuracy requirement?

## XD-2053 (train)

Historical cutoff: 2014-08-05T15:51:32.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `a5e2e1d6f51d7235e18f1a81f852aa7fd5bd6efb5db2b37a5b1122832e30e515`

Source input identity SHA-256: `f022a4488551743e154f0f868c01dd9cca2be837f24969c1dc689dc3449eec6d`

### Supplied historical plan

- **XD-2053** (`tawos-v1.1:1761`)
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2055** (`tawos-v1.1:1759`)
  - Title: "As an user, I'd like to have the ability to ingest data into ElasticSearch sink"
  - Description: "User should be able to leverage native ES sink to aggregate, search and analyze data insights in real-time.\n\nDetails: http://www.elasticsearch.org/overview/elasticsearch"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-2061** (`tawos-v1.1:1754`)
  - Title: null
  - Description: "As an user, I'd like to have the ability to ingest data into Redis sink."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-1912 does not identify the cause of the Rabbit-to-JDBC failure; a payload-encoding mechanism cannot be assumed.",
    "XD-1743 describes a completed Rabbit/Tweet class-resolution defect, but the new ElasticSearch/Redis source payloads, transports and adapter contracts are not supplied.",
    "The plan explicitly includes data accuracy and error validation; absent scenario detail does not establish omitted checks."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1295** (`tawos-v1.1:2512`), created 2014-02-10T00:54:04.000000Z
  - Title: "\"Module message conversion fails to work if JMX is enabled\""
  - Description: "\"If JMX is enabled for modules (enabling the IntegrationMBeanExporter), the ModuleTypeConversionPlugin fails to get the reference to input/output channel (for adding the ContentTypeHeaderInterceptor) and results in exception.  It seems like the IntegrationMBeanExporter (when JMX is enabled) creates JdkDynamicAopProxy for all the integration components and thereby the following check on ModuleTypeConversionPlugin to retrieve the AbstractMessageChannel fails.  AbstractMessageChannel channel = null;    if (isInput) {     channel = module.getComponent(\"\"input\"\", AbstractMessageChannel.class);    }    else {     channel = module.getComponent(\"\"output\"\", AbstractMessageChannel.class);    }  I see the reason why AbstractMessageChannel is used here (to use some of the methods in the implementing class that didn't exist in the interfaces) but IntegrationMBeanExporter creating JdkDynamicAopProxy for the channel fails to resolve as AbstractMessageChannel here.  Following is the full stack trace:  To replicate,  stream create testing --definition \"\"\"\"http --outputType=text/plain | log\"\" 3:45,238 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter1 handler.LoggingHandler:145 - org.spr"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: ["status", "estimate"]
  - Truncated fields: ["description"]
- **XD-1912** (`tawos-v1.1:1901`), created 2014-07-02T01:06:54.000000Z
  - Title: "\"Rabbitmq source is not ingested the data into jdbc sink\""
  - Description: "\"I am using Spring XD to ingest the data into Pivotal HD.My source is log files which is coming from logstash through Rabbitmq. I could able to ingest the log files in HDFS (by using Rabbitmq source and HDFS sink) However when i try to ingest the data directly into Hawq by using JDBC sink,it's not working. Shall we directly load Rabbitmq source into any databases like Hawq?   stream create --name pivotalqueue --definition \"\"rabbit --host=<my host name>   | jdbc   --columns='colum list'\"\"      ---Not working  I configured jdbc in jdbc.properties. There was no issue with jdbc configuration(because i tested this with simple tail source it's working and load the data into HAWQ. stream create --name pivotalqueue --definition \"\"tail --name=/tmp/xd/output/test.out   | jdbc  --columns='columns list'\"\"  ) \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1975** (`tawos-v1.1:1839`), created 2014-07-15T06:41:28.000000Z
  - Title: "Undeploying twitterstream logs warning - MessageDeliveryException"
  - Description: "To reproduce - \n\nDownload recent snapshot - http://repo.spring.io/libs-snapshot-local/org/springframework/xd/spring-xd/1.0.0.BUILD-SNAPSHOT/spring-xd-1.0.0.BUILD-20140715.101224-1-dist.zip\n\nStart XD and shell -\nxd:>stream create --name tweets --definition \"twitterstream | file\" --deploy \nxd:>stream undeploy --name tweets \n\n(Note: the IllegalStateException has been fixed for RC1, still need to fix the MessageDeliveryException)\n\nThere is an error logged in the logs:\n\n{code}\n08:37:57,022  INFO DeploymentsPathChildrenCache-0 module.ModuleDeployer - deployed SimpleModule [name=twitterstream, type=source, group=tweets, index=0 @581a12b9]\n08:38:02,685  INFO main-EventThread server.ContainerRegistrar - Undeploying module [ModuleDescriptor@4807f3e2 moduleName = 'twitterstream', moduleLabel = 'twitterstream', group = 'tweets', sourceChannelName = [null], sinkChannelName = [null], sinkChannelName = [null], index = 0, type = source, parameters = map[[empty]], children = list[[empty]]]\n08:38:02,687  INFO main-EventThread module.ModuleDeployer - removed SimpleModule [name=twitterstream, type=source, group=tweets, index=0 @581a12b9]\n08:38:02,705  INFO DeploymentsPathChildrenCache-0 server.Contain"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-465** (`tawos-v1.1:3330`), created 2013-07-12T07:43:37.000000Z
  - Title: "\"Shell should display error messages returned from the server\""
  - Description: "\"For example, using tcpdump I can see both an exception and message information:  'HTTP/1.1 500 Internal Server Error Server: Apache-Coyote/1.1 Content-Type: application/json;charset=UTF-8 Transfer-Encoding: chunked Date: Fri, 12 Jul 2013 13:38:26 GMT Connection: close  275 [{\"\"links\"\":[],\"\"logref\"\":\"\"MessageHandlingException\"\",\"\"message\"\":\"\"org.springframework.context.ApplicationContextException: Failed to start bean 'org.springframework.integration.monitor.IntegrationMBeanExporter#0#92e27d20-4c48-4131-866c-91b6cb642ca2'; nested exception is org.springframework.jmx.export.UnableToRegisterMBeanException: Unable to register MBean [MessageChannelMonitor: [name=nullChannel, sends=0, receives=0]] with key 'xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log'; nested exception is javax.management.InstanceAlreadyExistsException: xd.tap1:type=MessageChannel,name=nullChannel,index=1,module=log\"\"}]  However the client only shows:  http://localhost:8080:>tap create --name \"\"tap1\"\" --definition \"\"<EMAIL> | log\"\" --deploy true 14:38:26,113  WARN Spring Shell client.RestTemplate:524 - POST request for \"\"http://localhost:8080/taps\"\" resulted in 500 (Internal Server Error); invoking e"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1958** (`tawos-v1.1:1855`), created 2014-07-11T13:59:18.000000Z
  - Title: "\"filejdbc job broken in distributed mode\""
  - Description: "The filejdbc job is broken in distributed mode (redis and rabbit)\n\nTo reproduce:\n\nexport XD_TRANSPORT=rabbit\n\nstart xd-admin\nstart xd-container\n\nstart shell and create this job:\n\n{code}\n>job create mydata --definition \"filejdbc --names=col1,col2,col3 --resources=file:///home/trisberg/Test/input/*.csv --initializeDatabase=true\" --deploy\n>job launch mydata\n{code}\n\nresults in JOB starting but never completing:\n\n{code}\n>job execution list\n  Id  Job Name  Start Time                            Step Execution Count  Execution Status  Deployment Status  Definition Status\n  --  --------  ------------------------------------  --------------------  ----------------  -----------------  -----------------\n    0  mydata      2014-07-11 15:44:33 America/New_York  0                     STARTED           Deployed           Exists\n{code}\n\nSteps:\n\n{code}\nStep Id\tStep Name\tReads\tWrites\tCommits\tRollbacks\tDuration\tStatus\tDetails\n0\tstep1-master\t0\t0\t0\t0\t-1405349644032 ms\tEXECUTING\t\n1\tstep1-master:partition0\t292\t292\t3\t0\t302 ms\tCOMPLETED\t\n2\tstep1-master:partition1\t292\t292\t3\t0\t203 ms\tCOMPLETED\t\n3\tstep1-master:partition2\t292\t292\t3\t0\t193 ms\tCOMPLETED\t\n{code}\n\nWhen using Redis, I also get this stacktrace in cont"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-953** (`tawos-v1.1:2850`), created 2013-10-14T08:25:02.000000Z
  - Title: "\"Richer module options metadata\""
  - Description: "\"Module options are currently implemented using PropertySourcesPlaceholderConfigurer, doing simple \"\"text\"\" replacements.  This story proposes to introduce a richer model for module options, which could take the following xml representation (keeping in mind that there would be an underlying set of classes that could also apply to e.g. @Configuration approach):  {code:xml} <xd:params>   <xd:param name=\"\"port\"\" help=\"\"the http port to listen on\"\" /> </xd:params> {code}  So, the very first obvious benefit is providing help metadata. The second one is an easy way to list available option names, without resorting to brittle PropertySourcesPlaceholderConfigurer hacks (we wouldn't for example detect xd.stream.name or XD_TRANSPORT as a valid option)  One could also specify defaults/computations, this time benefiting from SpEL everywhere: {code:xml} <xd:params>   <xd:param name=\"\"directory\"\" default=\"\"headers.directory\"\" /> </xd:params> {code}  Lastly, this opens the door to better type checking / combinations / optionality support: {code:xml} <xd:params valid=\"\"fixedDelay || cron\"\">   <xd:param name=\"\"fixedDelay\"\" type=\"\"int\"\" />   <xd:param name=\"\"cron\"\" type=\"\"string\"\" /> </xd:params> {c"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1047** (`tawos-v1.1:2759`), created 2013-11-10T12:41:11.000000Z
  - Title: "\"Allow Aggregate Counter to use timestamp field in data.\""
  - Description: "\"Currently the aggregate counter aggerates by the current time. However the data may already have a timestamp in it (eg streams from activity events on a website).  It would be useful as an alternative approach to be able to specify this field to aggregate on.   This would have the following benefits:  1) The aggregate counts would be more accurate as they would reflect the acutal event times and not have any lag from an intermediate messgaging system they might have passed through. 2) If for whatever reason XD is down, comes back up and starts pulling queued messages from the messaging system the aggregate counter will reflect the correct event time. Currently you would get a gap and then a spike as a backlog of messages would get allocated to the current aggregate count. 3) Old data could be rerun through XD still creating the correct aggregate counts.  Configuration would be something like   stream create --name mytap --definition \"\"tap:mystream > aggregatecounter --name=mycount --timestampField=eventtime\"\"  without the timestampfield it would behave as currently. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1743** (`tawos-v1.1:2068`), created 2014-05-21T13:53:13.000000Z
  - Title: "\"ClassNotFoundException: o.s.social.twitter.api.Tweet with Rabbit-transport\""
  - Description: "Using Rabbit as a transport, I get the below error when creating the following stream:\n\n{code}\nstream create mytweets --definition \"twittersearch --query='spring' | log\" --deploy true\n{code}\n\nIn local mode, the stream executes just fine. Of course it works with *--outputType=application/json*. Nevertheless, I was not expecting that exception (see below)\n\nIssue was also verified by [~<USER>. \n\n{code}\norg.springframework.amqp.rabbit.listener.ListenerExecutionFailedException: Listener threw exception\n\tat org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer.wrapToListenerExecutionFailedExceptionIfNeeded(AbstractMessageListenerContainer.java:758)\n\tat org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer.doInvokeListener(AbstractMessageListenerContainer.java:653)\n\tat org.springframework.amqp.rabbit.listener.AbstractMessageListenerContainer.invokeListener(AbstractMessageListenerContainer.java:576)\n\tat org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer.access$001(SimpleMessageListenerContainer.java:75)\n\tat org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer$1.invokeListener(SimpleMessageListenerContainer.java"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1922** (`tawos-v1.1:1891`), created 2014-07-07T13:35:10.000000Z
  - Title: null
  - Description: "Currently specified Cron Expressions are executed in the Container's default TimeZone. In *Trigger.xml* we specify:\n\n{code}\n\t<beans profile=\"use-cron\">\n\t\t<int:inbound-channel-adapter channel=\"output\"\n\t\t\tauto-startup=\"false\" expression=\"'${payload}'\">\n\t\t\t<int:poller cron=\"${cron}\" />\n\t\t</int:inbound-channel-adapter>\n\t</beans>\n{code}\n\nThis translates in *org.springframework.integration.config.xml.PollerParser* to\n\n{code}\nBeanDefinitionBuilder builder = BeanDefinitionBuilder.genericBeanDefinition(CronTrigger.class);\nbuilder.addConstructorArgValue(cronAttribute)\n{code}\n\nWhich will call *org.springframework.scheduling.support.CronTrigger*:\n\n{code}\n\t/**\n\t * Build a {@link CronTrigger} from the pattern provided in the default time zone.\n\t * @param cronExpression a space-separated list of time fields,\n\t * following cron expression conventions\n\t */\n\tpublic CronTrigger(String cronExpression) {\n\t\tthis.sequenceGenerator = new CronSequenceGenerator(cronExpression);\n\t}\n{code}\n\n\"Build a {@link CronTrigger} from the pattern provided in the *default time zone*.\"\n\nWe need to pass-in a timezone. *Should cron expressions as part of an XD *Definition* have a TimeZone parameter?* When creating the strea"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Which specific source payloads, transports and accepted data representations are in scope for each new sink?
- Is there cutoff-visible evidence that either new adapter uses the failing conversion/classloading path documented in the prior incidents?

## XD-2054 (train)

Historical cutoff: 2014-08-05T16:13:25.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `4ccb54011ff395138220f8874d90682db17fc1a3f7f1fb6031a45c43d5d669fd`

Source input identity SHA-256: `2f8df5ac8823619cfa49d42e100493a86668f5961ffe09b31c22fbd341b99079`

### Supplied historical plan

- **XD-2054** (`tawos-v1.1:1760`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2015** (`tawos-v1.1:1799`)
  - Title: "Spring XD UI: end-to-end tests do not work"
  - Description: "Currently, end-to-end tests of Spring XD UI will not run, as protractor relies on a non-existing chromedriver.exe file.\n\nEither the configuration has to be removed from the Gruntfile or the necessary dependencies should be there."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The sole visible child, XD-2015, already identifies the missing chromedriver.exe dependency that prevents Protractor end-to-end tests from running, and explicitly offers configuration or dependency correction. It is not an omitted testing task.",
    "The prior tickets describe server classloading, job deployment, configuration and module-test utilities. None supplies a second comparable browser-test dependency failure to support an additional risk mechanism.",
    "The root is wholly unknown. Backend integration-test needs cannot be inferred as uncovered work from this narrow UI test-runner repair."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1318** (`tawos-v1.1:2489`), created 2014-02-12T16:03:13.000000Z
  - Title: "\"XD container can not be started before the admin server\""
  - Description: "\"The job single partitioned step support (from singlestep-partitioner-support.xml) has the batch job DAOs (loaded from batch.xml).  During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes).   Here is the exception:  15:30:03,600  INFO main xml.XmlBeanDefinitionReader:316 - Loading XML bean definitions from class path resource [META-INF/spring-xd/batch/batch.xml] 15:30:06,154  WARN main annotation.ConfigurationClassEnhancer:318 - @Bean method StepScopeConfiguration.stepScope is non-static and returns an object assignable to Spring's BeanFactoryPostProcessor interface. This will result in a failure to process annotations such as @Autowired, @Resource and @PostConstruct within the method's declaring @Configuration class. Add the 'static' modifier to this method to avoid these container lifecycle issues; see @Bean Javadoc for complete details 15:30:06,705  INFO main support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker:309 - Bean 'org.springframework.xd.dirt.server.ParentConfiguration$JmxConfiguration' of type [class org.springframework.xd.dirt.server.ParentConfigurat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1322** (`tawos-v1.1:2485`), created 2014-02-13T11:47:07.000000Z
  - Title: "Add way to provide module config options for XD on YARN"
  - Description: "There seems to be some intersection with the work for this issue and the rationalization of how module properties are handled.  There will be changes to configuration/property management support such that each module (source, sink, etc) will be able to also be overridden in spring-xd.yml (or wherever -Dspring.config.location points to.  The HDFS sink module for example, will have default values based on it's OptionsMetadata and will be of the form <type>.<module>.<option>\n\n\nThat means in the configuration for hdfs.xml sink, there would be a config section such as\n\n{code:xml}\n    <configuration>\n      fs.default.name=${sink.hdfs.hd.fs}\n      mapred.job.tracker=${sink.hdfs.hd.jt}\n      yarn.resourcemanager.address=${sink.hdfs.hd.rm}\n      mapreduce.framework.name=${sink.hdfs.mr.fw}\n    </configuration>\n{code}\n\nWith default values defined by a HdfsSinkOptionsMetadata class.  The hdfs.xml module file would not contain any references to a properties file.\n\nA file specified by -Dspring.config.location could override the values in a config section such as\n\nsink:\n  hdfs:\n    hd.fs : hdfs://foobarhost:8020\n    hd.jt : 10.123.123.123:9000\n\netc.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-703** (`tawos-v1.1:3097`), created 2013-08-16T15:58:55.000000Z
  - Title: "\"JobRepository should be persistent and shared across xd-admin/xd-container\""
  - Description: "\"The current code is creating an in-memory job repository for each batch job that is launched.  This makes it impossible to query the tables in the job repository across the cluster.  A single job repository that is backed by a file need to be shared across all jobs that are a launched.  *Implementation Suggestions* * The XDAdmin server should create the job repository schema, if not found, in a HSQLDB database, when it starts up * The bean definitions should be added to the same context that the analytics are being loaded in as it is already shared across xd-admin/xd-container.  The ‘analytics’ context should be renamed to something more generic, ‘shared parent context’ or something. * There is some clean up (removal) of the code in the current JobPlugin, META-INF/spring-xd/plugins/job/common.xml wouldn’t be needed anymore.  That might be all, not sure.  *How to verify it works* * A JUnit test that verifies the spring batch tables were created in the job repository when xd-admin is launched.  This would require deleting the backing db file before instantiating singlenode/xd-admin/xd-container.  * If you start the xd-container it should be able to find the necessary DataSource/JobR"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-742** (`tawos-v1.1:3058`), created 2013-08-22T14:18:55.000000Z
  - Title: "\"REST API for Job Management\""
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: []
  - Truncated fields: []
- **XD-756** (`tawos-v1.1:3044`), created 2013-08-26T09:53:02.000000Z
  - Title: "\"Create a splitter module\""
  - Description: "\"The splitter functionality in Spring Integration should be exposed to XD as a processing module.  The splitter should use a SpEL expression to specify how to split the message up.    *Implementation Suggestions*  This should be a simple XML based module definition that has input/output channels and has the SpEL expression parameterized.  The default value of the SpEL expression should result in the message not being split.  *How to check it works*  The current file or tail input source can be used to split up the text in a file into words.  The tail module should be checked to see how many lines of text it will read into memory at once.  The file module node with the file-to-string transformer will only work for small files as it keep the whole file in memory.    If there is a big memory inefficiency in using the tail file input source, create a new story to investigate how to have a file based input source that creates a message per line of text or something that is will not result in excessive memory usage.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1228** (`tawos-v1.1:2579`), created 2014-01-14T22:07:43.000000Z
  - Title: "Provide a easy, prescriptive means to perform unit and basic stream integration tests."
  - Description: "\"AbstractSingleNodeStreamDeploymentIntegrationTests is the basis of 'state of the art' testing for a stream that allows you to get a reference to the input and output channel of the stream  http | filter | transform | file.  One can send messages to the channel after the http module, but before filter and one can retrieve the messages that were sent to the channel after the transform module but before file.  The current implementation inside AbstractSingleNodeStreamDeploymentIntegrationTests can be improved in terms of ease of use for end-users.    The issue is to create as simple a way as possible for a user to test their processing modules/stream definitions without having to actually do a real integration test by sending data to the input module.  Either as a separate issue or as part of this one, the documentation   https://github.com/spring-projects/spring-xd/wiki/Creating-a-Processor-Module  should be updated to explicitly show how to use this issue's test functionality. \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which supported platforms and dependency-installation steps does the existing XD-2015 fix and its acceptance test cover?

## XD-2089 (train)

Historical cutoff: 2014-08-23T16:07:10.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `0fd3ed995c5ad91e9c8acba0cb95972577d1360eee01468c4be33ce3bb97ed0f`

Source input identity SHA-256: `a94d2d554f1e2c73578fe0f4e4c096f18aa0a52581c40e3252ab3e5c5a686e73`

### Supplied historical plan

- **XD-2089** (`tawos-v1.1:1726`)
  - Title: "Process of creating and deploying custom XD modules"
  - Description: null
  - Unknown fields: ["description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2090** (`tawos-v1.1:1725`)
  - Title: "Research how to package custom modules"
  - Description: "Design Spike: Investigate how to bundle/unbundle custom XD modules. What are the various approaches? What are the best practices?"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2091** (`tawos-v1.1:1724`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2090 explicitly investigates bundling/unbundling custom modules and best practices. XD-841 and XD-1863 describe packaging/distribution difficulties that are directly relevant to that existing investigation, not evidence that packaging research was omitted.",
    "XD-2034 supplies one configuration-location failure across local and Yarn deployment, but the other supplied tickets do not independently establish the same configuration-loading mechanism for the proposed packaging approach.",
    "No packaging approach is selected in the visible plan, and XD-2091 is unknown. Inferring a specific dependency, layout or validation defect before that decision would exceed the evidence."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2086** (`tawos-v1.1:1729`), created 2014-08-22T15:45:05.000000Z
  - Title: "Research how to leverage Spring Security for Authentication/Authorization"
  - Description: "Design Spike: Investigate 'Spring Security' features to determine whether it will fit XD's security requirements."
  - Unknown fields: ["type", "status", "estimate"]
  - Truncated fields: []
- **XD-2087** (`tawos-v1.1:1728`), created 2014-08-22T15:49:24.000000Z
  - Title: "Research how to leverage ZK's ACLs"
  - Description: "Design Spike: Investigate ZK's access control list to determine whether it will fit XD's security requirements. "
  - Unknown fields: ["type", "status", "estimate"]
  - Truncated fields: []
- **XD-2088** (`tawos-v1.1:1727`), created 2014-08-22T15:58:57.000000Z
  - Title: "Research how to orchestrate more than 1 job"
  - Description: "Design Spike: Investigate best approach to orchestrate more than 1 job."
  - Unknown fields: ["type", "status", "estimate"]
  - Truncated fields: []
- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1863** (`tawos-v1.1:1949`), created 2014-06-19T10:28:55.000000Z
  - Title: "\"Create way to deploy custom modules for XD on YARN\""
  - Description: "\"Need a way for end-user to package and add custom modules/scripts when deploying XD on YARN. Currently we have a zip file containing all code including modules. It's not convenient to un-zip/re-zip this archive to add custom modules/scripts.  See - https://github.com/spring-projects/spring-xd/issues/931\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2034** (`tawos-v1.1:1780`), created 2014-07-28T18:42:51.000000Z
  - Title: "Custom location for modules.yml not working"
  - Description: "tried local xd-admin/xd-container after setting\n\n{code}\nexport XD_MODULE_CONFIG_LOCATION=file:./spring-xd-1.0.0.BUILD-SNAPSHOT-yarn/config/\n{code}\n\nhave my twitter stuff in modules.yml in that directory but not picked up by the twitterstream module\n\nAlso not working for me deploying on YARN, this used to work at some point, not sure how long ago I actually tested this part - M6/M7?\n\nThe setting used for YARN deployment:\n\n{code}\n-Dxd.module.config.location: \"file:./\"\n{code}"
  - Unknown fields: []
  - Truncated fields: []
- **XD-238** (`tawos-v1.1:3545`), created 2013-06-17T10:03:00.000000Z
  - Title: "Deploying Custom Code"
  - Description: "When a module is deployed, it should run in its own isolated classpath.  The current code has all dependencies in a single classpath, taken from the lib directory at startup.  This has a number of drawbacks, one of the most important is the batch jobs can not be contributed to the system at runtime.  The work for this epic is decoupled from any module deployment story.  The assumption is that there will be a directory layout as shown below.\n\nCurrent layout\n\n./modules/.\n|-- common\n|-- job\n|-- processor\n|-- sink\n|-- source\n|-- trigger\n\nAnd inside source\n|-- source\n|   |-- file.xml\n|   |-- gemfire-cq.xml\n|   |-- gemfire.xml\n|   |-- http.xml\n|   |-- jms.xml\n|   |-- mqtt.xml\n|   |-- rabbit.xml\n|   |-- syslog-tcp.xml\n|   |-- syslog-udp.xml\n|   |-- tail.xml\n|   |-- tap.xml\n|   |-- tcp.xml\n|   |-- time.xml\n|   |-- twittersearch.xml\n|   |-- twitterstream.xml\n\n\nUsing an example of the source directory from the current layout.e.g ./modules/source/file, the new layout would be\n\n./modules/source/file/lib/spring-integration-file.jar\n./modules/source/file/config/file.xml\n\n\nWe should support both the new and old layout styles simultaneously.\n\nThere what is under 'file' directory is the 'package'  "
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-343** (`tawos-v1.1:3447`), created 2013-06-28T07:34:55.000000Z
  - Title: "Investigate JMX object naming of deployed modules and inbound/outbound channel adapters."
  - Description: "\"The object naming is still not ideal for XD since SI conventions add some noise. Likely  need to design and implement a custom naming strategy\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1018** (`tawos-v1.1:2788`), created 2013-10-28T11:06:30.000000Z
  - Title: "\"JobDeployer hides root exceptions on failure\""
  - Description: "\"When deploying jobs, the following code (line 103), hides the root cause of deployment failure:    if (exceptionClassName.equals(BEAN_CREATION_EXCEPTION) || exceptionClassName.equals(BEAN_DEFINITION_EXEPTION)) {     throw new MissingRequiredDefinitionException(definition.getName(), cause.getMessage());   }  For example:  org.springframework.xd.dirt.stream.MissingRequiredDefinitionException: Error creating bean with name 'dataSourceInitializer' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Cannot resolve reference to bean 'databasePopulator' while setting bean property 'databasePopulator'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'databasePopulator' defined in file [/Users/<USER>Work/spring-xd/build/dist/spring-xd/xd/modules/job/hdfsjdbc/config/hdfsjdbc.xml]: Initialization of bean failed; nested exception is java.lang.NullPointerException  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:103)  at org.springframework.xd.dirt.stream.JobDeployer.deploy(JobDeployer.java:67)  at org.springframework.xd.dirt.rest.XDController.save(XD"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1228** (`tawos-v1.1:2579`), created 2014-01-14T22:07:43.000000Z
  - Title: "Provide a easy, prescriptive means to perform unit and basic stream integration tests."
  - Description: "\"AbstractSingleNodeStreamDeploymentIntegrationTests is the basis of 'state of the art' testing for a stream that allows you to get a reference to the input and output channel of the stream  http | filter | transform | file.  One can send messages to the channel after the http module, but before filter and one can retrieve the messages that were sent to the channel after the transform module but before file.  The current implementation inside AbstractSingleNodeStreamDeploymentIntegrationTests can be improved in terms of ease of use for end-users.    The issue is to create as simple a way as possible for a user to test their processing modules/stream definitions without having to actually do a real integration test by sending data to the input module.  Either as a separate issue or as part of this one, the documentation   https://github.com/spring-projects/spring-xd/wiki/Creating-a-Processor-Module  should be updated to explicitly show how to use this issue's test functionality. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1245** (`tawos-v1.1:2562`), created 2014-01-15T07:04:57.000000Z
  - Title: "Develop basic acceptance test application to exercise based XD-EC2 deployment from CI"
  - Description: "Create a first pass at an acceptance test app for a stream definition of http | log.  \n\nThis will involve creating two new projects in xd\n\n1. spring-xd-integration-test\n2. spring-xd-acceptance-tests\n\n#1 will contain generally useful utility methods for acceptance test, such as sending data over http, obtaining and asserting JMX values of specific modules.\n#2 will contain tests that use #1 to test the various out of the box modules provides in XD."
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Does the spike compare dependency-complete archives, supported deployment modes and configuration discovery, and what additional scope is recorded in XD-2091?

## XD-2106 (train)

Historical cutoff: 2014-08-27T14:51:53.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `2ec0c28e0b94a67070988d6fc129c44c8851266c0218e13b6f943ce2891d3eeb`

Source input identity SHA-256: `4b376d2e1db69acb69f7da82d443206fa7e1c1bba037f63096d68b30a04f537c`

### Supplied historical plan

- **XD-2106** (`tawos-v1.1:1709`)
  - Title: "\"Provide the ability to visualize XD cluster view\""
  - Description: "\"As a user, I'd like to have the ability to visually explore XD's cluster view so that I'm aware where the components are deployed and how they are connected within the topology. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2092** (`tawos-v1.1:1723`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "estimate"]
  - Truncated fields: []
- **XD-2093** (`tawos-v1.1:1722`)
  - Title: "List Streams/Jobs based with deployed modules"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-2094** (`tawos-v1.1:1721`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2095** (`tawos-v1.1:1720`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2096** (`tawos-v1.1:1719`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2097** (`tawos-v1.1:1718`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root explicitly includes cluster topology visualization and XD-2093 includes listing streams/jobs with deployed modules. Unknown member descriptions do not establish that deployment-state handling is omitted.",
    "XD-1777 demonstrates orphaned partition deployment state, but the remaining supplied tickets do not provide a second comparable cluster-view failure. XD-1000 and XD-1001 are planned/completed UI precedents, not independent incidents.",
    "XD-1972 concerns an evolving job contract and XD-1695 concerns endpoint security; neither establishes that the topology view is blocked or will display incorrect data."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\nScope: Research the approach, design considerations and patterns that fits XD model.\n"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: null
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: ["title", "type"]
  - Truncated fields: ["description"]
- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1777** (`tawos-v1.1:2034`), created 2014-05-29T09:48:23.000000Z
  - Title: "Restore deployment properties for orphaned modules"
  - Description: "\"As part of XD-1338 we modified how module deployment works. Now module deployment requests include deployment properties as the data for the ZooKeeper node. This allows us to reuse those properties when a container exit the cluster and the module is redeployed to another container.  However if there are no other containers to handle the deployment, the module deployment node is erased, along with the properties. This mean no module will ever handle the partition that module was responsible for.  This condition needs to be handled so that partitioned streams continue to function in cases where the cluster temporarily doesn't have enough containers to support the stream.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-743** (`tawos-v1.1:3057`), created 2013-08-22T14:26:32.000000Z
  - Title: "\"Ensure that when batch jobs are created, they are created with the job bean definition id equal to the ‘stream name’\""
  - Description: "\"Unlike in spring-batch-admin, in SpringXD all the jobs the /modules/jobs directory is not ‘visible’ to query when the server starts.  Jobs only become visible to XD’s ‘jobs list’ command once they have been ‘created’.    Creating a Job in XD is an opportunity to specify additional values to any property placeholders in the job bean definition.  This isn’t part of spring-batch-admin.  We will not worry about the creation of job definition in this story.  Assume that they have been created already and that the GET for /jobs works as it does now for Spring XD.   We should however, make sure that there is always a replacement of the job name in the job bean definition to match the ‘--name’ specified in the command line.  That is “job create --name myjob --description “thisfunkyjob”  will use ‘myjob to replace <job id=\"\"${xd.stream.name}\"\" in the file thisfunkyjob.xml  *Implementation Suggestions*  This should hopefully just be a matter of changing job definition files to follow the naming pattern.  <job id=\"\"${xd.stream.name}\"\" … />  *How to verify it works*  1. Create a JUnit integration style test that has ‘job create --name myjob --defintion “testJob”’ and then deploy the job.  The"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1000** (`tawos-v1.1:2806`), created 2013-10-23T21:49:05.000000Z
  - Title: "\"User should be able to view the list of all the job definitions\""
  - Description: "\"Create a tab view with tabs “Job Definitions”, “Runtime Jobs” (Deployed Jobs?, “Job Instances” (Is Runtime Jobs a better name here?) and “Job Executions”. On clicking “Job Definitions” tab, we can have a table view of job definitions. Since we bootstrap.js, we can have a responsive table layout to list all the available job definitions. At the REST layer, “/jobs” provides the list of job definitions. We can expand the JobsController list()’s QueryOptions to add more criteria (especially to list JobDefinition’s status (Deployed/Undeployed). Also, this is the UI implementation for the shell command “job list” \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1001** (`tawos-v1.1:2805`), created 2013-10-23T22:03:13.000000Z
  - Title: "\"User should be able to view the list of all Deployed Jobs\""
  - Description: "\"On clicking the “Deployed Jobs”, we can have a table view of all the deployed jobs. This is again a responsive table layout with all the job definitions with status “deployed”. The deployed XD job corresponds to a single batch Job Instance.   This story addresses the UI layout changes to display existing JobInstance information.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1475** (`tawos-v1.1:2332`), created 2014-04-02T06:23:18.000000Z
  - Title: "\"Improve Exception handling for ZooKeeper data access\""
  - Description: "\"Currently we have many catch(Exception) blocks that simply wrap and rethrow RuntimeExceptions. We should create at least a top-level RuntimeException of our own, within the XD Exception hierarchy, and possibly a hierarchy of RuntimeExceptions extending from that, and mapping to the various checked Exceptions that can occur in ZooKeeper data access.  Also, we should not be re-wrapping those Exceptions that are already RuntimeExceptions, so we should consider a ZooKeeperExceptionHandler (and although I'm typically hesitant to recommend it, this might be a case where a static util method is the right approach). \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which cutoff-available member acceptance criteria define whether the view shows requested deployments, current placements or live module health?
- Is there two-ticket evidence of an actual topology/state visualization failure, and do planned members already handle the distinctions illustrated by the prior UI stories?

## XD-2134 (train)

Historical cutoff: 2014-09-17T16:56:24.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `1d1e14b10f15d31215102a8cff167f86de39dc4a8beded918b7a712f6d31f56d`

Source input identity SHA-256: `0a67c543af87ea1f44a642b3d0bb433abe8c16a729ae682a00978b769cb01aeb`

### Supplied historical plan

- **XD-2134** (`tawos-v1.1:1681`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2135** (`tawos-v1.1:1680`)
  - Title: null
  - Description: "As a user, I'd like to have the option to explicitly define/configure \"error channel\" so that I can stage and route the errors/exceptions through the dedicated channel and continue ingestion.\n\n*Example:*\n* 'http' source ingest \n* failure at either source, processor, or sink module\n* regardless of whether it is a custom module or not, traverse through the exception to propagate the actual _Caused by:..._, stage the error as payload, and route it to the error channel\n\n*Configuration:*\n* error channel definition similar to \"topic.errors.stream.module\"\n* configure custom exception similar to \"catch=**Exception\"\n* exception hierarchy\n** GlobalException\n** DefaultException\n** ModuleSpecificException\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2136** (`tawos-v1.1:1679`)
  - Title: "\"Restrict the use of reserved keywords\""
  - Description: "\"As a user, I should not be allowed to create a custom module with a _reserved_ keywords so that I it will avoid confusions from seeing duplicate strings in deployment manifest.  *Example:* We would like to avoid a _custom_ module name of *producer* to eliminate the confusion below: {code}  xd:>stream deploy --name test1 --properties \"\"module.producer.producer.deliveryMode= PERSISTENT,module.log.criteria=groups.contains('group1')\"\"  {code}  [List of available reserved keywords|https://github.com/spring-projects/spring-xd/wiki/Deployment#deployment-properties]\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2137** (`tawos-v1.1:1678`)
  - Title: "\"Preserve partition state on container restarts\""
  - Description: "\"As a user, I'd like to retain the data partitioning state so that when I restart the containers, I continue to write based on the original partitioning strategy.   Currently, the state is not preserved; hence, on restarts the definition of partitioning strategy is lost due to different _hashCode()_.  *Design consideration:* Mine through the container info to derive the \"\"partition index\"\" instead of relying on _hashCode()_.\""
  - Unknown fields: []
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The visible plan explicitly provides configurable error channels and root-cause propagation (XD-2135), reserved-keyword restrictions (XD-2136), and partition-state preservation on restart (XD-2137). These must not be relabelled as missing work.",
    "XD-1675 reports a missing errorChannel and XD-1586 reports deployed status despite a module failure; they motivate existing error-handling work but do not establish an additional uncovered gap in its stated source/processor/sink coverage.",
    "XD-1678 concerns reconnection to a job database, not hash-based partition assignment. XD-1601 concerns channel naming, not custom module reserved words. Combining these adjacent topics would overstate common-mechanism evidence.",
    "The root is unknown and no independent two-ticket mechanism establishes a new risk beyond the concerns already explicit in the supplied children."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1601** (`tawos-v1.1:2208`), created 2014-04-21T18:52:37.000000Z
  - Title: "\"Naming consistency for named channels\""
  - Description: "There seems to be some inconsistency with the naming strategy for the named channels.\n\nFor example:\n\nIf we create a job \"j1\", the job launching request queue name in the message broker would \"job:j1\". To send a launching request, we can either use \"queue:job:j1\" or \"job:j1\" (both seems to work).\n\nIf we create a stream with the named p2p channel \"foo\" we expect to use the syntax \"queue:foo\" and the message broker will have the queue name \"queue:foo\"\n\nThe StreamConfigParser resolves the source/sink channel names for tap to deduce the module index from the channel component: ChannelNode.resolve(StreamLookupEnvironment env)\n\nBut, in case of the named channels that have prefix \"topic:\" or \"queue:\", their names are used as is the only exception in a case where (From StreamConfigParser's eatChannelReference(boolean tapAllowed)\n \n{code:java}\n// queue:XXX\n// topic:XXX\nif (firstToken.data.equalsIgnoreCase(\"queue\")) {\n    channelType = ChannelType.QUEUE;\n}\nelse if (firstToken.data.equalsIgnoreCase(\"topic\")) {\n    channelType = ChannelType.TOPIC;\n}\n// TODO: DT not sure if this is the best way to handle\n// StreamConfigParserTests.substreamsWithSourceChannels()\nif (channelScopeComponents.size() "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1678** (`tawos-v1.1:2132`), created 2014-05-08T09:59:25.000000Z
  - Title: "\"XD does not reconnect to jobstore if connection is  lost, leaving Jobs in inconsistent state.\""
  - Description: "\"XD Deployment Description XD Cluster (1 Container) Environment EC2 Type Of Test Shell Command Line Test Failed On hdfs (only test that was run) Build Used Built May 7, 10:29 PST  [Overall issue] XD Admin and container lost connectivity to the the jobstore (MySql on RDS) and did not reconnect.   Exception Displayed in log. Caused by: com.mysql.jdbc.exceptions.jdbc4.CommunicationsException: The last packet successfully received from the server was 54,321,927 milliseconds ago.  The last packet sent successfully to the server was 54,321,928 milliseconds ago. is longer than the server configured value of 'wait_timeout'. You should consider either expiring and/or testing connection validity before use in your application, increasing the server configured values for client timeouts, or using the Connector/J connection property 'autoReconnect=true' to avoid this problem.  at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)  at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:57)  at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)  at java.lang.reflect.Constructor.newInstance(C"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: ["status", "estimate"]
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1586** (`tawos-v1.1:2223`), created 2014-04-16T14:01:09.000000Z
  - Title: "\"Stream should not be in deployed state following module failure. \""
  - Description: "\"Run singlenode. Ensure twitterstream credentials are not valid. e.g.,  no consumerKey property. This is the default state.  >stream create tweets --definition \"\"twitterstream | log\"\" --deploy Created and deployed stream 'tweets'  Meanwhile, Singlenode throws an exception, the stacktrace below   xd:>stream list   Stream Name  Stream Definition    Status   -----------  -------------------  --------   tweets       twitterstream | log  deployed  {code} 15:54:07,298 ERROR DeploymentsPathChildrenCache-0 cache.PathChildrenCache:550 - java.lang.RuntimeException: org.springframework.beans.factory.BeanDefinitionStoreException: Invalid bean definition with name 'twitterTemplate' defined in URL [file:/Users/<USER>spring-xd/spring-xd-1.0.0.M6/xd/modules/source/twitterstream/config/twitterstream.xml]: Could not resolve placeholder 'consumerKey' in string value \"\"${consumerKey}\"\"; nested exception is java.lang.IllegalArgumentException: Could not resolve placeholder 'consumerKey' in string value \"\"${consumerKey}\"\"  at org.springframework.xd.dirt.server.ContainerRegistrar.deployStreamModule(ContainerRegistrar.java:448)  at org.springframework.xd.dirt.server.ContainerRegistrar.onChildAdded(Containe"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1675** (`tawos-v1.1:2135`), created 2014-05-07T15:40:19.000000Z
  - Title: "\"FilePollHdfs is not writing results to hdfs\""
  - Description: "\"XD Deployment  Description:  XD Cluster (1 Container) Environment:  EC2 Type Of Test:  Manual Test Test Failed On  filepollhdfs (only test that was run) Build Used  Built May 7, 10:29 UTC  From the shell, attempted to create filepollhdfs however no results were written to hdfs (hadoop22).    The commands executed were the following: job create myjob --definition \"\"filepollhdfs  --names=forename,surname,address\"\" --deploy stream create mystream --definition \"\"file --dir=67fc27a6-224d-4c67-a02a-40730bcf8906 --pattern='*.out' > queue:job:myjob\"\" --deploy  No warnings nor exceptions were displayed till I changed the log4j.logger.org.springframework to INFO and restarted the container.  Then when I copied the sample file to the monitored directory the log reported: 21:30:07,605  INFO DeploymentsPathChildrenCache-0 module.ModuleDeployer:118 - deployed SimpleModule [name=file, type=source, group=mystream, index=0 @61612c7c] Exception in thread \"\"inbound.job:myjob-redis:queue-inbound-channel-adapter1\"\" org.springframework.messaging.core.DestinationResolutionException: failed to look up MessageChannel with name 'errorChannel' in the BeanFactory (and there is no HeaderChannelRegistry presen"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1912** (`tawos-v1.1:1901`), created 2014-07-02T01:06:54.000000Z
  - Title: "\"Rabbitmq source is not ingested the data into jdbc sink\""
  - Description: "\"I am using Spring XD to ingest the data into Pivotal HD.My source is log files which is coming from logstash through Rabbitmq. I could able to ingest the log files in HDFS (by using Rabbitmq source and HDFS sink) However when i try to ingest the data directly into Hawq by using JDBC sink,it's not working. Shall we directly load Rabbitmq source into any databases like Hawq?   stream create --name pivotalqueue --definition \"\"rabbit --host=<my host name>   | jdbc   --columns='colum list'\"\"      ---Not working  I configured jdbc in jdbc.properties. There was no issue with jdbc configuration(because i tested this with simple tail source it's working and load the data into HAWQ. stream create --name pivotalqueue --definition \"\"tail --name=/tmp/xd/output/test.out   | jdbc  --columns='columns list'\"\"  ) \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-701** (`tawos-v1.1:3099`), created 2013-08-15T10:05:31.000000Z
  - Title: "\"Refactor Message conversion in ChannelRegistrySupport\""
  - Description: "\"After an initial attempt which was not ready for M2 we are rethinking our strategy. One of the fundamental things we have come to realize is that its important to treat serialization and type conversion as separate concerns.  Serialization:  A core principle is the consumer should by default receive exactly what the producer sent:    -   If the producer sends a byte[] payload then no serialization is required.      -   A String payload can use simple byte conversion, taking the Charset into account    -  Transporting an Object uses whatever serialization is configured (json, xml, avro, protocol buffer, java.io, msgpack, etc.).   The actual serialization performed for each message must be shared with the producer and consumer. I.e., the consumer needs to know which case above applies to each payload. Currently we are using the MessageHeaders.CONTENT_TYPE defining custom mime types for this (The designated header is subject to change)  Conversion:     - The consumer optionally defines one or more content-types (read MimeType) it can accept in order of preference. If no conversion succeeds, we can either give them the byte[] payload or throw an exception (configurable?).  Examples:  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1228** (`tawos-v1.1:2579`), created 2014-01-14T22:07:43.000000Z
  - Title: "Provide a easy, prescriptive means to perform unit and basic stream integration tests."
  - Description: "\"AbstractSingleNodeStreamDeploymentIntegrationTests is the basis of 'state of the art' testing for a stream that allows you to get a reference to the input and output channel of the stream  http | filter | transform | file.  One can send messages to the channel after the http module, but before filter and one can retrieve the messages that were sent to the channel after the transform module but before file.  The current implementation inside AbstractSingleNodeStreamDeploymentIntegrationTests can be improved in terms of ease of use for end-users.    The issue is to create as simple a way as possible for a user to test their processing modules/stream definitions without having to actually do a real integration test by sending data to the input module.  Either as a separate issue or as part of this one, the documentation   https://github.com/spring-projects/spring-xd/wiki/Creating-a-Processor-Module  should be updated to explicitly show how to use this issue's test functionality. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1371** (`tawos-v1.1:2436`), created 2014-03-05T09:32:22.000000Z
  - Title: "Clarify API or syntax for managing deployment parameters"
  - Description: "\"Suppose we have 3 environements of Spring XD : - Dev environment  - Test environment  - Prod environement (  Suppose whe develop the script bellow: ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// stream1 = http | filter --expression=payload.contains('toto') | file --dir=/tmp/toto  stream2 = http | filter --expression=payload.contains('titi') | file --dir=/tmp/titi //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  When we need to deploy the script in Test and Prod environements , we must modify \"\"dir\"\" option of \"\"file\"\" sink. This is very easy when there is not a lot of options and when we have a small factory team. But in a big factory environment this will be problematic.   In order to industrialize deployment, it would be convenient to implement in DSL a directory interface API or something equivalent like below:  Suppose we call this directory interface XDDI ... like \"\"XD Directory Interface\"\" :-)  The script can be like that: /////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Do the existing error-routing acceptance criteria distinguish initialization failures from recoverable per-message errors and verify the stated continue-ingestion behavior?

## XD-2204 (train)

Historical cutoff: 2014-10-04T14:23:17.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `dfefc4e607bfdbd7b65b2f9181c579c423d28469af6bc4dcf0a739314d161e01`

Source input identity SHA-256: `9e816b8e44dbef1975184e67f5ec2570c0bd57db339292b48ea6b7ca5eccf837`

### Supplied historical plan

- **XD-2204** (`tawos-v1.1:1615`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2205** (`tawos-v1.1:1614`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2206** (`tawos-v1.1:1613`)
  - Title: null
  - Description: "As a user, I'd like to have a _R_ processor so that I can efficiently perform data computations and statistical analysis. \n\nInvestigate the right approach that fits Spring XD model.\n\n*References*\n[rJava|http://rforge.net/rJava/]\n[Renjin|http://www.renjin.org/]"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2206 explicitly calls for investigating an R processor approach using rJava or Renjin; runtime selection/design investigation is already planned.",
    "XD-100 discusses tuple terminology, while the source/sink, security and paging tickets concern different features; they do not provide two comparable R integration or computation failure mechanisms.",
    "The root and XD-2205 have no recoverable title/description, and the known R task does not specify a runtime choice, input representation or deployment contract from which to infer a compatibility gap."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-154** (`tawos-v1.1:3629`), created 2013-05-30T08:32:20.000000Z
  - Title: "\"Provided console output of started server\""
  - Description: "Shouldn't we have something like a ContextRefreshedEvent Listener and output some informational messages to the console, so the user knows the Container is up (Which contexts. Maybe even print a link to the docs))? Maybe even some simple ascii art (for demos)? Right now it looks somewhat barren.\n\nRedis provides something similar.\n\nThis may even go hand in hand to provided a better configuration model (storing common config parameters centrally)\n\n\n{code}\n   _____            _              __   _______  \n  / ____|          (_)             \\ \\ / /  __ \\ \n | (___  _ __  _ __ _ _ __   __ _   \\ V /| |  | |\n  \\___ \\| '_ \\| '__| | '_ \\ / _` |   > < | |  | |\n  ____) | |_) | |  | | | | | (_| |  / . \\| |__| |\n |_____/| .__/|_|  |_|_| |_|\\__, | /_/ \\_\\_____/ \n        | |                  __/ |               \n        |_|  v1.0.0.M1      |___/   eXtreme Data\n\nUsing Redis at localhost:6379    \nThe Server (PID: 12345) is now ready on http://myserver:123/streams\n\nDocumentation: https://github.com/SpringSource/spring-xd/wiki\n       \n{code}"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\n*Scope of this spike:*\n\n* Research Spring Security and Spring Boot and the OOTB features \n* Design considerations and approach for XD\n* Developer experience\n** How users will be configuring security credentials?\n** How DSL shell will be handled?\n** How Admin UI will be handled?"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2044** (`tawos-v1.1:1770`), created 2014-07-31T13:31:21.000000Z
  - Title: "Add SFTP source"
  - Description: "As a user, I'd like to have the option to use the _SFTP_ source module so that I can access, transfer, and mange files over any reliable data streams.\n\n*Reference:*\n[Spring Integration SFTP Adapter|http://docs.spring.io/spring-integration/reference/html/sftp.html]\n\nNeed to consider the infrastructure for testing."
  - Unknown fields: ["estimate"]
  - Truncated fields: []
- **XD-1864** (`tawos-v1.1:1948`), created 2014-06-19T12:02:56.000000Z
  - Title: "Add paging support for UI list views"
  - Description: "As a user, I'd like to have _paging_ support so that I can scroll through the list of streams, jobs and containers. \n\nCurrently the following error is thrown when we cross >20 rows:\n\nhttp://localhost:9393/jobs/definitions.json\n\nJSON Response:\n{code:xml}\n[\n\t{\n\t\tlinks: [ ],\n\t\tlogref: \"IllegalStateException\",\n\t\tmessage: \"Not all instances were looked at\"\n\t}\n]\n{code}\n\nStack trace:\n{code}\n15:51:21,931 ERROR http-nio-9393-exec-9 rest.RestControllerAdvice - Caught exception while handling a request\njava.lang.IllegalStateException: Not all instances were looked at\n\tat org.springframework.util.Assert.state(Assert.java:385)\n{code}"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2119** (`tawos-v1.1:1696`), created 2014-09-16T12:25:06.000000Z
  - Title: "Support accessing admin server endpoints over HTTPS"
  - Description: "As a user, I'd like to have the option to enable HTTPS so that I can access XD's Admin server [endpoints|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] over secured communication.\n\nTechnical Implementation:\n\nThis functionality is available in Spring Boot 1.2.0 M1 and has been backported into the 1.1.x branch to be released under Spring 1.1.7.  We can test against 1.1.7 SNAPSHOT.\n\nWorking through the way to update the build file to pick up a new version of boot is a bit tricky :("
  - Unknown fields: []
  - Truncated fields: []
- **XD-2120** (`tawos-v1.1:1695`), created 2014-09-16T12:34:08.000000Z
  - Title: "Secure all endpoints using file based security configurations"
  - Description: "As a user, I'd like to have the option to provide file based security configurations so that I can access the endpoints in a secured manner.\n\nIdeally, all the listed *endpoints* (http://localhost:9393/) needs to be encapsulated within file based security layer.\n\nReference:\n[Securing Web App|https://spring.io/guides/gs/securing-web/]"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-2124** (`tawos-v1.1:1691`), created 2014-09-16T15:58:15.000000Z
  - Title: "Provide a Sqoop 'tasklet' for mass data ingest"
  - Description: "As a user, I'd like to have the ability to mass-ingest data from various database systems so that I'm not restricted with the current approach (_jdbchdfs_) that is dependent on JDBC drivers. \n\n"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-2127** (`tawos-v1.1:1688`), created 2014-09-16T16:16:47.000000Z
  - Title: "\"Add JMX source\""
  - Description: "As a user, I'd like to have the option of _JMX_ source module so that I can publish/subscribe to JMX notifications.\n\n*Reference:*\n[Sprint Integration JMX Support|http://docs.spring.io/spring-integration/reference/html/system-management-chapter.html#jmx]"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2135** (`tawos-v1.1:1680`), created 2014-09-16T17:03:53.000000Z
  - Title: null
  - Description: "As a user, I'd like to have the option to explicitly define/configure \"error channel\" so that I can stage and route the errors/exceptions through the dedicated channel and continue ingestion.\n\n*Example:*\n* 'http' source ingest \n* failure at either source, processor, or sink module\n* regardless of whether it is a custom module or not, traverse through the exception to propagate the actual _Caused by:..._, stage the error as payload, and route it to the error channel\n\n*Configuration:*\n* error channel definition similar to \"topic.errors.stream.module\"\n* configure custom exception similar to \"catch=**Exception\"\n* exception hierarchy\n** GlobalException\n** DefaultException\n** ModuleSpecificException\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []

### Unresolved labelling questions

- What input/output data representation and computation semantics are expected for the R processor?
- What historical criteria distinguish the rJava and Renjin approaches in XD-2206?
- Did XD-2205 cover R runtime integration or tests, and can its cutoff-bound text be recovered?

## XD-2252 (train)

Historical cutoff: 2014-10-17T17:02:35.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `74164fda6298bc9b6849435cb8565c11e591cf92431e357ce118548e33968e84`

Source input identity SHA-256: `35ea50ef7f8eea4f714bacf33a1a36b70e6efa56f7a769dd09a2fbd409a40c8f`

### Supplied historical plan

- **XD-2252** (`tawos-v1.1:1568`)
  - Title: "Measure baseline performance of RabbitMQ using PerfTest (Distributed)"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-2253** (`tawos-v1.1:1567`)
  - Title: null
  - Description: "Using the [iperf tool|https://iperf.fr/], find out the transfer rate in MB/sec between three machines in a four machine configuration.\n\n*Topology to consider:*\ngenerator -> xd source -> broker -> xd sink \n\nFor each arrow, measure the transfer rate between the two machines on each side."
  - Unknown fields: ["title", "type"]
  - Truncated fields: []
- **XD-2254** (`tawos-v1.1:1566`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-2255** (`tawos-v1.1:1565`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-2256** (`tawos-v1.1:1564`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-2257** (`tawos-v1.1:1563`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2253 explicitly measures network transfer rates for every edge in the four-machine topology. A warning that the plan lacks network baseline work would contradict this member.",
    "XD-1870 and XD-1602 show XD Rabbit/JMS module configuration selecting unintended brokers, but the supplied plan does not show that standalone Rabbit PerfTest or iperf uses those module configuration paths.",
    "The scope of XD-2254 through XD-2257 is unknown. Prior Redis initialization, ZooKeeper recovery and Rabbit-to-JDBC failures do not jointly establish a failure in the planned raw RabbitMQ baseline measurements."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1912** (`tawos-v1.1:1901`), created 2014-07-02T01:06:54.000000Z
  - Title: "\"Rabbitmq source is not ingested the data into jdbc sink\""
  - Description: "\"I am using Spring XD to ingest the data into Pivotal HD.My source is log files which is coming from logstash through Rabbitmq. I could able to ingest the log files in HDFS (by using Rabbitmq source and HDFS sink) However when i try to ingest the data directly into Hawq by using JDBC sink,it's not working. Shall we directly load Rabbitmq source into any databases like Hawq?   stream create --name pivotalqueue --definition \"\"rabbit --host=<my host name>   | jdbc   --columns='colum list'\"\"      ---Not working  I configured jdbc in jdbc.properties. There was no issue with jdbc configuration(because i tested this with simple tail source it's working and load the data into HAWQ. stream create --name pivotalqueue --definition \"\"tail --name=/tmp/xd/output/test.out   | jdbc  --columns='columns list'\"\"  ) \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-799** (`tawos-v1.1:3001`), created 2013-09-02T23:31:17.000000Z
  - Title: "\"Change rabbitmq sink to use routing-key-expression instead of routing-key\""
  - Description: "\"The current rabbitmq sink uses the attribute routing-key, which defaults to the name of the stream.  This should be change to use the attribute routing-key-expression so that the routing-key can be determined using SpEL.  This will enable a dynamic evaluation of the routing-key based on message payload/header.  *Implementation Suggestions*  This hopefully should be changing the XML description of the sink to     routing-key-expression=\"\"${routingKey:'${xd.stream.name}'}  This way, the ${xd.stream.name} is surrounded by a single quote to indicate a string literal to SpEL in the default case.    *How to verify it works.*  One of the simple uses of this is to create a routing key based on payload.  In a distributed word-count example, the hashcode of a word would be sent to a certain number of processing modules that would perform the count. The idea is that the same word is sent to the same node over and over again, in particular if in-memory counters or state is computed - using centralized redis counters this wouldn't be necessary in the case of only counter state.  The stream   http | rabbit --routingKey=\"\"'word-' + payload.hashCode() % 3\"\"  is an example of a stream that can be "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1322** (`tawos-v1.1:2485`), created 2014-02-13T11:47:07.000000Z
  - Title: "Add way to provide module config options for XD on YARN"
  - Description: "There seems to be some intersection with the work for this issue and the rationalization of how module properties are handled.  There will be changes to configuration/property management support such that each module (source, sink, etc) will be able to also be overridden in spring-xd.yml (or wherever -Dspring.config.location points to.  The HDFS sink module for example, will have default values based on it's OptionsMetadata and will be of the form <type>.<module>.<option>\n\n\nThat means in the configuration for hdfs.xml sink, there would be a config section such as\n\n{code:xml}\n    <configuration>\n      fs.default.name=${sink.hdfs.hd.fs}\n      mapred.job.tracker=${sink.hdfs.hd.jt}\n      yarn.resourcemanager.address=${sink.hdfs.hd.rm}\n      mapreduce.framework.name=${sink.hdfs.mr.fw}\n    </configuration>\n{code}\n\nWith default values defined by a HdfsSinkOptionsMetadata class.  The hdfs.xml module file would not contain any references to a properties file.\n\nA file specified by -Dspring.config.location could override the values in a config section such as\n\nsink:\n  hdfs:\n    hd.fs : hdfs://foobarhost:8020\n    hd.jt : 10.123.123.123:9000\n\netc.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1602** (`tawos-v1.1:2207`), created 2014-04-22T07:53:03.000000Z
  - Title: "\"JMS Source on EC2 only uses localhost for activemq broker\""
  - Description: "\"[Problem] On a EC2 container jms-activemq.properties was configured to use a activemq broker on a different host, it still referred to localhost.   On my local mac, I was able to updated the jms-activemq.properties with an activemq on a different host and it worked.  [work-around] While not recommended you can set the amq.url in the jms-activemq-infrastructure-context.xml.  [Steps to reproduce] 1) Deploy a single admin/container using xd-ec2.   2) create a jms-activemq.properties file in the spring-xd-1.0.0.BUILD-SNAPSHOT/xd/ where it refers to a broker on another machine (ec2-54-221-32-82.compute-1.amazonaws.com).   3) Create a stream with JMS as its source.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1636** (`tawos-v1.1:2173`), created 2014-04-25T12:30:50.000000Z
  - Title: "\"servers.yaml's 'xd: -> transport: rabbit' overrides xd-singlenode's default of local transport\""
  - Description: "\"When working w/ SXD xd-singlenode, out of the box, it defaults to using all embedded components (transport, analytics, hsqldb, & zookeeper), which is easy and a great way to get going.  This is also great for development.  When I then started trying out the M6 distributed mode I set my transport to rabbit in servers.yaml (now that the --transport option is gone).  Rabbit is my preferred transport here.  I then went back to running the singlenode, for simplicity, and then got an exception saying that the singlenode couldn't contact RabbitMQ/AMQP (I was no longer running rabbit).  I then had to add the '--transport local' flag back to xd-singlenode.    Having the --transport option on xd-singlenode but not on xd-container is confusing.  Also I would expect xd-singlenode to default to local transport unless I specify another option in --transport.  -Derek\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1860** (`tawos-v1.1:1952`), created 2014-06-17T12:12:19.000000Z
  - Title: "\"Support for configuring more than one broker in rabbit source\""
  - Description: "\"Spring XD rabbit source supports these options  http://docs.spring.io/spring-xd/docs/1.0.0.BUILD-SNAPSHOT/reference/html/#rabbit  However, if there are multiple brokers available for a client to connect to then there is no way to configure that when creating a stream. I believe there is support for this already in the rabbitmq client (addresses field if I remember right from the meeting) but it needs to be exposed as one of the options in defining a stream with rabbitmq source. This way if one of the brokers die the client can automatically switch to one of the other configured brokers and provide high availability on the client side. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1870** (`tawos-v1.1:1942`), created 2014-06-20T15:18:32.000000Z
  - Title: "Rabbit Sink & Source --host and --port are not updating module host/port."
  - Description: "Acceptance Tests failed on the Rabbit Source and Sink Tests.  The test started failing when XD-1824 was introduced (Support RabbitMQ Cluster in source/sink).  This story added addresses to support rabbit cluster failover.  \nCurrently if a user set --host --port to a remote Rabbit instance, XD will use the default host=localhost and port=5672.  However using --addresses does work.  "
  - Unknown fields: []
  - Truncated fields: []
- **XD-2080** (`tawos-v1.1:1735`), created 2014-08-18T12:29:40.000000Z
  - Title: "\"Modules do not redeploy properly when Zookeeper node is lost.\""
  - Description: "* SHA baddfc24b08286a78392d5f565742c9bab5adfea\n* EC2 Environment\n** Look at Zookeeper Ec2 Deployment Test Topology.png for a view of the topology\n\nh2. The test scenario \n# Bring up a up a 5 container 2 admin XD Cluster up using 3 ZK Server ensemble.\n# Create ticktock  stream \"time|log\"\n# Deploy with --properties \"module.log.count=5\"\n# Kill one of the ZK Servers in the ensemble\n\nh2. Observed Behavior. \n# In this particular scenario 3 containers were affected by killing (sudo kill <pid>) Zookeeper 2\n# 2 Containers did not come back online even though they did show up in the runtime containers\n \nh2. Timeline\n# 14:08:21 deployed stream\n# 14:09:10 kill server in ZK Ensemble\n# After waiting a few seconds ran runtime Modules (*Note:* log2 is undeployed and log5 is then deployed)  :\n\nxd:>runtime modules\n  Module             Container Id                          Options                                     Deployment Properties\n  -----------------  ------------------------------------  ------------------------------------------  ---------------------\n  foo.sink.log.1     98a32c62-302a-484b-af9c-d670f2a3cfc2  {name=foo, expression=payload, level=INFO}  {count=5, sequence=1}\n  foo.sink.log.2  "
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-716** (`tawos-v1.1:3084`), created 2013-08-19T19:54:19.000000Z
  - Title: "\"TapCommandTests hangs when using a lazily instantiated Lettuce connection\""
  - Description: "\"A change was made in spring-data-redis to instantiate the shared Lettuce connection lazily instead of when the context is initialized. This caused TapCommandTests to hang due to a Netty worker thread trying to initialize the Lettuce connection (Lettuce uses Netty). The change was temporarily backed out of SDR, but we need to consider using a NettyExecutionHandler in NettyHttpInboundChannelAdapter or making the HTTP module's \"\"input\"\" channel an ExecutorChannel to avoid potentially long operations like from happening in an I/O thread.  Also, we need to address why this failure simply hangs the shell. Shell was hung waiting on IO here:  at org.springframework.http.client.SimpleClientHttpResponse.getRawStatusCode(SimpleClientHttpResponse.java:47)  at org.springframework.http.client.AbstractClientHttpResponse.getStatusCode(AbstractClientHttpResponse.java:32)  at org.springframework.xd.shell.command.HttpCommands$1.hasError(HttpCommands.java:93)  at org.springframework.web.client.RestTemplate.doExecute(RestTemplate.java:484)  at org.springframework.web.client.RestTemplate.execute(RestTemplate.java:460)  at org.springframework.web.client.RestTemplate.postForEntity(RestTemplate.java:335) "
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What cutoff-valid definitions of XD-2254 through XD-2257 identify the actual PerfTest client settings and measurement-validation process?
- Are any proposed measurements driven through XD modules rather than standalone PerfTest or iperf, and if so which source/sink options do they use?

## XD-2263 (train)

Historical cutoff: 2014-10-21T11:47:01.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `b85f6b980602e09e27a0f3e2246f7503e864553e429f7b876f6a5a61e01e9f1b`

Source input identity SHA-256: `2ee5d4ac06b01be9380cfb72f900da0a7db35c629c9c8ce40be119b7d36fad58`

### Supplied historical plan

- **XD-2263** (`tawos-v1.1:1557`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2264** (`tawos-v1.1:1556`)
  - Title: "Infrastructure for RabbitMQ Cluster (ECB)"
  - Description: "Pre-requisite for Rabbit MQ Benchmarks:\n\n* Infrastructure setup\n* Configuration changes\n* Tool-chain setup"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-2265** (`tawos-v1.1:1555`)
  - Title: "Vary consumers size (ECB-4)"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-2266** (`tawos-v1.1:1554`)
  - Title: "Vary producers size (ECB-5)"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2264 explicitly includes RabbitMQ cluster infrastructure, configuration changes and tool-chain setup, while XD-2265 and XD-2266 vary consumers and producers. These tasks are not missing from the supplied plan.",
    "XD-2084, XD-978 and XD-1342 provide completed deployment/configuration precedents rather than two demonstrated failures in RabbitMQ benchmark execution.",
    "XD-1793 documents stale XD job/stream state after a permission failure; XD-1495 concerns ZooKeeper runtime metadata and XD-1683 concerns Redis input handling. The supplied text does not establish that the benchmark clients use these failing paths.",
    "The root scope and benchmark acceptance details are unknown; this does not establish incorrect measurements or an unfulfilled prerequisite."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2084** (`tawos-v1.1:1731`), created 2014-08-21T09:06:19.000000Z
  - Title: "\"Spring XD EC2 needs to setup cluster that uses static resources.\""
  - Description: "h1. Summary \nUser wants the ability to deploy an ec2 cluster where the admin & containers use a pre existing ZK ensemble, Rabbit and redis instance that are deployed on different machines. \n\nh2. Current functionality\nCurrently spring-xd-ec2 sets up its containers & admin server to use a ZK, rabbit and redis that are provisioned and collocated with the admin server.  \n\nh2. Detail\nThe following properties will be added to the spring-xd-ec2.properties\n# *spring_zk_client_connect* - contains a comma delimited list of zk hosts:ports for a ensemble.  The application will check to see if the port is open on at least of the servers in the list, if not deployment will fail.  Default is adminServer_host:2181.\n# *spring_rabbitmq_addresses* - contains a comma delimited list of hosts:ports for a rabbit cluster.  The application will check to see if the port is open on at least of the servers in the list, if not deployment will fail.  Default is adminServer_host:5672.\n# *spring_redis* - contains a host:port for a redis instance. The application will check to see if the port is open , if not deployment will fail.  Default is adminServer_host:5672.\n# *ec2_zone* - user can specify the zone to which"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1707** (`tawos-v1.1:2103`), created 2014-05-14T08:55:46.000000Z
  - Title: "\"The Dynamic Router example in the docs throws an exception with Rabbit Transport\""
  - Description: "\"The example in the M6 documentation for the Dynamic Router (here: http://docs.spring.io/spring-xd/docs/1.0.0.M6/reference/html/#dynamic-router) for the SpEL-Based Routing throws an exception when processing the message (from the HTTP post) saying \"\"No bean named 'queue:foo' is defined\"\", when using RabbitMQ as the transport.  I do not know a workaround.  Steps to reproduce: 1) Run RabbitMQ locally 2) Run xd-singlenode --transport rabbit 3) xd:>stream create f --definition \"\"queue:foo > transform --expression=payload+'-foo' | log\"\" --deploy  xd:>stream create b --definition \"\"queue:bar > transform --expression=payload+'-bar' | log\"\" --deploy  xd:>stream create r --definition \"\"http | router --expression=payload.contains('a')?'queue:foo':'queue:bar'\"\" --deploy  4) xd:>http post --data \"\"a\"\"  5) This should give a stacktrace: Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No bean named 'queue:foo' is defined  at org.springframework.beans.factory.support.DefaultListableBeanFactory.getBeanDefinition(DefaultListableBeanFactory.java:641)  at org.springframework.beans.factory.support.AbstractBeanFactory.getMergedLocalBeanDefinition(AbstractBeanFactory.java:115"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1793** (`tawos-v1.1:2018`), created 2014-06-02T10:03:42.000000Z
  - Title: "Jobs  are not completely removed from Jobstore "
  - Description: "\"Deploy Type: Admin/Container on EC2 (Rabbit Transport) SHA: 8fba31d  [Steps to reproduce] 1) Using Rabbit 3.3 above create a user that does not have privileges to write to / * sudo rabbitmqctl add_user joe password * (omit this step) sudo rabbitmqctl set_permissions -p / joe \"\".*\"\" \"\".*\"\" \"\".*\"\" 2) Set the rabbitmq user name and password * export spring_rabbitmq_username=acctest * export spring_rabbitmq_password=acctest23 3) Start container. 4) Create stream or job \"\"foo\"\" 5) Error will occur 6) delete stream or job \"\"foo\"\" 7)  stop container 8) set privilege * sudo rabbitmqctl set_permissions -p / joe \"\".*\"\" \"\".*\"\" \"\".*\"\" 9) Start container 10) create stream or job \"\"foo\"\" 11)  System will report that foo exists.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-306** (`tawos-v1.1:3482`), created 2013-06-24T14:10:49.000000Z
  - Title: "\"User wants ability to test sources\""
  - Description: "Examples:\n1. Be able to start the rabbitmq source just by pointing to modules/source/rabbit.xml, pass in some property file for parameters to be replaced, and outgoing message is placed in a in-memory queue backed channel for use with assertions to verify functionality.  \n2. Test for as many source types as is 'reasonable', e.g. MQTT/TCP testing might be harder than say rabbitmq.\n3. Test that sending json, results in media-type header is set to json\n4. Test that sending POJO,   \"  POJO\n5. Test that sending Tuple, \"   Tuple\n6. Test that sending raw bytes, \" raw bytes\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-978** (`tawos-v1.1:2828`), created 2013-10-21T15:21:31.000000Z
  - Title: "\"Installer needs to launch a single node XD instance\""
  - Description: "\"* Create a Deployer class has methods ** RunningInstance  deploySingleNode *** takes into account machine size as specified in properties file ** void  destroyAllInstances()   *** or whatever JClouds returns from the destroy call ** ctor gets passed in the root boostrapping credentials. * Install Script Steps ** Setup XD_HOME variable ** Make sure privileges are set to ubuntu not root. ** start up redis and rabbit using ports as specified in xd-ec2.properties ** Use port watch to make sure they started ** Start singlenode after configuration. ** Display hostname of singlenode server ** Report successful and failed startup ** Hit root of xd-admin to see if there is a response on 9393 * Integration Testing ** Verify that config files have been setup ** Verify XD has been started ** Verify XD can process a basic http post  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1190** (`tawos-v1.1:2617`), created 2013-12-27T07:20:33.000000Z
  - Title: "\"Setup precedence order for module properties' property resolver\""
  - Description: "\"The PropertyResolver needs to follow the below precedence order on PropertySources when resolving the module properties:  From lowest to the highest order,  0 application.yml 1 applicaiton.yml fragment 2 property placeholders 2a  property placeholder under 'shared' config directory  2b property placeholder under module/(source/sink/processor)/config directory 3. environment variables 4. system properties 5. command line   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1310** (`tawos-v1.1:2497`), created 2014-02-12T07:56:21.000000Z
  - Title: "\"Misleading error message when trying to restart a job exec\""
  - Description: "\"Disregard the missing date that is caused by another problem. Here is the setup: {noformat} xd:>job execution list   Id  Job Name  Start Time                        Step Execution Count  Status   --  --------  --------------------------------  --------------------  ---------   13  foo         Europe/Paris                    0                     STARTING   12  foo       2014-02-12 15:39:46 Europe/Paris  1                     FAILED   11  foo       2014-02-12 15:39:29 Europe/Paris  1                     COMPLETED   10  foo       2014-02-12 15:38:36 Europe/Paris  1                     COMPLETED   9   foo       2014-02-12 15:38:21 Europe/Paris  1                     COMPLETED   8   foo         Europe/Paris                    0                     STARTING   7   foo       2014-02-12 15:25:41 Europe/Paris  1                     COMPLETED   6   foo       2014-02-12 15:25:04 Europe/Paris  1                     FAILED   5   foo       2014-02-12 15:14:32 Europe/Paris  1                     FAILED   4   foo       2014-02-12 15:14:13 Europe/Paris  1                     FAILED   3   foo       2014-02-12 15:13:54 Europe/Paris  1                     FAILED   2   foo       2014-02-12 15:13:18 Eu"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1342** (`tawos-v1.1:2465`), created 2014-02-21T18:04:43.000000Z
  - Title: "\"Configuration for RabbitMQ message bus concurrent consumers\""
  - Description: "\"By having the configuration option for concurrent consumers would help improve the performance of message consumption by the consumer modules when the ordering of the incoming messages don't matter.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1495** (`tawos-v1.1:2312`), created 2014-04-06T20:02:07.000000Z
  - Title: "\"xd:>runtime modules gives error from CLI\""
  - Description: "\"xd:>runtime modules Command failed org.springframework.xd.rest.client.impl.SpringXDException: java.lang.RuntimeException: org.apache.zookeeper.KeeperException$NoNodeException: KeeperErrorCode = NoNode for /xd/deployments/modules/4dc55d87-125b-4e4a-a76e-82bb6980820d/TickTock.sink.log-1/metadata  This is on OSX running in distributed mode with --transport rabbit --hadoopDistro hadoop22, redis 2.8.8, rabbit 3.2.3, hadoop 2.2.0, and zookeeper 3.4.5.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1566** (`tawos-v1.1:2242`), created 2014-04-12T10:12:09.000000Z
  - Title: "Document append configuration, else jdbchdfs writes empty file to hdfs"
  - Description: "\"Similar to XD-1565  so I'd link these 2 together.  [Steps to reproduce on Hadoop12] 1) Created Table People with columns forename,surname and address (use the result from filejdbc) 2) job create myjob --definition \"\"jdbchdfs --sql='select col1,col2,col3 from some_table'\"\" 3)job launch myjob 4) myjob is created on hdfs but with zero bytes 5) throws an exception, stack trace attached.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1683** (`tawos-v1.1:2127`), created 2014-05-09T15:51:29.000000Z
  - Title: "\"syslog-tcp throws exception when receiving syslog data\""
  - Description: "\"XD Deployment  Description XD Cluster (1 Container) Environment EC2 Type Of Test Manual test via shell Test Failed On syslog-tcp (only test that was run) Build Used Built May 7, 10:29 UTC  [Setting up the Environment] * Used the wiki instructions to setup the syslog on the ec2 instance.  * Deploy the stream below: stream create mystream --definition \"\"syslog-tcp | file --binary=true --mode=REPLACE\"\" --deploy  * On the EC2 Instance execute the line below: logger -p local3.info -t TESTING \"\"Test Syslog Message\"\"  [What occurred] Stream fails to process inbound syslog information and throws the exception below:   Exception in thread \"\"inbound.mystream.0-redis:queue-inbound-channel-adapter17\"\" org.springframework.messaging.core.DestinationResolutionException: failed to look up MessageChannel with name 'errorChannel' in the BeanFactory (and there is no HeaderChannelRegistry present).  at org.springframework.integration.support.channel.BeanFactoryChannelResolver.resolveDestination(BeanFactoryChannelResolver.java:108)  at org.springframework.integration.support.channel.BeanFactoryChannelResolver.resolveDestination(BeanFactoryChannelResolver.java:44)  at org.springframework.integration.ch"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Are these raw RabbitMQ client benchmarks or XD stream benchmarks, and which cutoff-available acceptance criteria verify the measured environment?
- Is there two-ticket evidence of a specific benchmark/configuration failure after accounting for the infrastructure and configuration work already in XD-2264?

## XD-2267 (train)

Historical cutoff: 2014-10-22T15:17:09.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `efb0b50c193bb07f9aedefcc1adcea89d19bca592591b4b2c7872672da24fc0e`

Source input identity SHA-256: `64fe25cef730f7d8f4b80b961aef211e42403d53989c1dc57b22b3ba7ed9ab7f`

### Supplied historical plan

- **XD-2267** (`tawos-v1.1:1553`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2268** (`tawos-v1.1:1552`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "Neither XD-2267 nor its supplied member XD-2268 has a known historical title or description, so no intended technical behavior can be identified from this input.",
    "No prior tickets were supplied by lexical retrieval, despite 1,963 eligible prior items being reported. A two-ticket-supported risk cannot be constructed from the supplied evidence.",
    "XD-2268 being In Progress does not establish that the plan is blocked, delayed or missing work; this empty target reflects unavailable support rather than verified safety."
  ]
}
```

### Supplied prior evidence for support and counterexample review


### Unresolved labelling questions

- Can any title or description for XD-2267/XD-2268 be recovered from a source demonstrably available at this cutoff?
- After recovering scope, which prior evidence available at the same cutoff should be supplied for review?

## XD-2292 (train)

Historical cutoff: 2014-10-30T16:08:27.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `d9467c25166441b5a7301c4d8c699dd2b94bec38c8569e72f8a98033de74af56`

Source input identity SHA-256: `bf62ee0f8fb8cbca940e6f28f5daaccb5bbe4e19c0289491319079113f914999`

### Supplied historical plan

- **XD-2292** (`tawos-v1.1:1528`)
  - Title: "Support for message brokers"
  - Description: null
  - Unknown fields: ["description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2098** (`tawos-v1.1:1717`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-2293** (`tawos-v1.1:1527`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The root only states support for message brokers, and both observed members have unknown titles/descriptions; the supplied plan does not identify brokers, versions or whether the work changes source/sink adapters or the internal MessageBus.",
    "XD-1564 documents Rabbit routing-expression failure and XD-1291 documents Redis shutdown ordering, but both are Done and no supplied plan text ties a proposed change to either mechanism.",
    "XD-162 explicitly placed transport-independent conversion in shared channel-registry logic, providing counterevidence to a blanket claim that message conversion is absent."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1100** (`tawos-v1.1:2707`), created 2013-11-19T08:53:37.000000Z
  - Title: "\"Create aggregator module that uses redis as a message store\""
  - Description: "\"There is a need for a persistent store for messages so that they can survive the crash of a container node.  The redis implementation in SI is useful since users may already be using redis for other features such as analytics.  This module would sit alongside the current in-memory based aggregator.  It brings in redis as a dependency and there should be configuration options exposed so that one can use a different version of redis as compared to the one that maybe used for analytics.    Due to the need to have redis on the CP, and the large number of different options that each message store implementation provides and the different 3rd party library dependencies, I would like to avoid going down the path of using a profile here as it would seem to go beyond what we had discussed for profile support.  We can revisit as the module contribution story based on boot unfolds.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1291** (`tawos-v1.1:2516`), created 2014-01-31T14:53:24.000000Z
  - Title: "Handle container shutdown gracefully"
  - Description: "\"Currently, ModuleDeployer is a disposable bean. When the container context is closed, the ModuleDeployer bean is destroyed along with its associated common context and deployed modules. Issue arises, if the connectionfactory bean associated with the deployed modules' message bus bindings  is destroyed before the ModuleDeployer bean, there is exception stacktrace (at least in case of Redis MessageBus) saying \"\"Connection closed\"\".   Adding SmartLifecycle support to ModuleDeployer will make sure all the beans are destroyed during Lifecycle processor's stop() method before any of the singletonbeans are destroyed.  The stacktrace (when using Redis MessageBus is):  org.springframework.data.redis.RedisSystemException: Redis exception; nested exception is com.lambdaworks.redis.RedisException: Connection closed at org.springframework.data.redis.connection.lettuce.LettuceExceptionConverter.convert(LettuceExceptionConverter.java:45) at org.springframework.data.redis.connection.lettuce.LettuceExceptionConverter.convert(LettuceExceptionConverter.java:35) at org.springframework.data.redis.connection.lettuce.LettuceConverters.toDataAccessException(LettuceConverters.java:158) at org.springframew"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1295** (`tawos-v1.1:2512`), created 2014-02-10T00:54:04.000000Z
  - Title: "\"Module message conversion fails to work if JMX is enabled\""
  - Description: "\"If JMX is enabled for modules (enabling the IntegrationMBeanExporter), the ModuleTypeConversionPlugin fails to get the reference to input/output channel (for adding the ContentTypeHeaderInterceptor) and results in exception.  It seems like the IntegrationMBeanExporter (when JMX is enabled) creates JdkDynamicAopProxy for all the integration components and thereby the following check on ModuleTypeConversionPlugin to retrieve the AbstractMessageChannel fails.  AbstractMessageChannel channel = null;    if (isInput) {     channel = module.getComponent(\"\"input\"\", AbstractMessageChannel.class);    }    else {     channel = module.getComponent(\"\"output\"\", AbstractMessageChannel.class);    }  I see the reason why AbstractMessageChannel is used here (to use some of the methods in the implementing class that didn't exist in the interfaces) but IntegrationMBeanExporter creating JdkDynamicAopProxy for the channel fails to resolve as AbstractMessageChannel here.  Following is the full stack trace:  To replicate,  stream create testing --definition \"\"\"\"http --outputType=text/plain | log\"\" 3:45,238 ERROR redisInboundAdapter-redis:queue-inbound-channel-adapter1 handler.LoggingHandler:145 - org.spr"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1310** (`tawos-v1.1:2497`), created 2014-02-12T07:56:21.000000Z
  - Title: "\"Misleading error message when trying to restart a job exec\""
  - Description: "\"Disregard the missing date that is caused by another problem. Here is the setup: {noformat} xd:>job execution list   Id  Job Name  Start Time                        Step Execution Count  Status   --  --------  --------------------------------  --------------------  ---------   13  foo         Europe/Paris                    0                     STARTING   12  foo       2014-02-12 15:39:46 Europe/Paris  1                     FAILED   11  foo       2014-02-12 15:39:29 Europe/Paris  1                     COMPLETED   10  foo       2014-02-12 15:38:36 Europe/Paris  1                     COMPLETED   9   foo       2014-02-12 15:38:21 Europe/Paris  1                     COMPLETED   8   foo         Europe/Paris                    0                     STARTING   7   foo       2014-02-12 15:25:41 Europe/Paris  1                     COMPLETED   6   foo       2014-02-12 15:25:04 Europe/Paris  1                     FAILED   5   foo       2014-02-12 15:14:32 Europe/Paris  1                     FAILED   4   foo       2014-02-12 15:14:13 Europe/Paris  1                     FAILED   3   foo       2014-02-12 15:13:54 Europe/Paris  1                     FAILED   2   foo       2014-02-12 15:13:18 Eu"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1338** (`tawos-v1.1:2469`), created 2014-02-20T10:14:16.000000Z
  - Title: "Deployment manifest to support partitioning a stream"
  - Description: "\"We need a methodology for providing partitioning hints.  A current proposal uses message headers to provide:  * partition_key – the item to partition on * destination_region – what to target  In the proposal the developer used \"\"partition_key\"\" to route the stream message to the node where data was stored in process.  This was done so downstream stream operations could work on the data with out suffering any network IO.  The \"\"destination_region\"\" was used to target the type of data the downstream streams were going to use in their stream processing.   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1361** (`tawos-v1.1:2446`), created 2014-03-02T07:08:12.000000Z
  - Title: "\"Classpath issue with homebrew version on MacOSX 10.9.1\""
  - Description: "I've installed spring xd for the first time today on my mac, using the homebrew distribution.\n\nI tried to create the following stream :\n\n{{xd> stream create --definition \"http --port=6666 | log\" --name httptest}}\n\nThis produced the following error : \n\norg.springframework.integration.MessageHandlingException: error occurred in message handler [moduleDeployer]\n\tat org.springframework.integration.handler.AbstractMessageHandler.handleMessage(AbstractMessageHandler.java:79)\n\tat org.springframework.integration.config.ServiceActivatorFactoryBean$1.handleRequestMessage(ServiceActivatorFactoryBean.java:83)\n\tat org.springframework.integration.handler.AbstractReplyProducingMessageHandler.handleMessageInternal(AbstractReplyProducingMessageHandler.java:142)\n\tat org.springframework.integration.handler.AbstractMessageHandler.handleMessage(AbstractMessageHandler.java:73)\n\tat org.springframework.integration.dispatcher.UnicastingDispatcher.doDispatch(UnicastingDispatcher.java:115)\n\tat org.springframework.integration.dispatcher.UnicastingDispatcher.dispatch(UnicastingDispatcher.java:102)\n\tat org.springframework.integration.channel.AbstractSubscribableChannel.doSend(AbstractSubscribableChannel.java:77"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1418** (`tawos-v1.1:2389`), created 2014-03-19T03:37:45.000000Z
  - Title: "\"Create subproject spring-xd-machine-learning-analytics\""
  - Description: "\"This project contains core abstractions that will allow for multiple implementations of a machine learning algorithm to be implemented via integration with various existing libraries or custom code implementations.    The initial code for this has been developed in a separate github repo and is located here   https://github.com/thomasdarimont/spring-xd/tree/feature/advanced-analytics-support/spring-xd-analytics/src/main/java/org/springframework/xd/analytics/model  The model can assume its use in evaluation of the model inside a stream where the data structure is a Tuple.  Note, it maybe useful to consider Message<Tuple> in case any metadata outside the core 'input data' is required to help guide the evaluation.  The build.gradle file should be updated such that there is a new build artifact spring-xd-machine-learning-analytics.jar along the lines of our other build artifacts.  Open to other naming suggestions.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1472** (`tawos-v1.1:2335`), created 2014-04-02T05:47:35.000000Z
  - Title: "\"Let modules define a default value for --inputType option\""
  - Description: "\"If a module e.g. always expects the payload of the message to be of a certain java type if would be good for documentation and convenience reasons in order to specify a default value for the --inputType option.   documentation = output for module info convenience = we could e.g. support to always accept a Json payload (or automatic message payload conversion once it is extensible)  currently, adding options.inputType.default to the module's property file has no effect  I've also tried to \"\"redefine\"\" it using options.inputType.description This leads to the following exception:  Command failed org.springframework.xd.rest.client.impl.SpringXDException: Module option named 'outputType' is present in several delegates: [org.springframework.xd.module.options.SimpleModuleOptionsMetadata@3c1d635a, FlattenedCompositeModuleOptionsMetadata [outputType] => PojoModuleOptionsMetadata backed by class org.springframework.xd.dirt.plugins.stream.ModuleTypeConversionPluginMetadataResolver$OutputOptionsMetadata, defining options [[ModuleOption [name=outputType, type=class org.springframework.util.MimeType, defaultValue=null, description=how this module should emit messages it produces]]] [inputType]"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1564** (`tawos-v1.1:2244`), created 2014-04-12T08:39:57.000000Z
  - Title: "\"Rabbit Sink with explicit routingKey as 'string' SpEl literal expression fails\""
  - Description: "\"Following stream fails to work:  tream create s3 --definition \"\"http | rabbit --routingKey='mytest1'\"\" --deploy  Created and deployed new stream 's3' xd:>http post --data \"\"testing\"\" > POST (text/plain;Charset=UTF-8) http://localhost:9000 testing > 500 INTERNAL_SERVER_ERROR > 500 INTERNAL_SERVER_ERROR  Error sending data 'testing' to 'http://localhost:9000'  The exception at the container log is:  07:24:57,245 ERROR pool-18-thread-4 http.NettyHttpInboundChannelAdapter:171 - Error sending message org.springframework.messaging.MessageHandlingException: Expression evaluation failed: mytest1  at org.springframework.integration.util.AbstractExpressionEvaluator.evaluateExpression(AbstractExpressionEvaluator.java:126)  at org.springframework.integration.handler.ExpressionEvaluatingMessageProcessor.processMessage(ExpressionEvaluatingMessageProcessor.java:76)  at org.springframework.integration.amqp.outbound.AmqpOutboundEndpoint.handleRequestMessage(AmqpOutboundEndpoint.java:196)  at org.springframework.integration.handler.AbstractReplyProducingMessageHandler.handleMessageInternal(AbstractReplyProducingMessageHandler.java:170)  at org.springframework.integration.handler.AbstractMessageHand"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-162** (`tawos-v1.1:3621`), created 2013-05-31T08:40:14.000000Z
  - Title: "Create design document for implementation strategy to support message conversion in ChannelRegistry"
  - Description: "\"The conversion should be based on content-type headers, similar to the way Spring's HttpMessageConverters work (with mime types).  Also, the map of available converters should be extensible while including the most common defaults (for JSON, XML, etc). We most likely want to add a few of our own content types also (e.g. for Tuples).  Most likely, this logic and the configuration methods for extending the converter map, belong in AbstractChannelRegistry since it should be common across all implementations (i.e. the logic should be the same regardless of the transport used after-serialization/before-deserialization).\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1650** (`tawos-v1.1:2160`), created 2014-04-29T12:58:35.000000Z
  - Title: "Update HDFS sink to accept a partition strategy"
  - Description: "Add configuration for the partition strategy to HDFS sink to support writing files into subdirectories based on a partition key provided in the header or field in the message of the stream data.\n\nThe writing using HDFS Store DataWriter should pass in the partition key value to be used for the write operation.\n\nPartition configuration could be made available to the sink using a  --format parameter:\n\nthat could then be used in XML config like:\n{code}\n      expression=\"new java.text.SimpleDateFormat('${format}').format(${timestamp})\n{code}\nSimilar to the time source."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1674** (`tawos-v1.1:2136`), created 2014-05-07T14:06:21.000000Z
  - Title: "\"Accessing non-existing module causes NullPointerException\""
  - Description: "This source exists:\n{code}\nhttp://localhost:9393/modules/source/time\n{code}\nBut trying to access a non-existing source such as:\n{code}\nhttp://localhost:9393/modules/source/time2\n{code}\nTriggers in the UI: \n{code}\n[{\"links\":[],\"logref\":\"NullPointerException\",\"message\":\"NullPointerException\"}]\n{code}\nOn the server-side:\n{code}\n6:03:45,387 ERROR http-nio-9393-exec-3 rest.RestControllerAdvice:199 - Caught exception while handling a request\njava.lang.NullPointerException\n\tat org.springframework.xd.dirt.rest.DetailedModuleDefinitionResourceAssembler.toResource(DetailedModuleDefinitionResourceAssembler.java:49)\n\tat org.springframework.xd.dirt.rest.ModulesController.info(ModulesController.java:104)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)\n\tat sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)\n\tat sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)\n\tat java.lang.reflect.Method.invoke(Method.java:483)\n\tat org.springframework.web.method.support.InvocableHandlerMethod.invoke(InvocableHandlerMethod.java:215)\n\tat org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- Which brokers and compatibility guarantees are intended by XD-2098 and XD-2293?
- Does this work add adapter modules, alter internal transport implementations or change broker configuration?
- Which existing conversion, routing-expression and shutdown-order fixes must remain compatible with the specified broker changes?

## XD-2297 (train)

Historical cutoff: 2014-10-31T18:27:30.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `f4b3a81d02faa26051595f94d7eed314e8c92479ad253fa040611fa6f3e7a283`

Source input identity SHA-256: `595cb64a585d3d48830adacc9779be9d14cc41ed2485b8a39e991dbf944a2bd1`

### Supplied historical plan

- **XD-2297** (`tawos-v1.1:1523`)
  - Title: "\"Add support for mass data ingest\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2298** (`tawos-v1.1:1522`)
  - Title: "Investigate options for mass data ingest into HDFS/HAWQ"
  - Description: "As a user, I'd like to mass ingest data from databases (and others) into HDFS/HAWQ so that I don't have to write custom code and as well as be able to ingest in an efficient way.\n\n*Spike scope:*\n* Identify and document options\n**_gpfdist_/_gpload_\n** HAWQ native format\n** PXF\n** Sqoop Tasklet\n* Decide whether to handle it via OOTB Batch Job or through other mechanism (perhaps HAWQ sink?)\n* Design specs"
  - Unknown fields: ["type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2298 already investigates gpfdist/gpload, native HAWQ format, PXF and a Sqoop Tasklet, and explicitly decides between a batch job and other mechanisms. The research and architecture choice are present in scope.",
    "XD-2124 and XD-2132 describe candidate ingestion capabilities, not observed failures that show those options are unavailable. XD-1985 records a concrete Guava/Hadoop compatibility failure, but no second supplied ticket supports the same failure mechanism for a selected approach here.",
    "No implementation or target runtime version is chosen in the supplied spike. Generic accuracy and error-handling criteria from XD-2052/2053 cannot establish that this design investigation will omit them."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2132** (`tawos-v1.1:1683`), created 2014-09-16T16:39:55.000000Z
  - Title: "\"Add HAWQ sink\""
  - Description: "\"As a user, I'd like to have the option of _HAWQ_ sink so that I can write data directly into HAWQ via PXF extensions through Avro/Parquet format.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2154** (`tawos-v1.1:1661`), created 2014-09-19T16:04:57.000000Z
  - Title: null
  - Description: "As a user, I'd like to have a REST API to point and push an archive that includes custom module definitions and configurations so that I don't have to manually move and set it up.\n\n*Scope of this spike:*\n* Assess customer requirement, brainstorm, and document options\n* Socialize with the team to collect feedback\n* Identify phases\n* Create new stories"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-2295** (`tawos-v1.1:1525`), created 2014-10-30T17:02:00.000000Z
  - Title: null
  - Description: "As a user, I'd like to stream ingest audio and video data so that I can apply predictive analytics algorithms for facial detection.\n\n*Spike scope:*\n* Research the feasibility of implementing [Motion-JPEG|http://en.wikipedia.org/wiki/Motion_JPEG]\n* Design specs on Motion-JPEG format\n\n*Note:* [opencv|http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html], although having OOTB support, it is not platform compatible. "
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2135** (`tawos-v1.1:1680`), created 2014-09-16T17:03:53.000000Z
  - Title: "\"Add explicit \"\"error channel\"\" support\""
  - Description: "As a user, I'd like to have the option to explicitly define/configure \"error channel\" so that I can stage and route the errors/exceptions through the dedicated channel and continue ingestion.\n\n*Scenario:*\n* 'http' source ingest \n* failure at either source, processor, or sink module\n* regardless of whether it is a custom module or not, traverse through the exception to propagate the actual _Caused by:..._, stage the error as payload, and route it to the error channel\n\n*Example Configuration:*\n* error channel definition similar to \"topic.errors.stream.module\"\n* configure custom exception similar to \"catch=**Exception\"\n* exception hierarchy\n** GlobalException\n** DefaultException\n** ModuleSpecificException\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1985** (`tawos-v1.1:1829`), created 2014-07-16T14:46:08.000000Z
  - Title: "Packaging of Guava 17 results in failure to deploy mapreduce job to Hadoop 2.4 based distros"
  - Description: "Trying to deploy the hashtagcount batch sample [1] to Hadoop 2.4.1 or Hortonworks HDP 2.1 fails with an IllegalAccessError exception.\n\nLooks like a Guava versioning issue - Swapping out guava-17.0.jar for guava-11.0.2.jar in the xd/lib directory solves it.\n\nMark P suggested we try 16.0.1 which is what Curator uses and that seems to work as well. \n\nLooking into changing the build to not force 17.0 which is the IO platform version.\n\nhttp://upstream-tracker.org/java/compat_reports/guava/16.0.1_to_17.0/src_compat_report.html \n\n\nI get the following exception:\n\n{code}\n16:42:22,214  INFO Deployer server.JobDeploymentListener - Deployment status for job 'hashtagCountJob': DeploymentStatus{state=deployed}\n16:42:27,315  WARN task-scheduler-2 mapreduce.JobSubmitter - No job jar file set.  User classes may not be found. See Job or Job#setJar(String).\n16:42:27,325 ERROR task-scheduler-2 step.AbstractStep - Encountered an error executing step hashtagcount in job hashtagCountJob\njava.lang.IllegalAccessError: tried to access method com.google.common.base.Stopwatch.<init>()V from class org.apache.hadoop.mapreduce.lib.input.FileInputFormat\n\tat org.apache.hadoop.mapreduce.lib.input.FileInputFormat.ge"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2124** (`tawos-v1.1:1691`), created 2014-09-16T15:58:15.000000Z
  - Title: "Provide a Sqoop 'tasklet' for mass data ingest"
  - Description: "As a user, I'd like to have the ability to mass-ingest data from various database systems so that I'm not restricted with the current approach (_jdbchdfs_) that is dependent on JDBC drivers. \n\n"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-2205** (`tawos-v1.1:1614`), created 2014-10-03T14:49:28.000000Z
  - Title: "\"Add Python processor\""
  - Description: "\"As a user, I'd like to have a _Python_ processor so that I can efficiently perform data computations and statistical analysis.   Investigate the right approach (native or via stdin/stdout) that fits Spring XD model.  [Integrate Java and Python|https://wiki.python.org/moin/IntegratingPythonWithOtherLanguages#Java]\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What runtime compatibility, throughput and data-correctness evidence will be required when the existing spike chooses among the listed ingestion options?

## XD-2336 (train)

Historical cutoff: 2014-11-13T13:28:03.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `05d348ed5f909e3dcfe1a85d4ce1f645948ac04402d093145ba4414d83e5db7c`

Source input identity SHA-256: `1385c8c3384632f2b7b9d72459ed8ad0947490d7d8568b0acc09e03593419894`

### Supplied historical plan

- **XD-2336** (`tawos-v1.1:1484`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2334** (`tawos-v1.1:1486`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2335** (`tawos-v1.1:1485`)
  - Title: "\"Update Performance AMI to include Kafka\""
  - Description: "\"Create an AMI that will contain the Kafka Executable as well as the Kafka performance test tools.\""
  - Unknown fields: []
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2335 explicitly includes the Kafka executable and Kafka performance tools in the performance AMI and is Done; these items cannot be labelled missing.",
    "The supplied EC2 provisioning, acceptance-test and YARN packaging stories describe existing work rather than two observed Kafka/AMI/performance-testing failures. The REST testing tasks do not establish a Kafka-specific mechanism.",
    "The root and XD-2334 have no known title/description, so intended benchmarks, readiness checks and AMI acceptance criteria cannot be inferred."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1245** (`tawos-v1.1:2562`), created 2014-01-15T07:04:57.000000Z
  - Title: "Develop basic acceptance test application to exercise based XD-EC2 deployment from CI"
  - Description: "Create a first pass at an acceptance test app for a stream definition of http | log.  \n\nThis will involve creating two new projects in xd\n\n1. spring-xd-integration-test\n2. spring-xd-acceptance-tests\n\n#1 will contain generally useful utility methods for acceptance test, such as sending data over http, obtaining and asserting JMX values of specific modules.\n#2 will contain tests that use #1 to test the various out of the box modules provides in XD."
  - Unknown fields: []
  - Truncated fields: []
- **XD-757** (`tawos-v1.1:3043`), created 2013-08-26T10:02:47.000000Z
  - Title: "\"Create aggregator module\""
  - Description: "\"Create a processing module based on SI's aggregator component.  The completion criteria for the aggregator should be a simple count of messages (e.g. received 50 messages) and a timeout so that messages don't stay in the aggregator module for more than 30 seconds.   *Implementation suggestions*  Create an XML based processing module definition using the SI aggregator namespace.  Only the options to support the features in the description should be exposed as property placeholders.  *How to know it works* A shell style integration test that has a source that sends a known amount of messages.  A ticktock like module would perhaps be a good example.  10 messages sent every 100ms with an aggregator set to a 'aggregate count' of 10, should have 1 message output (perhaps to file sink whose name is based on time as well, is that possible.).  A ticktock example with a 1 second delay and with the aggregator module set to have a timeout of 0.5 seconds will have only one message in the file (again assumign the file name has a timestamp/counter in the filename). \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-969** (`tawos-v1.1:2835`), created 2013-10-21T13:57:22.000000Z
  - Title: "Add functionality to provision EC2 instance and mount EBS"
  - Description: "* The Application should \n**  Create a Spring Application Context.\n**  Should take a command line parameter --config that will point to a property file with key/value pairs specified below.  By default the file xd-ec2.properties will be looked for on the classpath\n** Associate EBS shared volume for each machine instance\n\n* Packaging \n** Use gradle application plugin to generate a ‘bin’ directory with a script to start the application.  Seehttp://www.gradle.org/docs/current/userguide/application_plugin.html\n** The config file xd-ec2.properties should be in a directory (ideally a 'config' directory parallel to 'bin' and will be loaded by the application by default - loading via the CP is probably the easiest way.\n** Create a POJO to easily reference these properties, vs. using a raw java Properties object.\n\nHow to verify it works\n\n* Integration testing\n** Create JUnit based tests.  JClouds itself has extensive testing, can look at those for structure.\n** Verify what you created has been installed.\n** Verify ports are open\n\nInstance Information\n** EBS of 50GB Base for each instance.\n* Report successful and failed Instances.\n\nKey-Value pairs in configuration file\nproperties may include"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1076** (`tawos-v1.1:2731`), created 2013-11-18T08:55:59.000000Z
  - Title: "\"Create an FTP tasklet to get remote files and put them in the local file system.\""
  - Description: "\"This is along the lines of what is in this blog post  http://coreyreil.wordpress.com/2012/12/21/spring-batch-creating-an-ftp-tasklet-to-get-remote-files/  Note that there have been some new developments in SI to get at the underlying stream for FTP.  The way to test this is to create a new batch job in XD that has this as it's tasklet.  Going forward the target file system will also be HDFS.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1082** (`tawos-v1.1:2725`), created 2013-11-18T20:43:11.000000Z
  - Title: "Create REST API for getting information on a job execution for a given execution id"
  - Description: "Adopted functionality from Spring Batch admin\nShould include springmvc test framework style tests\n\nGET /batch/jobs/executions/{executionId} - Get information on all executions of a given job name."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1083** (`tawos-v1.1:2724`), created 2013-11-18T20:44:08.000000Z
  - Title: "\"Create REST API for getting information on all steps of a given job execution\""
  - Description: "Adopted functionality from spring batch admin\nShould include springmvc test framework style tests\n\nGET /batch/jobs/executions/{executionId}/steps - Get information on all steps of a given job execution"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1084** (`tawos-v1.1:2723`), created 2013-11-18T20:45:05.000000Z
  - Title: "\"Create REST API for getting information on a given step execution\""
  - Description: "Functionality adopted from spring batch admin\nShould include springmvc test framework style tests\n\nGET /batch/jobs/executions/{executionId}/steps/{stepId} - Get information on a given step execution"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1085** (`tawos-v1.1:2722`), created 2013-11-18T20:45:53.000000Z
  - Title: "\"Create REST API for stopping a specific job\""
  - Description: "Functionality adopted from spring batch admin\nShould include springmvc test framework style tests\n\nDELETE /batch/jobs/executions/{executionId} Stop a specific job"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1086** (`tawos-v1.1:2721`), created 2013-11-18T20:47:03.000000Z
  - Title: "\"Create REST API for stopping all job executions\""
  - Description: "\"Adopted functionality from spring batch admin Should include SpringMVC test framework style tests.  DELETE /batch/jobs/executions/ - stop all job executions\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1087** (`tawos-v1.1:2720`), created 2013-11-18T20:49:00.000000Z
  - Title: "\"Create REST API for restarting a specific job instance\""
  - Description: "\"Functionality adopted from spring-batch admin Should include springmvc test framework style tests  POST /batch/jobs/{jobName}/{jobInstanceId}/executions - restart a specific job instance  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1314** (`tawos-v1.1:2493`), created 2014-02-12T09:05:27.000000Z
  - Title: "\"Create XD .zip distribution for YARN\""
  - Description: "\"Create XD .zip distribution for YARN that adds an additional sub-project to the spring-xd repo for building the xd-YARN.zip  Link into main build file  Produce a new artifact spring-xd-v-xyz-yarn.zip as part of the nightly CI process -- will now have 2 artifacts, main xd.zip distribution and xd-yarn.zip  Does not include any Hadoop distribution libraries  Does include spring-hadoop jars for Apache22 ‘unflavored’ \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which Kafka benchmark scenarios and acceptance criteria were defined by XD-2334?
- How is the completed performance AMI verified to contain working Kafka executables and test tools?
- What cutoff-bound benchmark environment or reproducibility requirements, if any, were recorded in the unknown root?

## XD-2374 (train)

Historical cutoff: 2014-11-19T17:01:27.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `99ee8dc03b21bb8ce4285de010b1afb54997efeed6d398e8da5f4b09d92c1da2`

Source input identity SHA-256: `0d57a206d6e0438568127fb6bd1edcfdf54ad7c174ffb36e046c516d335aa921`

### Supplied historical plan

- **XD-2374** (`tawos-v1.1:1448`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2375** (`tawos-v1.1:1447`)
  - Title: "Add reactor-stream processor module"
  - Description: "As a user, I'd like to have a _reactor-stream_ processor module so that I can ingest data using XD source modules and process them as time-window operations. \n\n*Example:*\nhttp | reactor-stream --timeWindow=10s --field=payload.sensorData --expressions=min,avg\n\nThis would give you 10 second time window of the min and avg values."
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-2376** (`tawos-v1.1:1446`)
  - Title: "Add micro-batch support"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2375 explicitly specifies time-window processing with min and avg, so those aggregation operations cannot be labelled missing. The micro-batch member has no recoverable description.",
    "XD-2233 concerns REST time-series representation ordering and XD-2232 concerns median approximation; the plan does not specify REST output or median calculation, so those examples do not establish a comparable defect in the Reactor window processor.",
    "The source/sink acceptance criteria and error-channel proposal describe desired checks, not two independent historical Reactor or micro-batch failure mechanisms."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2135** (`tawos-v1.1:1680`), created 2014-09-16T17:03:53.000000Z
  - Title: "\"Add explicit \"\"error channel\"\" support\""
  - Description: "As a user, I'd like to have the option to explicitly define/configure \"error channel\" so that I can stage and route the errors/exceptions through the dedicated channel and continue ingestion.\n\n*Scenario:*\n* 'http' source ingest \n* failure at either source, processor, or sink module\n* regardless of whether it is a custom module or not, traverse through the exception to propagate the actual _Caused by:..._, stage the error as payload, and route it to the error channel\n\n*Example Configuration:*\n* error channel definition similar to \"topic.errors.stream.module\"\n* configure custom exception similar to \"catch=**Exception\"\n* exception hierarchy\n** GlobalException\n** DefaultException\n** ModuleSpecificException\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: ["status", "estimate"]
  - Truncated fields: ["description"]
- **XD-2232** (`tawos-v1.1:1588`), created 2014-10-12T12:50:40.000000Z
  - Title: null
  - Description: "Often it is useful to have access to the median value for fields of a data stream since they are more robust with respect to outliers.\n\nThe median is defined as the value of a dataset such that, when sorted, 50% of the data is smaller than the value and 50% of the data is larger then the value. Ordinarily this is difficult to calculate on a stream because it requires the collection and sorting of all data.\n\nThe median of a data stream can be approximated with a technique called stochastic averaging. To approximate the median value of a data stream one could use the following approach:\nGiven the current estimate of the median {{M}}. If the next observed value in the stream is larger than {{M}}, increase the current estimate by {{r}} (= the learning rate). If it is smaller, decrease the estimate by {{r}}. When {{M}} is close to the median, it increases as often as it decreases, and therefore it stabilizes.\n\n\nThe following example shows a primitive implementation of the above mentioned algorithm in groovy (to be placed under ${XD_HOME}/modules/processor/scripts).\n{code:groovy}\nimport org.springframework.xd.tuple.TupleBuilder;\nimport org.springframework.xd.tuple.Tuple;\n\n/**\n * Stochast"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: ["description"]
- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-1577** (`tawos-v1.1:2231`), created 2014-04-15T01:44:34.000000Z
  - Title: "\"Changing externalized module config properties at runtime\""
  - Description: "\"Once the container starts up and the module is deployed, the externalized module configuration properties could not be changed for the subsequent modules of same type.  Here is the scenario for a stream \"\"http | transform | log\"\", with XD_MODULE_CONFIG_LOCATION and XD_MODULE_CONFIG_NAME using their default values.  In, ${xd.config.home}/modules/modules.yml, I have: processor:   transform:     expression: \"\"'Inside modules.yml'\"\"  and, in, ${xd.config.home}/modules/processor/transform/transform.properties, I have: expression: \"\"'First module: inside transform.properties'\"\"  Now, I deploy this stream: \"\"http | transform | log\"\".  Lets say, I have another stream that uses the transform module, but this time I want to change the expression in ${xd.config.home}/modules/processor/transform/transform.properties to, expression: \"\"'Second module'\"\"  Now, when the stream containing this transform module gets deployed, it uses the same transform.properties that is used by the previously deployed transform module.  What I understand from this behavior is that, the EnvironmentAwareModuleOptionsMetadataResolver caches the module environments for a given module type and name. When the same modul"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2233** (`tawos-v1.1:1587`), created 2014-10-12T16:37:53.000000Z
  - Title: null
  - Description: "The current representation of REST resources of time-series data (e.g. aggregate counter) can lead to problems in consuming applications. \nDespite the time series data provided by the \"counts\" data structure is logically ordered by key (timestamps) it doesn't guarantee an ordering, since many consuming applications interpret JSON data as an unordered map like data structure. Because of this consuming applications have to apply special ordering / transformation logic in order to get the data in an chronologically ordered fashion. It would be helpful if one could configure the rendering of the time series data, e.g. as a list of json object like:\n{code:json}\n{\n \"ts\":\"Sun Oct 12 23:10:23 CEST 2014\"\n ,\"value\": 42\n} \n{code}\nWhere {ts} denotes the timestamp and {value} denotes the value.\n\nI attached an example for this in python that demonstrates the problem.\n\nSteps to reproduce:\nCreate stream\n{code}\nxd:>stream create test --definition \"http | filter --expression=payload.contains('pivotal') | log\"\n{code}\n\nCreate tap on stream with aggregate-counter\n{code}\nxd:>stream create test_tap --definition \"tap:stream:test.filter > aggregate-counter\"\n{code}\n\nPost some http data\n{code}\nxd:>http post "
  - Unknown fields: ["title", "type", "status"]
  - Truncated fields: ["description"]
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1048** (`tawos-v1.1:2758`), created 2013-11-10T13:19:29.000000Z
  - Title: null
  - Description: "This would be a combination of the existing aggregate counter and field value counter functionality.\n\nFor example if the stream data was for car purchases some fields might be colour, make and model. \nWhen analysing the aggregate data I dont just want to know how many were sold on Monday, but how many of each make or how many of each colour, \nor how many of a particular colour, make AND model. This would allow a dashboard type client to 'drill down' into each dimension or combination of dimensions (in real time without executing batch queries against the raw data)\n\nIdeally the aggregate counter would be specified as \n\nstream create --name mytap --definition \"tap:mystream > aggregatecounter --name=mycount --fieldNames=colour,make,model\"\n\nThe keys would be dynamically created according to the field values in each record (ie in a similar way to the field value counter you would not need to predefine field values) and keys would be created for all combinations of the fields specified eg the record \n\n{ \"colour\":\"silver\" , \"make\":\"VW\" , \"model\" : \"Golf\" } \n\nwould increment the following key counters (in addtion to the existing time buckets)\n\n<existing base counter - ie all fields for thi"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: ["description"]
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2295** (`tawos-v1.1:1525`), created 2014-10-30T17:02:00.000000Z
  - Title: "\"Add support for audio/video source\""
  - Description: "As a user, I'd like to stream ingest audio and video data so that I can apply predictive analytics algorithms for facial detection.\n\n*Spike scope:*\n* Research the feasibility of implementing [Motion-JPEG|http://en.wikipedia.org/wiki/Motion_JPEG]\n* Design specs on Motion-JPEG format\n\n*Note:* [opencv|http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html], although having OOTB support, it is not platform compatible. "
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What event-time or processing-time semantics, empty-window behavior and output contract are intended for the Reactor processor?
- Does the micro-batch work share implementation paths with the Reactor time-window processor, or require separate historical evidence?

## XD-2399 (train)

Historical cutoff: 2014-11-24T14:15:59.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `c346e79773afd7175a06af4336f69a327deb1f27819ea7ab27613ef43b18c773`

Source input identity SHA-256: `830cdbf690aab91d993dcb2f56b9cfc26ccdb6d792be03a77892c3ecedf51b84`

### Supplied historical plan

- **XD-2399** (`tawos-v1.1:1425`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2057** (`tawos-v1.1:1758`)
  - Title: "\"Investigate Travis issues\""
  - Description: "\"We are currently facing issues with Travis. Determine the root cause, isolate the bottleneck, and resolve the issues.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2058** (`tawos-v1.1:1757`)
  - Title: "\"Investigate long running tests\""
  - Description: "\"The goal is to optimize the build process and at the same time validate the feature capabilities as quickly as we can. Investigate the long running tests. Look for long timeout window declarations. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2319** (`tawos-v1.1:1501`)
  - Title: "\"Add spring-xd-python to the distribution\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2400** (`tawos-v1.1:1424`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type"]
  - Truncated fields: []
- **XD-2401** (`tawos-v1.1:1423`)
  - Title: "Include DIRT tests in CI builds"
  - Description: "As a developer, I'd like to include DIRT tests as part of the CI builds so that we can automatically evaluate DIRT features and functionalities."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2402** (`tawos-v1.1:1422`)
  - Title: "\"Investigate why builds have more WARN logs\""
  - Description: "\"As a developer, I'd like to investigate the increase in WARN logs so that I can troubleshoot and fix PMD/Sonar violations.  Consider notifying the violations through SONAR configurations. The committer should be notified.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2403** (`tawos-v1.1:1421`)
  - Title: "Create Windows based CI infrastructure"
  - Description: "As a build manager, I'd like to setup CI infrastructure so that I can run integration tests in Windows OS automatically as we commit-trigger new builds. "
  - Unknown fields: ["type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The plan explicitly includes Travis investigation in XD-2057, long-test investigation in XD-2058, DIRT CI tests in XD-2401 and Windows CI infrastructure in XD-2403. These requirements are already present.",
    "XD-1227 documents investigation of slow tests and is Done; XD-2078 reports an HDFS runtime failure after a few minutes. They do not jointly establish that the planned CI changes shorten away relevant tests or cause a build bottleneck.",
    "No two supplied prior tickets demonstrate a comparable Travis or Windows CI failure. XD-2399 and XD-2400 have unknown scope text, and prior packaging/API stories do not prove an omitted CI dependency."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-745** (`tawos-v1.1:3055`), created 2013-08-22T16:19:46.000000Z
  - Title: "\"Return the list of Jobs from spring-batch-admin\""
  - Description: "\"The current XD JobController that returns a list of jobs has quite a different API signature than what is in spring-batch-admin.  To simplify the UI development, a new controller JobAdminController, will be created that lives under the request path /jobs/admin.  The goal is to return a the current JSON structure of spring-batch-admin /jobs/ request and make only minimal changes to implementations of controllers as found .  See #1 in the Doc (link to json output doc for spring batch).  *Implementation Suggestions*  There will need to be some SpringMVC setup that will enable the current style of spring-batch-admin controller requests to co-exist with the existing XD Controllers, e.g. the use of .json for json marshalling etc.  This may in fact be the bulk of time spend in this first story to integration spring-batch-admin style controllers into XD.  A new controller named JobAdminController that in the spring-xd-dirt project in the package org.springframework.xd.dirt.rest.  The JobAdminController will not need to follow the same HATEOAS style as the other controllers at this time.  The current controller in Spring Batch Admin looks like this {code}     @RequestMapping(value = \"\"/job"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-671** (`tawos-v1.1:3128`), created 2013-08-12T07:41:19.000000Z
  - Title: "Add support for dynamic routing"
  - Description: "\"It should be possible to create streams like the following which rely upon named channel support and dynamic routing capabilities:  {code} http | somerouter :x > xtransformer | hdfs :y > ytransformer | hdfs {code}  The 'somerouter' processor could return \"\"x\"\" or \"\"y\"\" which determines the downstream path for each message.  This should be implemented in such a way that any developer adding a router module would only need to deal with existing Spring Integration semantics (in this case, only considering the return of \"\"x\"\" or \"\"y\"\" - whether it be SpEL or a POJO method invocation). Perhaps in the plugin that modifies a module context, we could simply add a new ChannelResolver implementation (by adding that ChannelResolver as a bean and/or a BeanPostProcessor that configures that as the resolver for any router, if necessary). That ChannelResolver would have a reference to the ChannelRegistry so that the router actually sends its messages to those shared channels. The shared channels themselves would have been created as long as a valid downstream flow has been defined.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1227** (`tawos-v1.1:2580`), created 2014-01-14T21:59:45.000000Z
  - Title: "\"Investigate long running tests and create refactoring issues\""
  - Description: "\"https://sonar.springsource.org/dashboard/index/7173?did=3  Shows which of our current tests take the most time to execute.  xd.dirt.stream and xd.shell.command are where the most time is spent.  In xd.dirt.stream it seems likely that time can be reduced by not restarting a new single node server per test, but sharing it across tests, e.g.   RabbitSingleNodeStreamDeploymentIntegrationTests    LocalSingleNodeStreamDeploymentIntegrationTests  RedisSingleNodeStreamDeploymentIntegrationTests    As a first pass, the test that take longer than 15 seconds in that report should be investigated. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1314** (`tawos-v1.1:2493`), created 2014-02-12T09:05:27.000000Z
  - Title: "\"Create XD .zip distribution for YARN\""
  - Description: "\"Create XD .zip distribution for YARN that adds an additional sub-project to the spring-xd repo for building the xd-YARN.zip  Link into main build file  Produce a new artifact spring-xd-v-xyz-yarn.zip as part of the nightly CI process -- will now have 2 artifacts, main xd.zip distribution and xd-yarn.zip  Does not include any Hadoop distribution libraries  Does include spring-hadoop jars for Apache22 ‘unflavored’ \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1922** (`tawos-v1.1:1891`), created 2014-07-07T13:35:10.000000Z
  - Title: "\"Make Cron-based Triggers TimeZone aware \""
  - Description: "Currently specified Cron Expressions are executed in the Container's default TimeZone. In *Trigger.xml* we specify:\n\n{code}\n\t<beans profile=\"use-cron\">\n\t\t<int:inbound-channel-adapter channel=\"output\"\n\t\t\tauto-startup=\"false\" expression=\"'${payload}'\">\n\t\t\t<int:poller cron=\"${cron}\" />\n\t\t</int:inbound-channel-adapter>\n\t</beans>\n{code}\n\nThis translates in *org.springframework.integration.config.xml.PollerParser* to\n\n{code}\nBeanDefinitionBuilder builder = BeanDefinitionBuilder.genericBeanDefinition(CronTrigger.class);\nbuilder.addConstructorArgValue(cronAttribute)\n{code}\n\nWhich will call *org.springframework.scheduling.support.CronTrigger*:\n\n{code}\n\t/**\n\t * Build a {@link CronTrigger} from the pattern provided in the default time zone.\n\t * @param cronExpression a space-separated list of time fields,\n\t * following cron expression conventions\n\t */\n\tpublic CronTrigger(String cronExpression) {\n\t\tthis.sequenceGenerator = new CronSequenceGenerator(cronExpression);\n\t}\n{code}\n\n\"Build a {@link CronTrigger} from the pattern provided in the *default time zone*.\"\n\nWe need to pass-in a timezone. *Should cron expressions as part of an XD *Definition* have a TimeZone parameter?* When creating the strea"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2052** (`tawos-v1.1:1762`), created 2014-08-04T15:49:24.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB source modules to integrate with various data sources to ingest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters. \n\nAcceptance Criteria:\n- User should be able to list the 'new source' through DSL commands \n- User should be able to optionally choose the \"new source\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new source' module\n- After successful stream creation with the 'new source' module, the definition should be included in stream listing\n- REST endpoints should include 'new source' definitions\n- Data ingested using the 'new source' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data using 'new source' module \n\n\n\n"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2078** (`tawos-v1.1:1737`), created 2014-08-13T22:02:52.000000Z
  - Title: "\"\"\"http | hdfs\"\" stream starts throwing exceptions after a few minutes \""
  - Description: "\"Environment: - Hadoop Installation: PHD Service for PCF  (PHD1.1 based on Apache Hadoop 2.0.5:  2.0.5-alpha-gphd-2.1.0.0 ) running on vCHS - Spring XD running in singlenode mode (version 1.0.0.RC1) on a vCHS VM  Steps to reproduce: 1- Setup a stream in Spring XD shell: \"\"http --port=9000 | hdfs --rollover=10M --idleTimeout=60000\"\" --deploy 2- Hit port 9000 every second with 1-10KB of JSON data 3- Observe the temp file being created in HDFS under /xd/<stream name> 4- Run `hadoop fs tail <file> --follow` to see that data is being written to HDFS  Expected result: - HDFS sink continues to operate and eventually roll-over at 10MB  Actual: - After about 2 minutes of successful HDFS writes, the HDFS sink crashes and starts throwing exceptions (see full log attached):  \"\"'java.io.IOException: All datanodes 192.168.109.61:50010 are bad. Aborting...\"\" - The temp file is never closed even after the stream is undeployed or destroyed.    Here are some details of our investigation that may be useful: - I start both the shell and the singlenode runner with --hadoopDistro phd1;  I also configured the hadoop fs namenode correctly in the XD shell. - \"\"http <options> | file <options>\"\" work as expe"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2119** (`tawos-v1.1:1696`), created 2014-09-16T12:25:06.000000Z
  - Title: "Support accessing admin server endpoints over HTTPS"
  - Description: "As a user, I'd like to have the option to enable HTTPS so that I can access XD's Admin server [endpoints|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] over secured communication.\n\nTechnical Implementation:\n\nThis functionality is available in Spring Boot 1.2.0 M1 and has been backported into the 1.1.x branch to be released under Spring 1.1.7.  We can test against 1.1.7 SNAPSHOT.\n\nWorking through the way to update the build file to pick up a new version of boot is a bit tricky :("
  - Unknown fields: []
  - Truncated fields: []
- **XD-239** (`tawos-v1.1:3544`), created 2013-06-17T10:10:41.000000Z
  - Title: "Epic For Distributed Monitoring Stories"
  - Description: "* As a user, I can view average performance statistics for each module involved in my stream, aggregated across a cluster\n** Batch/Integration stats (Message send/receive counts, avg execution time, queue stats, error rates, job stats, etc)\n** Implies grouping individual SI/Batch components by module\n** Metrics exposed in JMX and JSON through Jolokia?\n Existing monitoring tool for visualization and reporting vs custom dashboard\n* As a user, I can alert against these metrics and setup relevant control actions\n** TODO what makes sense as auto-responses to control actions? Auto-scaling of XD nodes, more fine-grained message queue throttling, etc\n* As a user, I can view performance of the XD system\n** Expose metrics of interest to the internal workings of XD, particularly throughput/storage in transport mechanism\n* As a user, I can correlate module statistics with XD system stats and node stats\n** Should be doable with external monitoring system\n* As a module developer, I can diagnose module performance issues by tracing a single message through a stream\n** Trace individual messages, average message throughput would be interesting to end users too if not too expensive to trace\n** Visua"
  - Unknown fields: ["type"]
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What cutoff-available investigation results or acceptance criteria define the Travis failures and DIRT/Windows test coverage?
- Do the intended build optimizations preserve runtime-duration scenarios, and is there actual two-ticket evidence of a relevant CI regression?

## XD-2464 (train)

Historical cutoff: 2014-12-09T04:54:19.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `d67fe709f6cb5d0a3589d19a372b1f766acfe5cf7449740e3fe807bc666f7476`

Source input identity SHA-256: `1ff9a8f5a51688937dffbae34e07ada1dcc2745f51d2aad4b298cbd7bef6ea4b`

### Supplied historical plan

- **XD-2464** (`tawos-v1.1:1360`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2432** (`tawos-v1.1:1392`)
  - Title: "Define developer-facing interfaces for Spark Streaming modules"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-2433** (`tawos-v1.1:1391`)
  - Title: "Implement a Spark Streaming Receiver that binds to the MessageBus"
  - Description: null
  - Unknown fields: ["description", "type"]
  - Truncated fields: []
- **XD-2465** (`tawos-v1.1:1359`)
  - Title: "Implement an XD module type that integrates with Spark Streaming"
  - Description: null
  - Unknown fields: ["description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2466** (`tawos-v1.1:1358`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2467** (`tawos-v1.1:1357`)
  - Title: "Implement a Spark Streaming Driver application that can be controlled as an XD module instance"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "The visible plan already defines Spark Streaming developer interfaces, a MessageBus receiver, an XD module type and a controllable driver. These integration boundaries must not be reported as forgotten tasks.",
    "XD-1470 supplies a concrete Jackson classloader conflict and XD-718 describes parent-last classloading, but the supplied Spark tasks do not state their library layout or cross-classloader types. A new library conflict cannot be inferred from dependency similarity alone.",
    "XD-1783 concerns cleanup after a departing deployment target, and XD-1318 concerns batch-database initialization order. The visible Spark design does not establish those same dependencies or failure paths.",
    "The root, XD-2466 and all implementation descriptions are unknown, so current acceptance and lifecycle coverage cannot be determined."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-718** (`tawos-v1.1:3082`), created 2013-08-20T09:49:11.000000Z
  - Title: "\"Use ParentLastClassLoader to create the Modules ApplicationContext.\""
  - Description: "\"The ParentLastClassloader is located in the spring-hadoop project.  It will resolve classes first looking at the child context and then the parent.  This works well for XD since the we want and dependencies of the module to be considered first and if not found, resolve against the parent. It would be possible to even include other versions of .jars already in the parent classloaders (e.g. Spring Integration jars), but for now, we will not immediately test that case.  SimpleModule needs to change to that we can pass in the classloader to use for creating the application context. The current implementation creates a GenericApplicationContext as a field initializer...that should change to be in the ctor.  ModuleDeployer should implement .BeanClassLoaderAware.  The classloader passed in to the BeanClassLoaderAware callback will be used as the ‘parent’ when creating the ParentLastClassloader.    The URL[] to pass into ParentLastClassloader should be ‘null’ or an empty array in this case of an older style module.  (Hopefully ParentLastClassloader  allows that type of fallback).  *Implementation Suggestions:* The ModuleDeployer code is where the application context for the module is defi"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1470** (`tawos-v1.1:2337`), created 2014-04-01T15:26:24.000000Z
  - Title: "\"Rationalize inclusion of JSON jars in xd/lib and in modules\""
  - Description: "To avoid CL conflicts, a short term solution to this problem is to make sure that there is only one copy of jackson related classes and have them live in xd/lib.  \n\nusing \njackson-core-2.3.2.jar\njackson-databind-2.3.2.jar\njackson-core-asl-1.9.13.jar\njackson-mapper-asl-1.9.13.jar\n\nare the latest versions and the ones to use.\n\nThere maybe other libraries that we duplicate in the same manner, we will need to investigate as well as part of another issue.\n\nTypical error is:\n\njava.lang.LinkageError: loader constraint violation: when resolving method \"org.springframework.http.converter.json.MappingJackson2HttpMessageConverter.setObjectMapper(Lcom/fasterxml/jackson/databind/ObjectMapper;)V\" the class loader (instance of org/springframework/xd/module/support/ParentLastURLClassLoader) of the current class, org/springframework/social/twitter/api/impl/TwitterTemplate, and the class loader (instance of sun/misc/Launcher$AppClassLoader) for resolved class, org/springframework/http/converter/json/MappingJackson2HttpMessageConverter, have different Class objects for the type com/fasterxml/jackson/databind/ObjectMapper used in the signature\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1472** (`tawos-v1.1:2335`), created 2014-04-02T05:47:35.000000Z
  - Title: "\"Let modules define a default value for --inputType option\""
  - Description: "\"If a module e.g. always expects the payload of the message to be of a certain java type if would be good for documentation and convenience reasons in order to specify a default value for the --inputType option.   documentation = output for module info convenience = we could e.g. support to always accept a Json payload (or automatic message payload conversion once it is extensible)  currently, adding options.inputType.default to the module's property file has no effect  I've also tried to \"\"redefine\"\" it using options.inputType.description This leads to the following exception:  Command failed org.springframework.xd.rest.client.impl.SpringXDException: Module option named 'outputType' is present in several delegates: [org.springframework.xd.module.options.SimpleModuleOptionsMetadata@3c1d635a, FlattenedCompositeModuleOptionsMetadata [outputType] => PojoModuleOptionsMetadata backed by class org.springframework.xd.dirt.plugins.stream.ModuleTypeConversionPluginMetadataResolver$OutputOptionsMetadata, defining options [[ModuleOption [name=outputType, type=class org.springframework.util.MimeType, defaultValue=null, description=how this module should emit messages it produces]]] [inputType]"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1783** (`tawos-v1.1:2028`), created 2014-05-30T15:32:29.000000Z
  - Title: "Make failed deployment cleanup more robust"
  - Description: "When a deployment fails, the supervisor will clean up failed deployment attempts. If the deployment path is removed while the supervisor is waiting (for instance if the target container departs the cluster) then a NoNodeException will be thrown:\n\n{code}\n17:22:59,702  WARN ContainersPathChildrenCache-0 server.ModuleDeploymentWriter:361 - Error while cleaning up failed deployment /deployments/modules/40494bdb-0d8c-4b5d-a895-bf94432d9d3b/s.sink.log-1\norg.apache.zookeeper.KeeperException$NoNodeException: KeeperErrorCode = NoNode for /xd/deployments/modules/40494bdb-0d8c-4b5d-a895-bf94432d9d3b/s.sink.log-1\n\tat org.apache.zookeeper.KeeperException.create(KeeperException.java:111)\n\tat org.apache.zookeeper.KeeperException.create(KeeperException.java:51)\n\tat org.apache.zookeeper.ZooKeeper.delete(ZooKeeper.java:873)\n\tat org.apache.curator.framework.imps.DeleteBuilderImpl$5.call(DeleteBuilderImpl.java:239)\n\tat org.apache.curator.framework.imps.DeleteBuilderImpl$5.call(DeleteBuilderImpl.java:234)\n\tat org.apache.curator.RetryLoop.callWithRetry(RetryLoop.java:107)\n\tat org.apache.curator.framework.imps.DeleteBuilderImpl.pathInForeground(DeleteBuilderImpl.java:230)\n\tat org.apache.curator.framework"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2232** (`tawos-v1.1:1588`), created 2014-10-12T12:50:40.000000Z
  - Title: null
  - Description: "Often it is useful to have access to the median value for fields of a data stream since they are more robust with respect to outliers.\n\nThe median is defined as the value of a dataset such that, when sorted, 50% of the data is smaller than the value and 50% of the data is larger then the value. Ordinarily this is difficult to calculate on a stream because it requires the collection and sorting of all data.\n\nThe median of a data stream can be approximated with a technique called stochastic averaging. To approximate the median value of a data stream one could use the following approach:\nGiven the current estimate of the median {{M}}. If the next observed value in the stream is larger than {{M}}, increase the current estimate by {{r}} (= the learning rate). If it is smaller, decrease the estimate by {{r}}. When {{M}} is close to the median, it increases as often as it decreases, and therefore it stabilizes.\n\n\nThe following example shows a primitive implementation of the above mentioned algorithm in groovy (to be placed under ${XD_HOME}/modules/processor/scripts).\n{code:groovy}\nimport org.springframework.xd.tuple.TupleBuilder;\nimport org.springframework.xd.tuple.Tuple;\n\n/**\n * Stochast"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: ["description"]
- **XD-2326** (`tawos-v1.1:1494`), created 2014-11-10T06:44:19.000000Z
  - Title: "\"Can't create stream running on Windows\""
  - Description: "\"Trying to test on Windows and getting the following exception when createing a stream - 'stream create --name tictoc --definition \"\"time | log'  {code} 09:34:20,789 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - XD Home: C:\\Test\\spring-xd-1.1.0.BUILD-SNAPSHOT\\xd\\bin\\.. 09:34:20,790 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - Transport: local 09:34:20,790 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - XD config location: file:C:\\Test\\spring-xd-1.1.0.BUILD-SNAPSHOT\\xd\\bin\\../config// 09:34:20,790 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - XD config names: servers,application 09:34:20,793 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - XD module config location: file:C:\\Test\\spring-xd-1.1.0.BUILD-SNAPSHOT\\xd\\bin\\../config//mo dules/ 09:34:20,794 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - XD module config name: modules 09:34:20,795 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - Admin web UI: http://Seattle:9393/admin-ui 09:34:20,797 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - Zookeeper at: localhost:64424 09:34:20,798 1.1.0.SNAP  INFO main util.XdConfigLoggingInitializer - Zookeeper namespace: xd 09:3"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2375** (`tawos-v1.1:1447`), created 2014-11-18T17:11:08.000000Z
  - Title: "Research reactor-stream integration options"
  - Description: "As a user, I'd like to have a _reactor-stream_ processor module so that I can ingest data using XD source modules and process them as time-window operations. \n\n*Example 1:*\nhttp | reactor-stream --timeWindow=10s --field=payload.sensorData --expressions=min,avg\n\nThis would give you 10 second time window of the min and avg values.\n\n*Example 2:*\nReactor as a module\n\n*Example 3:*\nIntegration with Spark streaming and reactor"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1081** (`tawos-v1.1:2726`), created 2013-11-18T20:24:04.000000Z
  - Title: "\"Create documentation on the lifcycle of a job in XD\""
  - Description: "\"This should go in the first section of the Batch Job documentation.  Here is a rough suggestion  The lifecycle of a job in XD.  1. Register a job module with the MoudleRegistry by putting a XML/jar files in the $XD_HOME/modules/jobs directory. 2. Create a job definition from a job module by providing a name and properties that apply to all job instances can be configured at this point.  The job is not yet deployed 3. Deploy the job to an xd-container.  A job instance can not be created by sending a message to a job queue that contains optional runtime job parameters 4. Launch a job by sending a message to the job queue with job parametres.  A Job Instance is created, representing a specific run of the job.  A Job Instance is the Job Definition plus the runtime job parameters.  You can query for the Job Instances associated with a given job name 5. The job is executed creating a Job Exection object that captures the success or failure of the job.  You can query for the Job Executions associated with a given job name. 6. Undeploy a job.  This removes the job from xd-container.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1222** (`tawos-v1.1:2585`), created 2014-01-13T11:12:11.000000Z
  - Title: "\"Duplicate MBean server definition by MBeanExportingPlugin\""
  - Description: "\"The MBeanServer is referred by XD admin/launcher when JMX is enabled (by setting --jmxEnabled option) and this is defined in xd-global-beans.xml.  The MBeans that are exposed by the modules also use the same MBeanServer define above and there is a duplicate MBeanServer definition (from jmx/common.xml) which the MBeanExportingPlugin adds as a component to the module which doesn't seem to be needed.  Also, currently the flag \"\"jmxEnabled\"\" is generic and used by adminserver/launcher as well as the module MBeanExportingPlugin. If we have a separate flag to enable the JMX *only* for modules then, a separate definition of MBeanServer could be necessary. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1262** (`tawos-v1.1:2545`), created 2014-01-22T10:45:01.000000Z
  - Title: "\"Provide a clean way to get a reference to the MessageBus running in SingleNodeApplication\""
  - Description: "Currently the message bus is only obtained via Module.getComponent(MessageBus.class). Stream testing scenarios that depend on sending and receiving payloads via named channels do not require a deployed module instance per se, but any stream flow control uses the MessageBus directly. Getting a deployed module instance in general is expensive, e.g., you have to wait for the module to deploy asynchronously, whereas the MessageBus implementation could be known a priori when the application starts. An improvement would be to ask the container for its MessageBus."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1318** (`tawos-v1.1:2489`), created 2014-02-12T16:03:13.000000Z
  - Title: "\"XD container can not be started before the admin server\""
  - Description: "\"The job single partitioned step support (from singlestep-partitioner-support.xml) has the batch job DAOs (loaded from batch.xml).  During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes).   Here is the exception:  15:30:03,600  INFO main xml.XmlBeanDefinitionReader:316 - Loading XML bean definitions from class path resource [META-INF/spring-xd/batch/batch.xml] 15:30:06,154  WARN main annotation.ConfigurationClassEnhancer:318 - @Bean method StepScopeConfiguration.stepScope is non-static and returns an object assignable to Spring's BeanFactoryPostProcessor interface. This will result in a failure to process annotations such as @Autowired, @Resource and @PostConstruct within the method's declaring @Configuration class. Add the 'static' modifier to this method to avoid these container lifecycle issues; see @Bean Javadoc for complete details 15:30:06,705  INFO main support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker:309 - Bean 'org.springframework.xd.dirt.server.ParentConfiguration$JmxConfiguration' of type [class org.springframework.xd.dirt.server.ParentConfigurat"
  - Unknown fields: []
  - Truncated fields: ["description"]

### Unresolved labelling questions

- What classloader, lifecycle and MessageBus ownership contracts are specified in the missing descriptions, and which existing acceptance tests cover them?

## XD-2476 (train)

Historical cutoff: 2014-12-09T14:57:39.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `cfc3b1f22dd14cfcf5f3477575d698392be0a123453f949839e934e659118b1b`

Source input identity SHA-256: `da39ca02dbd5008c1633b8d0a46eb6690f9bf54b6cc426147723eca21c9c2637`

### Supplied historical plan

- **XD-2476** (`tawos-v1.1:1348`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2430** (`tawos-v1.1:1394`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2477** (`tawos-v1.1:1347`)
  - Title: "Add support to stop existing Sqoop jobs"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []
- **XD-2478** (`tawos-v1.1:1346`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2479** (`tawos-v1.1:1345`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "status", "estimate"]
  - Truncated fields: []
- **XD-2480** (`tawos-v1.1:1344`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2477 explicitly adds stopping existing Sqoop jobs; stopping support is already planned and must not be labelled absent.",
    "XD-1793 reports stale Jobstore records after failed creation/deletion, and XD-742 describes ordinary job-management APIs. Their text does not establish two comparable Sqoop cancellation failures or confirm that Sqoop uses the same cleanup mechanism.",
    "Unknown root and other member text prevent determining the intended stop/cancel contract; the available estimate and broad job topics do not establish delivery risk."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1238** (`tawos-v1.1:2569`), created 2014-01-14T22:50:35.000000Z
  - Title: "Add to Acceptance Test EC2 CI build plan a stage that stops any existing CI EC2 deployments"
  - Description: "\"Add a stage to the plan that will stop any instances that the CI process may have started before and relaunch a 2 node install based on rabbit.  https://build.springsource.org/browse/XD-ATEC2 was created as an empty shell.  The running of across different transports will be handled in a separate story along with adding a stage to run a 'hello world' acceptance test.  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1575** (`tawos-v1.1:2233`), created 2014-04-14T15:42:10.000000Z
  - Title: "\"Add UDP support to reactor-syslog source module\""
  - Description: "\"Currently the reactor-syslog source module only supports TCP.  Once we add UDP support, we can probably remove the existing syslog-tcp and syslog-udp modules.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1793** (`tawos-v1.1:2018`), created 2014-06-02T10:03:42.000000Z
  - Title: "Jobs  are not completely removed from Jobstore "
  - Description: "\"Deploy Type: Admin/Container on EC2 (Rabbit Transport) SHA: 8fba31d  [Steps to reproduce] 1) Using Rabbit 3.3 above create a user that does not have privileges to write to / * sudo rabbitmqctl add_user joe password * (omit this step) sudo rabbitmqctl set_permissions -p / joe \"\".*\"\" \"\".*\"\" \"\".*\"\" 2) Set the rabbitmq user name and password * export spring_rabbitmq_username=acctest * export spring_rabbitmq_password=acctest23 3) Start container. 4) Create stream or job \"\"foo\"\" 5) Error will occur 6) delete stream or job \"\"foo\"\" 7)  stop container 8) set privilege * sudo rabbitmqctl set_permissions -p / joe \"\".*\"\" \"\".*\"\" \"\".*\"\" 9) Start container 10) create stream or job \"\"foo\"\" 11)  System will report that foo exists.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1864** (`tawos-v1.1:1948`), created 2014-06-19T12:02:56.000000Z
  - Title: "Add paging support for UI list views"
  - Description: "As a user, I'd like to have _paging_ support so that I can scroll through the list of streams, jobs and containers. \n\nCurrently the following error is thrown when we cross >20 rows:\n\nhttp://localhost:9393/jobs/definitions.json\n\nJSON Response:\n{code:xml}\n[\n\t{\n\t\tlinks: [ ],\n\t\tlogref: \"IllegalStateException\",\n\t\tmessage: \"Not all instances were looked at\"\n\t}\n]\n{code}\n\nStack trace:\n{code}\n15:51:21,931 ERROR http-nio-9393-exec-9 rest.RestControllerAdvice - Caught exception while handling a request\njava.lang.IllegalStateException: Not all instances were looked at\n\tat org.springframework.util.Assert.state(Assert.java:385)\n{code}"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1916** (`tawos-v1.1:1897`), created 2014-07-07T07:56:44.000000Z
  - Title: "Batch jobs using Spring Batch MongoDB support require adding MongoDB dependencies to the shared libs folder"
  - Description: "\"Using the MongoDB out-of-the-box capabilities of Spring Batch such as MongoItemReader and MongoItemWriter require that spring-data-mongodb and mongo-driver are added to xd/libs.  The above mentioned classes have dependencies on classes found in mongo-driver and spring-data-mongodb. Due to the fact that Spring Batch classes are loaded in the parent class loader, adding the complementary jars to the module will not make their dependencies visible to the deployment, resulting in a NoClassDefFoundError on spring-data-mongodb classes in this scenario.  There are a few possible solutions:   - requiring the user to add the missing jars to the shared libs folder - this is the straightforward solution, but has the disadvantage of putting the onus on enhancing the distribution on the user (who must have knowledge of the proper version(s) to include); - including the missing jars in the distribution (which can potentially increase its size to satisfy an optional scenario); - increasing the granularity of the packaged Spring Batch distribution and allowing the users to add the classes on demand;  Essentially, this applies to any other dependencies of Spring Batch that are not part of the dist"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2068** (`tawos-v1.1:1747`), created 2014-08-06T05:34:23.000000Z
  - Title: "\"Add support for specifying an undeploy-condition for stream definitions\""
  - Description: "In some scenarios like when performing exploratory data-analysis on streaming data one often create a stream, keep it running for some time (or until some condition is met) and then stop the stream and start to investigate the collected data.\n\nIt would be cool to be able to specify some undeploy condition, like e.g. a timeout after x minutes, no. of events collected, a specific counter past a given threshold, file-size greater then x etc."
  - Unknown fields: []
  - Truncated fields: []
- **XD-2083** (`tawos-v1.1:1732`), created 2014-08-20T10:05:48.000000Z
  - Title: "\"singlestep-partition-support needs to allow grid size to be configurable\""
  - Description: "\"h3.  Narrative As a developer, I need to be able to configure a partitioned job's grid size so that the correct number of partitions are created (the current code is hard coded to 1 for the grid size).  h3.  Acceptance Criteria # Expose the gridSize attribute of the {{MessageChannelPartitionHandler}} as an option.  h3.  Assumptions # Existing OOTB jobs should not be impacted by this given they don't use the grid size. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-349** (`tawos-v1.1:3441`), created 2013-07-01T08:26:27.000000Z
  - Title: "\"Trigger - Add support for date-based one-time execution\""
  - Description: "\"Currently Jobs can be either executed using cron expression or immediately at once. We should also support the one-time scheduling of jobs in the future.  Would this possibly require us to implement schedule-persistence? That could severely impact story-points.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-671** (`tawos-v1.1:3128`), created 2013-08-12T07:41:19.000000Z
  - Title: "Add support for dynamic routing"
  - Description: "\"It should be possible to create streams like the following which rely upon named channel support and dynamic routing capabilities:  {code} http | somerouter :x > xtransformer | hdfs :y > ytransformer | hdfs {code}  The 'somerouter' processor could return \"\"x\"\" or \"\"y\"\" which determines the downstream path for each message.  This should be implemented in such a way that any developer adding a router module would only need to deal with existing Spring Integration semantics (in this case, only considering the return of \"\"x\"\" or \"\"y\"\" - whether it be SpEL or a POJO method invocation). Perhaps in the plugin that modifies a module context, we could simply add a new ChannelResolver implementation (by adding that ChannelResolver as a bean and/or a BeanPostProcessor that configures that as the resolver for any router, if necessary). That ChannelResolver would have a reference to the ChannelRegistry so that the router actually sends its messages to those shared channels. The shared channels themselves would have been created as long as a valid downstream flow has been defined.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-73** (`tawos-v1.1:3708`), created 2013-05-17T11:03:29.000000Z
  - Title: "\"add test to start/stop stream server\""
  - Description: "\"in additional to existing tests that check for redis connection, we need to add tests that start/stop stream server. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-742** (`tawos-v1.1:3058`), created 2013-08-22T14:18:55.000000Z
  - Title: "\"REST API for Job Management\""
  - Description: "Spring Batch Admin provides a complete, but outdated implementation style, which covers the full administrative lifecycle of batch jobs, their creation, stop/start, and retrieving information about previous job executions and the status of currently executing job executions.  SpringXD has a different way of deploying, starting, and stopping jobs - by sending messages to containers that run the batch job.  However, the reporting state of a job is still stored in a common job repository.  The purpose of this story is to take the first step to merging in the existing code base that focuses only on the retrieval of information from Spring Batch Admin’s Job controller.\n\nThe current ‘REST API’ style of these commands should stay as close to the original spring batch admin style as possible.  There are several reasons for this\n1. It works, and time to springone is short, and we mgmt has expectations around deliverables that we must strive to meet.\n2. It gives Andrew a working contract to start developing a UI\n3. We can take on this technical debt, but refactor after RC1 and before GA while and deliver end-user functionality.  \n\nAttached is the list of endpoints in spring batch admin "
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Must stopping a Sqoop job cancel an external Sqoop execution, change XD job state, or both?
- Does XD-2430 or another supplied member define the stop acknowledgment and restart behavior?

## XD-2500 (train)

Historical cutoff: 2014-12-13T07:43:00.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `6d46b831daa6dab3cd71410ca280c166a4ccd02748f86a616d1220228707ec8e`

Source input identity SHA-256: `06a9ec72eebf9d477b7b73836edf7741c234292c1ab920c1c482bc0fca018641`

### Supplied historical plan

- **XD-2500** (`tawos-v1.1:1324`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2501** (`tawos-v1.1:1323`)
  - Title: "Upgrade to Boot 1.2.0 RELEASE and the depdencies"
  - Description: null
  - Unknown fields: ["description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2501 already includes upgrading Boot 1.2.0 RELEASE and its dependencies; a warning that dependency updates are missing would contradict the plan.",
    "XD-1967 records broken distro-specific Hadoop jars and XD-1464 records an unexpected Groovy version from snapshots, but the supplied text does not show that the Boot RC-to-release change repeats those resolution mechanisms.",
    "XD-2270 shows the earlier Boot 1.2.0 RC1 upgrade marked Done, and multiple completed Hadoop upgrades include explicit compatibility tests; these counterexamples prevent inferring a validation gap from the short current title."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2270** (`tawos-v1.1:1550`), created 2014-10-23T12:13:03.000000Z
  - Title: "Upgrade to Spring Boot 1.2.0"
  - Description: "As to prepare for 1.1 release, we would like to upgrade to Spring Boot 1.2.0 (RC1) (depends on Spring 4.1.2) so that we can leverage the new features, enhancement and bug fixes. \n\n[Spring Boot Milestones|https://github.com/spring-projects/spring-boot/milestones]"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1041** (`tawos-v1.1:2765`), created 2013-11-08T09:12:37.000000Z
  - Title: "\"Upgrade to Spring for Apache Hadoop 1.0.2.RELEASE and Pivotal HD 1.1\""
  - Description: "\"Make sure the sinks and jobs work against Pivotal HD 1.1\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2177** (`tawos-v1.1:1642`), created 2014-09-25T10:47:23.000000Z
  - Title: "Add support for Pivotal HD 2.1 (XD 1.0.2 Release)"
  - Description: "*XD 1.0.2 Release + PHD 2.1 Upgrade - Action Items:*\n\n* Update to SHDP 2.0.3\n* Add Hadoop 2.5 (hadoop25)\n* Change PHD 2.x from phd20 to phd21\n* Test PHD 2.0 with phd21 \n* Document that both PHD 2.1 and PHD 2.0 is supported with phd21\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2307** (`tawos-v1.1:1513`), created 2014-11-03T11:28:08.000000Z
  - Title: "Add support for PHD 2.1 (XD 1.1 M1 Release)"
  - Description: "\"*XD 1.1 M1 Release + PHD 2.1 Upgrade - Action Items:*  * Update to SHDP 2.1.M2,  * Add Hadoop 2.5 (hadoop25) * Remove hadoop22 * Remove PHD 1.0 (phd1)  * Change PHD 2.x from phd20 to phd21 * Test PHD 2.0 with phd21\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1318** (`tawos-v1.1:2489`), created 2014-02-12T16:03:13.000000Z
  - Title: "\"XD container can not be started before the admin server\""
  - Description: "\"The job single partitioned step support (from singlestep-partitioner-support.xml) has the batch job DAOs (loaded from batch.xml).  During container startup, when the jobExecutionDao bean is initialized it makes the db connection to the underlying batch database (which admin server initializes).   Here is the exception:  15:30:03,600  INFO main xml.XmlBeanDefinitionReader:316 - Loading XML bean definitions from class path resource [META-INF/spring-xd/batch/batch.xml] 15:30:06,154  WARN main annotation.ConfigurationClassEnhancer:318 - @Bean method StepScopeConfiguration.stepScope is non-static and returns an object assignable to Spring's BeanFactoryPostProcessor interface. This will result in a failure to process annotations such as @Autowired, @Resource and @PostConstruct within the method's declaring @Configuration class. Add the 'static' modifier to this method to avoid these container lifecycle issues; see @Bean Javadoc for complete details 15:30:06,705  INFO main support.PostProcessorRegistrationDelegate$BeanPostProcessorChecker:309 - Bean 'org.springframework.xd.dirt.server.ParentConfiguration$JmxConfiguration' of type [class org.springframework.xd.dirt.server.ParentConfigurat"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1394** (`tawos-v1.1:2413`), created 2014-03-13T05:39:53.000000Z
  - Title: "\"Upgrade to Spring 4.0.2.RELEASE\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1464** (`tawos-v1.1:2343`), created 2014-03-31T22:51:51.000000Z
  - Title: "\"Upgrade to Spring Integration 4.0.0.M4\""
  - Description: "\"Currently on snapshots, which is oddly pulling in groovy 2.1.0\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1944** (`tawos-v1.1:1869`), created 2014-07-10T07:29:49.000000Z
  - Title: "\"Error deploying stream when admin running and container arrives after stream deployment request\""
  - Description: "\"Steps to reproduce:  1. start xd-admin  2. start shell and create and deploy stream (\"\"time | hdfs\"\")  3. start container  I got:  [2014-07-10 09:10:29.019] boot - 19923  INFO [DeploymentSupervisorCacheListener-0] --- InitialDeploymentListener: Path cache event: /deployments/streams/test, type: CHILD_ADDED [2014-07-10 09:10:29.137] boot - 19923  INFO [Deployer] --- StreamDeploymentListener: Deploying stream Stream{name='test'} [2014-07-10 09:10:29.146] boot - 19923  WARN [Deployer] --- StreamDeploymentListener: No containers available for deployment of stream test [2014-07-10 09:10:29.146] boot - 19923  INFO [Deployer] --- StreamDeploymentListener: Stream Stream{name='test'} deployment attempt complete [2014-07-10 09:11:08.003] boot - 19923  INFO [DeploymentSupervisorCacheListener-0] --- ContainerListener: Path cache event: /containers/007c2bcc-13f4-466e-95d3-bd926bb456ea, type: CHILD_ADDED [2014-07-10 09:11:08.006] boot - 19923  INFO [DeploymentSupervisorCacheListener-0] --- ArrivingContainerModuleRedeployer: Container arrived: 007c2bcc-13f4-466e-95d3-bd926bb456ea [2014-07-10 09:11:08.176] boot - 19923 ERROR [DeploymentSupervisorCacheListener-0] --- PathChildrenCache:  org.apache"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1958** (`tawos-v1.1:1855`), created 2014-07-11T13:59:18.000000Z
  - Title: "\"filejdbc job broken in distributed mode\""
  - Description: "The filejdbc job is broken in distributed mode (redis and rabbit)\n\nTo reproduce:\n\nexport XD_TRANSPORT=rabbit\n\nstart xd-admin\nstart xd-container\n\nstart shell and create this job:\n\n{code}\n>job create mydata --definition \"filejdbc --names=col1,col2,col3 --resources=file:///home/trisberg/Test/input/*.csv --initializeDatabase=true\" --deploy\n>job launch mydata\n{code}\n\nresults in JOB starting but never completing:\n\n{code}\n>job execution list\n  Id  Job Name  Start Time                            Step Execution Count  Execution Status  Deployment Status  Definition Status\n  --  --------  ------------------------------------  --------------------  ----------------  -----------------  -----------------\n    0  mydata      2014-07-11 15:44:33 America/New_York  0                     STARTED           Deployed           Exists\n{code}\n\nSteps:\n\n{code}\nStep Id\tStep Name\tReads\tWrites\tCommits\tRollbacks\tDuration\tStatus\tDetails\n0\tstep1-master\t0\t0\t0\t0\t-1405349644032 ms\tEXECUTING\t\n1\tstep1-master:partition0\t292\t292\t3\t0\t302 ms\tCOMPLETED\t\n2\tstep1-master:partition1\t292\t292\t3\t0\t203 ms\tCOMPLETED\t\n3\tstep1-master:partition2\t292\t292\t3\t0\t193 ms\tCOMPLETED\t\n{code}\n\nWhen using Redis, I also get this stacktrace in cont"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1967** (`tawos-v1.1:1847`), created 2014-07-14T14:01:05.000000Z
  - Title: "Dependendcies for Hadoop distros are broken "
  - Description: "\"We used to have distro specific jars i the lib/[distro] directory. That is no longer working and all distros seem to contain mostly the same version (hadoop 2.2.0 dependencies)  This is the list for phd1 now:  avro-1.7.5.jar hadoop-annotations-2.2.0.jar hadoop-auth-2.2.0.jar hadoop-client-2.0.5-alpha-gphd-2.1.0.0.jar hadoop-common-2.2.0.jar hadoop-distcp-2.2.0.jar hadoop-hdfs-2.2.0.jar hadoop-mapreduce-client-app-2.2.0.jar hadoop-mapreduce-client-common-2.2.0.jar hadoop-mapreduce-client-core-2.2.0.jar hadoop-mapreduce-client-jobclient-2.2.0.jar hadoop-mapreduce-client-shuffle-2.2.0.jar hadoop-streaming-2.2.0.jar hadoop-yarn-api-2.2.0.jar hadoop-yarn-client-2.2.0.jar hadoop-yarn-common-2.2.0.jar hadoop-yarn-server-common-2.2.0.jar hadoop-yarn-server-nodemanager-2.2.0.jar jersey-core-1.9.jar jersey-server-1.9.jar jetty-util-6.1.26.jar protobuf-java-2.5.0.jar spring-data-hadoop-2.0.1.RELEASE.jar spring-data-hadoop-batch-2.0.1.RELEASE.jar spring-data-hadoop-core-2.0.1.RELEASE.jar spring-data-hadoop-store-2.0.1.RELEASE.jar \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2050** (`tawos-v1.1:1764`), created 2014-08-04T11:43:28.000000Z
  - Title: "\"HDFS sink Partition Path causing writes to be slower in certain cases\""
  - Description: "\"I have not tested this on M7 but I believe it is the case with latest release as well.  Stream definition 1: stream create logIngestion --definition \"\"rabbit --queues=demo --host=<rabbitmq-broker> | script --location=linemerge.groovy | hdfs --rollover=10M --idleTimeout=10000 --fileUuid=true --directory=/data/loganalysis --partitionPath=path(payload.split('\\u0001')[1],dateFormat('yyyy/MM/dd/HH',payload.split('\\u0001')[0],'yyyyMMddHHmmss'))\"\"  we noticed this was causing writes to be slower  Stream definition 2: stream create logIngestion --definition \"\"rabbit --queues=demo --host=<rabbitmq-broker> | script --location=linemerge.groovy | hdfs --rollover=10M --idleTimeout=10000 --fileUuid=true --directory=/data/loganalysis \"\"  but this definition caused the writes to be much faster.  Please note this was just a one time test I did and not reproduced multiple times.   Janne also seems to have reproduced this in another use case.  Thanks Girish\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2119** (`tawos-v1.1:1696`), created 2014-09-16T12:25:06.000000Z
  - Title: "Support accessing admin server endpoints over HTTPS"
  - Description: "As a user, I'd like to have the option to enable HTTPS so that I can access XD's Admin server [endpoints|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] over secured communication.\n\nTechnical Implementation:\n\nThis functionality is available in Spring Boot 1.2.0 M1 and has been backported into the 1.1.x branch to be released under Spring 1.1.7.  We can test against 1.1.7 SNAPSHOT.\n\nWorking through the way to update the build file to pick up a new version of boot is a bit tricky :("
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which managed and transitive versions change between the completed Boot RC1 upgrade and 1.2.0 RELEASE?
- Does the existing upgrade test matrix verify distro-specific Hadoop jars, distributed jobs and HTTPS behavior after dependency resolution?

## XD-2540 (train)

Historical cutoff: 2015-01-05T09:26:26.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `ef907367e955333e834b21e75c2ca06e2624659e47d75a06f02174fb26b0682f`

Source input identity SHA-256: `235a1dcd5a2a96f57292a5a76d578f49d71bd0b4b0dcfd3edcc2af1f2a99cbd1`

### Supplied historical plan

- **XD-2540** (`tawos-v1.1:1287`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2541** (`tawos-v1.1:1286`)
  - Title: "Define developer facing interfaces for RxJava processors"
  - Description: "As a user, I'd like to implement the core interface contract so that I can create a processor module that uses RxJava API."
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2542** (`tawos-v1.1:1285`)
  - Title: "Create ReactorMessageHandler for RxJava based XD processor/sink modules"
  - Description: "As a user, I'd like to have a flexible RxJava module so that it can act both as a sink as well as a processor. \n"
  - Unknown fields: ["type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2541 already defines a developer-facing RxJava interface contract and XD-2542 already creates a flexible processor/sink handler. Unknown root text does not establish that a particular contract behavior is omitted.",
    "XD-2481 asks for Reactor error-handling considerations and XD-2487 assigns error handling to another ticket. These are design precedents, not two demonstrated RxJava failures or evidence that the planned contract cannot address errors.",
    "XD-2135 proposes explicit error-channel support, but the supplied input does not establish that RxJava modules depend on this uncompleted feature or that errors will be lost. No such dependency was inferred from current links."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2481** (`tawos-v1.1:1343`), created 2014-12-08T16:34:30.000000Z
  - Title: "\"Define developer facing interfaces for Reactor Stream processors\""
  - Description: "\"What is the core interface contract users will be exposed to when creating a processor module that uses Reactor's Stream API.   Some consideration for error handling should be considered as it maybe outside normal exception throwing signatures.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2487** (`tawos-v1.1:1337`), created 2014-12-09T12:06:36.000000Z
  - Title: "\"Create ReactorMessageHandler for Reactor based XD processor/sink modules\""
  - Description: "\"The module should be flexible to act as a sink as well as a processor.  ErrorHandling will be considered as part of another JIRA\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2135** (`tawos-v1.1:1680`), created 2014-09-16T17:03:53.000000Z
  - Title: "\"Add explicit \"\"error channel\"\" support\""
  - Description: "As a user, I'd like to have the option to explicitly define/configure \"error channel\" so that I can stage and route the errors/exceptions through the dedicated channel and continue ingestion.\n\n*Scenario:*\n* 'http' source ingest \n* failure at either source, processor, or sink module\n* regardless of whether it is a custom module or not, traverse through the exception to propagate the actual _Caused by:..._, stage the error as payload, and route it to the error channel\n\n*Example Configuration:*\n* error channel definition similar to \"topic.errors.stream.module\"\n* configure custom exception similar to \"catch=**Exception\"\n* exception hierarchy\n** GlobalException\n** DefaultException\n** ModuleSpecificException\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2375** (`tawos-v1.1:1447`), created 2014-11-18T17:11:08.000000Z
  - Title: "Research reactor-stream integration options"
  - Description: "As a user, I'd like to have a _reactor-stream_ processor module so that I can ingest data using XD source modules and process them as time-window operations. \n\n*Example 1:*\nhttp | reactor-stream --timeWindow=10s --field=payload.sensorData --expressions=min,avg\n\nThis would give you 10 second time window of the min and avg values.\n\n*Example 2:*\nReactor as a module\n\n*Example 3:*\nIntegration with Spark streaming and reactor"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-245** (`tawos-v1.1:3539`), created 2013-06-17T12:31:26.000000Z
  - Title: "\"Deploy Batch Jobs on XD\""
  - Description: "h2. Narrative\nAs a developer, I need a way to deploy job configurations as well as the related custom code to XD.\n\nh2.  Acceptance Criteria\n# Provide the ability to register jobs that have been deployed as modules via something like {{curl -d \"job\" http://localhost:8080/streams/myJob}} where job is the name of the job definition located in /modules/job and myJob is the name of the resulting registered job\n# Confirm that both \"regular\" jobs and Spring Hadoop based jobs can be packaged/run."
  - Unknown fields: []
  - Truncated fields: []
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1420** (`tawos-v1.1:2387`), created 2014-03-19T03:52:28.000000Z
  - Title: "Create a JPMML module that will evaluate a model."
  - Description: "\"A analytical model should be evaluated as a processor in a stream.  The model evaluation will take the input variables from a Tuple and output variable will be placed into the tuple as well.  A strawman of the stream definition can be   stream create --definition \"\" SOURCE | jpmml ‘fraud-detection’ | PROC1 … | PROCN \"\" --name stream1  Using profiles and playing all implementations of the analytical model in the same module lib directory, it maybe possible to select one of multiple implementations in the form   \"\" SOURCE | analytic --library=jpmml --name=‘fraud-detection’ | PROC1 … | PROCN \"\"  such that the core module name is the same but parameterized by what library type to use.  This may be problematic in that different libraries may have incompatible dependencies.  The analytical model can define the names of input and output fields, so at a minimum a name is required, however to easily adapt a given analytic model evaluation to a specific source modules output, it seems desirable to specify which fields are to be used as input, overriding the names of the input fields could be done in a manner such as   jpmml –name=linear-regresssion –inputFields=a,b,c \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\n*Scope of this spike:*\n\n* Research Spring Security and Spring Boot and the OOTB features \n* Design considerations and approach for XD\n* Developer experience\n** How users will be configuring security credentials?\n** How DSL shell will be handled?\n** How Admin UI will be handled?"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2053** (`tawos-v1.1:1761`), created 2014-08-04T15:51:32.000000Z
  - Title: null
  - Description: "As an user, I'd like to have OOTB sink modules to integrate with various data sources to egest data using Spring XD. \n\nNote:\nThe OOTB support, however, is limited to currently available Spring Integration adapters.\n\nAcceptance Criteria:\n- User should be able to list the 'new sink' through DSL commands \n- User should be able to optionally choose the \"new sink\" adapters for stream creation using XD shell\n- User should see appropriate error messages if the required attributes are missing while creating a stream with the 'new sink' module\n- After successful stream creation with the 'new sink' module, the definition should be included in stream listing\n- REST endpoints should include 'new sink' definitions\n- Data ingested into 'new sink' should be validated for accurateness\n- Appropriate error/exception message needs logged if there's any problem ingesting data into 'new sink' module"
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2090** (`tawos-v1.1:1725`), created 2014-08-22T16:08:46.000000Z
  - Title: "Custom module packaging strategy"
  - Description: "As a user, I'd like to have guidance to create custom modules so that I can align the development practices with recommended approach. \n\n11/20: Update: Scope of this task is to create an example to demonstrate and document the capability."
  - Unknown fields: []
  - Truncated fields: []
- **XD-2128** (`tawos-v1.1:1687`), created 2014-09-16T16:21:29.000000Z
  - Title: "\"Add WebSocket source\""
  - Description: "\"As a user, I'd like to have the option of _WebSocket_ source module so that I can create a interactive communication channel between user's browser session and the runtime to ingest browser based events and activities.  *Reference:* [Spring Integration WebSocket Support|https://github.com/spring-projects/spring-integration/tree/master/spring-integration-websocket/src]\""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What cutoff-bound contract decisions specify RxJava asynchronous error signalling, propagation and termination semantics?
- Does any supplied historical evidence identify an actual failure or explicit incompatible handler contract that applies to this planned RxJava integration?

## XD-2629 (train)

Historical cutoff: 2015-01-22T07:42:10.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `d8ff7212e690788a0caa4318f70b3bddc052f37a2d68060f8af3bf5bac4ce3a6`

Source input identity SHA-256: `e835f8ebbd822806d1097868e6ae195de0a82d7579332e4e29a861ee3d55bb73`

### Supplied historical plan

- **XD-2629** (`tawos-v1.1:1199`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2630** (`tawos-v1.1:1198`)
  - Title: "Spike: Study scope to develop Ambari plugin for XD"
  - Description: "As a SysAdmin, I'd like to use Ambari plugin so that I can provision, manage, and monitor Spring XD clusters using the same tool I use for Hadoop clusters."
  - Unknown fields: ["type"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2630 explicitly scopes a study of an Ambari plugin for provisioning, management and monitoring. The supplied plan does not yet specify plugin implementation or library choices.",
    "XD-1530 and XD-1857 demonstrate different Hadoop API/classpath failures, but their supplied descriptions do not establish that the proposed Ambari study or eventual plugin uses those same dependencies.",
    "XD-1695 and XD-2143 describe security research and Basic Auth work marked Done; XD-2288 is a port-discovery spike. These precedents do not establish an unmet Ambari dependency or an access-control failure.",
    "The unknown root scope and bounded prior sample cannot establish further deliverables, schedule effects or a missing implementation task."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\n*Scope of this spike:*\n\n* Research Spring Security and Spring Boot and the OOTB features \n* Design considerations and approach for XD\n* Developer experience\n** How users will be configuring security credentials?\n** How DSL shell will be handled?\n** How Admin UI will be handled?"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2288** (`tawos-v1.1:1532`), created 2014-10-27T16:11:42.000000Z
  - Title: "\"Research how to use 'admin' server ports from ZK\""
  - Description: "\"As a user, I'd like to have the ability to access the random port (generated by tomcat) of the admin server (via _xd-shell_) so that I can point to the server and continue my interactions.   *Spike Details:* * Research whether connecting _xd-shell_ directly to ZK is a good approach or have a LB in-charge for the interaction. * How about something other than a pointer to a ZK directory in the shell for folks to experiment a bit before getting a LB involved?  *Note:* On some hadoop/hdfs setups access to zk is mandatory from hdfs client libs. There are some HA and federation setups which would anyway require xd shell to get access to zk if fs shell commands are used. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2304** (`tawos-v1.1:1516`), created 2014-11-03T07:25:42.000000Z
  - Title: "Research refactoring effort for Kafka source to use simple consumer instead of high-level API"
  - Description: "As a user, I'd like to use Kafka source through simple consumer API (as opposed to high-level) so that I can gain full control to offsets and partition assignment deterministically.\n\n*Spike scope*:\n- Study simple consumer API functionality\n- Document findings, approach and next steps"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1972** (`tawos-v1.1:1842`), created 2014-07-14T20:52:32.000000Z
  - Title: "\"Add ability to define nested jobs\""
  - Description: "h3.  Narrative\nAs a developer, I need to be able to create a Spring XD job module that consists of a job orchestrating the execution of other Spring Batch jobs using the Spring Batch Job Step (see section 5.3.6 here: http://docs.spring.io/spring-batch/reference/html/configureStep.html) within the same module definition.\n\nh3.  Acceptance Criteria\n# Define the \"contract\" for a job module\n## Currently the contract consists of a single job definition within the assembled {{ApplicationContext}} ({{context.getBean(Job.class)}}).\n## The new version will need to document what job definition within the assembled {{ApplicationContext}} should be run as the entry point.  I'm assuming it would be by id ({{context.getBean(\"job\")}} for example) of the job but am open to other options.\n# A custom job module that orchestrates multiple Spring Batch jobs via Job steps should be able to be deployed and executed as a single Spring XD module.\n## Spring XD launches the job that conforms to the previously defined \"contract\".\n## Spring Batch manages the execution of the child jobs.\n# The existing OOTB jobs should work under the new \"contract\".\n\nh3.  Assumptions\n# The UI should \"just work\" in that child jo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2143** (`tawos-v1.1:1672`), created 2014-09-17T21:33:37.000000Z
  - Title: "\"Add Basic Auth support\""
  - Description: "As a user, I'd like to have the option of _Basic Auth_ so that I'm challenged to provide _user name_ and _password_ when making a request.\n\nTechnical Implementation:\n\nThis functionality is provided in Spring Boot 1.1.x, it should be a matter of adding the spring boot security starter dependency to the spring-xd-dirt project.  \n\nIt will be controlled using the spring boot property server.basic.enabled = true/false.  Our default in application.yml for this property should be false.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2308** (`tawos-v1.1:1512`), created 2014-11-03T12:01:44.000000Z
  - Title: "\"Create sample app to demonstrate Kafka integration\""
  - Description: "\"As a user, I'd like to have a sample app (GitHub project) so that I can use it as a reference while provisioning Spring XD cluster with Kafka.  Consider: * Kafka as message bus * Kafka as source  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-705** (`tawos-v1.1:3095`), created 2013-08-19T10:27:10.000000Z
  - Title: "\"A batch job can be launched by sending a message on a channel\""
  - Description: "*Description*  When a job is ‘created’ in SpringXD, a ‘control-channel’ for that job is also created.  The listener for that channel will receive a message, be able to take the ‘jobParameters’ and other launch information from the message, and be able to launch/run the job.\n\nNOTE: I can see a few other stories that should probably be made to break this up after writing it. I put estimate of 10 for now, but we should break this up.  Here are some suggestions\n\n1. create ‘data only’ JobParametersBean equivalent with primitive types\n2. create jobLauncher source\n3. create jobParameterTransformer processor\n4. Refactoring of ChannelRegistry’s aliasHing to use a callback strategy.\n\n\n*Implementation Suggestions*\n\njob create --name helloWorldJob --definition \"myjob --somePropertyToOverride=someValue\n\n* This would not execute the batch job immediately, but instead register the job definition and deploys a “jobLauncher” and the job definition to an XD-Container.\n\n* The XD-Container that receives the deploy request message will create a module application context, will also create a channel with the Channel registry named after the job, e.g. :myJob.  This should be a pub/sub channel from the po"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-841** (`tawos-v1.1:2959`), created 2013-09-11T18:07:02.000000Z
  - Title: "\"Create a packaging model for custom modules\""
  - Description: "Like just discussed after the Spring One session, it would be nice to have a packaging model for custom modules. Instead of putting all libs in one directory and an XML in another, it could be a fat jar including some metadata file pointing to either an XML or to a JavaConfig configuration class inside the jar.\nSome more words why I think it's important to have something like that:\nSpring XD can be very well used in the enterprise, and at least for job modules it's likely to have some dependencies. So what do you have to do now to deploy such a module? Build a jar with your build process, then get it from your repository, unpack it and somehow find the relevant XML to copy it into the appropriate folder, then inspect the POM to find out what all the dependencies are, direct and transient, and get them from your repository to copy them into the appropriate folder. And of course, copy the jar. And when using Spring XD in distributed mode, you have to do it several times.\nWith the approach mentioned above you just build your fat jar with your build process and distribute it to all your nodes, nothing complicated.\n\nAnd if you implement it like that it's easy to have a JavaConfig suppor"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-100** (`tawos-v1.1:3682`), created 2013-05-20T23:28:13.000000Z
  - Title: "\"Rename Tuple class in spring-xd-tuple\""
  - Description: "\"The Tuple classes in Reactor follow the more traditional data structure concept of Tuples, an immutable fixed length sequence of values where each value can have different types.  They are ordered and can often be access by index.  An example in a static language is the Tuple class found in .NET http://msdn.microsoft.com/en-us/library/system.tuple.aspx or in Scala http://www.tutorialspoint.com/scala/scala_tuples.htm  Using this standard definition of a Tuple, they do not support named values.  There is also a different tuple class instance for each length, e.g. Tuple<T1,T2>, Tuple<T1,T2,T3>.  The Tuple class in XD is more like a record or named tuple.   Python has a named tuple concept - http://docs.python.org/2/library/collections.html#collections.namedtuple  and http://stackoverflow.com/questions/1490413/languages-that-allow-named-tuples shows that other languages use the term 'Record' for a 'named tuple' - Haskell, Standard ML, OCaml, and F#.  http://en.wikibooks.org/wiki/F_Sharp_Programming/Tuples_and_Records#Defining_Records  So boiling it all down, to avoid conflicts of names, and also to open up the possibility of using Reactor tuples as keys (instead of strings for names),"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1369** (`tawos-v1.1:2438`), created 2014-03-05T02:28:49.000000Z
  - Title: "\"Using hdfs sink throwing an error\""
  - Description: "\"I am trying to use HDFS as sink while creating streams and I am encountering the following error :  Please refer attached document : Exception - localhost - 8020.txt   The fs.default.name set in hadoop.properties is : fs.default.name=hdfs://localhost:8020  I have also tried the following variation in the hadoop.properties file : fs.default.name=hdfs://127.0.0.2:8020 fs.default.name=hdfs://127.0.0.2:50070  Using these values are also throwing me exceptions as mentioned in the following files attached :  Exception - 127.0.0.2 - 8020.txt  Exception - 127.0.0.2 - 50070.txt   We are using : Pivotal HD 1.0.1 spring-xd-1.0.0.M5-dist  Kindly let us know the way around for this issue.   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1530** (`tawos-v1.1:2277`), created 2014-04-10T10:53:39.000000Z
  - Title: "\"Error when removing HDFS files in shell\""
  - Description: "I get this:\n\n{code}\nxd:>hadoop fs rm /xd/test/time-3.log\nError: run HDFS shell failed. Message is: org.apache.hadoop.fs.FileStatus.isDirectory()Z\n{code}\n\nso far I have seen this with --hadoopDistro hdp13 and hadoop12\n\nsame command works fine using shell from M5 release\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1857** (`tawos-v1.1:1955`), created 2014-06-17T09:08:43.000000Z
  - Title: "\"Can't use webhdfs with hdfs sink\""
  - Description: "\"When using spring.hadoop.fsUri set to webhdfs://localhost/ I'm getting an error:  java.lang.NoClassDefFoundError: javax/ws/rs/core/MediaType  including the following in xd/lib seems to fix this: - jersey-core-1.9.jar - jersey-server-1.9.jar \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What cutoff-available study success criteria define the Ambari/XD integration boundary and intended findings?
- Does any supplied historical incident directly concern Ambari integration, rather than general Hadoop packaging or administrative configuration?

## XD-2660 (train)

Historical cutoff: 2015-01-30T09:52:04.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `bb16cb88143d7f809612b7d62f828adce9e74cdcb8ec37d80bc51e2642ee1f13`

Source input identity SHA-256: `eb8c1fa99c6c2999827958091c22729da5cdf98c2fc29fda019d77bf83daff37`

### Supplied historical plan

- **XD-2660** (`tawos-v1.1:1168`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2661** (`tawos-v1.1:1167`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2662** (`tawos-v1.1:1166`)
  - Title: null
  - Description: "As a developer, I'd like to add test coverage so that I can evaluate XD functionalities in Windows."
  - Unknown fields: ["title", "type", "status", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2662 explicitly adds Windows test coverage, so Windows validation is planned rather than demonstrably missing. The root and XD-2661 descriptions are unknown.",
    "XD-2401 describes failing distributed tests excluded from CI, but no second supplied ticket establishes a comparable Windows failure or a requirement for this Windows plan to repair the distributed CI suite.",
    "Completed YARN, Gemfire, Kafka and analytics acceptance-test stories show existing scenario checks; their topic similarity cannot establish a gap in Windows coverage."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2566** (`tawos-v1.1:1261`), created 2015-01-07T07:46:00.000000Z
  - Title: "\"Add support to test XD on YARN in EC2\""
  - Description: "\"As a developer, I'd like to have acceptance test coverage for XD + YARN on EC2 so that I can verify simple XD features running on YARN on every build cycle.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2401** (`tawos-v1.1:1423`), created 2014-11-23T14:21:42.000000Z
  - Title: "Include distributed tests in CI builds"
  - Description: "As a developer, I'd like to include DIRT tests as part of the CI builds so that we can automatically evaluate DIRT features and functionalities.\n\n*Scope:*\nThe distributed (single host / multi-jvm) tests are failing at the moment; hence, they're not included in CI. Perhaps related to high CPU startup  (XD-2548) issues observed recently. "
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2209** (`tawos-v1.1:1610`), created 2014-10-03T17:25:37.000000Z
  - Title: "\"Add acceptance test to include Gemfire use case\""
  - Description: "\"To enrich acceptance test, I'd like to have basic coverage to evaluate Gemfire use cases.   An example would be to ingest data from HTTP source and write it to Gemfire server.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2212** (`tawos-v1.1:1607`), created 2014-10-03T17:32:33.000000Z
  - Title: "\"Add acceptance tests for FieldValueCounts and AggregateCounts\""
  - Description: "\"To enrich acceptance tests, I'd like to have test coverage to evaluate _FieldValueCounts_ and _AggregateCounts_ for a given scenario.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2333** (`tawos-v1.1:1487`), created 2014-11-12T12:29:42.000000Z
  - Title: "Add test coverage for Kafka source and sink modules"
  - Description: "As a PM, I'd like to have test coverage for both Kafka source and sink modules so that we can assert its functionality as part of the CI builds. "
  - Unknown fields: []
  - Truncated fields: []
- **XD-2664** (`tawos-v1.1:1164`), created 2015-01-29T11:13:00.000000Z
  - Title: "Create samples to demonstrate new features and functionalities"
  - Description: "As a developer, I'd like to build samples using XD so that we can demonstrate some of the new features included in 1.1 release.\n\n*Areas to consider*\n* Spark streaming\n* Spark (MLLIb, ..)\n* Sqoop\n* Reactive-streams\n"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: []
- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\n*Scope of this spike:*\n\n* Research Spring Security and Spring Boot and the OOTB features \n* Design considerations and approach for XD\n* Developer experience\n** How users will be configuring security credentials?\n** How DSL shell will be handled?\n** How Admin UI will be handled?"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2119** (`tawos-v1.1:1696`), created 2014-09-16T12:25:06.000000Z
  - Title: "Support accessing admin server endpoints over HTTPS"
  - Description: "As a user, I'd like to have the option to enable HTTPS so that I can access XD's Admin server [endpoints|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] over secured communication.\n\nTechnical Implementation:\n\nThis functionality is available in Spring Boot 1.2.0 M1 and has been backported into the 1.1.x branch to be released under Spring 1.1.7.  We can test against 1.1.7 SNAPSHOT.\n\nWorking through the way to update the build file to pick up a new version of boot is a bit tricky :("
  - Unknown fields: []
  - Truncated fields: []
- **XD-2143** (`tawos-v1.1:1672`), created 2014-09-17T21:33:37.000000Z
  - Title: "\"Add Basic Auth support\""
  - Description: "As a user, I'd like to have the option of _Basic Auth_ so that I'm challenged to provide _user name_ and _password_ when making a request.\n\nTechnical Implementation:\n\nThis functionality is provided in Spring Boot 1.1.x, it should be a matter of adding the spring boot security starter dependency to the spring-xd-dirt project.  \n\nIt will be controlled using the spring boot property server.basic.enabled = true/false.  Our default in application.yml for this property should be false.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2169** (`tawos-v1.1:1650`), created 2014-09-22T11:12:37.000000Z
  - Title: "\"Evaluate Spring Boot dependency upgrade\""
  - Description: "\"As a user, I'd like to evaluate Spring Boot dependency upgrades so that I can make sure there aren't any side effects or impacts to existing functionalities. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2205** (`tawos-v1.1:1614`), created 2014-10-03T14:49:28.000000Z
  - Title: "\"Add Python processor\""
  - Description: "\"As a user, I'd like to have a _Python_ processor so that I can efficiently perform data computations and statistical analysis.   Investigate the right approach (native or via stdin/stdout) that fits Spring XD model.  [Integrate Java and Python|https://wiki.python.org/moin/IntegratingPythonWithOtherLanguages#Java]\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2208** (`tawos-v1.1:1611`), created 2014-10-03T17:22:38.000000Z
  - Title: "\"Add acceptance test to extract and assert payload from JSON object\""
  - Description: "\"To enrich the acceptance test, I'd like to evaluate JSON object to extract \"\"Good\"\" and \"\"Bad\"\" instead of just relying on a basic filter test to assert the payload content. \""
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- Which Windows versions, shell scripts, transports and module scenarios does XD-2662 intend to exercise?
- Is reusing the distributed test suite part of the Windows plan, and if so are the XD-2401 failures relevant on Windows?

## XD-2692 (train)

Historical cutoff: 2015-02-06T08:51:31.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `12ca6d25ed109278b0fb8f0293011c21ac6011da3a56bad793deffe23b797db3`

Source input identity SHA-256: `525df1bfaffef2937dc324e52a74b46ec4d1a0105e594df16e866fa05236c4f1`

### Supplied historical plan

- **XD-2692** (`tawos-v1.1:1136`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2573** (`tawos-v1.1:1254`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2596** (`tawos-v1.1:1232`)
  - Title: "\"KafkaMessageBusTests#testCompression failing\""
  - Description: "\"Intermittent. Reported on ubuntu and OS/x\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2693** (`tawos-v1.1:1135`)
  - Title: "\"Run Kafka tests with Kafka Server as separate process\""
  - Description: "As a developer, I'd like to run Kafka tests with Kafka Server as a separate running process so that I can improve build experience.\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2698** (`tawos-v1.1:1130`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2596 explicitly targets intermittent Kafka compression-test failures on Ubuntu and OS X, while XD-2693 already moves the Kafka server into a separate process and is historically marked Done. Neither is omitted work.",
    "XD-2104 describes a UI test/server single-process failure, but that mechanism is not established for the remaining Kafka compression failure. XD-2401 records failing distributed tests excluded from CI and only suggests high startup CPU as a possible cause. These do not jointly establish a new Kafka-specific gap.",
    "XD-2462 explicitly provides prior Kafka message-bus CI acceptance coverage. The unknown root, XD-2573 and XD-2698 prevent inferring which remaining checks or process-management changes are absent."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2403** (`tawos-v1.1:1421`), created 2014-11-23T14:46:09.000000Z
  - Title: "Create Windows based CI infrastructure"
  - Description: "As a build manager, I'd like to setup CI infrastructure so that I can run integration tests in Windows OS automatically as we commit-trigger new builds. "
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2119** (`tawos-v1.1:1696`), created 2014-09-16T12:25:06.000000Z
  - Title: "Support accessing admin server endpoints over HTTPS"
  - Description: "As a user, I'd like to have the option to enable HTTPS so that I can access XD's Admin server [endpoints|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] over secured communication.\n\nTechnical Implementation:\n\nThis functionality is available in Spring Boot 1.2.0 M1 and has been backported into the 1.1.x branch to be released under Spring 1.1.7.  We can test against 1.1.7 SNAPSHOT.\n\nWorking through the way to update the build file to pick up a new version of boot is a bit tricky :("
  - Unknown fields: []
  - Truncated fields: []
- **XD-2401** (`tawos-v1.1:1423`), created 2014-11-23T14:21:42.000000Z
  - Title: "Include distributed tests in CI builds"
  - Description: "As a developer, I'd like to include DIRT tests as part of the CI builds so that we can automatically evaluate DIRT features and functionalities.\n\n*Scope:*\nThe distributed (single host / multi-jvm) tests are failing at the moment; hence, they're not included in CI. Perhaps related to high CPU startup  (XD-2548) issues observed recently. "
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2566** (`tawos-v1.1:1261`), created 2015-01-07T07:46:00.000000Z
  - Title: "\"Add support to test XD on YARN in EC2\""
  - Description: "\"As a developer, I'd like to have acceptance test coverage for XD + YARN on EC2 so that I can verify simple XD features running on YARN on every build cycle.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2662** (`tawos-v1.1:1166`), created 2015-01-29T09:55:48.000000Z
  - Title: "\"Add test coverage for Windows in EC2\""
  - Description: "As a developer, I'd like to run acceptance test coverage in Windows so that I can evaluate XD functionalities.\n\nThe scope is to provision Windows image in EC2 and run acceptance test in the environment. Potentially also try to create this as CI build."
  - Unknown fields: []
  - Truncated fields: []
- **XD-2681** (`tawos-v1.1:1147`), created 2015-02-02T12:16:06.000000Z
  - Title: null
  - Description: "As a developer, I'd like to refer to wiki so that I can configure machines with recommended _ulimit_ setting for XD's distributed setup.\n\n*Note:*\nRecommended _ulimit_ setting is 10K under \"Troubleshooting\" (new) section\n\n*Exception:* (reason to increase _ulimit_)\n8:25:52,266 1.1.0.SNAP ERROR DeploymentsPathChildrenCache-0 server.DeploymentListener - Exception deploying module\njava.lang.IllegalStateException: java.io.FileNotFoundException: /var/vcap/data/packages/springxd/ee02bd3482eeb620a65862fb54e1f23fcece8022.1-bd\na341640a5de2f922fd3db906ce504b85819c1e/spring-xd-1.1.0.BUILD-SNAPSHOT/xd/config/modules/modules.yml (Too many open files)"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\n*Scope of this spike:*\n\n* Research Spring Security and Spring Boot and the OOTB features \n* Design considerations and approach for XD\n* Developer experience\n** How users will be configuring security credentials?\n** How DSL shell will be handled?\n** How Admin UI will be handled?"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2104** (`tawos-v1.1:1711`), created 2014-08-25T20:24:25.000000Z
  - Title: "\"Investigate and Fix E2E test execution for grunt task \"\"test:e2e\"\"\""
  - Description: "\"As a result of fixing XD-2015 we still cannot execute:  {code} grunt test:e2e {code}  Basically running the tests AND the server together in one process fails. We see the following error: *Fatal error: socket hang up*.  If we separate the protractor execution into 2 separate steps, the tests pass:  {code} grunt serve (one console window) grunt protractor:run (second console window) {code}  In the *grunt serve* window, you can still observe *Fatal error: socket hang up* being printed out but the tests execute successfully.   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2143** (`tawos-v1.1:1672`), created 2014-09-17T21:33:37.000000Z
  - Title: "\"Add Basic Auth support\""
  - Description: "As a user, I'd like to have the option of _Basic Auth_ so that I'm challenged to provide _user name_ and _password_ when making a request.\n\nTechnical Implementation:\n\nThis functionality is provided in Spring Boot 1.1.x, it should be a matter of adding the spring boot security starter dependency to the spring-xd-dirt project.  \n\nIt will be controlled using the spring boot property server.basic.enabled = true/false.  Our default in application.yml for this property should be false.\n\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2400** (`tawos-v1.1:1424`), created 2014-11-23T14:19:31.000000Z
  - Title: "\"Research options to improve CI reliability\""
  - Description: "\"As a build master, I'd like to research CI options so that I can improve CI build stability and reliability.  *Potential Option:* [npm-cache|https://github.com/swarajban/npm-cache]  Caching previously installed dependencies, _npm-cache_ doesn't require downloading the internet each time we build.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2462** (`tawos-v1.1:1362`), created 2014-12-07T15:08:11.000000Z
  - Title: "Acceptance test for Kafka as a message bus"
  - Description: "\"As a QA, I'd like to include acceptance test coverage for _Kafka_ as a message bus so that I can validate the functionality as part of every CI build.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2562** (`tawos-v1.1:1265`), created 2015-01-06T09:26:42.000000Z
  - Title: "\"Move the Hadoop test dependencies to a different project\""
  - Description: "As a developer, I'd like to isolate the Hadoop tests in a different project so that the DIRT project doesn't have to depend upon, thus eliminating the incorrect CP file generation in eclipse. "
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What failure evidence distinguishes the remaining compression issue from the separate-process change, and what scope does XD-2698 add?

## XD-2963 (validation)

Historical cutoff: 2015-04-18T10:23:43.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `193be86a38a92d18181fce02b8f4a782e35959ef90788f04cfb63cf2fe24f89d`

Source input identity SHA-256: `b406ae929785cb30837ce2a6624c805e2268573304ba05f49a64e2bd16a35f30`

### Supplied historical plan

- **XD-2963** (`tawos-v1.1:865`)
  - Title: "\"Add support for stateful stream processing\""
  - Description: ""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2964** (`tawos-v1.1:864`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []
- **XD-2965** (`tawos-v1.1:863`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "Only the broad stateful-stream-processing title is recoverable; both observed children have unknown title and description. No state backend, consistency contract, restart behavior or implementation is supplied.",
    "XD-1338 describes partitioning to colocate messages with in-process state and XD-2232 describes an approximate streaming median. These are relevant designs, not evidence that this plan omits state locality or uses an incorrect algorithm.",
    "XD-1707 reports a Rabbit dynamic-router failure and XD-1742 reports unwanted String conversion. Neither is tied to the unspecified stateful-processing design, and they do not establish a common state-management failure mechanism."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-1060** (`tawos-v1.1:2746`), created 2013-11-12T08:28:43.000000Z
  - Title: "Add support for Hortonworks Data Platform 2.0"
  - Description: "\"(apologies if a ticket already exists for this, but I didn't see one)  I spun up the Hortonworks Data Platform 2.0 sandbox, but see it isn't supported by Spring XD yet.  How hard would it be to add these Distro's in?  Is it just a matter of dropping in a lib folder for hadoop22 and/or hdp20, and allowing those and options to be passed in via the --hadoopDistro option?  I'm currently trying to work through the following tutorial, but using the HDP 2.0 sandbox instead of the 1.3 sandbox  http://hortonworks.com/hadoop-tutorial/using-spring-xd-to-stream-tweets-to-hadoop-for-sentiment-analysis/  Thanks!\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1338** (`tawos-v1.1:2469`), created 2014-02-20T10:14:16.000000Z
  - Title: "Deployment manifest to support partitioning a stream"
  - Description: "\"We need a methodology for providing partitioning hints.  A current proposal uses message headers to provide:  * partition_key – the item to partition on * destination_region – what to target  In the proposal the developer used \"\"partition_key\"\" to route the stream message to the node where data was stored in process.  This was done so downstream stream operations could work on the data with out suffering any network IO.  The \"\"destination_region\"\" was used to target the type of data the downstream streams were going to use in their stream processing.   \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1447** (`tawos-v1.1:2360`), created 2014-03-25T11:03:24.000000Z
  - Title: "\"Add documentation for a 'stdin' source module\""
  - Description: "\"In order to support ingestion from stdin, the suggested approach is to do the following.  xd:>stream create --definition \"\"tcp --decoder=LF | log\"\" --name foo  $ cat my.log | netcat localhost 1234  So while this is really a tcp based ingestion case, once can use pipe or redirect of stdin/err in order to achieve the same goal.  It should appear as a source module in the docs on par with other source modules in its own section. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1482** (`tawos-v1.1:2325`), created 2014-04-03T09:33:35.000000Z
  - Title: "Add initial support for DeploymentManifest"
  - Description: "The REST API for deploy should accept parameters, which provide manifest key/value pairs (e.g. ?http.instances=5). Ultimately we will want to support passing a named manifest which had been stored previously.\n\nThe 'stream deploy' shell command should support passing these as --options.\n\nInitially we should support [modulename].instances and [modulename].group."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1650** (`tawos-v1.1:2160`), created 2014-04-29T12:58:35.000000Z
  - Title: "Update HDFS sink to accept a partition strategy"
  - Description: "Add configuration for the partition strategy to HDFS sink to support writing files into subdirectories based on a partition key provided in the header or field in the message of the stream data.\n\nThe writing using HDFS Store DataWriter should pass in the partition key value to be used for the write operation.\n\nPartition configuration could be made available to the sink using a  --format parameter:\n\nthat could then be used in XML config like:\n{code}\n      expression=\"new java.text.SimpleDateFormat('${format}').format(${timestamp})\n{code}\nSimilar to the time source."
  - Unknown fields: []
  - Truncated fields: []
- **XD-1706** (`tawos-v1.1:2104`), created 2014-05-14T08:41:47.000000Z
  - Title: "\"Add tab completion for named channels (i.e., queue:xyz >)\""
  - Description: "\"Tab completion doesn't currently list/support \"\"queue\"\" as a source.  For example if typing the following stream: stream create b --definition \"\"queue:bar > transform --expression=payload+'-bar' | log\"\" --deploy  Tab completion doesn't recognize or suggest \"\"queue\"\" or anything after it until after the first bar \"\"|\"\".    The same applies to named channels, \"\"queue\"\", as a sink.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-1707** (`tawos-v1.1:2103`), created 2014-05-14T08:55:46.000000Z
  - Title: "\"The Dynamic Router example in the docs throws an exception with Rabbit Transport\""
  - Description: "\"The example in the M6 documentation for the Dynamic Router (here: http://docs.spring.io/spring-xd/docs/1.0.0.M6/reference/html/#dynamic-router) for the SpEL-Based Routing throws an exception when processing the message (from the HTTP post) saying \"\"No bean named 'queue:foo' is defined\"\", when using RabbitMQ as the transport.  I do not know a workaround.  Steps to reproduce: 1) Run RabbitMQ locally 2) Run xd-singlenode --transport rabbit 3) xd:>stream create f --definition \"\"queue:foo > transform --expression=payload+'-foo' | log\"\" --deploy  xd:>stream create b --definition \"\"queue:bar > transform --expression=payload+'-bar' | log\"\" --deploy  xd:>stream create r --definition \"\"http | router --expression=payload.contains('a')?'queue:foo':'queue:bar'\"\" --deploy  4) xd:>http post --data \"\"a\"\"  5) This should give a stacktrace: Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No bean named 'queue:foo' is defined  at org.springframework.beans.factory.support.DefaultListableBeanFactory.getBeanDefinition(DefaultListableBeanFactory.java:641)  at org.springframework.beans.factory.support.AbstractBeanFactory.getMergedLocalBeanDefinition(AbstractBeanFactory.java:115"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1742** (`tawos-v1.1:2069`), created 2014-05-21T10:37:23.000000Z
  - Title: "Remove toStringTransformer from tcp Source; Add Binary Support to the http Source"
  - Description: "The TCP source unconditionally converts to String. This prevents binary transfers.\n\nRemove the transformer; if the user wants a String; (s)he can use\n\n{{tcp --outputType=text/plain;charset=UTF-8}} (assuming the byte stream has valid UTF-8 encoding).\n\nAnother option would be to add a {{--binary}} option, but since conversion can already handle it, it's probably better to use that.\n\nOn the other hand, a {{--binary}} option would enable backwards compatibility.\n\nThe http source also unconditionally converts to String."
  - Unknown fields: []
  - Truncated fields: []
- **XD-2068** (`tawos-v1.1:1747`), created 2014-08-06T05:34:23.000000Z
  - Title: "\"Add support for specifying an undeploy-condition for stream definitions\""
  - Description: "In some scenarios like when performing exploratory data-analysis on streaming data one often create a stream, keep it running for some time (or until some condition is met) and then stop the stream and start to investigate the collected data.\n\nIt would be cool to be able to specify some undeploy condition, like e.g. a timeout after x minutes, no. of events collected, a specific counter past a given threshold, file-size greater then x etc."
  - Unknown fields: []
  - Truncated fields: []
- **XD-2135** (`tawos-v1.1:1680`), created 2014-09-16T17:03:53.000000Z
  - Title: "\"Add explicit \"\"error channel\"\" support\""
  - Description: "As a user, I'd like to have the option to explicitly define/configure \"error channel\" so that I can stage and route the errors/exceptions through the dedicated channel and continue ingestion.\n\n*Scenario:*\n* 'http' source ingest \n* failure at either source, processor, or sink module\n* regardless of whether it is a custom module or not, traverse through the exception to propagate the actual _Caused by:..._, stage the error as payload, and route it to the error channel\n\n*Example Configuration:*\n* error channel definition similar to \"topic.errors.stream.module\"\n* configure custom exception similar to \"catch=**Exception\"\n* exception hierarchy\n** GlobalException\n** DefaultException\n** ModuleSpecificException\n"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2232** (`tawos-v1.1:1588`), created 2014-10-12T12:50:40.000000Z
  - Title: "\"Add support for estimating the median value of a data stream.\""
  - Description: "Often it is useful to have access to the median value for fields of a data stream since they are more robust with respect to outliers.\n\nThe median is defined as the value of a dataset such that, when sorted, 50% of the data is smaller than the value and 50% of the data is larger then the value. Ordinarily this is difficult to calculate on a stream because it requires the collection and sorting of all data.\n\nThe median of a data stream can be approximated with a technique called stochastic averaging. To approximate the median value of a data stream one could use the following approach:\nGiven the current estimate of the median {{M}}. If the next observed value in the stream is larger than {{M}}, increase the current estimate by {{r}} (= the learning rate). If it is smaller, decrease the estimate by {{r}}. When {{M}} is close to the median, it increases as often as it decreases, and therefore it stabilizes.\n\n\nThe following example shows a primitive implementation of the above mentioned algorithm in groovy (to be placed under ${XD_HOME}/modules/processor/scripts).\n{code:groovy}\nimport org.springframework.xd.tuple.TupleBuilder;\nimport org.springframework.xd.tuple.Tuple;\n\n/**\n * Stochast"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2295** (`tawos-v1.1:1525`), created 2014-10-30T17:02:00.000000Z
  - Title: "\"Add support for audio/video source\""
  - Description: "As a user, I'd like to stream ingest audio and video data so that I can apply predictive analytics algorithms for facial detection.\n\n*Spike scope:*\n* Research the feasibility of implementing [Motion-JPEG|http://en.wikipedia.org/wiki/Motion_JPEG]\n* Design specs on Motion-JPEG format\n\n*Note:* [opencv|http://docs.opencv.org/trunk/doc/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html], although having OOTB support, it is not platform compatible. "
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What state ownership, partitioning, recovery and accuracy semantics are recorded in XD-2964 and XD-2965 before assigning a risk label?

## XD-2978 (validation)

Historical cutoff: 2015-04-23T08:11:43.000000Z

Status: **generated_unreviewed**

Evidence fingerprint: `a47ebb65ffa04cecb064239f3d263e135bbc4f3f319c70b273c91626511c4c70`

Source input identity SHA-256: `c7434b2a7d68e72d3168c22661a20ffe5b2a8cad42850b99dc4b23c323a07089`

### Supplied historical plan

- **XD-2978** (`tawos-v1.1:850`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "status", "estimate"]
  - Truncated fields: []
- **XD-2979** (`tawos-v1.1:849`)
  - Title: "Submit Java receptor client for CF incubation"
  - Description: "As a user, I'd like to use the java receptor client, so I can interact with Diego runtime using the receptor REST APIs.\n\nScope:\n* Complete the remaining refactoring and polishing work\n* Document\n* Submit for CF incubation process"
  - Unknown fields: ["type"]
  - Truncated fields: []
- **XD-2980** (`tawos-v1.1:848`)
  - Title: null
  - Description: null
  - Unknown fields: ["title", "description", "type", "estimate"]
  - Truncated fields: []

### Proposed target

```json
{
  "risks": [],
  "limitations": [
    "XD-2979 explicitly includes remaining refactoring, documentation and CF incubation submission; none of those activities can be labelled missing.",
    "XD-2916 provides one directly relevant completed Receptor client implementation, but no second supplied ticket documents a comparable Receptor or incubation failure mechanism.",
    "The other REST, security, stream cleanup and Hadoop packaging examples concern different interfaces and lifecycles; they do not establish a dependency or validation gap for the Java Receptor client."
  ]
}
```

### Supplied prior evidence for support and counterexample review

- **XD-2916** (`tawos-v1.1:912`), created 2015-04-06T10:51:42.000000Z
  - Title: "\"Create a Java client for Receptor\""
  - Description: "\"As a developer, I'd like to create a [java client|https://github.com/markfisher/receptor-client] for Receptor, so I can interact with Diego runtime via Receptor API calls from XD. \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2304** (`tawos-v1.1:1516`), created 2014-11-03T07:25:42.000000Z
  - Title: "Research refactoring effort for Kafka source to use simple consumer instead of high-level API"
  - Description: "As a user, I'd like to use Kafka source through simple consumer API (as opposed to high-level) so that I can gain full control to offsets and partition assignment deterministically.\n\n*Spike scope*:\n- Study simple consumer API functionality\n- Document findings, approach and next steps"
  - Unknown fields: []
  - Truncated fields: []
- **XD-2154** (`tawos-v1.1:1661`), created 2014-09-19T16:04:57.000000Z
  - Title: null
  - Description: "As a user, I'd like to have a REST API to point and push an archive that includes custom module definitions and configurations so that I don't have to manually move and set it up.\n\n*Scope of this spike:*\n* Assess customer requirement, brainstorm, and document options\n* Socialize with the team to collect feedback\n* Identify phases\n* Create new stories"
  - Unknown fields: ["title", "type", "estimate"]
  - Truncated fields: []
- **XD-2231** (`tawos-v1.1:1589`), created 2014-10-10T13:45:06.000000Z
  - Title: "\"Document job repo schema overrides\""
  - Description: "\"As a user, I'd like to have the flexibility to configure DB creds so that I can use a DB of choice for batch job repository (metadata persistence).   The scope of this task is to have the configuration specifics documented in the wiki.\""
  - Unknown fields: []
  - Truncated fields: []
- **XD-2635** (`tawos-v1.1:1193`), created 2015-01-22T13:35:57.000000Z
  - Title: "\"Update 'partitionColumn' wiki to include mutual exclusiveness of 'sql' and 'tableName' options\""
  - Description: "\"As a user, I'd like to refer to the wiki so that I can create a job with 'partitions' that in turn expects _tableName_ and _columns_ be explicitly included in the job definition.   It is also beneficial to call-out _sql_ and _tableName_ metadata options are mutually exclusive. Following logic in _JdbcHdfsOptionsMetadata_ needs documented.  {code:java} @AssertTrue(message = \"\"Use ('tableName' AND 'columns') when using partition column\"\") boolean isPartitionedWithTableName() {  if (StringUtils.hasText(partitionColumn)) {   return StringUtils.hasText(tableName) && !StringUtils.hasText(sql);  }  else {   return true;  } } {code}  \""
  - Unknown fields: []
  - Truncated fields: []
- **XD-434** (`tawos-v1.1:3360`), created 2013-07-09T11:42:15.000000Z
  - Title: "Consider removing the Topic/Queues when deleting the Stream"
  - Description: "As a user, I'd like to have the option to delete the queues/topics so that we can include an _optional_ attribute as part of the stream destroy command to also clean-up the associated queues/topics.\n\n*Notes:*\n* Spring-AMQP {{RabbitAdmin}} now has a {{getQueueProperties()}} method which returns the number of consumers so it may be possible to use it for this purpose.\n* Consider the possibility of _producers_ and/or _queues_ still containing data\n* Consider the scenario even after the topics/queues are cleaned-up, what to do with fanout exchange?\n\n*Some Further Thoughts*\n* Consider using the upcoming Spring AMQP REST API {{RabbitManagementTemplate}} if the timing is not right, we could temporarily invoke the rabbit REST API directly.\n* Should be optional; perhaps via {{stream destroy foo --clean}}\n* Should this be done by the admin? Or, via a new plugin handling module undeployments - in the rabbit case, undeploying a consumer would check for us being the last consumer and remove the queue/binding/exchange, since we undeploy left->right, everything can be cleaned up on the consumer side.\n* Third option would be new methods on the bus {{cleanConsumer}} etc invoked by the {{StreamPlugi"
  - Unknown fields: ["type", "estimate"]
  - Truncated fields: ["description"]
- **XD-1695** (`tawos-v1.1:2115`), created 2014-05-12T10:35:58.000000Z
  - Title: "Research how to secure Admin's REST endpoints"
  - Description: "As a user, I'd like to have the option to provide security configurations so that I can access REST endpoints in a secured manner. \n\nIdeally, all the listed [REST|https://github.com/spring-projects/spring-xd/wiki/REST-API#xd-resources] endpoints needs to be wrapped within a security layer. \n\n*Scope of this spike:*\n\n* Research Spring Security and Spring Boot and the OOTB features \n* Design considerations and approach for XD\n* Developer experience\n** How users will be configuring security credentials?\n** How DSL shell will be handled?\n** How Admin UI will be handled?"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1738** (`tawos-v1.1:2073`), created 2014-05-20T10:01:20.000000Z
  - Title: "Stream destroy fails to remove if the underlying modules have been removed."
  - Description: "In short if you attempt to destroy a stream that has had its modules removed, the destroy will fail.\n1) So if I create my own processor:x and use the processor in a stream.\n2) I then shutdown the admin and container.\n3) Delete the processor:x from the $XD_HOME/modules directory\n4) Restart the admin and container.\n5) if you do a stream list the stream that used the processor.x is still present.\n6) but you can not delete the stream because of the exception below. \n\n[To Reproduce using Payload Conversion example]\n1) Follow the instructions to install and use the myTupleProcessor module in a stream.\n2) Now shutdown the admin and container\n3) rm -rf $XD_HOME/modules/processor/myTupleProcessor.xml \n4) rm -rf $XD_HOME/lib/payload-conversion.jar\n5) Startup your admin and container\n6) stream all destroy.  Then type 'y'<return>\n   6a) The shell will report ommand failed org.springframework.xd.rest.client.impl.SpringXDException: No content to map due to end-of-input at [Source: java.io.StringReader@5b8bd3d0; line: 1, column: 1]\n   6b) The Admin Server will report\n11:59:43,543 ERROR http-nio-9393-exec-1 rest.RestControllerAdvice:199 - Caught exception while handling a request\norg.springframewo"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-1746** (`tawos-v1.1:2065`), created 2014-05-22T07:55:03.000000Z
  - Title: "Add MVC-aware HTTP source module"
  - Description: "As a developer, I'd like to have an OOTB MVC-aware HTTP module (with embedded tomcat), so I can use this module to leverage spring-mvc and spring-security features, instead of rewriting them within the existing HTTP source module. \n\n* Adds richer support for content-type in the HTTP Source module. See [~<USER> comments: https://github.com/spring-projects/spring-xd/pull/879.\n\n* Adds full header mapping in the source (see comments)\n\n* See SO request: http://stackoverflow.com/questions/29353471/spring-xd-as-a-rest-endpoint"
  - Unknown fields: ["type", "status"]
  - Truncated fields: []
- **XD-1864** (`tawos-v1.1:1948`), created 2014-06-19T12:02:56.000000Z
  - Title: "Add paging support for UI list views"
  - Description: "As a user, I'd like to have _paging_ support so that I can scroll through the list of streams, jobs and containers. \n\nCurrently the following error is thrown when we cross >20 rows:\n\nhttp://localhost:9393/jobs/definitions.json\n\nJSON Response:\n{code:xml}\n[\n\t{\n\t\tlinks: [ ],\n\t\tlogref: \"IllegalStateException\",\n\t\tmessage: \"Not all instances were looked at\"\n\t}\n]\n{code}\n\nStack trace:\n{code}\n15:51:21,931 ERROR http-nio-9393-exec-9 rest.RestControllerAdvice - Caught exception while handling a request\njava.lang.IllegalStateException: Not all instances were looked at\n\tat org.springframework.util.Assert.state(Assert.java:385)\n{code}"
  - Unknown fields: []
  - Truncated fields: []
- **XD-1985** (`tawos-v1.1:1829`), created 2014-07-16T14:46:08.000000Z
  - Title: "Packaging of Guava 17 results in failure to deploy mapreduce job to Hadoop 2.4 based distros"
  - Description: "Trying to deploy the hashtagcount batch sample [1] to Hadoop 2.4.1 or Hortonworks HDP 2.1 fails with an IllegalAccessError exception.\n\nLooks like a Guava versioning issue - Swapping out guava-17.0.jar for guava-11.0.2.jar in the xd/lib directory solves it.\n\nMark P suggested we try 16.0.1 which is what Curator uses and that seems to work as well. \n\nLooking into changing the build to not force 17.0 which is the IO platform version.\n\nhttp://upstream-tracker.org/java/compat_reports/guava/16.0.1_to_17.0/src_compat_report.html \n\n\nI get the following exception:\n\n{code}\n16:42:22,214  INFO Deployer server.JobDeploymentListener - Deployment status for job 'hashtagCountJob': DeploymentStatus{state=deployed}\n16:42:27,315  WARN task-scheduler-2 mapreduce.JobSubmitter - No job jar file set.  User classes may not be found. See Job or Job#setJar(String).\n16:42:27,325 ERROR task-scheduler-2 step.AbstractStep - Encountered an error executing step hashtagcount in job hashtagCountJob\njava.lang.IllegalAccessError: tried to access method com.google.common.base.Stopwatch.<init>()V from class org.apache.hadoop.mapreduce.lib.input.FileInputFormat\n\tat org.apache.hadoop.mapreduce.lib.input.FileInputFormat.ge"
  - Unknown fields: []
  - Truncated fields: ["description"]
- **XD-2090** (`tawos-v1.1:1725`), created 2014-08-22T16:08:46.000000Z
  - Title: "Custom module packaging strategy"
  - Description: "As a user, I'd like to have guidance to create custom modules so that I can align the development practices with recommended approach. \n\n11/20: Update: Scope of this task is to create an example to demonstrate and document the capability."
  - Unknown fields: []
  - Truncated fields: []

### Unresolved labelling questions

- What CF incubation requirements and compatibility tests apply to the client at this cutoff?
- Which remaining refactoring items are covered by XD-2979 and the unknown XD-2980 member?


## Independent assistant decisions

Original and final targets are preserved in `semantic-review.jsonl`. All decisions remain generated and unreviewed by a human.

- **XD-697 — reject**: The two citations describe genuine retry/cleanup faults, and XD-467 is still To Do, but the proposed warning assumes the new harness checks only successful message flow. The root explicitly includes stream testing across transports and nothing limits it to happy-path assertions. Unknown children do not establish missing lifecycle coverage. XD-476 is Done, and no supplied design shows the harness retaining its state-cleanup defect. The conditional test-omission claim is not established by the historical plan.
- **XD-742 — reject**: The plan introduces job retrieval controllers for a UI, but the packet does not establish that their response resources use the failing StreamDefinitionResource marshaller in XD-555 or that the intended UI is served from a different origin as in XD-556. Both prior fixes are Done. Unknown member scope and an unsupplied endpoint attachment cannot establish loss of those fixes or missing compatibility tests. The root explicitly says the original API works; the proposal converts two relevant review questions into unsupported regression predictions.
- **XD-1260 — revise**: XD-1206 is a directly applicable, still-To-Do partitioned-job failure with null persisted StepExecution IDs. The plan concretely introduces multi-node partitioning and MessageBus StepExecutionHandlers, so this is more than a generic regression scenario. However, XD-752 concerns multiple configured batch jobs sharing an XD registry name, not the cause of null step IDs. Narrow the claim to persisted step history and cite the explicitly shared repository constraint in XD-703 alongside the actual failure; do not invent identity corruption in the MessageBus.
- **XD-1317 — retain**: The plan explicitly introduces a YARN Client/AppMaster and XD deployment scripts, so the container-launch boundary is a concrete planned integration change. XD-703 independently identifies the admin as owner of shared repository/schema initialization; XD-1318 documents a container-startup DAO connection failure when the admin has not initialized that database. This is an applicable readiness contract plus an actual failure, rather than merely two related topics or a claim of missing tests. Retain only as the stated conditional integration concern: both tickets are Done, so the existing fix may already make startup order safe and no current defect or omitted work is established. Other supplied tickets concern shell/parser behavior, deployment content or stream lifecycle and do not contradict or further prove this readiness condition.
- **XD-1392 — reject**: XD-1126 concretely changes property naming, but the proposed claim assumes validation only reads names and then infers a regression of completed source-loading/default-precedence defects. XD-1186 concerns YAML classpath shadowing and XD-1194 concerns option-default precedence; neither supplied text connects the naming migration to a changed source-resolution or default-precedence implementation. No incorrect renamed-key mapping or incompatible override contract is demonstrated. Unknown members cannot establish absent effective-value checks.
- **XD-1605 — revise**: The link to the planned behavior is explicit: XD-1497 moves JMX endpoints into management/jolokia, and still-To-Do XD-1496 reports an exception on the management context path. XD-1396 additionally documents JMX/Jolokia-enabled management-context startup behavior, but its completed fix cannot be presumed lost. Narrow the risk to accessibility of the planned management-context route and investigation of the currently reported exception; remove the suggestion that unknown acceptance scope itself establishes an omitted configuration matrix.
- **XD-1606 — reject**: XD-1601 describes naming inconsistencies and the parser, but explicitly says both job:j1 and queue:job:j1 seem to work. It does not supply a final naming change, removal of aliases, or a current failed resolution. XD-641 and XD-1177 are completed tap/source and repeated-module fixes; they show relevant mechanisms but no supplied fact makes this plan re-enter the old failure conditions. The proposed rewrite and loss of parser/broker compatibility are hypothetical design choices, and unknown members cannot establish missing tests.
- **XD-1820 — reject**: The positive assumes acceptance based only on logical transitions, but the plan explicitly says undeploy will stop all modules and supplies no acceptance-test design supporting that assumption. XD-1738 concerns destroy after manual removal of module artifacts; XD-1754 concerns connections retained across Gemfire stream create/destroy cycles. These are real failures, but the supplied evidence does not link either destroy implementation to the planned undeploy state transition or orphaned partition-module redeployment, nor establish that Gemfire is exercised by this change. Grouping them as physical cleanup does not establish the missing shared applicability. Unknown children cannot justify a validation_gap.
- **XD-1821 — revise**: The original assumption that validation covers only ordinary pipes is unsupported and is removed. A narrower compatibility mechanism is grounded in the specific planned StreamConfigParser/StreamDefinition/descriptor refactor: XD-1601 explicitly gives different job versus named-stream prefix semantics and references the same parser channel-resolution path, while XD-641 documents an actual tap-source identity/registration failure. This links a concrete structural change to an explicit existing constraint and an observed failure; it does not infer that tests or source/sink metadata are missing.
- **XD-1832 — reject**: XD-1197 and XD-1493 substantiate command-specific historical completion issues, but the epic already exists to address shell tab-completion issues and both child specifications are unknown. There is no concrete planned implementation restricted to one command family and no evidence its validation is restricted that way. XD-1493 and entity completion XD-670 are Done; retaining their possibility of regression alone would not establish a new gap. XD-796 gives a real command-ambiguity design constraint, but it also describes completed work and no visible target change is tied to it. The conditional missing cross-command matrix therefore exceeds available scope evidence.
- **XD-1875 — reject**: The plan explicitly requests equivalent tests, while no supplied plan text chooses the isolated downstream-injection approach in XD-1228. Inferring loss of externally driven coverage from that optional prior test style and unknown members invents a planned design choice. The two source/Redis incidents are real but Done, and XD-1245 supplies an externally driven acceptance harness. Conditional wording does not establish that this conversion will bypass the affected boundary.
- **XD-2053 — reject**: XD-1912 shows a Rabbit-to-JDBC failure but does not identify type/encoding as its cause. XD-1743 is a completed Tweet class-resolution problem on Rabbit. No supplied plan text specifies Rabbit transport, Tweet/native object payloads, or the same conversion/classloader path for the new ElasticSearch and Redis sinks. The plan already mandates accurate ingested data and appropriate errors. Inferring a validation gap for these new adapters from completed problems in other destination/type combinations generalizes beyond supported applicability.
- **XD-2252 — retain**: The abstention survives challenge. The root explicitly names RabbitMQ PerfTest and XD-2253 explicitly uses iperf on each topology edge, so network-baseline work is already included. XD-1870 and XD-1602 concern configuration resolution inside XD Rabbit/JMS modules; the topology labels do not show that standalone PerfTest or iperf traverses those module configuration paths. XD-1860, XD-1636 and XD-1322 likewise concern XD transport/module configuration rather than a supplied limitation of the baseline tools. No prior excerpt establishes a PerfTest/iperf measurement failure or a relevant cross-tool constraint, and unknown members cannot supply that linkage.
- **XD-2540 — retain**: The abstention is supported after considering the uncited evidence. XD-2481 identifies asynchronous error handling as a design consideration and XD-2487 defers Reactor error handling; neither reports a failure or states what RxJava handlers do. XD-2135 is a desired explicit error-channel feature, not proof of a dependency or lost errors. The visible plan explicitly defines the RxJava core contract and a processor/sink handler, so there is no evidence that those omit asynchronous error propagation. No identical RxJava incident is required, but the supplied design notes and unrelated packaging/model/REST stories do not establish an applicable failure mechanism or an incompatible planned behavior.
