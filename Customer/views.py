from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, HTTP_226_IM_USED, HTTP_406_NOT_ACCEPTABLE
import random
from threading import Thread
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Customer


def sing_up(request):
    return render(request, "singUp.html")




# OTP sending by Phone number


def send_otp(phone_number, otp):
    import requests

    url = "https://api.sms.net.bd/sendsms"

    payload = {'api_key': '0F0T0PDo46h5HgX558r99PL9HdoNlxAdpu4pq8gh',
               'msg': "your Mushroomyan OTP : "+str(otp),
               'to': '88'+phone_number
               }

    response = requests.request("POST", url, data=payload)
    return response


def thread_send_otp(phone_number, otp):
    thread = Thread(target=send_otp, args=(phone_number, otp))
    thread.start()




# APIs


class ApiSingUp(CreateAPIView):

    permission_classes = []

    def post(self, request):

        result = {}

        try:
            data = json.loads(request.body)

            if 'full_name' not in data or data['full_name'] == '':
                result['massage'] = "Name can not be null."
                result['error'] = "Full name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'phone_number' not in data or data['phone_number'] == '':
                result['massage'] = "Phone number can not be null."
                result['error'] = "Phone number"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['massage'] = "Password can not be null."
                result['error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['phone_number']).first()

            if not user:

                user = User()
                user.username = data['phone_number']
                user.first_name = data['full_name']
                user.password = make_password(data['password'])
                user.is_active = False
                user.save()

                random_number = random.randint(000000, 999999)
                customer = Customer()
                customer.full_name = data['full_name']
                customer.phone_number = data['phone_number']
                customer.user = user
                customer.otp = random_number
                customer.save()

                # thread_send_otp(data['phone_number'], random_number)

                result['status'] = HTTP_202_ACCEPTED
                result['massage'] = "Success"
                result['phone_number'] = data['phone_number']
                return Response(result)
            else:
                result['status'] = HTTP_226_IM_USED
                result['massage'] = "This phone number is already have a account"
                return Response(result)

        except Exception as ex:
            result['massage'] = str(ex)
            return Response(result)


class ApiOTPCheck(CreateAPIView):

    permission_classes = []

    def put(self, request):

        result = {}
        try:
            data = json.loads(request.body)

            if 'phone_number' not in data or data['phone_number'] == '':
                result['massage'] = "Phone number can not be null."
                result['error'] = "Phone number"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            if 'otp' not in data or data['otp'] == '':
                result['massage'] = "otp can not be null."
                result['error'] = "OTP"
                return Response(result, status=HTTP_400_BAD_REQUEST)

            user = User.objects.filter(username=data['phone_number']).first()
            if not user:

                result['massage'] = "Please create a account."
                return Response(result, status=HTTP_406_NOT_ACCEPTABLE)

            elif user.is_active:

                result['massage'] = "You already created account."
                return Response(result, status=HTTP_226_IM_USED)

            else:
                customer = Customer.objects.filter(user=user).first()
                if customer.otp == data['otp']:
                    user.is_active = True
                    user.save()
                    customer.otp = ''
                    customer.save()
                    result['massage'] = "Success."
                    result['status'] = HTTP_202_ACCEPTED
                    return Response(result)

                else:

                    result = {}
                    result['status'] = HTTP_400_BAD_REQUEST
                    result['massage'] = "OTP did not match."
                    result['Error'] = "OTP"
                    return Response(result)

        except Exception as ex:
            result = {}
            result['massage'] = str(ex)
            return Response(result)