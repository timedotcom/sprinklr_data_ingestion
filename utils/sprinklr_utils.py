# file contains schema for big query and sfmc data view columns

api_url = "https://api2.sprinklr.com/api/v1/reports/query"

social_schema = [
    {"name": "post_published_date", "type": "TIMESTAMP"},
    {"name": "social_network", "type": "STRING"},
    {"name": "campaign", "type": "STRING"},
    {"name": "campaign_id", "type": "STRING"},
    {"name": "media_type", "type": "STRING"},
    {"name": "actual_link", "type": "STRING"},
    {"name": "vertical_outbound_message", "type": "STRING"},
    {"name": "topic_outbound_message", "type": "STRING"},
    {"name": "advertiser_outbound_message", "type": "STRING"},
    {"name": "magazine_outbound_message", "type": "STRING"},
    {"name": "evergreen_outbound_message", "type": "STRING"},
    {"name": "is_live_video", "type": "BOOLEAN"},
    {"name": "is_dark_post", "type": "BOOLEAN"},
    {"name": "is_branded_content", "type": "BOOLEAN"},
    {"name": "post_real_click_count", "type": "INTEGER"},
    {"name": "post_reach_count", "type": "INTEGER"},
    {"name": "total_impressions", "type": "INTEGER"},
    {"name": "post_like_count", "type": "INTEGER"},
    {"name": "post_comment_count", "type": "INTEGER"},
    {"name": "post_share_count", "type": "INTEGER"},
    {"name": "twitter_url_clicks", "type": "INTEGER"},
    {"name": "twitter_video_views", "type": "INTEGER"},
    {"name": "post_fb_consumptions_by_type_link_clicks", "type": "INTEGER"},
    {"name": "post_total_reaction_count", "type": "INTEGER"},
    {"name": "post_fb_stream_comment_count", "type": "INTEGER"},
    {"name": "post_fb_stream_share_count", "type": "INTEGER"},
    {"name": "post_fb_video_views", "type": "INTEGER"},
    {"name": "instagram_post_comments_count", "type": "INTEGER"},
    {"name": "instagram_post_likes_count", "type": "INTEGER"},
    {"name": "instagram_business_post_impressions", "type": "INTEGER"},
    {"name": "instagram_business_post_reel_plays", "type": "INTEGER"},
    {"name": "linkedin_video_views", "type": "INTEGER"},
    {"name": "youtube_video_views", "type": "INTEGER"},
    {"name": "youtube_video_likes", "type": "INTEGER"},
    {"name": "youtube_video_comments", "type": "INTEGER"},
    {"name": "youtube_video_shares", "type": "INTEGER"},
    {"name": "youtube_video_dislikes", "type": "INTEGER"},
    {"name": "tiktok_video_views", "type": "INTEGER"},
    {"name": "tiktok_video_likes", "type": "INTEGER"},
    {"name": "tiktok_video_comments", "type": "INTEGER"},
    {"name": "tiktok_video_shares", "type": "INTEGER"},
    {"name": "tiktok_video_reach", "type": "INTEGER"},
    {"name": "tiktok_full_video_watched_rate", "type": "FLOAT64"},
    {"name": "post_id", "type": "STRING"},
]


paid_schema = [
    {"name": "post_promotion_start_date", "type": "TIMESTAMP"},
    {"name": "date", "type": "TIMESTAMP"},
    {"name": "channel", "type": "STRING"},
    {"name": "paid_initiative_name", "type": "STRING"},
    {"name": "creative_headline", "type": "STRING"},
    {"name": "outbound_message_tags", "type": "STRING"},
    {"name": "impressions", "type": "INTEGER"},
    {"name": "acm_global_link_clicks", "type": "INTEGER"},
    {"name": "acm_global_total_engagements", "type": "INTEGER"},
    {"name": "acm_global_video_views", "type": "INTEGER"},
    {"name": "paid_initiative_lifetime_budget", "type": "INTEGER"},
    {"name": "ad_variant_id", "type": "STRING"},
    {"name": "spent", "type": "FLOAT64"},
    {"name": "cost_per_1000_impressions_cpm", "type": "FLOAT64"},
    {"name": "paid_initative_end_date", "type": "TIMESTAMP"},
]


