#Made by Thomas Mirbey, Discord : tfx_, github: github.com/ThomasM2568
#This Python script automates the process of creating a weekly backup playlist of the "Discover Weekly"
#playlist on Spotify. It uses the Spotipy library to interact with the Spotify Web API.
#The script checks if the "Discover Weekly" playlist exists in the user's profile and creates a new playlist named a
#fter the current week if it doesn't exist. Then, it copies the songs from the "Discover Weekly" playlist to the new backup playlist
#ensuring that your favorite weekly recommendations are saved for future listening. The script requires proper authentication using Spotify's OAuth flow
#and it may need to be authorized with the necessary scopes to perform playlist-related actions.
#Make sure to set up your Spotify credentials and authentication details before running the script.

# -----------------------------------------------------------------------------------------------
#                           Importing modules
# -----------------------------------------------------------------------------------------------

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime
# -----------------------------------------------------------------------------------------------
#                           Client Information
# -----------------------------------------------------------------------------------------------

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://localhost:8080'
scope = 'playlist-read-private playlist-modify-public playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# -----------------------------------------------------------------------------------------------
#                                  Functions
# -----------------------------------------------------------------------------------------------

def get_user_playlists(sp):
    playlists={}
    try:
        results = sp.current_user_playlists()

        for idx, item in enumerate(results['items']):
            playlists[item['name']]=item['id']
    except:
        print("An error occured")
    return playlists

def get_weekly_discovery_playlist_name():
    current_date = datetime.datetime.now().isocalendar()[1]
    date1=str(datetime.datetime.now().date()).split("-")
    date2=date1[0]+"-"+date1[1]
    playlist_name="Weekly Playlist - Week "+str(current_date)+" ("+date2+")"
    return playlist_name


def is_playlist_in_dict(playlist_name,dictionnary):
    if not(playlist_name in dictionnary.keys()):
        return False
    else:
        return True
    
def get_user_id():
    return sp.me()["id"]

def get_playlist_id(playlist_name, sp):
    playlists = get_user_playlists(sp)
    if playlist_name in playlists.keys():
        return playlists[playlist_name]
    return None

        
def main(sp):
    try:
        playlists = get_user_playlists(sp)
        playlist_name = get_weekly_discovery_playlist_name()
        
        if not is_playlist_in_dict('Discover Weekly', playlists):
            print("No Discover Weekly playlist in user's profile")
        else:
            weekly_discover_playlist_id = playlists["Discover Weekly"]
            
            if is_playlist_in_dict(playlist_name, playlists):
                print("Weekly Discover playlist backup already exists")
            else:
                user_info = get_user_id()
                week = datetime.datetime.now().isocalendar()[1]
                sp.user_playlist_create(user=user_info, name=playlist_name, public=False, collaborative=False, description='Copy of the Discover Weekly playlist (Week '+str(week)+')')
                
                playlist_name_id = get_playlist_id(playlist_name, sp)
                if playlist_name_id is not None:
                    try:
                        for songs in sp.user_playlist_tracks(user=user_info, playlist_id=weekly_discover_playlist_id, fields=None, limit=100, offset=0, market=None)["items"]:
                            sp.user_playlist_add_tracks(user=user_info, playlist_id=playlist_name_id, tracks=[songs["track"]["uri"]], position=None)
                        
                        return("Playlist created successfully")
                    
                    except spotipy.exceptions.SpotifyException as e:
                        print("Error while adding tracks:", e)
                else:
                    return("Error in get_playlist_id()")
        
    except Exception as e:
        # Exception handling code
        return str(e)

    

# -----------------------------------------------------------------------------------------------
#                                Code Execution
# -----------------------------------------------------------------------------------------------
    

print(main(sp))




#Old code in case it does work 
    
"""
try:
    if not("Discover Weekly" in playlists.keys()):
        print("No Discover Weekly playlist in user's profile")
    else:
        weekly_discover_playlist_id=playlists["Discover Weekly"]
        
        if(playlist_name in playlists.keys()):
            print("Weekly Discover playlist backup already exists")
        else:
            user_info=sp.me()["id"]
            sp.user_playlist_create(user=user_info, name=playlist_name, public=False, collaborative=False, description='Copy of the recommanded playlist of the '+str(date_actuelle)+' week')
            
            try:
                results = sp.current_user_playlists()

                for idx, item in enumerate(results['items']):
                    if(item['name']==playlist_name):
                        playlist_name_id=item["id"]
            except:
                print("An error occured")
                
            try:
                for songs in sp.user_playlist_tracks(user=user_info, playlist_id=weekly_discover_playlist_id, fields=None, limit=100, offset=0, market=None)["items"]:
                    sp.user_playlist_add_tracks(user=user_info, playlist_id=playlist_name_id, tracks=[songs["track"]["uri"]], position=None)
                    
            except spotipy.exceptions.SpotifyException as e:
                print("Error while adding tracks :", e)
                
                
except spotipy.exceptions.SpotifyException as e:
    print("Error:", e)
"""

