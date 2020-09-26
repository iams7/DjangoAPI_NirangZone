# DjangoAPI_NirangZone 
## API Development

As per the instructions mentioned in the given scenario, the API has been developed using Django REST Framework and a simple python script to test the flow of the API in it's all test case satisfaction.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django
pip install djangorestframework
```
## Usage
1. Installation and Execution of Django Server
```python
django-admin startproject Nirang_Zone

```
2. Setting up the API URLS 
```python
from django.conf.urls import url

    url( r'^api/users_list/$' , UserList.as_view() , name='user_list' ),
    url( r'^api/users_list/(?P<user_id>\d+)/$' , UserDetail.as_view() , name='user_list' ),
    url (r'^api/auth/$',UserAuthentication.as_view() , name='User Authentication API' )

```
##### Usage of Create Django App in Nirang_Zone Project

```python
django-admin startapp accounts
```

##### Create a Users Model in *models.py*

```python
    user_id = models.CharField(max_length=10, unique=True) # Eg. 14MSE1007
    user_name = models.CharField(max_length=100) # MS Dhoni
    user_email = models.EmailField(max_length=100) # msd@bot.com
    user_password = models.CharField(max_length=100)
    user_age = models.IntegerField() # 39
    user_ranking = models.FloatField() # 7
```

##### Create a new *serializer.py* file in **App** directory to Serialize the *models.py*
```python
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__' # to fetch all the record of the users 
```
##### Usage of Django Admin to test with Django UI for easier purpose
```python
http://127.0.0.1:8000/admin/accounts/users/

```

###### Serialized data from *models.py* is supposed to be used for data transmission in REST API for data transaction


3. Creation of an API using Python Django Framework.
```python
def get(self, request):

        model = Users.objects.all()
        serializer = UsersSerializer(model, many=True)

        return Response(serializer.data)


```
 
4. Addition New Entries to the Database using the POST method
```python
from .serializers import *
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

```
5. Modification of data in database using the PUT method
```python
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

```
6. Deletion of data from database using the DELETE method
```python
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

```
7. Authentication to the Application in Django REST API
Please make sure to update tests as appropriate.
```python
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
```
8. Create Django REST API data using Request from *NirangZoneClient/client.py* seperately to perform requests (*exclusively for testing APIs*)

```python
URL = 'http://127.0.0.1:8000'

def get_token():

    # get auth token
    url = f'{URL}/api/auth/'
    response = requests.post(url, data={
        'username':'<username>',
        'password':'<password>'
    })
    return response.json()

def get_data(): # definition to call API
def create_new(count): # definition to call API
def edit_data(user_id): # definition to call API
def delete_data(user_id): # definition to call API

```

## Test Cases
#### Accomplished testcases are published on Postman Document

```python
https://documenter.getpostman.com/view/11578501/TVKHTaAs

```

