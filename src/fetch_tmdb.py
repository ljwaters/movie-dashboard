import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
if not TMDB_API_KEY:
    raise RuntimeError("TMDB_API_KEY not found in environment")

# Endpoint for movies currently playing
URL = "https://api.themoviedb.org/3/movie/now_playing"

def get_now_playing(page=1):
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": page
    }

    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        now_playing_dict = response.json()
        return now_playing_dict
    else:
        print(f"Failed to retrieve data {response.status_code}")

now_playing = get_now_playing()

if now_playing:
    print("Titles of movies currently playing:")
    for movie in now_playing['results'][:5]:
        print(f"Name: {movie["title"]}")
        print(f"Release Date: {movie['release_date']}")