gender_all_schema = [
    {"name": "unified_gender", "type": "STRING"},
    {"name": "paid_initiative_name", "type": "STRING"},
    {"name": "impressions", "type": "INTEGER"},
    {"name": "acm_global_link_clicks", "type": "INTEGER"},
    {"name": "acm_global_video_views", "type": "INTEGER"},
]

age_all_platform_schema = [
    {"name": "audience_age", "type": "STRING"},
    {"name": "paid_initiative_name", "type": "STRING"},
    {"name": "impressions", "type": "INTEGER"},
    {"name": "acm_global_link_clicks", "type": "INTEGER"},
    {"name": "acm_global_video_views", "type": "INTEGER"},
]

social_data_columns = [
    "post_published_date",
    "social_network",
    "campaign",
    "campaign_id",
    "media_type",
    "post_id_5",
    "actual_link",
    "vertical_outbound_message",
    "topic_outbound_message",
    "advertiser_outbound_message",
    "magazine_outbound_message",
    "evergreen_outbound_message",
    "is_live_video",
    "is_dark_post",
    "is_branded_content",
    "post_real_click_count",
    "post_reach_count",
    "total_impressions",
    "post_like_count",
    "post_comment_count",
    "post_share_count",
    "twitter_url_clicks",
    "post_twitter_faorites_count",
    "post_twitter_replies_count",
    "post_twitter_retweets_count",
    "post_twitter_reach_count",
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
    "tiktok_full_video_watched_rate",
    "post_id",
]

paid_data_columns = [
    "post_promotion_start_date",
    "date",
    "channel",
    "paid_initiative_name",
    "ad_variant_id",
    "ad_variant",
    "creative_headline",
    "outbound_message_tags",
    "impressions",
    "acm_global_link_clicks",
    "acm_global_total_engagements",
    "acm_global_video_views",
    "paid_initiative_lifetime_budget",
    "spent",
    "cost_per_1000_impressions_cpm",
    "paid_initative_end_date",
]

gender_all_platform_columns = [
    "unified_gender",
    "paid_initiative_name",
    "impressions",
    "acm_global_link_clicks",
    "acm_global_video_views",
]

age_all_platform_columns = [
    "audience_age",
    "paid_initiative_name",
    "impressions",
    "acm_global_link_clicks",
    "acm_global_video_views",
]


age_all_platform_schema = [
    {"name": "audience_age", "type": "STRING"},
    {"name": "paid_initiative_name", "type": "STRING"},
    {"name": "impressions", "type": "INTEGER"},
    {"name": "acm_global_link_clicks", "type": "INTEGER"},
    {"name": "acm_global_video_views", "type": "INTEGER"},
]


age_all_platform_payload = {
    "report": "DAILY_AD_STAT",
    "reportingEngine": "PAID",
    "timeZone": "America/New_York",
    "filters": [
        {
            "dimensionName": "clientId",
            "filterType": "IN",
            "values": [8691, "-1", "-1"],
            "details": {"accessible": True},
        }
    ],
    "groupBys": [
        {
            "heading": "audienceAge_0",
            "dimensionName": "audienceAge",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "paidInitiativeId_1",
            "dimensionName": "paidInitiativeId",
            "groupType": "FIELD",
            "details": {},
        },
    ],
    "projections": [
        {
            "heading": "M_DAILY_AD_STAT_IMPRESSIONS_0",
            "measurementName": "impressions",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_ACM_GLOBAL_LINK_CLICKS_1390_1",
            "measurementName": "ACM_GLOBAL_LINK_CLICKS_1390",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_ACM_GLOBAL_VIDEO_VIEWS_5748_2",
            "measurementName": "ACM_GLOBAL_VIDEO_VIEWS_5748",
            "aggregateFunction": "SUM",
        },
    ],
    "projectionDecorations": [],
    "additional": {
        "Timezone": "America/New_York",
        "dashboardWidget": "true",
        "moduleType": "REPORTING",
        "widgetId": "636a5fdf1a43e71d8841ca20",
        "exportInfo": "false",
        "MARGIN": "false",
        "dashboardId": "63697f8c49a1ee141fdda3aa",
        "engine": "PAID",
        "showTotal": "false",
        "chartType": "TABLE",
        "showRolloverTrends": "false",
        "TABULAR": "true",
    },
    "skipResolve": False,
    "jsonResponse": False,
}

