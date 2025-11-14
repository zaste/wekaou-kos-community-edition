# KOS Community Edition

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![WEKAOU Compliant](https://img.shields.io/badge/WEKAOU-Spec%202.5-brightgreen)](https://github.com/zaste/wekaou-specification)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

> Open-source reference implementation of the Knowledge Operating System (KOS) based on the WEKAOU specification.

KOS Community Edition (KOS-CE) is a production-ready implementation of WEKAOU's Knowledge Operating System, providing the core infrastructure for knowledge representation, process orchestration, and systemic integration in organizational environments.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Usage](#usage)
- [Examples](#examples)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

### What is KOS?

The **Knowledge Operating System (KOS)** is the foundational runtime for WEKAOU-based systems. It provides:

- **Knowledge Management**: Store, query, and transform knowledge using SPOC-M
- **Process Orchestration**: Execute K-Cycle workflows with full lifecycle support
- **Ontological Validation**: Ensure compliance with OOS (Ontological Operating System) constraints
- **Quality Assurance**: Apply VQF (Validation Quality Framework) metrics
- **Systemic Integration**: Connect knowledge across organizational boundaries

### Why KOS-CE?

- ✅ **Production-Ready**: Battle-tested in real-world deployments
- ✅ **WEKAOU-Compliant**: Passes all compliance suite tests
- ✅ **Extensible**: Plugin architecture for custom extensions
- ✅ **Open Source**: MIT licensed for maximum flexibility
- ✅ **Well-Documented**: Comprehensive docs and examples

---

## ✨ Features

### Core Capabilities

- **SPOC-M Engine**: Full implementation of Subject-Predicate-Object-Context-Mechanism knowledge representation
- **K-Cycle Runtime**: Execute knowledge cycles with all standard stages (Discovery, Analysis, Synthesis, Application, Validation, Integration)
- **CRL Interpreter**: Parse and execute Canonical Representation Language expressions
- **OOS Validator**: 12-dimensional ontological validation with 170 primitives
- **VQF Metrics**: Quality validation across completeness, consistency, and correctness dimensions

### Storage Backends

- **In-Memory**: Fast development and testing
- **SQLite**: Embedded database for simple deployments
- **PostgreSQL**: Production-grade relational storage
- **MongoDB**: Document-oriented knowledge graphs
- **Custom Adapters**: Extend with your own storage layer

### API Interfaces

- **REST API**: HTTP/JSON interface for web applications
- **GraphQL**: Flexible query language for complex traversals
- **Python SDK**: Native Python bindings
- **CLI**: Command-line tools for automation

---

## 🚀 Installation

### Prerequisites

- **Python**: 3.9 or higher
- **pip**: 20.0 or higher
- **Optional**: PostgreSQL, MongoDB (for production deployments)

### Using pip

```bash
pip install wekaou-kos-ce
```

### From Source

```bash
git clone https://github.com/zaste/wekaou-kos-community-edition.git
cd wekaou-kos-community-edition
pip install -e \".[dev]\"
```

### Using Docker

```bash
docker pull wekaou/kos-ce:latest
docker run -p 8000:8000 wekaou/kos-ce
```

---

## ⚡ Quick Start

### 1. Initialize KOS

```python
from kos import KOS, Config

# Initialize with in-memory storage
config = Config(storage=\"memory\")
kos = KOS(config)
```

### 2. Create Knowledge

```python
from kos.models import SPOCM

knowledge = SPOCM(
    subject={\"id\": \"user:001\", \"type\": \"Person\"},
    predicate={\"relation\": \"hasRole\"},
    object={\"value\": \"Administrator\"}
)

kos.knowledge.create(knowledge)
```

### 3. Query Knowledge

```python
# Query by subject
results = kos.knowledge.query(subject_id=\"user:001\")

# CRL query
results = kos.query('FIND(subject.type: \"Person\")')
```

### 4. Execute K-Cycle

```python
from kos.kcycle import KCycle

cycle = KCycle(kos)
result = cycle.execute(
    stages=[\"discover\", \"analyze\", \"synthesize\"],
    context={\"domain\": \"user-management\"}
)
```

---

## 🏗️ Architecture

### Core Components

```
kos/
├── engine/          # Core KOS runtime
│   ├── knowledge.py    # SPOC-M knowledge engine
│   ├── kcycle.py       # K-Cycle orchestrator
│   └── validation.py   # OOS/VQF validators
├── storage/         # Storage adapters
│   ├── memory.py
│   ├── sqlite.py
│   ├── postgres.py
│   └── mongodb.py
├── api/             # API interfaces
│   ├── rest.py
│   ├── graphql.py
│   └── cli.py
├── models/          # Data models
│   ├── spocm.py
│   ├── kcycle.py
│   └── schemas.py
└── plugins/         # Extension system
    └── registry.py
```

### Architecture Diagram

```
┌─────────────────────────────────────────┐
│           Client Applications           │
└─────────────┬───────────────────────────┘
              │
   ┌──────────┴──────────┐
   │                     │
┌──▼────┐           ┌────▼────┐
│ REST  │           │ GraphQL │
│  API  │           │   API   │
└───┬───┘           └────┬────┘
    │                    │
    └──────────┬─────────┘
               │
    ┌──────────▼──────────┐
    │   KOS Core Engine   │
    │  ┌──────────────┐   │
    │  │ SPOC-M Engine│   │
    │  ├──────────────┤   │
    │  │ K-Cycle Exec │   │
    │  ├──────────────┤   │
    │  │ OOS Validator│   │
    │  ├──────────────┤   │
    │  │ VQF Metrics  │   │
    │  └──────────────┘   │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │  Storage Adapters   │
    │  [Memory│SQL│NoSQL] │
    └─────────────────────┘
```

---

## 📖 Usage

### Knowledge Management

#### Creating Knowledge

```python
# Simple knowledge creation
kos.knowledge.create(
    subject={\"id\": \"doc:123\", \"type\": \"Document\"},
    predicate={\"relation\": \"hasAuthor\"},
    object={\"value\": \"user:456\"}
)

# With full SPOC-M
knowledge = SPOCM(
    subject={
        \"id\": \"process:onboarding\",
        \"type\": \"BusinessProcess\",
        \"label\": \"Employee Onboarding\"
    },
    predicate={
        \"relation\": \"requires\",
        \"modality\": \"necessity\"
    },
    object={
        \"value\": \"resource:hr-system\",
        \"type\": \"System\"
    },
    context={
        \"domain\": \"HR\",
        \"scope\": \"Company-wide\"
    },
    metadata={
        \"version\": \"2.5\",
        \"confidence\": 0.95
    }
)
kos.knowledge.create(knowledge)
```

#### Querying Knowledge

```python
# By subject
results = kos.knowledge.query(subject_id=\"user:001\")

# By relation
results = kos.knowledge.query(relation=\"hasRole\")

# Complex CRL query
results = kos.query('''
    FIND(
        subject.type: \"Person\",
        predicate.relation: \"hasRole\",
        object.value: \"Administrator\"
    )
''')
```

#### Updating Knowledge

```python
kos.knowledge.update(
    knowledge_id=\"kb:001\",
    updates={\"object.value\": \"Senior Administrator\"}
)
```

### K-Cycle Execution

```python
from kos.kcycle import KCycle, Stage

# Define custom K-Cycle
cycle = KCycle(kos, name=\"analysis-cycle\")

# Add stages
cycle.add_stage(Stage.DISCOVER, {
    \"sources\": [\"api:data\", \"db:metrics\"],
    \"filters\": {\"category\": \"performance\"}
})
cycle.add_stage(Stage.ANALYZE, {
    \"methods\": [\"statistical\", \"pattern-recognition\"]
})
cycle.add_stage(Stage.SYNTHESIZE, {
    \"output_format\": \"spoc-m\"
})

# Execute
result = cycle.execute()

if result.success:
    print(f\"Generated {len(result.knowledge)} SPOC-M statements\")
    print(f\"Quality score: {result.quality_score}\")
```

### Validation

```python
from kos.validation import OOSValidator, VQFValidator

# Ontological validation (OOS)
oos = OOSValidator(kos)
result = oos.validate(knowledge)
print(f\"OOS compliance: {result.score}/12 dimensions\")

# Quality validation (VQF)
vqf = VQFValidator(kos)
result = vqf.validate(knowledge)
print(f\"VQF metrics: {result.metrics}\")
```

---

## 💡 Examples

### Example 1: User Management System

```python
from kos import KOS, Config

# Initialize
kos = KOS(Config(storage=\"sqlite\", db_path=\"users.db\"))

# Create user knowledge
kos.knowledge.create(
    subject={\"id\": \"user:alice\", \"type\": \"Person\"},
    predicate={\"relation\": \"hasRole\"},
    object={\"value\": \"Developer\"}
)

# Query users
developers = kos.query('FIND(object.value: \"Developer\")')
print(f\"Found {len(developers)} developers\")
```

### Example 2: Process Orchestration

```python
# Define organizational process
process_cycle = KCycle(kos, \"procurement-approval\")

process_cycle.add_stage(Stage.DISCOVER, {
    \"trigger\": \"purchase-request\",
    \"collect\": [\"budget\", \"approvers\", \"policies\"]
})

process_cycle.add_stage(Stage.ANALYZE, {
    \"validate\": [\"budget-available\", \"policy-compliant\"]
})

process_cycle.add_stage(Stage.APPLICATION, {
    \"actions\": [\"notify-approvers\", \"create-ticket\"]
})

# Execute when triggered
result = process_cycle.execute(context={\"request_id\": \"PR-001\"})
```

### More Examples

See the [`/examples`](examples/) directory for:

- Complete application examples
- Integration patterns
- Best practices
- Performance optimization

---

## ⚙️ Configuration

### Configuration File

Create `kos.config.yaml`:

```yaml
storage:
  type: postgres
  host: localhost
  port: 5432
  database: kos
  user: kos_user
  password: secret

api:
  rest:
    enabled: true
    host: 0.0.0.0
    port: 8000
  graphql:
    enabled: true
    path: /graphql

validation:
  oos:
    enabled: true
    strict_mode: false
  vqf:
    enabled: true
    thresholds:
      completeness: 0.8
      consistency: 0.9

logging:
  level: INFO
  format: json
```

### Environment Variables

```bash
KOS_STORAGE_TYPE=postgres
KOS_DB_HOST=localhost
KOS_API_PORT=8000
KOS_LOG_LEVEL=INFO
```

---

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/zaste/wekaou-kos-community-edition.git
cd wekaou-kos-community-edition

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install with dev dependencies
pip install -e \".[dev]\"

# Run tests
pytest tests/ -v

# Run linters
ruff check .
mypy kos/
```

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_knowledge.py

# With coverage
pytest --cov=kos tests/
```

### Building Documentation

```bash
cd docs
make html
```

---

## 🤝 Contributing

We welcome contributions! Please see:

- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CODE_OF_CONDUCT.md](https://github.com/zaste/wekaou-.github/blob/main/CODE_OF_CONDUCT.md) - Community standards
- [GOVERNANCE](https://github.com/zaste/wekaou-governance) - Project governance

---

## 📚 Resources

- **Documentation**: [Full Docs](docs/)
- **Specification**: [WEKAOU Spec](https://github.com/zaste/wekaou-specification)
- **Compliance Suite**: [Test Your Implementation](https://github.com/zaste/wekaou-compliance-suite)
- **Community**: [Discussions](https://github.com/zaste/wekaou-community/discussions)
- **RFC Process**: [Propose Changes](https://github.com/zaste/wekaou-rfc)

---

## 📄 License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

KOS Community Edition is maintained by the WEKAOU Technical Steering Committee and community contributors.

For support:
- [Open an Issue](https://github.com/zaste/wekaou-kos-community-edition/issues)
- [Join Discussions](https://github.com/zaste/wekaou-community/discussions)
- [Read the Docs](docs/)

---

**Built with ❤️ by the WEKAOU Community**
