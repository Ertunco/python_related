# Description

This Python script creates a connection to an SFTP server. This server is a test SFTP server hence credentials shared directly in case somebody wants to connect to the same server (test.rebex.net)

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

The script will connect to a directory in the given SFTP server.

# Example usage:

```python
python create_connection.py
```

Troubleshooting:

If you are having trouble using the script, please check the following:

- Make sure you have installed all of the required dependencies.
- Make sure you have entered the SFTP server credentials correctly.
- Make sure that the SFTP server is accessible.
- Make sure that you have write permission to the remote directory on the SFTP server.

If you are still having trouble, please post an issue on the GitHub repository for this project.