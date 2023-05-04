from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def checkout(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount')) * 100 # amount in paise
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        return JsonResponse(payment)
    return render(request, 'checkout.html')
