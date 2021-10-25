import json
import Box
import logging
import urllib
import os
from boxsdk import OAuth2, Client
from os.path import join, dirname
from dotenv import load_dotenv

logging.getLogger('boxsdk').setLevel(logging.CRITICAL)

box_setting = {
    "client_id": "BOX_CLIENT_ID",
    "client_secret": "BOX_CLIENT_SECRET",
    "enterprise_id": "BOX_ENTERPRISE_ID",
    "jwt_key_id": "BOX_JWT_KEY_ID",
    "rsa_private_key_data": "BOX_PRIVATE_KEY"
}

box_folder_id = "BOX_FOLDER_ID"
box_user = "BOX_USER"
box_file = Box.File(**box_setting)
box_file.login(box_user)


def main():
    file = fetch_recordings_file()
    transfer(file)


def fetch_recordings_file():
    zoom_recordins_file = "hoge"
    return zoom_recordins_file


def transfer(file):
    url = file["download_url"]
    token = file["download_token"]
    headers = {"Authorization": "Bearer {}".format(token)}
    stream, length = downloader(url, headers)


def downloader(url, headers):
    args = locals()
    req = urllib.request.Request(**args)
    try:
        res = urllib.request.urlopen(req)
        headers = res.headers
        contentLength = int(headers["Content-Length"])
        return res, contentLength
    except Exception as e:
        raise e


def uploadToBox():
    box_folder_id = "hoge"
    upload_file = Client.folder(box_folder_id)
