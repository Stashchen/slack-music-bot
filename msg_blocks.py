import json
from undefined_func import get_of_songs


START_DISCO = {
    "type": "section",
    "text": {
        "type": "plain_text",
        "text": "Hey. Please, vote for the next song"
    },
    "accessory": {
        "type": "checkboxes",
        "action_id": "music_poll",
        "options": [
            {
                "value": "1",
                "text": {
                    "type": "plain_text",
                    "text": "Checkbox 1"
                }
            },
            {
                "value": "2",
                "text": {
                    "type": "plain_text",
                    "text": "Checkbox 2"
                }
            }
        ]
    }
}

def create_block_of_songs(request, limit):
    """
    Main function that creates blocks with songs to choose.
    This block needs to be connected to messages sent by bot.
    """
    get_of_songs(limit)

    checkbox_options = []

    # Get temp song data
    with open('songs.json') as f:
        songs = json.load(f)

    for index, song in enumerate(songs):
        song_option = {
            'value': str(index + 1),
            'text': {
                'type': 'plain_text',
                'text': '{} --- {} votes'.format(song['title'], len(song['voted_users']))
            }
        }
        checkbox_options.append(song_option)
    
    START_DISCO['accessory']['options'] = checkbox_options

    return [START_DISCO]