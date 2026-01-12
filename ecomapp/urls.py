# ecomapp/urls.py   ← Replace your current file with this

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home2/', views.home2, name='home2'),
    path('userlog/', views.userlog, name='userlog'),
    
    # Cart & Products
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_page, name='cart_page'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('checkout/<int:product_id>/', views.checkout_page, name='checkout_page'),
    
    # History
    path('addhis/<int:id>/', views.his),
    path('viewhis/', views.viewhis),
    
    # Payment Flow - THESE ARE THE IMPORTANT ONES
    path('payment/<int:product_id>/', views.payment, name='payment'),
    path('success/<int:product_id>/', views.success, name='success'),
    path('download-invoice/<int:product_id>/', views.generate_invoice, name='download_invoice'),
]