
# <span style="font-size:30px">Weekly Backup Playlist for "Discover Weekly" on Spotify :musical_note::sparkles:</span>


This Python script automates the process of creating a weekly backup playlist of the "Discover Weekly" playlist on Spotify. :rocket: It uses the Spotipy library to interact with the Spotify Web API.

# <span style="font-size:20px">:bookmark_tabs: Requirements</span>


Make sure to install the required modules using the following commands:

```bash

pip install spotipy
pip install datetime
```
# <span style="font-size:20px">:bulb: How it Works</span>


The script checks if the "Discover Weekly" playlist exists in the user's Spotify profile. If the playlist does not exist, it informs the user that there is no "Discover Weekly" playlist. If the playlist already exists, it creates a new playlist with the name "Weekly Playlist - Week XX (YYYY-MM)" (where "XX" represents the current week number and "YYYY-MM" represents the year and month). :date:

After creating the backup playlist, the script copies all the songs from the "Discover Weekly" playlist to the newly created backup playlist. This ensures that your favorite weekly recommendations are saved for future listening. :headphones:


# <span style="font-size:20px">:key: Spotify Client Information</span>
To use this script, you need to set up your Spotify client information:

```bash
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
```
# <span style="font-size:20px">:floppy_disk: Code Execution</span>

To run the script, execute the following command:

```bash

python Spotify_Weekly_Playlist.py
```

# <span style="font-size:20px">:mag: Additional Notes</span>

The script requires proper authentication using Spotify's OAuth flow and may need to be authorized with the necessary scopes to perform playlist-related actions.

Please ensure that you have your Spotify credentials and authentication details set up correctly before running the script. :lock:

If you encounter any issues or errors, the script will display appropriate error messages to help troubleshoot the problem. :warning:

Please note that this script was made by Thomas Mirbey. If you have any questions or need further assistance, feel free to reach out via Discord (tfx_) or visit my GitHub https://github.com/ThomasM2568. Happy music listening! :musical_note:
