import pandas as pd
import pytz
from datetime import datetime
import json
import requests
from utils.sprinklr_utils import (
    age_all_platform_payload,
    age_all_platform_schema,
    age_all_platform_columns,
    api_url,
)
from utils.utils import get_logger
from utils.gbq_client import check_and_update_table


logger = get_logger("INGEST_AGE_ALL_PLATFORM")


class ProceedAgeAllPlatform:
    def __init__(self, header, start_time, end_time, project_id, bq_client):
        self.header = header
        self.start_time = start_time
        self.end_time = end_time
        self.project_id = project_id
        self.bq_client = bq_client

    def ingest_age_all_platform_data(self):
        logger.info("Processing.....age_all_platform")
        destination_table = "sprinklr_src.age_all_platforms"
        temp_table = "sprinklr_src.age_all_platforms_temp"
        row_status = True
        page_number = 0
        payload = {
            "startTime": self.start_time,
            "endTime": self.end_time,
        }
        while row_status:
            report_payload = dict(payload, **age_all_platform_payload)
            page = {"page": page_number, "pageSize": 1000}
            sprinklr_payload = {**report_payload, **page}
            sprinklr_response = requests.post(
                url=api_url, headers=self.header, data=json.dumps(sprinklr_payload)
            )
            if sprinklr_response.status_code == 200:
                sprinklr_data = sprinklr_response.json()
                if "rows" in sprinklr_data:
                    print(
                        f"row exist in sprinklr data of page {page_number}".format(
                            page_number=page_number
                        )
                    )
                    df = pd.DataFrame(
                        sprinklr_data["rows"], columns=age_all_platform_columns
                    )
                    df["paid_initiative_name"] = pd.json_normalize(
                        df["paid_initiative_name"]
                    )["name"]
                    lower_case_column = ["paid_initiative_name"]
                    for i in lower_case_column:
                        df[i] = df[i].apply(
                            lambda x: str(x).lower() if pd.notnull(x) else x
                        )
                    float_to_int_columns = [
                        "impressions",
                        "acm_global_link_clicks",
                        "acm_global_video_views",
                    ]
                    for i in float_to_int_columns:
                        df[i] = df[i].astype(int)

                    df.to_gbq(
                        temp_table,
                        project_id=self.project_id,
                        table_schema=age_all_platform_schema,
                        if_exists="append",
                    )
                    print("ingested rows completed ")
                    page_number += 1
                else:
                    print(
                        f"Sprinklr table has not more datas with given time at page {page_number}".format(page_number=page_number)
                    )
                    row_status = False

        check_and_update_table(self.project_id, temp_table, destination_table)
