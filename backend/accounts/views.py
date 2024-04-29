from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ViewSet):
    """
    A ViewSet for listing, creating, logging in, and logging out users.
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    @csrf_exempt
    @action(detail=False, methods=['get'])
    def list_users(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @csrf_exempt
    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_profile(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
    
    @csrf_exempt
    @action(detail=False, methods=['get', 'post'])
    def login(self, request):
        if request.method == 'GET':
            data = {
                "message": "To log in, send a POST request to this endpoint with 'username' and 'password' in the request body.",
                "example": {
                    "username": "your_username",
                    "password": "your_password"
                }
            }
            return Response(data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['get'])
    def index(self, request):
        data = {
            'message': 'Welcome to the uUser API index page. You can find the list of available endpoints here.',
            'endpoints': [
                {
                    'page':'List users',
                    'url': request.build_absolute_uri('/api/user/list/'),
                    'requires_auth':True,
                    'description':'Show a list of existent users',
                    'supported_methods':['GET'],
                },
                {
                    'page':'Create User',
                    'url': request.build_absolute_uri('/api/user/create/'),
                    'requires_auth':False,
                    'description':'Let a new user create his own account',
                    'supported_methods':['POST'],
                },
                {
                    'page':'User Profile',
                    'url': request.build_absolute_uri('/api/user/profile/'),
                    'requires_auth':True,
                    'description':'Show the account details',
                    'supported_methods':['GET'],
                },
                {
                    'page':'Login',
                    'url': request.build_absolute_uri('/api/user/login/'),
                    'requires_auth':False,
                    'description':'Let the user access his account',
                    'supported_methods':['POST'],
                },
                {
                    'page':'Logout',
                    'url': request.build_absolute_uri('/api/user/logout/'),
                    'requires_auth':True,
                    'description':'Let the user end his sessión, destroying his token',
                    'supported_methods':['POST'],
                },
            ]
        }
        return Response(data)