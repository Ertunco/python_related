from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

folder_id = '1Iwd4U0ittLP2dne4I0QFufuyxXkDPwtZ'

# Query the files
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

# List files
for file1 in file_list:
    print(f'Title: {file1["title"]}, ID: {file1["id"]}')