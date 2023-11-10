from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def page_404(request, exception):
    return render(request, '404_page.html', status=404)


def page_500(request):
    return render(request, '500_page.html', status=500)
