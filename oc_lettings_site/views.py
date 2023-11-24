from django.shortcuts import render


def index(request):
    """
    View function for the index page.
    Parameters:request: HTTP request object.
    Returns:HttpResponse: HTTP response object, rendering the 'index.html' template.
    """
    return render(request, 'index.html')


def page_404(request, exception):
    """
    View function for handling 404 error and return 404_page.
    Parameters:request: The HTTP request object.
              :exception: the exception object represent 404 error
    Returns:HttpResponse: The HTTP response object with 404 status code, rendering the
            '404_page.html' template.
    """
    return render(request, '404_page.html', status=404)


def page_500(request):
    """
    View function for the handling 500 error and turn 500_page
    Parameters:request: The HTTP request object.
    Returns:HttpResponse: The HTTP response object with 500 status code, rendering the
            '500_page.html' template.
    """
    return render(request, '500_page.html', status=500)
