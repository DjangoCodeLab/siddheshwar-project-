from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from App.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import cache_page
from App.forms import *

# Create your views here.
from django.core.cache import cache


def homePage(request):
    return render(request, "home.html")


@cache_page(60 * 1)
def home(request, slug):
    category = Category.objects.filter(category_slug=slug)
    if category:
        queryset = Product.objects.filter(category__category_slug=slug)

    else:
        queryset = Product.objects.all()

    context = {"queryset": queryset}
    return render(request, "index.html", context)


@cache_page(60 * 1)
def productDetails(request, slug):
    product = Product.objects.filter(product_slug=slug)
    context = {"product": product}
    return render(request, "productDetails.html", context)


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()

    context = {"form": form}

    return render(request, "register_user.html", context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(
            request, data=request.POST
        )  # Pass `request` as the first argument
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user from the form
            login(request, user)
            return redirect("/")  # Redirect only if login is successful

    else:
        form = LoginForm()  # Empty form for GET request

    context = {"form": form}
    return render(
        request, "login_user.html", context
    )  # Show form with errors if login fails


def cart_data(request):
    product = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in product)

    context = {"cart_items": product, "total": total}
    return render(request, "Cart.html", context)


def logout_user(request):
    logout(request)
    return redirect('homePage')


# def add_to_cart(request,id):
#     product = Product.objects.get(id = id)
#     print(product)
#     cart_item, created = CartItem.objects.get_or_create(
#         product = product,
#         user = request.user
#     )
#     cart_item.quantity +=1
#     cart_item.save()
#     return redirect('cart')


def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            product=product, user=request.user
        )
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart = request.session.get("cart", {})
        cart[str(id)] = cart.get(str(id), 0) + 1
        request.session["cart"] = cart  # Save back to session

    return redirect("cart")


def remove_cart(request, id):
    product = CartItem.objects.get(id=id)
    product.delete()
    return redirect("cart")
