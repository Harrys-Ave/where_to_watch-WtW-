from django.shortcuts import render

# Create your views here.

"""
This says:
When the user visits /, return the template file home.html.
"""
def home(request):
    return render(request, "search/home.html")