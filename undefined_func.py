# Contain functions that I do not know where to place

import json
import random
import requests
from os import system
from bs4 import BeautifulSoup

import json
import urllib


def get_of_songs(limit: int) -> None:
    """
    Download random songs from ZAYCEV.NET.
    """
    songs = []

    response = requests.get('https://zaycev.net')
    soup = BeautifulSoup(response.content, 'html.parser')

    all_top_songs = soup.find_all(class_='musicset-track__download-link')

    for index, song_a in enumerate(random.sample(all_top_songs, limit)):        
        song = {}
        song['index'] = index + 1
        song['title'] = song_a.get('title').split(' ', 2)[-1]
        song['link'] = 'https://zaycev.net' + song_a.get('href')
        song['votes'] = 0

        songs.append(song)

    with open('songs.json', 'w') as f:
        f.write(json.dumps(songs))

def download_song(title, link, path):
    system(f'wget -O {path}/{title}.mp3 "{link}"')

def choose_the_winner_song() -> dict:
    """
    For now, it parse songs.json file and find song with max votes.
    Later it will be based on db.
    """
    with open('songs.json') as f:
        songs = json.load(f) 
    
    winner = songs[0]
    for song in songs[1:]:
        if song['votes'] > winner['votes']:
            winner = song

    return winner

def delete_songs_json() -> None:
    system('rm songs.json')