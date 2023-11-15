from django.shortcuts import render
import logging

from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharaoh, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    View function for profiles app's index page.
    Parameters: request: The HTTP request object.
    Returns:HttpResponse: The HTTP response object , rendering the 'index.html' template with
                context contains a list of all profile's objects.
    """
    logger = logging.getLogger('django')
    profiles_list = Profile.objects.all()

    if profiles_list:
        logger.info(f'The index load the profiles successfully')
    else:
        logger.warning(f'There are no profiles infos')

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """
    View function for profiles app's profile element page.
    Parameters: request: The HTTP request object.
    Returns:HttpResponse: The HTTP response object , rendering the 'profile.html' template with
            context contains a profile object's each element's details, if profile object's not
            found,then render 404 error page
    """
    logger = logging.getLogger('django')
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        #???? ici comme logger.warning, pourquoi sur error.log,il ny a pas cette pharse?
        logger.warning(f'The username of profile does not exist')
        return render(request, '404_page.html', status=404)
    # profile = Profile.objects.get(user__username=username)

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
