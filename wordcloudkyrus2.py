import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Spotify API credentials
CLIENT_ID = "4656a4330aa14b26aa5103670483668a"
CLIENT_SECRET = "ae442d65b8fa4538bb6ab92531bf5ad8"

# Playlist ID
playlist_id = '6Wc2THamjv092cevwohMyt'

# Authenticate with the Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get the track titles from the specified playlist
results = sp.playlist_tracks(playlist_id)
print (results)
track_titles = [track['track']['name'] for track in results['items']]
print (track_titles)

# Combine track titles into a single string
text = ' '.join(track_titles)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Save the word cloud plot as an image (PNG format)
wordcloud.to_file("wordcloud.png")

# Convert the image to base64
with open("wordcloud.png", "rb") as image_file:
    wordcloud_base64 = base64.b64encode(image_file.read()).decode('utf-8')

# Create an HTML file to display the word cloud
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Spotify Word Cloud</title>
</head>
<body>
    <h1>Spotify Word Cloud</h1>
    <img src="data:image/png;base64,{wordcloud_base64}" alt="Word Cloud">
</body>
</html>
"""

# Save the HTML content to a file
with open("wordcloud_output.html", "w") as html_file:
    html_file.write(html_content)
