# Architecture

## Components

- Flask API (`src/apis/app.py`)
- Data extractors (`src/extractors/`)
- BigQuery utilities (`src/bigquery/`)
- Monitoring setup (`src/monitoring/`)
- Deployment container (`deployment/cloudrun/Dockerfile`)

## Data Flow

1. Client calls `/extract/<platform>`
2. Extractor fetches/normalizes source data
3. Service ensures destination table exists
4. Data is merged into BigQuery
