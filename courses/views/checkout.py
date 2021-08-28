import math
from django.http import request

from razorpay.client import Client
import courses
from courses.models import Course, payment, payments, user_course, usercourse
from courses.models.couponcode import Coupon
from django.shortcuts import HttpResponse, redirect, render
from django.template import Context, Template, context
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.
from time import time, timezone
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from cwp.settings import KEY_SECRET, kEY_ID
import razorpay
import json
import random
client = razorpay.Client(auth=(kEY_ID, KEY_SECRET))

@login_required(login_url='login')
def Checkout(request, slug):
    selected_course = Course.objects.get(slug=slug)
    action = request.GET.get('action')
    order = None
    user = request.user
    amount = None
    coupon = None
    coupon_error_msg = None
    coupon_data = None
    coupon = request.GET.get('couponcode')
    try:
        usercheck = user_course.objects.get(
            user=user, course=selected_course)
        error = "You are Already Enrolled in this Course"
    except:
        error = None
    if coupon:
        try:
            print("abc")
            coupon_data=Coupon.objects.get(coupon_name=coupon,coupon_course=selected_course)
            print("abc2")
        except:
            print("error")
            coupon_error_msg = "Invalid Coupon Code"
            print("error2")
    if error is None:
        amount = int((selected_course.cprice - (selected_course.cprice *
                                                selected_course.cdiscount * 0.01)) * 100)
        if coupon_data is not None:
            total = amount
            amount = (total  * coupon_data.discount * 1/100)

    if amount == 0:
        usercourse = user_course()
        usercourse.user = request.user
        usercourse.course = selected_course
        usercourse.save()
        return redirect(f'/show/{slug}')
        # coupon code
    if action == 'create_payment' and amount:
        receipt = int(time()) + random.randint(0, 9)+random.randint(0, 9)
        receipt = str(receipt)
        currency = "INR"
        if coupon_data:
            notes = {
                "email": user.email,
                "name": f'{user.first_name} {user.last_name}',
                "discount":(f"{coupon_data.discount}%")
            }
        else:
             notes = {
                "email": user.email,
                "name": f'{user.first_name} {user.last_name}'
            }
        order = client.order.create(
            {'receipt': receipt, 'amount': amount,
                'currency': currency, 'notes': notes}
        )
        payments = payment()
        payments.user  = user
        payments.course = selected_course
        payments.order_id = order.get('id')
        payments.save()

    context = {
        "selected_course": selected_course,
        "order": order,
        "error": error,
        "user":user,
        "coupon":coupon_data,
        "coupon_error_msg":coupon_error_msg
    }
    return render(request, 'courses/check_out.html', context=context)
@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        try:
            data = request.POST
            print(data)
            client.utility.verify_payment_signature(data)
            raz_orderid = request.POST.get('razorpay_order_id')
            raz_paymentid = request.POST.get('razorpay_payment_id')
            payments = payment.objects.get(order_id=raz_orderid)
            payments.payment_id = raz_paymentid
            payments.status = True

            usercourse = user_course(
                user=payments.user, course=payments.course)
            usercourse.save()
            payments.user_course = usercourse
            payments.save()
            return redirect("mycourses")
            
        except:
            return HttpResponse("Invalid Payment Details")
        
        
