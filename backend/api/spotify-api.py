import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your-client-id",
                                               client_secret="your-client-secret",
                                               redirect_uri="your-redirect-uri",
                                               scope="user-library-read"))

results = sp.current_user_playlists()
for idx, item in enumerate(results['items']):
    print(f"{idx + 1}. {item['name']}")
