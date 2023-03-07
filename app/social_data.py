import pandas as pd
import pytz
from datetime import datetime
import json
import requests
from utils.sprinklr_utils import (
    social_data_payload,
    social_schema,
    social_data_columns,
    api_url,
)
from utils.utils import get_logger
from utils.gbq_client import check_and_update_table


logger = get_logger("INGEST_SOCIAL_DATA")


class ProceedSocialData:
    def __init__(self, header, start_time, end_time, project_id, bq_client):
        self.header = header
        self.start_time = start_time
        self.end_time = end_time
        self.project_id = project_id
        self.bq_client = bq_client

    def ingest_social_data(self):
        logger.info("Processing.....social_data")
        destination_table = "sprinklr_src.social_data"
        temp_table = "sprinklr_src.social_data_temp"
        row_status = True
        page_number = 0
        payload = {
            "reportingEngine": "PLATFORM",
            "report": "POST_INSIGHTS",
            "startTime": self.start_time,
            "endTime": self.end_time,
        }
        while row_status:
            report_payload = dict(payload, **social_data_payload)
            page = {"page": page_number, "pageSize": 1000}
            sprinklr_payload = {**report_payload, **page}
            sprinklr_response = requests.post(
                url=api_url, headers=self.header, data=json.dumps(sprinklr_payload)
            )
            if sprinklr_response.status_code == 200:
                sprinklr_data = sprinklr_response.json()
                if "rows" in sprinklr_data:
                    logger.info(f"row exist in sprinklr data of page {page_number}")
                    df = pd.DataFrame(
                        sprinklr_data["rows"], columns=social_data_columns
                    )
                    drop_column = [
                        "post_id_5",
                        "post_twitter_faorites_count",
                        "post_twitter_replies_count",
                        "post_twitter_retweets_count",
                        "post_twitter_reach_count",
                    ]
                    for i in drop_column:
                        df.drop(i, axis=1, inplace=True)

                    lower_case_column = [
                        "post_id",
                        "social_network",
                        "media_type",
                        "campaign",
                        "vertical_outbound_message",
                        "topic_outbound_message",
                        "advertiser_outbound_message",
                        "magazine_outbound_message",
                        "evergreen_outbound_message",
                        "actual_link"
            
                    ]
                    for i in lower_case_column:
                        df[i] = df[i].apply(
                            lambda x: str(x).lower() if pd.notnull(x) else x
                        )

                    df["post_published_date"] = df["post_published_date"].apply(
                        lambda x: datetime.fromtimestamp(
                            int(x) / 1000, pytz.timezone("America/New_York")
                        ).strftime("%Y-%m-%d %H:%M:%S")
                        if pd.notnull(x)
                        else x
                    )
                    df["post_published_date"] = pd.to_datetime(
                        df["post_published_date"], errors="coerce"
                    )
                    float_to_int_columns = [
                        "post_real_click_count",
                        "post_reach_count",
                        "total_impressions",
                        "post_like_count",
                        "post_comment_count",
                        "post_share_count",
                        "twitter_url_clicks",
                        "twitter_video_views",
                        "post_fb_consumptions_by_type_link_clicks",
                        "post_total_reaction_count",
                        "post_fb_stream_comment_count",
                        "post_fb_stream_share_count",
                        "post_fb_video_views",
                        "instagram_post_comments_count",
                        "instagram_post_likes_count",
                        "instagram_business_post_impressions",
                        "instagram_business_post_reel_plays",
                        "linkedin_video_views",
                        "youtube_video_views",
                        "youtube_video_likes",
                        "youtube_video_comments",
                        "youtube_video_shares",
                        "youtube_video_dislikes",
                        "tiktok_video_views",
                        "tiktok_video_likes",
                        "tiktok_video_comments",
                        "tiktok_video_shares",
                        "tiktok_video_reach",
                    ]
                    for i in float_to_int_columns:
                        df[i] = df[i].astype(int)

                    for i in ["is_live_video", "is_dark_post", "is_branded_content"]:
                        df[i] = df[i].map(
                            {"true": True, "True": True, "False": False, "false": False}
                        )
                    try:
                        df.to_gbq(
                            temp_table,
                            project_id=self.project_id,
                            table_schema=social_schema,
                            if_exists="append",
                        )
                    except Exception as e:
                        logger.error("ingested rows not completed ")
                        raise e
                    page_number += 1
                else:
                    logger.info(
                        f"Sprinklr table has not more datas with given time at page {page_number}"
                    )
                    row_status = False
            else:
                logger.error("could not connect sprinklr api")

        check_and_update_table(self.project_id, temp_table, destination_table)
        # check on log table if temp table then replace that table with main table and delete temp table
