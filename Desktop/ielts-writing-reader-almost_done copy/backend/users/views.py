# from rest_framework import APIView
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime

from django.conf import settings



# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        user.update_paid_status()  # Check and update paid status

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') 

        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response
    

    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # raise AuthenticationFailed('Unauthenticated!') # Basta buydu sonra token expire oldu diye dusundum, altina yazdim updated kodu
            response = Response({'error': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
            response.delete_cookie('jwt')
            return response

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class LogoutView(APIView):
    def post(self, request):
        response=  Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'cookie was successfuly deleted'
        }
        return response
    

# Chatgpt key insertation
# class GptKeyView(APIView):
#     def post(self, request):
#         id = request.data.get('id') # user_id
#         gptkey = request.data.get('gptkey')

#         if not id or not gptkey:
#             return Response({'error': 'user_id and gptkey are required'}, status = status.HTTP_400_BAD_REQUEST)
        
#         try:
#             user = User.objects.get(id= id)
#         except User.DoesNotExist:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         user.gptkey = gptkey
#         user.save()

#         re
