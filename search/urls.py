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
    path('', views.home, name='home'), # when the path is empty, go to home view
    path('results/', views.search_results, name='search_results'), # when the path is results/, go to search_results view
]