import os
from boxsdk import OAuth2, Client
from os.path import join, dirname
from dotenv import load_dotenv

from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ID = os.getenv("BOX_ID")
SECRET = os.getenv("BOX_SECRET_KEY")
TOKEN = os.getenv("BOX_TOKEN")

auth = OAuth2(
    client_id='ID',
    client_secret='SECRET',
    access_token='TOKEN',
)
client = Client(auth)

folder_id = os.getenv("FOLDER_ID")
uploaded_file = client.folder(folder_id).upload('test.py')
