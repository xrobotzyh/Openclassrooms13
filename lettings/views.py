from django.shortcuts import render
import logging

from lettings.models import Letting

logger = logging.getLogger(__name__)
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam
# vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim
# cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis
# in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    View function for lettings app's index page.
    Parameters: request: The HTTP request object.
    Returns:HttpResponse: The HTTP response object , rendering the 'index.html' template with
            context contains a list of all letting objects.
    """

    lettings_list = Letting.objects.all()

    if lettings_list:
        logger.info(f'The lettings info loaded successfully')
    else:
        logger.warning(f'There are no available lettings')

    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu,
# vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas
# auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna.
# Suspendisse potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan
# interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique
# mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi
# ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    View function for lettings app's letting element page.
    Parameters: request: The HTTP request object.
    Returns:HttpResponse: The HTTP response object , rendering the 'letting.html' template with
            context contains a letting object's each element's details, if letting object's not
            found,then render 404 error page
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f'Get the letting_id={letting_id} successful')
    except Letting.DoesNotExist:
        logger.error(f'The letting id does not exist')
        return render(request, '404_page.html', status=404)

    context = {
        'title': letting.title,
        'address': letting.address,
    }
    # a = context['i']
    return render(request, 'lettings/letting.html', context)
