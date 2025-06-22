from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from .permissions import IsOwner
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.

class RegisterView(APIView):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	
class ProfileView(APIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]
	def get_object(self):
		return self.request.user

