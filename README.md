# family-office-long-term-memory

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License: MIT" />
  <img src="https://img.shields.io/badge/version-0.1.0-blue" alt="Version 0.1.0" />
  <img src="https://img.shields.io/badge/language-Python-yellow" alt="Python" />
</p>

**Long-term memory service for family office workflows — preserving client decisions, relationships, and institutional knowledge.**

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Recall institutional context on demand** — query the memory graph to bring back prior decisions, alternatives considered, and rationale, with entity extraction, context profiling (`_build_context_family-office-long-term-memory`), priority-result guarantees, and deduplication so your advisor assistant returns the *why*, not just similar snippets (`automem/api/recall.py::handle_recall`).
- **Record typed associations between memories** — batch-create links between decisions, mandates, and follow-up work so a client's risk-tolerance change stays connected to the rebalancing it triggered (`create_memory_blueprint`, `_create_association_batch`, `_batch_association_response`).
- **Manage client and entity relationships** — persist entities with aliases, audit memory-to-entity tags, and serialize identity rows so a principal, trust, or entity appears consistently across the graph (`create_entity_blueprint`, `_parse_aliases`, `_audit_memory_entity_tags`).
- **Consolidate and enrich memories over time** — scheduled consolidation and enrichment pipelines keep the memory base clean and structured as the family's record grows (`create_consolidation_blueprint_full`, `create_enrichment_blueprint`, `automem/consolidation/runtime_scheduler.py`).
- **Operate with admin controls and backups** — full admin API, API-token and admin-token authentication, backup endpoints, and an automated FalkorDB backup script with retention and optional S3 upload (`create_admin_blueprint_full`, `require_admin_token`, `create_backup_blueprint`, `.railway/backup-falkordb.sh`).
- **Plug in your preferred embedding provider** — OpenAI, Ollama, or local FastEmbed providers for vector retrieval of family office records (`automem/embedding/openai.py`, `automem/embedding/ollama.py`, `automem/embedding/fastembed.py`).

## Installation

```bash
git clone https://github.com/AvicenaIG/family-office-long-term-memory.git
cd family-office-long-term-memory

python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Quick Start

The service is a Python API application. Start it and use the blueprints registered by `register_blueprints` in `automem/api/runtime_bootstrap.py`:

```bash
python app.py
```

Then record and recall family office knowledge through the memory and recall endpoints handled by `create_memory_blueprint` and `handle_recall`:

```python
import requests

BASE_URL = "http://localhost:8000"
headers = {"Authorization": "Bearer <your-api-token>"}

# Save a client decision
memory = {
    "content": "Family principal approved the direct real estate allocation "
               "after reviewing the co-investment alternative.",
    "tags": ["investment-committee", "real-estate"],
}
requests.post(f"{BASE_URL}/memory", json=memory, headers=headers)

# Recall it later, with related context
response = requests.get(
    f"{BASE_URL}/recall",
    params={"query": "why did we choose direct real estate?"},
    headers=headers,
)
print(response.json())
```

## Usage

### Recalling an investment decision with its rationale

An advisor asks the connected assistant about a prior committee decision. `handle_recall` extracts query entities via `_extract_query_entities`, expands related memories through `_expand_related_memories`, and returns the decision, the alternatives considered, and the work that followed:

```python
response = requests.get(
    f"{BASE_URL}/recall",
    params={"query": "Kuykendall trust risk mandate", "tags": "investment-policy"},
    headers=headers,
)
results = response.json()
```

### Reviewing memories by tag for a client entity

Use the tag-based paging routes in `automem/api/runtime_memory_routes.py` (`_parse_by_tag_request`, `_load_memories_by_tag_page`) to page through all memories tagged for a reporting period — for example, everything tagged for the annual family review:

```python
response = requests.get(
    f"{BASE_URL}/memories/by-tag",
    params={"tag": "annual-review", "page": 1},
    headers=headers,
)
```

## Configuration

Environment variables detected in the code and deployment scripts:

| Option | Type | Default | Description |
|---|---|---|---|
| `BACKUP_DIR` | string | `/data/backups` | Directory for FalkorDB backup files |
| `RETENTION_DAYS` | integer | `7` | Days to retain compressed backups |
| `AWS_ACCESS_KEY_ID` | string | — | Optional; enables S3 upload of backups |
| `S3_BACKUP_BUCKET` | string | — | S3 bucket for backup upload |
| API token | string | — | Bearer token required by `require_api_token` |
| Admin token | string | — | Bearer token required by `require_admin_token` for admin routes |
| Viewer allowed origins | string | — | Parsed by `_parse_viewer_allowed_origins` to control viewer CORS origins |
| Embedding provider | string | — | Selects the OpenAI, Ollama, FastEmbed, or placeholder embedding provider |

## Contributing

Contributions are welcome. Please open an issue describing the family office use case before submitting a pull request, and keep changes covered by the existing test and documentation conventions.

## License

Released under the MIT License. Copyright © 2026 family-office-long-term-memory contributors.