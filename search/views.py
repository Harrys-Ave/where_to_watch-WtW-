from django.shortcuts import render

# Create your views here.



from django.shortcuts import render
from .services.tmdb import search_movie, get_watch_providers

"""
This says:
When the user visits /, return the template file home.html.
"""

def home(request):
    return render(request, "search/home.html")

"""
function to handle search results
- read user input from query parameters
- call TMDB search
- get watch providers for the first result
- pass everything to the template
"""
def search_results(request):
    # 1. Read user input from the query parameters
    title = request.GET.get("title")
    region = request.GET.get("region", "GR")  # default to GR if missing # probably this should be changed

    if not title:
        # If no title is provided, just go back to home (or show an error)
        return render(request, "search/home.html", {
            "error": "Please enter a movie title."
        })

    # 2. Call TMDB search
    results = search_movie(title)

    if not results:
        # No movie found
        return render(request, "search/results.html", {
            "title": title,
            "region": region,
            "movie": None,
            "providers": None,
            "error": "No results found for this title."
        })

    # 3. Pick the first result (later we can improve this)
    movie = results[0]
    movie_id = movie["id"]

    # 4. Get watch providers for this movie and region
    providers = get_watch_providers(movie_id, region)

    # 5. Pass everything to the template. This is the data we make available to the template (results.html).
    context = {
        "title": title,
        "region": region.upper(),
        "movie": movie,
        "providers": providers,
        "error": None,
    }

    # this tells django: "Use templates/search/results.html" and "Pass it the context data"
    return render(request, "search/results.html", context)
