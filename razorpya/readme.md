
# Razropay 

Payment Integration of Razropay with Django.

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
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Razorpya%20(3).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Razorpya%20(4).png?raw=true)

![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Razorpya%20(5).png?raw=true)
![App Screenshot](https://github.com/Experiya/snapshot/blob/main/Razorpya%20(6).png?raw=true)



## Steps

- [Create an account in Razorpay](https://razorpay.com/)
- [Use the official documentation for the implementation](https://razorpay.com/docs/payment-gateway/quick-integration/)

1. This is for the checkout functionality

Internship/rozarpay/views.py


```bash
import razorpay
client = razorpay.Client(auth=("api_key", "api_secret"))

def razorpayHome(request):
    
    if request.method=="POST":
        DATA = {
            "amount": 100,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",
                "key2": "value2"
                }
            }
        client.order.create(data=DATA)

    return render(request,'razorpay/index.html')
```


Aftre successful payment you can see the details in your dashboard whic is prodvided by Razorpay.
