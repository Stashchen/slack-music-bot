import json


def get_payload_as_dict(request) -> dict:
    """
    Function that get payload from POST request and convert it to dict with json lib.
    """
    payload = request.form.get('payload')
    return json.loads(payload)

def get_current_channel_id(request):
    pass

def get_user_id(request) -> str:
    """
    Function that return user id from POST request.
    """
    payload = get_payload_as_dict(request)
    return payload['user']['id']

def get_selected_songs_list(request) -> list:
    """
    Function that return selected_songs_list from POST request.
    """
    payload = request.form.get('payload')

    payload_as_dict = json.loads(payload)

    block_name = payload_as_dict['message']['blocks'][0]['block_id']
    return payload_as_dict['state']['values'][block_name]['music_poll']['selected_options']