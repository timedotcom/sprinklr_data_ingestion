import logging
import os
import re
import yaml
import google.auth
from google.cloud import secretmanager

from google.cloud.logging.handlers import CloudLoggingHandler


def get_cloud_handler():
    client = google.cloud.logging.Client()
    return CloudLoggingHandler(client)


def get_logger(name):
    log_format = "%(asctime)s - %(name)s -  %(levelname)s - %(message)s"
    try:
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        log_file = log_dir + "/prod.log"
    except OSError:
        return logging.getLogger(name)
    logging.basicConfig(level=logging.INFO, filename=log_file, filemode="a")
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(log_format))
    logging.getLogger(name).addHandler(console)
    logger = logging.getLogger(name)
    logger.addHandler(get_cloud_handler())
    return logger


def download_creds(secret_id, config_version):
    """Downloads secret from Google Secret Manager"""

    client = secretmanager.SecretManagerServiceClient()
    credentials, project_id = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{config_version}"

    response = client.access_secret_version(request={"name": name})
    raw_config = response.payload.data.decode("UTF-8")
    return yaml.safe_load(raw_config)
