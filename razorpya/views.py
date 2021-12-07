from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay

#add your public and private key
client = razorpay.Client(auth=("", ""))

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
@csrf_exempt
def success(request):
    return render(request,'razorpay/success.html')

def cancel(request):
    return render(request,'razorpay/cancel.html')