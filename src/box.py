import os
from boxsdk import OAuth2, Client
from os.path import join, dirname
from dotenv import load_dotenv

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

file_path = '/testfile/photo.jpg'
file_name = 'photo.jpg'
folder_id = os.getenv("FOLDER_ID")
uploaded_file = client.folder(folder_id).upload('file_path, file_name')
