# Phase 3 – Search Form, Views, and Result Rendering

This phase adds the first complete user-facing functionality:

- A search form on the homepage  
- A Django view that processes the search  
- Calls to TMDB API to fetch movie + streaming availability  
- A results page that displays streaming services  

This creates the full flow:

**User → Form → View → TMDB API → Providers → Display Results**

---

## 1. Adding a Search Form on the Homepage

In Phase 1, the homepage (`home.html`) only displayed a static message.

Now we convert it into a working search page.

**File:** `templates/search/home.html`

The form submits data using:

- `method="GET"`  
  The form data is passed through the URL  
  (e.g. `/results/?title=godfather&region=GR`)

- `action="{% url 'search_results' %}"`  
  This tells Django to send the form data to the URL pattern named **search_results**

- `name="title"` and `name="region"`  
  These keys are read in the Django view using  
  `request.GET.get("title")` and `request.GET.get("region")`

The homepage now displays a simple form where the user enters:

- Movie/series title  
- Region code (e.g. GR, US, DE)

---

## 2. Adding a URL for the Results Page

We need a URL that receives the data submitted from the form.

**File:** `search/urls.py`

We add:

```python
path('results/', views.search_results, name='search_results'),
```

**What this does**

'results/' → maps /results/ to the search_results view

name='search_results' → allows templates to reference this path using {% url 'search_results' %}

**Flow after adding this route**

User visits / → sees the search form

User submits form → browser navigates to:
/results/?title=godfather&region=GR

Django now invokes the search_results view.

## 3. Creating the search_results View

This view performs the core logic:

-Reads user input

-Searches for the movie

-Selects a result

-Fetches provider (streaming) information

-Sends everything to the template for display

**File:** search/views.py

## 4. Creating the Results Template

The results page displays:

-The movie title

-Release date

-Region

-Streaming options (subscription, rent, buy)

-Direct link to TMDB’s “Where to Watch” page

-Messages when a category is empty (e.g. “Not on a streaming service yet.”)

**File:** templates/search/results.html

## 5. Testing the Flow
Start the Django development server:
```
python manage.py runserver
```
Visit in your browser:
```
http://127.0.0.1:9999/
```
