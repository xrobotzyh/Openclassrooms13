from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def page_404(request, exception):
    return render(request, '404_page.html', status=404)
