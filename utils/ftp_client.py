import pysftp as sftp


def list_dir_ftp(folder_name, creds, creds_key):
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    connection = sftp.Connection(
        host=creds[creds_key]["host"],
        username=creds[creds_key]["user_name"],
        password=creds[creds_key]["password"],
        cnopts=cnopts,
    )
    files = connection.listdir(folder_name)
    connection.close()
    return files


def download_sftp_file(file_name, download_path, creds, creds_key):
    print("downloading file {} from ftp...".format(file_name))
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    connection = sftp.Connection(
        host=creds[creds_key]["host"],
        username=creds[creds_key]["user_name"],
        password=creds[creds_key]["password"],
        cnopts=cnopts,
    )
    connection.get(download_path + file_name, "/tmp/" + file_name)
    print("downloading completed for {} ".format(file_name))

    connection.close()
