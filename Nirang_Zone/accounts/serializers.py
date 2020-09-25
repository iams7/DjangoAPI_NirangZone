from rest_framework import serializers
from accounts.models import Users

class UsersSerializer(serializers.ModelSerializer):

    user_id = serializers.CharField(required=False)
    user_name = serializers.CharField(required=False)
    user_age = serializers.IntegerField(required=False)
    user_email = serializers.EmailField(required=False)
    user_ranking = serializers.FloatField(required=False)

    class Meta:
        model = Users
        fields = '__all__'