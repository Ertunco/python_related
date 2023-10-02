import paramiko, errno, os

def create_sftp_client(host, port, username, password):
    # Initialize the SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    ssh.connect(host, port, username, password)

    # Initialize the SFTP client
    sftp = ssh.open_sftp()

    # Perform SFTP operations
    # For example, list files in the home directory
    print(sftp.listdir('.'))

    # Close SFTP and SSH sessions
    sftp.close()
    ssh.close()

def main():
    """Transfers images from Google Drive to an SFTP server."""

    # Get the SFTP client
    host = 'test.rebex.net'
    port = 22
    username = 'demo'
    password = 'password'
    sftp_client = create_sftp_client(host, port, username, password)

if __name__ == '__main__':
    main()