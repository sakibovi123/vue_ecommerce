"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/httsp/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from store import views
from cart.views import cart_details
from store.views import (Home, CartView, Checkout, Search, Register, Login, UserOrders,
                        logout, Product_details, AllProd, TopProd, NewProd, OrderProcess)
from django.conf.urls.static import static

from store.api import api_for_add_to_cart, api_remove_from_cart, api_checkout

urlpatterns = [
    ## Django Built-in Admin Panel
    path('adminpanel/', admin.site.urls),
    ## Home Page View
    path('',Home.as_view(), name="home"),

    ## New Paths ##

    path('new_cart/', cart_details, name="cart_details"),

    path('api/add_to_cart', api_for_add_to_cart, name="api_for_add_to_cart"),
    path('api/api_remove_from_cart', api_remove_from_cart, name="api_remove_from_cart"),
    path('api/api_checkout', api_checkout, name="api_checkout"),








    ## Producr Details Route

    path('products/<str:slug>/', Product_details.as_view(), name="Product_details"),
    ## Cart View


    path('cart/', CartView.as_view(), name="cart"),

    ## Checkout View FOr Customers
    path('checkout/', Checkout.as_view(), name="checkout"),


    ## Searc Form Functions to search by products
    path('search/', Search.as_view(), name="search_by"),
    # All product page url
    path('all-products/', AllProd.as_view(), name="allProd"),
    # Top product page url
    path('top-products/', TopProd.as_view(), name="topProd"),
    # New product page url
    path('new-products/', NewProd.as_view(), name="newProd"),

    ## For Registering, Login and Logout
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),

    ## Showing Customers Orders By their own Id

    # User dashboard
    path('user-dashboard/', UserOrders.as_view(), name="user_orders"),
    # Order process
    path("order-process/", OrderProcess.as_view(), name="order_process"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)