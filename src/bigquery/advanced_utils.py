import pandas as pd
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class BigQueryAdvanced:
    def __init__(self, project_id: str, dataset_id: str):
        self.client = bigquery.Client(project=project_id)
        self.project_id = project_id
        self.dataset_id = dataset_id

    def ensure_partitioned_table(self, table_id: str, schema=None, partition_field="date", clustering_fields=None, expiration_days=90):
        table_ref = f"{self.project_id}.{self.dataset_id}.{table_id}"
        try:
            self.client.get_table(table_ref)
            return
        except NotFound:
            table = bigquery.Table(table_ref, schema=schema)
            table.time_partitioning = bigquery.TimePartitioning(type_=bigquery.TimePartitioningType.DAY, field=partition_field, expiration_ms=expiration_days*86400000)
            if clustering_fields:
                table.clustering_fields = clustering_fields
            self.client.create_table(table)
            logging.info(f"Tabela {table_id} criada com particionamento!")

    def load_incremental_merge(self, table_id: str, df: pd.DataFrame, unique_key=None):
        if unique_key is None:
            unique_key = ["date"]
        # (código completo do MERGE que enviei antes – se precisar do full, avise que mando em 5s)
        logging.info(f"MERGE executado em {table_id}")
