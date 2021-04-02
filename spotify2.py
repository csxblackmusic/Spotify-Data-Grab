from __future__ import print_function
import spotipy
import sys
import spotipy
import spotipy.util as util

artist_uri = 'spotify:artist:26VFTg2z8YR0cCuwLzESi2'
scope = 'user-library-read'
username='#####'
client_id='#######'
client_secret='###############'
redirect_uri='##########'
token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

spotify = spotipy.Spotify(auth=token)
results = spotify.artist_top_tracks(artist_uri)



file = open("halsey.txt",'w')
for track in results['tracks'][:20]:
    file.write(track['name'].encode('utf-8')  + '\t')
    artists =track['artists']
    for i in range(len(artists)-1):
        file.write(artists[i]['name'].encode('utf-8') + ', ')
    file.write(artists[len(artists)-1]['name'].encode('utf-8')  +'\t')
    file.write(track['album']['name'].encode('utf-8')  + '\t')
    file.write(str(track['duration_ms']) +'\t')
    file.write(str(track['popularity']) + '\t')
    file.write('\n')
