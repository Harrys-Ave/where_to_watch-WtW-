# Where_to_Watch (WtW) – Phase 2 Documentation  
**TMDB Integration & Service Layer Setup**

-- Phase 2 Steps --

1️⃣ Implement TMDB API service functions


2️⃣ Add API key to Django settings


3️⃣ Install requests


4️⃣ TEST the functions in Django Shell


5️⃣ Make sure both functions work together

Get movie ID

Fetch providers

Check the JSON structure

Confirm nothing crashes


---

## 1. Phase 2 Goal

In **Phase 2**, we begin connecting our Django app to an external API so that:

- We can **search for a movie or series by title** (e.g., “Godfather”)
- Then, using that movie’s **TMDB ID**, we can **fetch where it is available to watch** (e.g., Netflix, Prime Video) for a specific region (e.g., Greece / `"GR"`)

We are using **TMDB (The Movie Database)** as our movie API provider.

TMDB gives us:

- Movie search by title  
- Detailed movie info  
- An endpoint called **`/watch/providers`**, which tells us where a movie is available in each country  

Later, we will connect this logic to Django views and templates so a user can type:

> Movie: “Godfather”  
> Region: “GR”

and get back:

> Available on: Netflix, Amazon Prime, …

For now, Phase 2 focuses only on the **backend logic**:  
**how we talk to TMDB and retrieve data.**

---

## 2. Why We Use a “Service Layer” (`services` folder)

Inside the `search` app, we created a folder:



```text
search/
    services/
        __init__.py
        tmdb.py
```


The `services` folder contains all code that talks to **external services or APIs**.

This keeps our Django views clean and ensures the API logic lives in one place.

---

## 3. What Is `__init__.py` and Why Do We Need It?

Inside `search/services/`, we created:



search/services/__init__.py



This file may remain **empty**. Its purpose is:

- To tell Python that `services` is a **package**  
- This allows imports such as:

```python
from search.services.tmdb import search_movie
```


Without __init__.py, services would just be a folder, and Python might not treat it as an importable package.

So:

__init__.py → “Hey Python, this folder is a module/package.”

tmdb.py → where the actual logic lives.

## 4. The tmdb.py Module – Purpose

The file:
```
search/services/tmdb.py
```

is where we put all functions related to TMDB:

-Searching for movies by title

-Getting streaming providers for a specific movie and region


The idea is that other parts of the Django project (like views) will call functions from tmdb.py instead of dealing with raw HTTP calls themselves.

Example later:
```
from search.services.tmdb import search_movie, get_watch_providers
```


Going back now to the tmdb.py file, we use 
```
from django.conf import settings
```

-This gives us access to Django’s settings object.

-In settings.py, we add a line like:

TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"

-Then in code we can read it as: settings.TMDB_API_KEY.

## 5. How to Test TMDB API Functions in Django
```
 Navigate to your project folder (if not already there)
cd F:\projects\WtW

 Activate the virtual environment
.venv\Scripts\activate
```

(We can also do it in VSCode by oppening the terminal) 

### Run Django Shell
```
python manage.py shell
```

### Import the TMDB service functions
```
from search.services.tmdb import search_movie, get_watch_providers
```

### Test the search_movie() function
```
results = search_movie("godfather")
results[:3]   # show first 3 results
```
Expected output example:
```
[
    {'id': 755450, 'title': 'Godfather', ...},
    {'id': 238, 'title': 'The Godfather', ...},
    {'id': 141460, 'title': 'Hong Kong Godfather', ...}
]
```

### Extract the movie ID
```
movie_id = results[1]["id"]   # The real "The Godfather" has ID = 238
movie_id
```

### Test the get_watch_providers() function
For Greece 🇬🇷:
```
providers = get_watch_providers(movie_id, "GR")
providers
```
Example output:
```
{
 'link': 'https://www.themoviedb.org/movie/238-the-godfather/watch?locale=GR',
 'rent': [
     {'provider_name': 'Apple TV', ...},
     {'provider_name': 'Google Play Movies', ...}
 ],
 'buy': [
     {'provider_name': 'Apple TV', ...},
     {'provider_name': 'Google Play Movies', ...}
 ],
 'flatrate': [
     {'provider_name': 'Netflix', ...}
 ]
}
```


