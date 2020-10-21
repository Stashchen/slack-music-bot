from slack import WebClient
import msg_blocks

from handlers.common_functions import is_admin
from handlers.msg_functions import send_msg_to_user, send_msg_to_chat


def limit_disco_songs(limit: int, command_arguments: str) -> int:
    """
    Check the argument of /disco command and return the number of songs,
    that are going to be listed.
    VALID: 1 < limit <= 10
    """
    try:
        # As it is valid to have only integer as argument, then it should
        # Be possible to convert it
        limit_arg = int(command_arguments)
    except ValueError:
        return limit

    if 1 < limit_arg <= limit:
        return limit_arg
    else:
        return limit

def start_disco(client: WebClient, request_form: dict, limit: int) -> None:
    """
    Main function that is invoked when we run /disco command.
    /disco is valid only for channel admin.
    """
    if is_admin(client, request_form):
        send_msg_to_chat(client, request_form, 'GOOD')
    else:
        send_msg_to_user(client, request_form, 'You have no permission.')

def handle_command(client: WebClient, request_form: dict) -> None:
    """
    Function that will handle all the commands that is going to be sent to the bot.
    """
    
    command = request_form.get('command')

    if command == '/disco':
        if command_args:=request_form.get('text'):
            limit_of_songs = limit_disco_songs(10, command_args)
            start_disco(client, request_form, limit_of_songs)
        else:
            start_disco(client, request_form, 10)
        