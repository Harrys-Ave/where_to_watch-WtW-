# Where_to_Watch (WtW) – Django Setup Guide  
Version: Phase 1 – Project Creation and Initial Homepage

---

# 1. Project Directory Structure

The root directory of the project is:

```
F:\projects\WtW
```

All commands in this documentation assume that you are inside this directory.

---

# 2. Creating and Activating a Python Virtual Environment

A Python virtual environment (commonly referred to as a "venv") is an isolated environment that contains its own Python interpreter and its own installed packages.  
It ensures the following:

- Different projects can use different versions of packages without conflict.  
- Team members can reproduce the exact environment by installing the same dependencies.  
- The global system Python installation remains unaffected.

## Create the virtual environment
(inside the folder F:\projects\WtW. You do that by using "cd F:\projects\WtW" in Powershell)

```
python -m venv .venv
```

This generates a new folder:

```
.venv/
```

which contains a standalone Python environment.

## Activate the virtual environment (Windows PowerShell)

```
.venv\Scripts\activate
```

After activation, the prompt will show:

```
(.venv)
```

To deactivate the virtual environment:

```
deactivate
```

---

# 3. Installing Django

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Django provides:

- A built-in project structure  
- URL routing  
- Templating system  
- ORM (Object-Relational Mapping)  
- Built-in server  
- Admin interface  

We will use Django because it simplifies backend development, provides robust architecture, and integrates well with APIs such as TMDB and JustWatch.

Install Django inside the virtual environment:

```
pip install "Django>=5.0,<6.0"
```

Verify installation:

```
django-admin --version
```

---

# 4. Creating the Django Project

A Django project contains the global configuration of the entire site.

Run:

```
django-admin startproject wtw .
```

This command generates the following files:

```
manage.py
wtw/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```

## Explanation of generated files

### manage.py  
A command-line utility used to interact with the project.  
Examples:
- Running the development server  
- Creating apps  
- Running migrations  
- Managing databases  

### wtw/settings.py  
The global configuration file for the project.  
It includes settings for:
- Installed apps  
- Middleware  
- Database configuration  
- Template settings  
- Static files  

### wtw/urls.py  
The root URL router for the entire project.  
It defines which URL patterns direct to which Django apps or views.

### wtw/asgi.py  
Entry point for ASGI-compatible web servers (used for asynchronous communication, WebSockets, etc.).

### wtw/wsgi.py  
Entry point for WSGI-compatible web servers (standard for Python web hosting).

---

# 5. Creating the Search App

Create the app:

```
python manage.py startapp search
```

A Django app is a modular component that contains related functionality.  
Each app is responsible for a specific part of the website.

Examples of apps in a large project:
- Authentication  
- Search  
- Payments  
- Profiles  
- Administration  

Our `search` app will handle:
- Searching movie/series titles  
- Communicating with TMDB and JustWatch  
- Rendering search results

The command generates:

```
search/
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

---

# 6. Registering the App in Django Settings

In `wtw/settings.py`, add the search app to the installed apps:

```python
INSTALLED_APPS = [
    ...
    'search',
]
```

This tells Django to load and recognize the app.

---

# 7. Configuring Project-Level URL Routing

File: `wtw/urls.py`

Update the file as follows:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
]
```

## Why this step is needed

Django projects use a hierarchical URL routing system.  
The project-level `urls.py` determines which application should handle which URL patterns.

By writing:

```
path('', include('search.urls'))
```

we are telling Django:

- When the user visits the base URL (`/`),  
- Forward the request to the URL configuration defined inside the `search` app.

Without this step, Django would not know how to direct incoming requests to our app.

---

# 8. Creating URL Routing for the Search App

Inside the `search` directory, create a new file:

```
search/urls.py
```

Add the following:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## Why this file is required

Each Django app can define its own URL patterns.  
This improves modularity and organization.

The `search/urls.py` file:

- Declares which URLs belong to this app  
- Connects individual URLs to specific view functions  
- Keeps the application's routing independent from the main project

## What the code does

```
path('', views.home, name='home')
```

means:

- When the user visits the base URL for this app (`/`),  
- Call the function `home` in `search/views.py`  
- Give this route the name `"home"` (useful for reverse URL lookup)

---

# 9. Creating the Homepage View

Open:

```
search/views.py
```

Add:

```python
from django.shortcuts import render

def home(request):
    return render(request, "search/home.html")
```

## What a view is

A **view** is a Python function (or class) that:

1. Receives an HTTP request  
2. Processes data (optional)  
3. Returns an HTTP response  

This response is usually:

- HTML template  
- JSON data  
- Redirect  

In this case, the view simply returns an HTML template.

## What our view does

The line:

```
return render(request, "search/home.html")
```

means:

- Render the template located at `templates/search/home.html`  
- Return it to the browser as an HTML page  

This is required so Django knows what content to show on the homepage.

---


# 10. Creating the Template Directory and Homepage Template

## Why we need a `templates/` folder

Templates are HTML files rendered by Django.  
They allow separation between backend logic (views) and frontend presentation (HTML).

Django needs to know where your HTML templates are located.  
By convention, projects place templates inside a top-level `templates/` folder.

## Where to create the folder

Create this folder structure in the **project root**:

```
templates/
    search/
        home.html
```

This keeps all templates organized and accessible to all apps.

## Configure Django to use this folder

In `wtw/settings.py`, modify the TEMPLATES setting:

```python
'DIRS': [BASE_DIR / "templates"],
```

This instructs Django:

- When rendering templates, also search inside the directory `templates/` located in the project root.

## Create the template file

Create:

```
templates/search/home.html
```

Add:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Where_to_Watch – Search</title>
</head>
<body>
    <h1>Where_to_Watch – Search</h1>
    <p>Django is running successfully.</p>
</body>
</html>
```

When the `home` view is called, Django loads this file and sends its HTML to the browser.

---

# 11. Running the Development Server

Run:

```
python manage.py runserver
```

This command:

1. Starts Django’s built-in development web server  
2. Listens for requests at `http://127.0.0.1:8000/`  
3. Routes incoming requests using `urls.py`  
4. Calls the correct view  
5. The view renders and returns a template  
6. The browser displays the HTML page  

Visit:

```
http://127.0.0.1:8000/
```

You should now see:

```
Where_to_Watch – Search
Django is running successfully.
```

This confirms that:

- URL routing is correct  
- Views are working  
- Templates are configured  
- The project structure is valid  
- Django is running successfully  

---

# Folder structure
WtW/
│
├── manage.py
├── db.sqlite3
│
├── .venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── wtw/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── search/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
└── templates/
    └── search/
        └── home.html
        
# Useful Command Lines for PowerShell
### Activate the Virtual Environment

```
.venv\Scripts\activate
```

This command activates the Python virtual environment located inside the project folder.
When activated, your terminal prompt will change to show:
```
(.venv)
```
This ensures that Python and Django run inside the correct environment.

### Show Contents of the Project Directory
```
dir F:\projects\WtW\
```

### Run the Django Development Server
```
python manage.py runserver
```
Starts Django’s built-in development server.
After running this command, the terminal will show something like:
```
Starting development server at http://127.0.0.1:8000/
```

To stop the django server you:
```
CTRL + C
```

# End of Phase 1  
The base project structure is complete and functional.

You now have:  
- A Django project  
- A Django app  
- URL routing  
- A homepage view  
- A template system  
- A fully running development server  

Phase 2 will include creating the search form and connecting to external APIs.
