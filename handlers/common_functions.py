from slack import WebClient


def is_admin(client: WebClient, request_form: dict) -> bool:
    """
    Checks if the user that send the request is admin.
    """
    info = client.conversations_info(
            channel=request_form.get('channel_id')
        )

    if info['channel']['creator'] != request_form['user_id']:
        return False
    return True

def upload_file(client: WebClient, request_form: dict, file_to_upload) -> None:
    client.files_upload(
        channels=request_form.get('channel_id'),
        file=file_to_upload
    )
