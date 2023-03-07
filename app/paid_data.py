import pandas as pd
import pytz
from datetime import datetime
import json
import requests
from utils.sprinklr_utils import (
    paid_data_payload,
    paid_schema,
    paid_data_columns,
    api_url,
)
from utils.utils import get_logger
from utils.gbq_client import check_and_update_table


logger = get_logger("INGEST_paid_DATA")


class ProceedPaidData:
    def __init__(self, header, start_time, end_time, project_id, bq_client):
        self.header = header
        self.start_time = start_time
        self.end_time = end_time
        self.project_id = project_id
        self.bq_client = bq_client

    def ingest_paid_data(self):
        logger.info("Processing.....paid_data")
        destination_table = "sprinklr_src.paid_data"
        temp_table = "sprinklr_src.paid_data_temp"
        row_status = True
        page_number = 0
        payload = {
            # "reportingEngine": "PLATFORM",
            # "report": "POST_INSIGHTS",
            "startTime": self.start_time,
            "endTime": self.end_time,
        }
        while row_status:
            report_payload = dict(payload, **paid_data_payload)
            page = {"page": page_number, "pageSize": 1000}
            sprinklr_payload = {**report_payload, **page}
            sprinklr_response = requests.post(
                url=api_url, headers=self.header, data=json.dumps(sprinklr_payload)
            )
            if sprinklr_response.status_code == 200:
                sprinklr_data = sprinklr_response.json()
                if "rows" in sprinklr_data:
                    logger.info("row exist in sprinklr data of page {page_number}".format(page_number))
                    df = pd.DataFrame(sprinklr_data["rows"], columns=paid_data_columns)
                    df["paid_initiative_name"] = pd.json_normalize(
                        df["paid_initiative_name"]
                    )["name"]
                    df.drop("ad_variant", axis=1, inplace=True)
                    df["post_promotion_start_date"] = pd.to_datetime(
                        df["post_promotion_start_date"], errors="coerce"
                    )
                    df["paid_initative_end_date"] = pd.to_datetime(
                        df["paid_initative_end_date"], errors="coerce"
                    )
                    lower_case_column = [
                        "creative_headline",
                        "outbound_message_tags",
                        "channel",
                        "paid_initiative_name",
                        "ad_variant_id",
                    ]
                    float_to_int_columns = [
                        "acm_global_video_views",
                        "paid_initiative_lifetime_budget",
                        "acm_global_video_views",
                        "acm_global_total_engagements",
                        "acm_global_link_clicks",
                        "impressions",
                    ]
                    for i in float_to_int_columns:
                        df[i] = df[i].astype(int)

                    for i in lower_case_column:
                        df[i] = df[i].apply(
                            lambda x: str(x).lower() if pd.notnull(x) else x
                        )
                    df.to_gbq(
                        temp_table,
                        project_id=self.project_id,
                        table_schema=paid_schema,
                        if_exists="append",
                    )
                    logger.info(
                        "ingested rows completed of page {page_number}".format(
                            page_number
                        )
                    )
                    page_number += 1
                else:
                    logger.info(
                        "Sprinklr table has not more datas with given time at page {page_number}".format(
                            page_number
                        )
                    )
                    row_status = False
                    # log to bq
            else:
                logger.error("could not connect sprinklr api")
        check_and_update_table(self.project_id, temp_table, destination_table)
