# -*- coding: utf-8 -*-
from django.test import TestCase
from django.urls import reverse

class TestPages(TestCase):
    def setUp(self):
        self.home_url = reverse('home')

    def test_go_to_home_page(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)

