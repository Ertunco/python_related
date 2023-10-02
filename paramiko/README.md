# Description

This Python script transfers images from Google Drive to an SFTP server.

To use the script, you will need to have the following installed:

- Python 3.6 or higher
- Paramiko

## Paramiko
Pure-python(3.6+) implementation of the SSHv2 protocol, providing both client and server functionality

# Installation

```bash
pip install requirements.txt
```

Once you have installed the required dependencies, you can run the script as follows:

Python
```python
python create_connection.py
```

Use code with caution. Learn more
The script will prompt you for your Google Drive credentials and SFTP server credentials. Once you have entered your credentials, the script will begin transferring the images.

The script will create a local directory called images1/ to store the downloaded images. Once the images have been transferred, the script will delete the local directory.

# Example usage:

```python
python create_connection.py
```

Troubleshooting:

If you are having trouble using the script, please check the following:

- Make sure you have installed all of the required dependencies.
- Make sure you have entered your Google Drive credentials and SFTP server credentials correctly.
- Make sure that the SFTP server is accessible.
- Make sure that you have write permission to the remote directory on the SFTP server.

If you are still having trouble, please post an issue on the GitHub repository for this project.