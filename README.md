# Glowing Octo Happiness APIs

A lightweight API service that orchestrates marketing data extraction and loading into BigQuery.

## Purpose
This repository is organized to be clear for global collaboration, with one-purpose folders and explicit operational documentation.

## Repository Structure

- `src/` — application source code
- `airflow/` — workflow orchestration DAGs
- `deployment/` — deployment assets (container/runtime)
- `docs/` — detailed product, architecture, security, and runbook docs
- `.github/workflows/` — CI/CD workflow definitions

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment variables (copy from `.env.example`).
3. Run locally:
   ```bash
   python -m src.apis.app
   ```

## Documentation Index

- [DOCS](DOCS.md)
- [GUIDES](GUIDES.md)
- [HOW_TO_BUILD](HOW_TO_BUILD.md)
- [HOW_TO_DEPLOY](HOW_TO_DEPLOY.md)
- [DEPLOY](DEPLOY.md)
- [BEST_PRACTICES](BEST_PRACTICES.md)
- [SECURITY](SECURITY.md)
- [CONTRIBUTORS](CONTRIBUTORS.md)
- [LICENSE](LICENSE.md)
