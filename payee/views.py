from rest_framework.response import Response
from .models import Payee
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication # get user
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.http import HttpResponse 

from .serializers import PayeeSerializer
# class RegisterView(APIView):
class AddPayee(APIView):
    def post(self, request):
        serializer = PayeeSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetPayee(APIView):
    def get(self, request,userId):
        payee = Payee.objects.filter(user=userId).values()
        serializer = PayeeSerializer(payee,many=True)
        return Response(serializer.data)

class UpdatePayee(APIView):
    def patch(self, request,id):
        payee = Payee.objects.get(id=id)
        serializer=PayeeSerializer(instance=payee,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class DeletePayee(APIView):
    # permission_classes = [IsAuthenticated]
    def delete(self, request,id):
        payee = Payee.objects.get(id=id)
        payee.delete()
        return Response("Item Successfully Deleted")


        