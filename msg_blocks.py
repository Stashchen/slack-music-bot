START_DISCO = {
    "type": "section",
    "text": {
        "type": "plain_text",
        "text": "Hey. Please, vote for the next song"
    },
    "accessory": {
        "type": "checkboxes",
        "action_id": "this_is_an_action_id",
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

def create_block_of_songs(request):
    START_DISCO['accessory']