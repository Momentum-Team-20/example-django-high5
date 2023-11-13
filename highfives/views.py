from django.shortcuts import render


def list_albums(request):
    return render(request, 'highfives/index.html')
