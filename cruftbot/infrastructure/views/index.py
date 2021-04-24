"""Application home page."""
from django.shortcuts import render


def index(request):
    """Open home page."""
    return render(request, "index.html")
