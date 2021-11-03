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
