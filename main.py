import time
from ApiShit import *
import json

with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)

TOKEN = jsonObject["ID"] 

#config stuff
#TOKEN_STR = "BQAgARCDqCT8oB2AHeM155YIQWGrZTR2lR6NT1Jv6Dc4UO-iLcGUZaQ3WUHG94snjEZBqKydXzFefAQR2MBMdNvRb3Rgn19w_9US-yVNxmiqb-IKGbBJ4yqUj-qPrSCxoEmPfZt8P0ESpaZUd7X9U7fVEw5Jk8381VDleWpW"

def writer(Artist, SongName):
    with open("song.txt", "w") as f:
        message = "Song: %s Artist: %s" % (Artist, SongName)
        f.write(message)


#Slicing final text


while True:
    Artist_Name = get_current_track(TOKEN)['artists']
    Song_Name = get_current_track(TOKEN)['track_name']
    writer(Song_Name, Artist_Name)