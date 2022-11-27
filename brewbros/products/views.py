from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import DetailView

from cart.forms import CartAddProductForm
from .forms import FilterByKindForm
from .models import Product, ProductKind


def home(request: HttpRequest):
    return render(request=request, template_name='products/home.html')


def shop(request: HttpRequest):
    main = Product.objects.select_related("kind").prefetch_related("origin").filter(archived=False).order_by(
        "price").all()
    kind = ProductKind.objects.all()
    form1 = FilterByKindForm()
    if request.method == "POST":
        key = request.POST.get("choice")
        form1.is_valid()
        context = {"form": form1, "products": main.filter(kind=key), "kind": kind, "filter_by": 0}
    else:
        context = {"form": form1, "products": main, "kind": kind, "filter_by": 0}
    return render(request=request, template_name='products/shop.html', context=context)


class ProductDetailView(DetailView):
    template_name = "products/details.html"
    context_object_name = "product"
    cart_product_form = CartAddProductForm()
    queryset = (
        Product
        .objects
        .select_related("profile", "kind")
        .prefetch_related("origin")
    )


def about(request: HttpRequest):
    return render(request=request, template_name='products/index.html')


def article(request: HttpRequest):
    return render(request=request, template_name='products/article.html')
