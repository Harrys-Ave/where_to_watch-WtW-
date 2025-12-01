# new file that we created
"""
created because we need:
-a URL file for the search app
-a view function to return a webpage
-a template to render
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]