import google.auth
import pandas as pd
from google.cloud import bigquery
from utils.utils import get_logger


credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
logger = get_logger("SFMC_BQ_Update_Table")

bqclient = bigquery.Client(credentials=credentials, project=project_id)


def run_query_bq(query):
    query_updated = bqclient.query(query)
    if not [x for x in query_updated.result()]:
        logger.info("successfully updated table...")


def update_active_inactive(source_table, deduped_table):
    query = """
            create or replace table `{project_id}.{deduped_table}` 
            OPTIONS (
            description = "Deduped active_inactive table",
            labels=[("resource-creator","santosh_silwal"),
            ("pipeline","domestic_data_view_ingestion"),
            ("stage","production")])  
            
            as
                        with  duplicates as (select *, row_number() over(partition by  
                        cm_subscriber_key,		
                        email_customer_id,		
                        email_address,	
                        subscriptions_product,	
                        email_capture_date,	
                        email_updated_date,	
                        subscriptions_expires_at_date,	
                        email_status,	
                        email_status_change_date,	
                        subscriptions_account_status,	
                        subscriptions_account_status_change_date,	
                        subscriber_name,	
                        subscriber_state_province,	
                        subscriber_postal_code,	
                        wait_for_cds,	
                        source	,
                        lastsend_date,
                        lastopen_date,	
                        lastclick_date,	
                        old_email_address,	
                        email_change_date,	
                        in_journey,	
                        journey_injected_date,	
                        iteration,	
                        journey_status,	
                        ejected,
                        journey_ejected_date,	
                        journey_date_updated,	
                        bq_to_sfmc_date,
                        country,		
                        cds_to_bq_date
                        order by ingestion_date asc) 
                        as rn from `{project_id}.{source_table}`) select * from duplicates where rn =1
    """.format(
        project_id=project_id,
        source_table=source_table,
        deduped_table=deduped_table,
    )
    run_query_bq(query)


def update_prospect(source_table, deduped_table):
    query = """
            create or replace table `{project_id}.{deduped_table}` 
            OPTIONS (
            description = "Deduped prospect table",
            labels=[("resource-creator","santosh_silwal"),
            ("pipeline","domestic_data_view_ingestion"),
            ("stage","production")])  
            
            as
                with  duplicates as (select *, row_number() over(partition by  
                cm_subscriber_key,	
                email_address,	
                newsletter_subkey,	
                newsletter_name,	
                first_name,	
                last_name,	
                full_name,	
                zip,	
                country,	
                source,	
                latest_newsletter_optin_flag,	
                orig_sub_date,	
                latest_sub_date,	
                newsletter_status,	
                newsletter_status_change_date,	
                source_createupdate_date,	
                newsletter_lastsend_date,	
                newsletter_lastopen_date,	
                newsletter_lastclick_date,	
                old_email_address,	
                email_change_date,	
                subscriptions_account_status,	
                subscriptions_account_status_change_date,	
                wait_for_cds,	
                in_journey,	
                journey_injected_date,	
                iteration,	
                journey_status,	
                ejected,
                journey_ejected_date,	
                journey_date_updated,	
                lastsend_date,	
                lastopen_date,	
                lastclick_date,	
                email_status,	
                email_status_change_date,	
                create_date,	
                city,	
                state,	
                school_name
                order by ingestion_date asc)
                 as rn from `{project_id}.{source_table}`) select * from duplicates where rn =1

    """.format(
        project_id=project_id,
        source_table=source_table,
        deduped_table=deduped_table,
    )
    run_query_bq(query)


def update_newsletter_confirmation(source_table, deduped_table):
    query = """
            create or replace table `{project_id}.{deduped_table}` 
            OPTIONS (
            description = "Deduped newsletter_confirmation table",
            labels=[("resource-creator","santosh_silwal"),
            ("pipeline","domestic_data_view_ingestion"),
            ("stage","production")])  
            
            as
                with  duplicates as (select *, row_number() over(partition by  
                newsletter_guid,
                email_address,
                newsletter_name	,
                sub_date,
                first_name,	
                last_name,
                full_name,
                zip,
                country,
                source,	
                optin_flag,	
                createupdate_date,
                create_date,
                confirmation_date,
                confirmation_failed_date,
                newsletter_preconfirm_subkey,
                confirmation_email_status,
                newsletter_postconfirm_subkey,
                expire_date,
                doi_content,
                from_doir	
                order by ingestion_date asc)
                 as rn from `{project_id}.{source_table}`) select * except (rn) from duplicates where rn =1

    """.format(
        project_id=project_id,
        source_table=source_table,
        deduped_table=deduped_table,
    )
    run_query_bq(query)


def update_supscious_email_table():
    suspicious_email_table = "newsletter_confirmation_supscious_email"
    # query to find suspecious email
    suspecious_email_query = "select email_address, source, count(*) as count from `{table_id}` where email_address <> '' group by email_address, source having count(*)>36".format(
        table_id=project_id + ".sfmc_100023869.newsletter_confirmation_updated"
    )
    suspecious_email_df = pd.read_gbq(suspecious_email_query)
    suspecious_email_df.to_gbq(
        destination_table="sfmc_100023869." + suspicious_email_table,
        project_id=project_id,
        if_exists="replace",
    )
    remove_suspecious_email_query = "delete from `{table_id}` where email_address in(select email_address from `{supscious_table}`)".format(
        table_id=project_id + ".sfmc_100023869.newsletter_confirmation_updated",
        supscious_table=project_id
        + ".sfmc_100023869.newsletter_confirmation_supscious_email",
    )
    run_query_bq(remove_suspecious_email_query)
    logger.info(
        " updated suspcious email table and remove email from newsletter_confirmation table"
    )


def update_newsletter(source_table, deduped_table):
    query = """
            create or replace table `{project_id}.{deduped_table}` 
            OPTIONS (
            description = "Deduped newsletter table",
            labels=[("resource-creator","santosh_silwal"),
            ("pipeline","domestic_data_view_ingestion"),
            ("stage","production")])  
            
            as
                with  duplicates as (select *, row_number() over(partition by  
                newsletter_subkey,
                email_address,
                newsletter_name,
                first_name,
                last_name,
                full_name,
                zip,
                country,
                source,
                optin_flag,
                optin_flag_change_date,
                orig_sub_date,
                latest_sub_date,
                status,
                status_change_date,
                old_email_address,
                email_address_change_date,
                createupdate_date,
                demodata_change_date,
                html_email_preference,
                html_email_preference_change_date,
                events,
                eventsuserstatus,
                eventsuserstatus_change_date,
                staging_flag,
                events_count	
                order by ingestion_date asc)
                 as rn from `{project_id}.{source_table}`) select * except (rn) from duplicates where rn =1

    """.format(
        project_id=project_id,
        source_table=source_table,
        deduped_table=deduped_table,
    )
    run_query_bq(query)
