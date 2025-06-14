from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app import models
from rest_framework import status

@api_view(['GET'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)

    data = {}

    if serializer.is_valid():
        account = serializer.save()

        data['username'] = account.username
        data['email'] = account.email

        token = Token.objects.get(user=account)

        data['token'] = token.key
    else:
        data = serializer.errors

    return Response(data)