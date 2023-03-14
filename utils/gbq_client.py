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


def dedup_socail_data(project_id, temp_table):
    query = """
            create or replace table `{project_id}.{temp_table}` as

                with table_1 as(
                SELECT 
                *,
                row_number() over(partition by post_id, social_network order by post_published_date desc) as rn



                FROM `{project_id}.{temp_table}` )

                select * except(rn) from table_1 where rn = 1
                    
                    """.format(
        project_id=project_id, temp_table=temp_table
    )
    query_updated = bq_client.query(query)
    if not list(query_updated.result()):
        logger.info("successfully dedup social table...")


def dedup_paid_data(project_id, temp_table):
    query = """
            create or replace table `{project_id}.{temp_table}` as

                with table_1 as(
                SELECT 
                *,
                row_number() over(PARTITION BY channel, ad_variant_id, paid_initiative_name, date, outbound_message_tags, impressions) as rn



                FROM `{project_id}.{temp_table}` )

                select * except(rn) from table_1 where rn = 1
                    
                    """.format(
        project_id=project_id, temp_table=temp_table
    )
    query_updated = bq_client.query(query)
    if not list(query_updated.result()):
        logger.info("successfully dedup social table...")


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

        if temp_table == "sprinklr_src.social_data_temp":
            dedup_socail_data(project_id, temp_table)
        
        if temp_table == "sprinklr_src.paid_data_temp":
           dedup_paid_data(project_id, temp_table)

        run_query_bq(project_id, temp_table, destination_table)

    else:
        print("not created temp table")
