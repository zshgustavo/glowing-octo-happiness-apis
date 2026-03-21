# HOW_TO_DEPLOY

## Prerequisites

- GCP project configured
- Cloud Run and Artifact/Container registry access
- `GCP_SA_KEY` secret and `GCP_PROJECT_ID` variable configured in GitHub

## Deployment Workflow

Deployment is automated via `.github/workflows/deploy-cloudrun.yml` on pushes to `main`.

## Manual Reference

Use the runbook in [DEPLOY](DEPLOY.md) for a step-by-step manual deployment path.
