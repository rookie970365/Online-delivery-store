from django.urls import path
from .views import (shop, home, ProductDetailView)

app_name = "products"

urlpatterns = [
    path("", home, name="home"),
    path("shop/", shop, name="shop"),
    path("<int:pk>/", ProductDetailView.as_view(), name="details"),
]
