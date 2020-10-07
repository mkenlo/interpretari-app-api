from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    """ @action(detail=False, methods=['POST'], url_path='login')
    def login(self, request):
        return Response({'status':'login view'})

    @action(detail=False, methods=['POST'], url_path='logout')
    def logout(self):
        return Response({'status':'logout view'}) """