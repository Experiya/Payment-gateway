from django.shortcuts import render, redirect
from Internship.settings import STRIPE_KEY_SECRET
from django.urls import reverse

import socket

import stripe
from django.conf import settings

# YOUR_DOMAIN = 'http://127.0.0.1:8000'


# This is your test secret API key.
stripe.api_key = STRIPE_KEY_SECRET


def stripeHome(request):
    
    return render(request,'stripe/index.html')
    
def success(request):
    return render(request,'stripe/success.html')

def cancel(request):
    return render(request,'stripe/cancel.html')


def create_checkout_session(request):
    YOUR_DOMAIN = "http://127.0.0.1:8000"  # change in production
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': 'price_1K43rdSJb0jqRJt58xfrW96t',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN +'/stripeapp/success' ,
        cancel_url=YOUR_DOMAIN +'/stripeapp/cancel'
    )
    return redirect(checkout_session.url)



