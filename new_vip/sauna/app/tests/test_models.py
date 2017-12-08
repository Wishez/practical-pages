from django.test import TestCase
from ..models import *

class TestModels(TestCase):
    def setUp(self):
        self.contacts_data = {
            "contacts_phone": '+7(999) 000-99-99; +7 (111) 000-99-99',
            "email": 'shiningfinger@list.ru',
            "name": 'Main',
            "footer_phone": "+7(999) 000-99-99",
            "address": "ul.Pushkino, d. Kolotushkino",
            "addressHref": "https://google.com"
        }

        self.settings_data = {
            "name": "Main",
            "widgets": "<script>conosle.log('test')</script>",
            "meta": "Site\'s Description"
        }
    def test_contacts_model(self):
        data = self.contacts_data
        contacts = Contacts.objects.create(**data)

        self.assertEquals(contacts.name, data["name"])
        self.assertEquals(contacts.contacts_phone, data["contacts_phone"])
        self.assertEquals(contacts.email, data["email"])
        self.assertEquals(contacts.footer_phone, data["footer_phone"])
        self.assertEquals(contacts.address, data["address"])
        self.assertEquals(contacts.addressHref, data["addressHref"])

    def test_setting_model(self):

        data = self.settings_data
        setting = Settings.objects.create(**data)

        self.assertEquals(setting.name, data["name"])
        self.assertEquals(setting.widgets, data["widgets"])
        self.assertEquals(setting.meta, data["meta"])
    def test_bound_settings_and_contacts(self):

        contacts = Contacts.objects.create(**self.contacts_data)

        setting = Settings.objects.create(**self.settings_data, contacts=contacts)

        self.assertEquals(setting.contacts.id, contacts.id)
