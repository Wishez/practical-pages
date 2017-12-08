# -*- coding: utf-8 -*-
from django.test import TestCase
from ..models import *

class TestModels(TestCase):
    def setUp(self):
        self.settings_data = {
            "name": "Main",
            "widgets": "<script>conosle.log('test')</script>",
            "meta": "Site\'s Description",
            "contacts_phone": '+7(999) 000-99-99; +7 (111) 000-99-99',
            "email": 'shiningfinger@list.ru',
            "footer_phone": "+7(999) 000-99-99",
            "address": "ul.Pushkino, d. Kolotushkino",
            "addressHref": "https://google.com"
        }
    def test_setting_model(self):

        data = self.settings_data
        setting = Settings.objects.create(**data)

        self.assertEquals(setting.name, data["name"])
        self.assertEquals(setting.widgets, data["widgets"])
        self.assertEquals(setting.meta, data["meta"])
        self.assertEquals(setting.name, data["name"])
        self.assertEquals(setting.widgets, data["widgets"])
        self.assertEquals(setting.meta, data["meta"])
        self.assertEquals(setting.contacts_phone, data["contacts_phone"])
        self.assertEquals(setting.email, data["email"])
        self.assertEquals(setting.footer_phone, data["footer_phone"])
        self.assertEquals(setting.address, data["address"])
        self.assertEquals(setting.addressHref, data["addressHref"])