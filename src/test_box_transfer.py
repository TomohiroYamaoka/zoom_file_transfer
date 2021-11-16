from boxsdk import JWTAuth
from boxsdk import Client


auth = JWTAuth.from_settings_file('../config.json')
client = Client(auth)

root_folder = client.folder(folder_id='0')

base_dir = root_folder.create_subfolder('hogefuga')
