from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

from inst_app.serializer import UserSerializer, UserLoginSerializer
from inst_app.models import User


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LoginUser(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                if user.password == serializer.validated_data['password']:
                    token = Token.objects.get_or_create(user=user)
                    return Response({'token': str(token[0])})
                else:
                    return Response({'exception': 'Wrong password'})
            except ObjectDoesNotExist:
                return Response({'exception': 'User does not exist'})
                
class GetUserByID(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UpdateUser(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'message': 'User has been updated'})
            except ObjectDoesNotExist:
                return Response({'exception': 'User does not exist'})
    
class DeleteUser(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            if request.user.id == pk:
                request.user.delete()
                return Response({'message': 'User has been deleted'})
            else:
                return Response({'exception': 'You\'re haven\'nt permissons'})
        except ObjectDoesNotExist:
            return Response({'exception': 'User does not exist'})
        
        
        