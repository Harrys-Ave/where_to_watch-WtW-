# This is a service module that makes API calls


import requests # requests is a Python library for making HTTP requests (GET, POST, etc.).
from django.conf import settings # This imports Django’s settings object.. We use it to get the api key

TMDB_BASE_URL = "https://api.themoviedb.org/3"

"""
The function search_movie("query") returns a list of movie dicts.
query=string: the movie that the user will search for
"""
def search_movie(query):
    url = f"{TMDB_BASE_URL}/search/movie"
    params = {
        "api_key": settings.TMDB_API_KEY, # My TMDB API key, pulled from Django settings.
        "query": query, # search text we pass to the function.
        "language": "en-US" # tells TMDB in which language to return titles/overviews.
    }

    # response is an object containing: status_code, text (raw response) and a json() 
    response = requests.get(url, params=params) # Makes an HTTP GET request to the API endpoint.
    response.raise_for_status() # Raises an error if the request was unsuccessful.
    data = response.json() # Converts the JSON body to a Python dictionary.

    return data.get("results", []) # extracts the results list from the response data.


"""
What it does:

-Takes a movie_id (TMDB ID, e.g. 238 for The Godfather).
-Takes a region like "GR" for Greece.


data.get("results", {}) → get the dictionary of region data.
.get(region.upper(), {}) → then get the info for "GR" or "US", etc.

(If region not found, return {} instead of crashing.)

So get_watch_providers(238, "GR") returns the providers for The Godfather in Greece.
"""

def get_watch_providers(movie_id, region="GR"):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}/watch/providers"
    params = {
        "api_key": settings.TMDB_API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # The region code must be uppercase (e.g., "GR" for Greece)
    return data.get("results", {}).get(region.upper(), {})
