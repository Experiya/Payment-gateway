from django.shortcuts import render
from django.urls import path
from .import views
urlpatterns = [
    path('',views.razorpayHome ,name='razorpayHome'),
    path('success',views.success ,name='success'),
    path('cancel',views.cancel ,name='cancel'),

]
