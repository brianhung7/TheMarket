from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Seller, Product
from django.urls import reverse


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"


class ProductList(TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_query = self.request.GET.get("name")

        if name_query != None:
            context['products'] = Product.objects.filter(name__icontains = name_query)
            context['header'] = f"Searching for {name_query}"
        else:
            context['products'] = Product.objects.all()
            context['header'] = "Popular Products"

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"

class SellerList(TemplateView):
    template_name = "seller_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name_query = self.request.GET.get("name")

        if name_query != None:
            context['sellers'] = Seller.objects.filter(name__icontains = name_query)
            context['header'] = f"Searching for {name_query}"
        else:
            context['sellers'] = Seller.objects.all()
            context['header'] = "Popular Sellers"

        return context


class SellerCreate(CreateView):
    model = Seller
    fields = ['name','img','bio']
    template_name = 'seller_create.html'

    def get_success_url(self):
        return reverse('seller_detail', kwargs = {'the_slug': self.object.slug})


class SellerDetail(DetailView):
    model = Seller
    template_name = "seller_detail.html"
    slug_url_kwarg = 'the_slug'
    # Should match the name of the slug field on the model 
    slug_field = 'slug' # DetailView's default value: optional


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"