gender_all_platform_payload = {
    "report": "UNIFIED_AD_STAT_BY_GENDER",
    "reportingEngine": "PAID",
    "timeZone": "America/New_York",
    "filters": [
        {
            "dimensionName": "clientId",
            "filterType": "IN",
            "values": [8691, "-1", "-1"],
            "details": {"accessible": True},
        }
    ],
    "groupBys": [
        {
            "heading": "unifiedGenderId_0",
            "dimensionName": "unifiedGenderId",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "paidInitiativeId_1",
            "dimensionName": "paidInitiativeId",
            "groupType": "FIELD",
            "details": {},
        },
    ],
    "projections": [
        {
            "heading": "M_UNIFIED_AD_STAT_BY_GENDER_IMPRESSIONS_0",
            "measurementName": "impressions",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_UNIFIED_AD_STAT_BY_GENDER_ACM_GLOBAL_LINK_CLICKS_1390_1",
            "measurementName": "ACM_GLOBAL_LINK_CLICKS_1390",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_UNIFIED_AD_STAT_BY_GENDER_ACM_GLOBAL_VIDEO_VIEWS_5748_2",
            "measurementName": "ACM_GLOBAL_VIDEO_VIEWS_5748",
            "aggregateFunction": "SUM",
        },
    ],
    "projectionDecorations": [],
    "additional": {
        "Timezone": "America/New_York",
        "dashboardWidget": "true",
        "moduleType": "REPORTING",
        "widgetId": "636a5fa91a43e71d88419ce4",
        "exportInfo": "false",
        "MARGIN": "false",
        "dashboardId": "63697f8c49a1ee141fdda3aa",
        "engine": "PAID",
        "showTotal": "false",
        "chartType": "TABLE",
        "showRolloverTrends": "false",
        "TABULAR": "true",
    },
    "skipResolve": False,
    "jsonResponse": False,
}

paid_data_payload = {
    "report": "DAILY_AD_STAT",
    "reportingEngine": "PAID",
    "timeZone": "America/New_York",
    "filters": [
        {
            "dimensionName": "clientId",
            "filterType": "IN",
            "values": [8691, "-1"],
            "details": {"accessible": True},
        }
    ],
    "groupBys": [
        {
            "heading": "postPromotionStartDate_0",
            "dimensionName": "postPromotionStartDate",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "measurementTime_1",
            "dimensionName": "measurementTime",
            "groupType": "DATE_HISTOGRAM",
            "details": {"isDateTypeDimension": True, "interval": "1h"},
        },
        {
            "heading": "adChannel_2",
            "dimensionName": "adChannel",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "paidInitiativeId_3",
            "dimensionName": "paidInitiativeId",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "adVariantSprinklrId_4",
            "dimensionName": "adVariantSprinklrId",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "adVariantId_5",
            "dimensionName": "adVariantId",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "pivotHeadline_6",
            "dimensionName": "pivotHeadline",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "OUTBOUND_CUSTOM_PROPERTY_7",
            "dimensionName": "OUTBOUND_CUSTOM_PROPERTY",
            "groupType": "FIELD",
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "_TAGS",
                "isSecureField": False,
            },
        },
    ],
    "projections": [
        {
            "heading": "M_DAILY_AD_STAT_IMPRESSIONS_0",
            "measurementName": "impressions",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_ACM_GLOBAL_LINK_CLICKS_1390_1",
            "measurementName": "ACM_GLOBAL_LINK_CLICKS_1390",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_ACM_GLOBAL_TOTAL_ENGAGEMENTS_1851_2",
            "measurementName": "ACM_GLOBAL_TOTAL_ENGAGEMENTS_1851",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_ACM_GLOBAL_VIDEO_VIEWS_5748_3",
            "measurementName": "ACM_GLOBAL_VIDEO_VIEWS_5748",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_PILIFETIMEBUDGETMETRIC_4",
            "measurementName": "piLifetimeBudgetMetric",
            "aggregateFunction": "COUNT",
        },
        {
            "heading": "M_DAILY_AD_STAT_SPENT_5",
            "measurementName": "spent",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_DAILY_AD_STAT_CPM_6",
            "measurementName": "CPM",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "D_PIENDDATE_0",
            "measurementName": "piEndDate",
            "aggregateFunction": "EXTERNAL_VALUE",
        },
    ],
    "projectionDecorations": [],
    "sorts": [{"heading": "paidInitiativeId_3", "order": "DESC"}],
    "additional": {
        "Timezone": "America/New_York",
        "dashboardWidget": "true",
        "moduleType": "REPORTING",
        "widgetId": "6388dce64ff92f5f9d190846",
        "exportInfo": "false",
        "MARGIN": "false",
        "dashboardId": "63697f8c49a1ee141fdda3aa",
        "engine": "PAID",
        "showTotal": "true",
        "chartType": "TABLE",
        "showRolloverTrends": "false",
        "TABULAR": "true",
    },
    "skipResolve": False,
    "jsonResponse": False,
}

