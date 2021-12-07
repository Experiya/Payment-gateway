
# Stripe

Payment Integration of Stripe with Django.

## Installation 

Install my-project with pip

```bash 
  py -m venv env   [for virtual environment || make sure you have install python virtualenv]
  .\env\Scripts\activate
  pip install -r requirements.txt
  cd Internship
  py manage.py runserver
  http://127.0.0.1:8000/
```
I have removed my private key's from setting.py, So you have to add your own key's.

    
## Screenshots

![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Razorpya%20(2).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Stripe%20(1).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Stripe%20(3).png?raw=true)

![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Stripe%20(4).png?raw=true)




## Steps

- [Create an account in Stripe](https://stripe.com/)  || Make sure you have complete the registration process otherwise you will definitely going to have some error. 
- [Use the official documentation for the implementation](https://stripe.com/docs/checkout/quickstart)

1. This is for the checkout functionality

Internship/stripeapp/views.py


```bash
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
```

I've added a product manually in the stripe dashboard and after that I have the productID for the price here.



Aftre successful payment you can see the details in your dashboard which is prodvided by Stripe.
