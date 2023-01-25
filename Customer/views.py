from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED
from .models import Customer

def sing_up(request):
    return render(request, "singUp.html")


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

            customer = Customer()
            customer.full_name = data['full_name']
            customer.phone_number = data['phone_number']
            customer.save()

            result['status'] = HTTP_202_ACCEPTED
            result['massage'] = "Success"
            result['phone_number'] = data['phone_number']
            return Response(result)
        except Exception as ex:
            result['message'] = str(ex)
            return Response(result)
        return Response("True")