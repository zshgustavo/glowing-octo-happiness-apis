from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from src.bigquery.advanced_utils import BigQueryAdvanced
from src.monitoring.otel_setup import init_otel
from src.extractors import EXTRACTORS

load_dotenv()
app = Flask(__name__)
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
if not PROJECT_ID:
    raise RuntimeError(
        "GCP_PROJECT_ID must be set (e.g. in .env or the deployment environment). "
        "BigQuery requires a project ID."
    )
DATASET_ID = os.getenv("BIGQUERY_DATASET", "marketing_raw")
bq = BigQueryAdvanced(PROJECT_ID, DATASET_ID)
init_otel(app)

@app.route("/extract/<platform>", methods=["POST"])
def extract(platform):
    if platform not in EXTRACTORS:
        return jsonify({"error": "Plataforma não implementada"}), 501
    try:
        data = request.json or {}
        df = EXTRACTORS[platform](data.get("start_date"), data.get("end_date"))
        table_id = f"{platform}_raw"
        bq.ensure_partitioned_table(table_id, partition_field="date")
        bq.load_incremental_merge(table_id, df)
        return jsonify({"status": "success", "rows": len(df), "table": table_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
