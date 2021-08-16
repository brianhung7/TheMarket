from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView


# Create your views here.
class Home(TemplateView):

    def get(self, request):
          template_name = "home.html"


class ProductList(TemplateView):
    template_name = "product_list.html"