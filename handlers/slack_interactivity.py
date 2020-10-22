import json


def update_poll_with_user_votes(user_id, selected_songs):
    """
    Now: Function that updates main songs.json file when user vote for a song.
    return example: votes: {user_id: user_id, votes: [votes]}
    
    Future: Function that updates <storage> when user vote for a song.
    """
    
    with open('songs.json') as file_with_songs:
        songs = json.load(file_with_songs)

        selected_songs_values = [int(song['value']) for song in selected_songs]

        print(selected_songs_values)

        for song in songs:
            if song['value'] in selected_songs_values:
                song['voted_users'].append(user_id)
            else:
                if user_id in song['voted_users']:
                    songs['voted_users'].pop(song['voted_users'].find(user_id))

        print(songs)

        # file_with_songs.write(json.dump(songs))