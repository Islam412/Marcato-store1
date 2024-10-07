from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Product, Brand, ProductImage, Review


class ProductList(ListView):
    model = Product


class ProductDetails(DetailView):
    model = Product
    
    
