from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import MainUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import viewsets
from rest_framework.decorators import action
import logging

logger = logging.getLogger(__name__)

class UserRegister(viewsets.ViewSet):
    permission_classes_by_action = {'register': [AllowAny],
                           'create_stuff': [IsAdminUser]}
    @action(methods=['POST'], detail=False)
    def register(self, request):
        if request.method == 'POST':
            user_data = request.data
            new_user = MainUser.objects.create(email=user_data['email'],
                                               first_name=user_data['first_name'],
                                               last_name=user_data['last_name'])
            new_user.set_password(user_data['password'])
            new_user.save()
            serializer = UserSerializer(new_user)
            logger.debug(f'User registered: {serializer.instance}')
            logger.info(f'User registered : {serializer.instance}')
            return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create_stuff(self, request):
        if request.method == 'POST':
            user_data = request.data

            new_user = MainUser.objects.create_superuser(email=user_data['email'],
                                                         first_name=user_data['first_name'],
                                                         password=user_data['password'],
                                                         last_name=user_data['last_name'],
                                                         role = user_data['role'])
            new_user.save()
            serializer = UserSerializer(new_user)
            logger.debug(f'Registered new user with some permissions, ID: {serializer.instance}')
            logger.info(f'Registered new user with some permissions, ID: {serializer.instance}')
            return Response(serializer.data)
    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
get_token = obtain_jwt_token