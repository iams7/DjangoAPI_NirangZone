from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import *
from django.conf import settings

class UserAuthentication(ObtainAuthToken):

    def post(self,request,*args,**kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={
                'request':request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response(token.key)

class UserList(APIView):

    def get(self, request):

        model = Users.objects.all()
        serializer = UsersSerializer(model, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            subject = 'Welcome to NirangZone'
            message = 'Thank you for signing up with Django RESTAPI'
            from_email = settings.EMAIL_HOST_USER
            # to_mail = [serializer.user_email, settings.EMAIL_HOST_USER,]
            to_mail = [settings.EMAIL_HOST_USER,]
            send_mail(subject,message,from_email,to_mail,fail_silently=True)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )

class UserDetail(APIView):

    def get_user(self, user_id):

        try:

            model = Users.objects.get(id=user_id)
            return model

        except Users.DoesNotExist:

            return

    def get(self, request, user_id):

        if not self.get_user(user_id):

            return Response(
                f'Users with ID:{user_id} is not found in the database',
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsersSerializer(self.get_user(user_id))
        return Response(serializer.data)

    def put(self, request, user_id):

        if not self.get_user(user_id):

            return Response(
                f'Users with ID:{user_id} is not found in the database',
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UsersSerializer(
            self.get_user(user_id),
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )

    def delete(self,request,user_id):

        if not self.get_user(user_id):

            return Response(
                f'Users with ID:{user_id} is not found in the database',
                status=status.HTTP_404_NOT_FOUND
            )

        model = self.get_user(user_id)
        model.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )