import paramiko, errno, os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

## Paramiko Connection ##
def CreateSFTP(host, port, username, password):
    """Creates an SFTP client to connect to the given server.

    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect on.
        username (str): The username to use to authenticate to the server.
        password (str): The password to use to authenticate to the server.

    Returns:
        paramiko.SFTPClient: An SFTP client connected to the server.
    """

    client = paramiko.SSHClient()
    # client.load_system_host_keys()
    client.connect(host, port, username, password)
    return client.open_sftp()

def sFtpExists(sftpclient, path):
    """Returns True if the remote path exists.

    Args:
        sftpclient (paramiko.SFTPClient): An SFTP client connected to the server.
        path (str): The remote path to check.

    Returns:
        bool: True if the path exists, False otherwise.
    """

    try:
        sftpclient.stat(path)
    except IOError as e:
        if e.errno == errno.ENOENT:
            return False
        raise
    else:
        return True

## Google Drive Connection ##
def GetGoogleDriveClient():
    """Returns a Google Drive client.

    Returns:
        GoogleDrive: A Google Drive client.
    """

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def main():
    """Transfers images from Google Drive to an SFTP server."""

    # Get the SFTP client
    host = 'test.rebex.net'
    port = 22
    username = 'demo'
    password = 'password'
    sftp_client = CreateSFTP(host, port, username, password)

    # Get the Google Drive client
    drive_client = GetGoogleDriveClient()
    print(drive_client)

    # Get the list of folders to transfer images from
    folder_list = drive_client.ListFile({'q': "'1Iwd4U0ittLP2dne4I0QFufuyxXkDPwtZ' in parents and trashed=false"}).GetList()
    print(folder_list)

    # # Iterate over the folders and transfer the images
    # for folder in folder_list:
    #     # Create the remote directory if it doesn't exist
    #     remote_dir = '/www/shs/mf_gim_9fc2/i/' + folder['title']
    #     if not sFtpExists(sftp_client, remote_dir):
    #         sftp_client.mkdir(remote_dir)

    #     # Get the list of images to transfer
    #     image_list = drive_client.ListFile({'q': "'" + folder['id'] + "' in parents and trashed=false"}).GetList()

    #     # Iterate over the images and transfer them
    #     for image in image_list:
    #         # Download the image to the local machine
    #         local_file = './images1/' + image['title']
    #         image.GetContentFile(local_file)

    #         # Upload the image to the remote server
    #         remote_file = remote_dir + '/' + image['title']
    #         sftp_client.put(local_file, remote_file)

    #         # Delete the local file
    #         os.remove(local_file)

    # # Close the SFTP client
    # sftp_client.close()

    # # Remove the local directory
    # os.rmdir('./images1/')

if __name__ == '__main__':
    main()