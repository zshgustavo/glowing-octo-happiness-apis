# HOW_TO_BUILD

## Local Build

1. Install Python 3.12+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Validate that imports resolve:
   ```bash
   python -c "import src.apis.app"
   ```

## Container Build

```bash
docker build -f deployment/cloudrun/Dockerfile -t marketing-data-api:local .
```
