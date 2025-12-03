from django.shortcuts import render


def home(request):
    """Vista simple para la página de inicio."""
    return render(request, 'infografia.html')