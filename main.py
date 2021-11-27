import time
from ApiShit import *
import json


#open config file end load settings
with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)

token = jsonObject["ID"] 

#config stuff
#TOKEN_STR = "BQAgARCDqCT8oB2AHeM155YIQWGrZTR2lR6NT1Jv6Dc4UO-iLcGUZaQ3WUHG94snjEZBqKydXzFefAQR2MBMdNvRb3Rgn19w_9US-yVNxmiqb-IKGbBJ4yqUj-qPrSCxoEmPfZt8P0ESpaZUd7X9U7fVEw5Jk8381VDleWpW"


#write song name and artist name into "song.txt" file
def writer(Artist, SongName):
    with open("song.txt", "w") as f:
        message = "Song: %s Artist: %sa" % (Artist, SongName)
        f.write(message)


#read song name and artist name from apishit.py and write it to song.txt file
while True:
    Artist_Name = get_current_track(token)['artists']
    Song_Name = get_current_track(token)['track_name']
    writer(Song_Name, Artist_Name)
