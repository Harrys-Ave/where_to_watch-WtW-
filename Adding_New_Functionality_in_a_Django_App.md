# Adding New Functionality in a Django App

# Understanding How Views, Templates, and Services Work Together

When we add small features (like movie posters, provider logos, error messages, extra fields, etc.), we always follow the same logical structure:

- Add or modify logic in a Django view → backend processing

- Pass additional data to the template → make it available to the page

- Update the template (.html) → display the new feature on the website

This is the core workflow behind all Django features.

# ----------------------------------------------------------------------

# 1. Understanding the Components

Django uses a clean separation of responsibilities.

## 1.1. Views (search/views.py)

**A view is the brain of the operation.**

A view:

- Receives the request sent by the browser

- Reads user input (GET or POST)

- Calls service functions (like TMDB API helpers)

- Processes or enriches the data (e.g., build poster URLs)

- Sends the final data to a template for rendering

In simple terms:

➡️ Views prepare the data needed for the page.

If the website were a restaurant:
- The view is the chef

- It takes the customer's order (the request)

- Prepares the meal (data)

- Gives it to the waiter (template) to serve

You can add any new logic in a view:

- Build poster URLs

- Add provider logo URLs

- Combine results

- Transform TMDB data

- Perform caching

- Validate user input

This is why we edited search_results in views.py to add poster URLs and provider logo URLs.
The logic belongs there.

## 1.2. Templates (templates/search/results.html)

**A template is the presentation layer — it shows the data.**

Templates DO NOT:

- Call APIs

- Modify data

- Contain business logic

Templates ONLY:

- Receive a context dictionary from the view

- Display the data inside HTML

- Loop through lists

- Conditionally show/hide sections

for example
```
{% if movie.poster_url %}
  <img src="{{ movie.poster_url }}">
{% endif %}
```
The template doesn't know how the poster URL was constructed.
It just uses it.

➡️ Views send data → Templates show data.

Continuing the restaurant analogy:
- The template is the waiter

- It receives the prepared meal from the chef

- It arranges the table and serves it

- It does NOT cook anything

## 1.3. Service Modules (search/services/tmdb.py)

Service files hold independent, reusable logic, for example:
- Calling TMDB API

- Transforming external data

- Handling authentication

- Wrapping external requests

They are not tied to Django directly — they are standalone helpers.

A view imports them, uses the functions, and forwards the results to templates.

Restaurant analogy:

- Services are the suppliers

- They bring ingredients (TMDB data)

- The chef (view) uses the ingredients to prepare meals


# 2. Example of how all work together

Here is the entire system flow for one feature (e.g., showing movie posters):

**Step 1 — User submits a form**

Title: “godfather”
Region: “GR”

Browser sends a request to:
```
/results/?title=godfather&region=GR
```

**Step 2 — Django receives the request**

The URL /results/ is routed to:
```
views.search_results
```

**Step 3 — The view processes the request**

The view:
1) Reads GET data

2) Calls search_movie() from services/tmdb.py

3) Takes the best movie

4) Builds a poster URL

5) Calls get_watch_providers()

6) Adds provider logo URLs

7) Creates a context dictionary

**Step 4 — Django renders a template**

The view returns:
```
return render(request, "search/results.html", context)
```
Then the template receives the context and displays it:
```
<img src="{{ movie.poster_url }}">
```

**Step 5 — Browser shows final page**

# 3. Why We Add Features in the View First

Whenever we add a new feature, the logic is always:

✔️ Add the backend logic in the view

(e.g., generate a poster URL, fetch extra data, filter results)

✔️ Then expose it to the template via context

(the template cannot do logic, it only displays)

✔️ Then update the template to show it

(conditions, loops, styling, etc.)

This pattern repeats for every small feature.
