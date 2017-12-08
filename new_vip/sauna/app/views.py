# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class BaseView(TemplateView):
    def __init__(self):
        self.title = 'Home'
        self.meta = 'Meta'
        self.setting = None
        self.info = None


    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        context['meta'] = self.meta
        context['title'] = self.title
        context['setting'] = self.setting
        context['info'] = self.info

        return context

class HomePage(BaseView):
    template_name = 'index.html'

    # def get(self, request):
    #     return render(
    #         request,
    #         self.template_name,
    #         super().get_context_data(),
    #     )