from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
@api_view(['GET'])
def root_view(request):
    return Response({"message": "Welcome to the API"})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = get_tokens_for_user(user)
        return Response({"token": token, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Incorrect credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    token = get_tokens_for_user(user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token, "user": serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f"Access granted for {request.user.email}")
