from slack import WebClient


def send_msg_to_user(client: WebClient, request_form: dict, msg: str) -> None:
    """
    Function, that makes bot send message to user that send the request.
    """
    client.chat_postEphemeral(
            channel=request_form.get('channel_id'),
            user=request_form.get('user_id'),
            text=msg
        )

def send_msg_to_chat(client: WebClient, request_form: dict, msg: str) -> None:
    """
    Function, that makes bot send message to the chat.
    """
    client.chat_postMessage(
            channel=request_form.get('channel_id'),
            text=msg
        )
