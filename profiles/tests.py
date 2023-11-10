from django.test import TestCase
from .models import Profile


class MyTestCase(TestCase):

    def setUp(self):
        Profile.objects.create(favorite_city='paris', user_id=1)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_profile_index_page_can_be_opened(self):
        response = self.client.get('/profiles/')
        assert response.status_code == 200

    # def test_letting_object_page_can_be_opened(self):
    #     response = self.client.get('/profiles/2/')
    #     assert response.status_code == 200


