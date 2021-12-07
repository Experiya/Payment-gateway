from django.shortcuts import render
from django.urls import path
from .import views
urlpatterns = [
    path('',views.stripeHome ,name='stripeHome'),
    path('success',views.success ,name='success'),
    path('cancel',views.cancel ,name='cancel'),
    path('create-checkout-session',views.create_checkout_session ,name='checkoutPage'),
]
