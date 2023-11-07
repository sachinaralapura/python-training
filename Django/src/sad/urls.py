from django.urls import path, include
from sad import views

urlpatterns = [
    path("home", views.Home, name="home"),
    path("products", views.Products, name="products"),
    path("service", views.Service , name='service'),
    path("contact", views.Contact , name="contact"),
    path("careers", views.Careers , name='careers'),
    path("base", views.Base),
]
