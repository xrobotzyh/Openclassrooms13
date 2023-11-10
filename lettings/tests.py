# Create your tests here.
from django.test import TestCase

from .models import Letting, Address


class MyTestCase(TestCase):

    def setUp(self):
        Address.objects.create(
            number=1,
            street='generale leclerc',
            city='paris',
            state='75',
            zip_code='75001',
            country_iso_code='fr'
        )
        Letting.objects.create(title='test', address_id=1)

    def tearDown(self):
        Address.objects.all().delete()
        Letting.objects.all().delete()

    def test_letting_index_can_be_opened(self):
        response = self.client.get('/lettings/')
        assert response.status_code == 200

    def test_letting_object_can_be_opened(self):
        response = self.client.get('/lettings/1/')
        assert response.status_code == 200

    # def test_none_letting_object_can_be_opend(self):
    #     response = self.client.get('/lettings/17/')
    #     assert response.status_code == 404
