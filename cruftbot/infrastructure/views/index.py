from django.shortcuts import render


def index(request):
    """Main (or index) view."""
    return render(request, "index.html")