social_data_payload = {
    "filters": [
        {
            "dimensionName": "ACCOUNT_ID",
            "filterType": "IN",
            "values": ["334938", "334934", "335365", "334940", "334941", "1260555"],
            "details": {"type": "DIMENSION"},
        },
        {
            "dimensionName": "CLIENT_ID",
            "filterType": "IN",
            "values": [8691, "-1", "-1"],
            "details": {"accessible": True},
        },
    ],
    "groupBys": [
        {
            "heading": "POST_PUBLISHED_DATE_0",
            "dimensionName": "POST_PUBLISHED_DATE",
            "groupType": "FIELD",
            "details": {"isDateTypeDimension": True, "interval": "1h"},
        },
        {
            "heading": "SN_TYPE_1",
            "dimensionName": "SN_TYPE",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "CAMPAIGN_ID_2",
            "dimensionName": "CAMPAIGN_ID",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "CAMPAIGN_ID_DIMENSION_3",
            "dimensionName": "CAMPAIGN_ID_DIMENSION",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "MEDIA_TYPE_4",
            "dimensionName": "MEDIA_TYPE",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "POST_ID_5",
            "dimensionName": "POST_ID",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "ACTUAL_LINK_6",
            "dimensionName": "ACTUAL_LINK",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "OUTBOUND_CUSTOM_PROPERTY_7",
            "dimensionName": "OUTBOUND_CUSTOM_PROPERTY",
            "groupType": "FIELD",
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "5d6fe5b3b9c15063a02f8018",
                "isSecureField": False,
            },
        },
        {
            "heading": "OUTBOUND_CUSTOM_PROPERTY_8",
            "dimensionName": "OUTBOUND_CUSTOM_PROPERTY",
            "groupType": "FIELD",
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "5d6fe621b9c15063a02fb1ef",
                "isSecureField": False,
            },
        },
        {
            "heading": "OUTBOUND_CUSTOM_PROPERTY_9",
            "dimensionName": "OUTBOUND_CUSTOM_PROPERTY",
            "groupType": "FIELD",
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "5d7c548794de9d798224a1a2",
                "isSecureField": False,
            },
        },
        {
            "heading": "OUTBOUND_CUSTOM_PROPERTY_10",
            "dimensionName": "OUTBOUND_CUSTOM_PROPERTY",
            "groupType": "FIELD",
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "5d79bba794de9d4aa31c0677",
                "isSecureField": False,
            },
        },
        {
            "heading": "OUTBOUND_CUSTOM_PROPERTY_11",
            "dimensionName": "OUTBOUND_CUSTOM_PROPERTY",
            "groupType": "FIELD",
            "details": {
                "srcType": "CUSTOM",
                "fieldName": "5d79af6194de9d4aa31a8c2f",
                "isSecureField": False,
            },
        },
        {
            "heading": "IS_LIVE_VIDEO_12",
            "dimensionName": "IS_LIVE_VIDEO",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "IS_DARK_POST_13",
            "dimensionName": "IS_DARK_POST",
            "groupType": "FIELD",
            "details": {},
        },
        {
            "heading": "IS_BRANDED_CONTENT_14",
            "dimensionName": "IS_BRANDED_CONTENT",
            "groupType": "FIELD",
            "details": {},
        },
    ],
    "projections": [
        {
            "heading": "M_POST_INSIGHTS_POST_REAL_CLICK_COUNT_0",
            "measurementName": "POST_REAL_CLICK_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_REACH_COUNT_1",
            "measurementName": "POST_REACH_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TOTAL_IMPRESSIONS_2946_2",
            "measurementName": "TOTAL_IMPRESSIONS_2946",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_LIKE_COUNT_3",
            "measurementName": "POST_LIKE_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_COMMENT_COUNT_4",
            "measurementName": "POST_COMMENT_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_SHARE_COUNT_5",
            "measurementName": "POST_SHARE_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TWITTER_URL_CLICKS_6",
            "measurementName": "TWITTER_URL_CLICKS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_TWITTER_FAVORITES_COUNT_7",
            "measurementName": "POST_TWITTER_FAVORITES_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_TWITTER_REPLIES_COUNT_8",
            "measurementName": "POST_TWITTER_REPLIES_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_TWITTER_RETWEETS_COUNT_9",
            "measurementName": "POST_TWITTER_RETWEETS_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_TWITTER_REACH_COUNT_10",
            "measurementName": "POST_TWITTER_REACH_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TWITTER_VIDEO_VIEWS_11",
            "measurementName": "TWITTER_VIDEO_VIEWS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_FB_CONSUMPTIONS_BY_TYPE_LINK_CLICKS_12",
            "measurementName": "POST_FB_CONSUMPTIONS_BY_TYPE_LINK_CLICKS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_TOTAL_REACTION_COUNT_13",
            "measurementName": "POST_TOTAL_REACTION_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_FB_STREAM_COMMENT_COUNT_14",
            "measurementName": "POST_FB_STREAM_COMMENT_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_FB_STREAM_SHARE_COUNT_15",
            "measurementName": "POST_FB_STREAM_SHARE_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_POST_FB_VIDEO_VIEWS_16",
            "measurementName": "POST_FB_VIDEO_VIEWS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_INSTAGRAM_POST_COMMENTS_COUNT_17",
            "measurementName": "INSTAGRAM_POST_COMMENTS_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_INSTAGRAM_POST_LIKES_COUNT_18",
            "measurementName": "INSTAGRAM_POST_LIKES_COUNT",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_INSTAGRAM_BUSINESS_POST_IMPRESSIONS_19",
            "measurementName": "INSTAGRAM_BUSINESS_POST_IMPRESSIONS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_INSTAGRAM_BUSINESS_POST_REEL_PLAYS_20",
            "measurementName": "INSTAGRAM_BUSINESS_POST_REEL_PLAYS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_LINKEDIN_VIDEO_VIEWS_21",
            "measurementName": "LINKEDIN_VIDEO_VIEWS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_YOUTUBE_VIDEO_VIEWS_22",
            "measurementName": "YOUTUBE_VIDEO_VIEWS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_YOUTUBE_VIDEO_LIKES_23",
            "measurementName": "YOUTUBE_VIDEO_LIKES",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_YOUTUBE_VIDEO_COMMENTS_24",
            "measurementName": "YOUTUBE_VIDEO_COMMENTS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_YOUTUBE_VIDEO_SHARES_25",
            "measurementName": "YOUTUBE_VIDEO_SHARES",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_YOUTUBE_VIDEO_DISLIKES_26",
            "measurementName": "YOUTUBE_VIDEO_DISLIKES",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TIKTOK_VIDEO_VIEWS_27",
            "measurementName": "TIKTOK_VIDEO_VIEWS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TIKTOK_VIDEO_LIKES_28",
            "measurementName": "TIKTOK_VIDEO_LIKES",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TIKTOK_VIDEO_COMMENTS_29",
            "measurementName": "TIKTOK_VIDEO_COMMENTS",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TIKTOK_VIDEO_SHARES_30",
            "measurementName": "TIKTOK_VIDEO_SHARES",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TIKTOK_VIDEO_REACH_31",
            "measurementName": "TIKTOK_VIDEO_REACH",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "M_POST_INSIGHTS_TIKTOK_FULL_VIDEO_WATCHED_RATE_32",
            "measurementName": "TIKTOK_FULL_VIDEO_WATCHED_RATE",
            "aggregateFunction": "SUM",
        },
        {
            "heading": "D_POSTIDEXTERNAL_0",
            "measurementName": "postIdExternal",
            "aggregateFunction": "EXTERNAL_VALUE",
        },
    ],
    "projectionDecorations": [],
    "sorts": [{"heading": "POST_PUBLISHED_DATE_0", "order": "DESC"}],
    "additional": {
        "Timezone": "America/New_York",
        "dashboardWidget": "true",
        "moduleType": "REPORTING",
        "widgetId": "637cfdb421261d58aa0d45ab",
        "exportInfo": "false",
        "dashboardId": "637cfbf321261d58aa0c2ecd",
        "engine": "PLATFORM",
        "showTotal": "false",
        "chartType": "TABLE",
        "showRolloverTrends": "false",
        "TABULAR": "true",
    },
    "skipResolve": False,
    "jsonResponse": False,
}
