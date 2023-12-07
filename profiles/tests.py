from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile


class MyProfilesTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='fifi')
        Profile.objects.create(favorite_city='paris', user_id=1)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_profile_index_page_can_be_opened(self):
        response = self.client.get('/profiles/')
        assert response.status_code == 200
        assert b'Profiles' in response.content

    def test_letting_object_page_can_be_opened(self):
        response = self.client.get('/profiles/fifi/')
        assert response.status_code == 200
        assert b'fifi' in response.content

    def test_none_letting_object_page_can_be_opened(self):
        """
        When the url is not exist,it will redirect to my 404_page, so initial status code is 301,
        with follow=true,it will redirect to the final status code of the url
        """
        response = self.client.get('/profiles/didi', follow=True)
        assert response.status_code == 404
        assert b'The page you request is not found !' in response.content
