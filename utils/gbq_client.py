import pandas as pd
from datetime import datetime
import logging
from google.cloud import bigquery
import os
import google.auth



credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
logger = logging.getLogger("SPRINKLR INGESTION")
bq_client = bigquery.Client()


def run_query_bq(project_id, temp_table, destination_table):
    query = """create or replace table `{project_id}.{destination_table}` OPTIONS(description = "sprinklr data from sprinklr API", labels=[("resource-creator","santosh_silwal"),("pipeline","sprinklr"),("stage","raw")]) as SELECT * FROM `{project_id}.{source_table}` """.format(
        project_id=project_id,
        destination_table=destination_table,
        source_table=temp_table,
    )
    query_updated = bq_client.query(query)
    if not list(query_updated.result()):
        logger.info("successfully created new table...")
        # delete temp table
        logger.info("deleting temp table")
        bq_client.delete_table(project_id + "." + temp_table)


def check_and_update_table(project_id, temp_table, destination_table):
    bq_table = bq_client.get_table(project_id + "." + temp_table)
    table_modified_date = datetime.strptime(
        str(bq_table.modified), "%Y-%m-%d %H:%M:%S.%f%z"
    )
    current_date = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")

    if current_date.date() == table_modified_date.date():
        logger.info("temp table updated today")

        run_query_bq(project_id, temp_table, destination_table)

    else:
        print("not created temp table")
