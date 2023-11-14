from django.shortcuts import render


def list_highfives(request):
    return render(request, 'highfives/index.html')
