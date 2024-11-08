import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()  

# Initialize Spotify client
app = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("Spotify_Client_ID"),
        client_secret=os.getenv("Spotify_Client_Secret")
    )
)

# Search for the track
results = app.search(q='24h', type='track', limit=1)

# Iterate through results
for idx, track in enumerate(results['tracks']['items']):
    track_id = track['id']
    track_name = track['name']
    artists = '; '.join([artist['name'] for artist in track['artists']])
    album_name = track['album']['name']
    popularity = track['popularity']
    duration_ms = track['duration_ms']
    explicit = track['explicit']
    
    # Get audio features for the track
    audio_features = app.audio_features(track_id)[0]
    danceability = audio_features['danceability']
    energy = audio_features['energy']
    key = audio_features['key']
    loudness = audio_features['loudness']
    mode = audio_features['mode']
    speechiness = audio_features['speechiness']
    acousticness = audio_features['acousticness']
    instrumentalness = audio_features['instrumentalness']
    liveness = audio_features['liveness']
    valence = audio_features['valence']
    tempo = audio_features['tempo']
    time_signature = audio_features['time_signature']
    
    # Get genres of the first artist
    artist_id = track['artists'][0]['id']
    artist_info = app.artist(artist_id)
    track_genre = ', '.join(artist_info['genres']) if artist_info['genres'] else "Unknown"
    
    # Print the results
    print(f"Track ID: {track_id}")
    print(f"Track Name: {track_name}")
    print(f"Artists: {artists}")
    print(f"Album Name: {album_name}")
    print(f"Popularity: {popularity}")
    print(f"Duration (ms): {duration_ms}")
    print(f"Explicit: {explicit}")
    print(f"Danceability: {danceability}")
    print(f"Energy: {energy}")
    print(f"Key: {key}")
    print(f"Loudness: {loudness}")
    print(f"Mode: {mode}")
    print(f"Speechiness: {speechiness}")
    print(f"Acousticness: {acousticness}")
    print(f"Instrumentalness: {instrumentalness}")
    print(f"Liveness: {liveness}")
    print(f"Valence: {valence}")
    print(f"Tempo: {tempo}")
    print(f"Time Signature: {time_signature}")
    print(f"Track Genre: {track_genre}")

