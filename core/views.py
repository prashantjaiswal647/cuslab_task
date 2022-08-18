from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({ 'status': 200, 'message': 'hello'})


@api_view(['GET'])
def get_destination(request, id):

    acc_obj = Account.objects.get(id = id)
    serializer = AccountSerializer(acc_obj , many=True)

    return Response({ 'status': 200 , 'payload': serializer.data })




from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({ 'status': 200 , 'payload': serializer.data , 'refresh': str(refresh),
        'access': str(refresh.access_token) , 'message': 'you sent'})


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class AccountAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        acc_obj = Account.objects.all()
        serializer = AccountSerializer(acc_obj , many=True)
        print(request.user)

        return Response({ 'status': 200 , 'payload': serializer.data })


    def post(self, request):
        data = request.data
        serializer = AccountSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })
        serializer.save()

        return Response({ 'status': 200 , 'payload': serializer.data , 'message': 'you sent'})

        
         

    def patch(self, request):
        try:
            acc_obj = Account.objects.get(id = request.data['id'])
            serializer = AccountSerializer(acc_obj , data = request.data , partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })

            serializer.save()
            return Response({ 'status': 200 , 'payload': serializer.data , 'message': 'you sent'})

        except Exception as e:
            return Response({ 'status': 403 , 'message' : 'invalid id'})
        

    def put(self, request):
        try:
            acc_obj = Account.objects.get(id = request.data['id'])
            serializer = AccountSerializer(acc_obj , data = request.data, partial = False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })

            serializer.save()
            return Response({ 'status': 200 , 'payload': serializer.data , 'message': 'you sent'})

        except Exception as e:
            return Response({ 'status': 403 , 'message' : 'invalid id'})

    def delete(self, request):
        try:
            id = request.GET.get('id')
            acc_obj = Account.objects.get(id = id)
            acc_obj.delete()
            
            
            return Response({ 'status': 200 ,  'message': 'Deleted'})

        except Exception as e:
            print(e)
            return Response({ 'status': 403 , 'message' : 'invalid id'})




class DestinationAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        des_obj = Destination.objects.all()
        serializer = DestinationSerializer(des_obj , many=True)
        print(request.user)

        return Response({ 'status': 200 , 'payload': serializer.data })


    def post(self, request):
        data = request.data
        serializer = DestinationSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })
        serializer.save()

        return Response({ 'status': 200 , 'payload': serializer.data , 'message': 'you sent'})

        
         

    def patch(self, request):
        try:
            des_obj = Destination.objects.get(id = request.data['id'])
            serializer = DestinationSerializer(des_obj , data = request.data , partial = True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })

            serializer.save()
            return Response({ 'status': 200 , 'payload': serializer.data , 'message': 'you sent'})

        except Exception as e:
            return Response({ 'status': 403 , 'message' : 'invalid id'})
        

    def put(self, request):
        try:
            des_obj = Destination.objects.get(id = request.data['id'])
            serializer = DestinationSerializer(des_obj , data = request.data, partial = False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({ 'status': 403 ,'errors' : serializer.errors ,'message': 'Un Authenticate' })

            serializer.save()
            return Response({ 'status': 200 , 'payload': serializer.data , 'message': 'you sent'})

        except Exception as e:
            return Response({ 'status': 403 , 'message' : 'invalid id'})

    def delete(self, request):
        try:
            id = request.GET.get('id')
            des_obj = Destination.objects.get(id = id)
            des_obj.delete()
            
            
            return Response({ 'status': 200 ,  'message': 'Deleted'})

        except Exception as e:
            print(e)
            return Response({ 'status': 403 , 'message' : 'invalid id'})