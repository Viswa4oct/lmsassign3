from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import LoginSerializer, SignUpSerializer, UserSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        print('SignUp')
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            queryset = User.objects.filter(email=request.data.get('email'))
            if queryset.exists():
                serializer = SignUpSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'GET':
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        print('Login')
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            queryset = User.objects.filter(
                email=request.data.get('email'),
                password=request.data.get('password'))
            if queryset.exists():
                serializer = UserSerializer(queryset.first())
                return Response(serializer.data)
            else:
                return Response({}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
