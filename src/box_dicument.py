from boxsdk import JWTAuth
from boxsdk import Client

# Configure JWT auth object
sdk = JWTAuth(
    client_id="********************",
    client_secret="*****************",
    enterprise_id="00000",
    jwt_key_id="AAAAAA",
    rsa_private_key_file_sys_path="****.pem",
    rsa_private_key_passphrase="******"
)

# Get auth client
client = Client(sdk)

# Set upload values
file_path = '/testfile/photo.jpg'
file_name = 'photo.jpg'
folder_id = '0'

box_file = client.folder(folder_id).upload(file_path, file_name)
print(vars(box_file))
