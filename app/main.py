import requests
import json
import google.auth
import os
from google.cloud import bigquery
from utils.utils import download_creds, get_logger
import time
import datetime
import pytz

from google.cloud import error_reporting

from flask import request
from app import app

from .social_data import ProceedSocialData

from .paid_data import ProceedPaidData
from .age_all_platform_data import ProceedAgeAllPlatform
from .gender_all_platform_data import ProceedGenderAllPlatform


credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
error_reporting_client = error_reporting.Client(service="sprinklr_data_ingestion")
logger = get_logger("sprinklr_data_ingestion")

timezone = pytz.timezone("America/New_York")

bq_client = bigquery.Client()
creds = download_creds("sprinklr", 1)


@app.route("/run", methods=["POST"])
def ingest_sprinklr_data():
    current_day_epoch_time = int(
        time.mktime(
            datetime.datetime.now(timezone)
            .replace(hour=23, minute=59, second=0, microsecond=0)
            .timetuple()
        )
    )
    # for startting time we are pulling last 6 moth data so delta days here 180
    start_day = (
        datetime.datetime.now(timezone) - datetime.timedelta(days=180)
    ).replace(hour=0, minute=0, second=0, microsecond=0)
    start_day_epoch_time = int(time.mktime(start_day.timetuple()))

    api_token = creds["api_token"]
    api_key = creds["api_key"]
    start_time = f"{start_day_epoch_time}000"
    end_time = f"{current_day_epoch_time}000"
    logger.info("start time {start_time}".format(start_time= start_time))
    logger.info("end time {end_time}".format(end_time=end_time))
    header = {
        "Content-Type": "application/json",
        "key": api_key,
        "Authorization": f"Bearer {api_token}",
        "startTime": start_time,
        "endTime": end_time,
    }
    try:
        ProceedSocialData(
            header, start_time, end_time, project_id, bq_client
        ).ingest_social_data()

        ProceedPaidData(
            header, start_time, end_time, project_id, bq_client
        ).ingest_paid_data()

        ProceedAgeAllPlatform(
            header, start_time, end_time, project_id, bq_client
        ).ingest_age_all_platform_data()

        ProceedGenderAllPlatform(
            header, start_time, end_time, project_id, bq_client
        ).ingest_gender_all_platform_data()

        return (
            json.dumps({"success": True, "message": "ingest sprinklr data completed"}),
            200,
            {"ContentType": "application/json"},
        )
    except Exception as e:
        logger.error(f"Main Crashed. Error: {e}")
        error_reporting_client.report_exception()
        raise e


@app.route("/success")
def root():
    return (
        json.dumps({"success": True, "message": "ingest sprinklr_data is running"}),
        200,
        {"ContentType": "application/json"},
    )


# if __name__ == "__main__":
#     ingest_sprinklr_data()
