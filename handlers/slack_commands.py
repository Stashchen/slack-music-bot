from slack import WebClient
import msg_blocks

from handlers.common_functions import is_admin, upload_file
from handlers.msg_functions import send_msg_to_user, send_msg_to_chat
from undefined_func import choose_the_winner_song, download_song, delete_songs_json, make_valid_song_name


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

        # Realization of only one poll, based on a song.json file.
        # Needs to be rebuild for db.
        try:
            f = open('songs.json')
            send_msg_to_user(client, request_form, 'Previous poll is not finished. Type /lightsoff to finish it.')
        except FileNotFoundError:
            blocks = msg_blocks.create_block_of_songs(request_form, limit)
            send_msg_to_chat(client, request_form, 'MUSIC POLL🎶', blocks=blocks)
        
    else:
        send_msg_to_user(client, request_form, 'You have no permission.')

def start_lightsoff(client: WebClient, request_form: dict):
    """
    Function that is invoked when we run /lightsoff command.
    Finish the last poll and give the song.
    """
    try:
        f = open('songs.json')
        send_msg_to_chat(client, request_form, 'The poll is finished. The winner is ...')
        winner = choose_the_winner_song()
        song_title = make_valid_song_name(winner)
        download_song(song_title, winner['link'], './songs')
        upload_file(client, request_form, './songs/{}.mp3'.format(song_title))
        delete_songs_json()
    except FileNotFoundError:
        send_msg_to_user(client, request_form, 'No polls started yet. Use /disco command to run poll.')


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
    elif command == '/lightsoff':
        start_lightsoff(client, request_form)
        