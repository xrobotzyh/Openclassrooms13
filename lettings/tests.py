# Create your tests here.
import os

import pytest
from django.conf import settings
from django.test import TestCase

from .models import Letting, Address


class MyLettingsTestCase(TestCase):
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
        assert b'test' in response.content

    def test_letting_object_can_be_opened(self):
        response = self.client.get('/lettings/1/')
        assert response.status_code == 404
        assert b'test' in response.content

    def test_none_letting_object_can_be_opened(self):
        response = self.client.get('/lettings/2/')
        assert response.status_code == 404
        assert b'The page you request is not found !' in response.content
