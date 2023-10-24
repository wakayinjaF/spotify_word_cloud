import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Spotify API credentials
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"

# Playlist ID
playlist_id = '6Wc2THamjv092cevwohMyt'

# Authenticate with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get the track titles from the specified playlist
results = sp.playlist_tracks(playlist_id)
track_titles = [track['track']['name'] for track in results['items']]

# Combine track titles into a single string
text = ' '.join(track_titles)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
