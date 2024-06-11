from django.shortcuts import render

def pageNotFound(request, exception):
    return render(request, 'main/404/404.html')
