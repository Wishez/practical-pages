# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from app.models import Settings
from .models import *
# Create your views here.

def get_single_model(Model):
    return Model.objects.get()

class BaseView(TemplateView):
    def __init__(self):
        self.page_model = None
        self.page = None
        self.settings = get_single_model(Settings)
        self.meta = self.settings.meta
    # Дополняет контекст свойствами нужной страницы, если нужно
    def set_additional_context(self, context):

        return context
    def get_page(self):
        self.page = self.page_model.objects.get()

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        if self.page is None:
            self.get_page()

        page = self.page
        #
        # # Установка мета-описания для текущей страницы
        if page.meta != '':
            self.meta = page.meta

        context['meta'] = self.meta
        context['page'] = page
        context['settings'] = self.settings

        return self.set_additional_context(context)

class HomeView(BaseView):
    template_name = 'index.html'

    def __init__(self):
        super(HomeView, self).__init__()
        self.page_model = HomePage


class ServicesView(BaseView):
    template_name = 'services.html'

    def __init__(self):
        super(ServicesView, self).__init__()
        self.page_model = ServicesPage
class PricesView(BaseView):
    template_name = 'prices.html'

    def __init__(self):
        super(PricesView, self).__init__()
        self.page_model = PricesPage

class ContactsView(BaseView):
    template_name = 'contacts.html'

    def __init__(self):
        super(ContactsView, self).__init__()
        self.page_model = ContactsPage

class SaunaView(BaseView):
    template_name = 'sauna.html'

    def get(self, request, slug):
        self.page = get_object_or_404(SaunaPage, slug=slug)

        return super(SaunaView, self).get(request)

