import requests
import json
import google.auth
import os
from google.cloud import bigquery
from utils.utils import download_creds, get_logger
import time
import datetime
import pytz
import threading

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


def process_social_data(header, start_time, end_time, project_id, bq_client):
    ProceedSocialData(header, start_time, end_time, project_id, bq_client).ingest_social_data()

def process_paid_data(header, start_time, end_time, project_id, bq_client):
    ProceedPaidData(header, start_time, end_time, project_id, bq_client).ingest_paid_data()

def process_age_all_data(header, start_time, end_time, project_id, bq_client):
    ProceedAgeAllPlatform(header, start_time, end_time, project_id, bq_client).ingest_age_all_platform_data()

def process_gender_all_data(header, start_time, end_time, project_id, bq_client):
    ProceedGenderAllPlatform(header, start_time, end_time, project_id, bq_client).ingest_gender_all_platform_data()


@app.route("/run", methods=["POST"])
def ingest_sprinklr_data():
    logger.info("starting.....")

    current_day = datetime.datetime.now(timezone)
    target_time = datetime.time(hour=23, minute=59, second=0, microsecond=0)
    target_datetime = datetime.datetime.combine(current_day, target_time)

    current_day_epoch_time = int(target_datetime.timestamp())
   
    logger.info("accessing access toekn")
    token_url = 'https://api2.sprinklr.com/oauth/token'
    api_key = creds['client_id']
    data = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': creds['client_secret']
    }
    response = requests.post(token_url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get('access_token')
        logger.info("access token generated successfully")

    else:
        logger.error("issue to generate access code")

    api_token = access_token

    start_date = timezone.localize(datetime.datetime(2023, 1, 1, 0, 0, 0))

    start_time_epoch = (
        int(start_date.timestamp()) * 1000
    )  # Multiply by 1000 to convert to milliseconds

    start_time = str(start_time_epoch)

    # start_time = f"{start_day_epoch_time}000"
    end_time = f"{current_day_epoch_time}000"
    logger.info("start time {start_time}".format(start_time=start_time))
    logger.info("end time {end_time}".format(end_time=end_time))
    header = {
        "Content-Type": "application/json",
        "key": api_key,
        "Authorization": f"Bearer {api_token}",
        "startTime": start_time,
        "endTime": end_time,
    }
    try:
        #proceed all in thread 
        thread1 = threading.Thread(target=process_paid_data, args=(header, start_time, end_time, project_id, bq_client))
        thread2 = threading.Thread(target=process_social_data, args=(header, start_time, end_time, project_id, bq_client))
        thread3 = threading.Thread(target=process_age_all_data, args=(header, start_time, end_time, project_id, bq_client))
        thread4 = threading.Thread(target=process_gender_all_data, args=(header, start_time, end_time, project_id, bq_client))

        # Start all threads
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        # Wait for all threads to complete
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        logger.info("completed all")
        return (
            json.dumps({"success": True, "message": "ingest sprinklr data completed"}),
            200,
            {"ContentType": "application/json"},
        )
    except Exception as e:
        logger.error(f"Main Crashed. Error: {e}")
        error_reporting_client.report_exception()


@app.route("/success")
def root():
    return (
        json.dumps({"success": True, "message": "ingest sprinklr_data is running"}),
        200,
        {"ContentType": "application/json"},
    )


# if __name__ == "__main__":
#     ingest_sprinklr_data()
