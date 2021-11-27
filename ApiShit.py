import requests
from pprint import pprint

apiUrl = 'https://api.spotify.com/v1/me/player/currently-playing'

#open spotify url and do all weird complicated api shit
def get_current_track(access_token):
    response = requests.get(
        apiUrl, headers={
            "Authorization": "Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link,
    }

    return current_track_info
