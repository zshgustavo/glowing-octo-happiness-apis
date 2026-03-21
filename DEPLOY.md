# DEPLOY

## Manual Deployment Runbook

1. Build image:
   ```bash
   gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/marketing-data-api
   ```
2. Deploy to Cloud Run:
   ```bash
   gcloud run deploy marketing-data-api \
     --image gcr.io/$GCP_PROJECT_ID/marketing-data-api \
     --region southamerica-east1
   ```
3. Verify health endpoint and extraction endpoints.
