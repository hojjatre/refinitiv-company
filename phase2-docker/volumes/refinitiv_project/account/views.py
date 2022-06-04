from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Account
from .serializers import AccountSerializer, LoginSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.hashers import check_password


class Register(APIView):

    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "register.html"

    def get(self, request):
        serializer = AccountSerializer
        return Response({'serializer': serializer})
    
    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            print(serialized_data.validated_data)
            serialized_data.create(serialized_data.validated_data)
        return redirect('show-user')


class ShowUser(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "showUser.html"

    def get(self, request):
        accounts = Account.objects.all()
        return Response({'users': accounts})
    


class login(APIView):
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"

    def get(self, request):
        serializer = LoginSerializer
        return Response({'serializer': serializer})
    

    def post(self, request):
        
        token = None
        serializer = LoginSerializer
        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            email = serialized_data.data['email']
            password = serialized_data.data['password']
            try:
                account = Account.objects.get(email=email)
                account_pass = account.password
                check_pass = check_password(password=password, encoded=account_pass)
                print(check_pass)
                if not check_pass:
                    print("Password not match.")
                    return Response({'serializer': serializer, 'error':"error is Password not match."})
                else:
                    try:
                        token = Token.objects.get(user=account)
                    except Token.DoesNotExist as t:
                        token = Token.objects.create(user=account)

                    print(f"Token: {token.key}")
                    return Response({'serializer': serializer, 'Token':f"{token.key}"})
            except:
                return Response({'serializer': serializer, 'error':"error is email is not correct."})