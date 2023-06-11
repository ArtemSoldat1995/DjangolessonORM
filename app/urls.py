from django.urls import path
from .views import *

urlpatterns = [
    path ('', home),
    path('product/<int:id>', product_detail),
    ]