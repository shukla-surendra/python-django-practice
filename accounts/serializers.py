from django.contrib.auth.models import User
from rest_framework import serializers


#from accounts.models import Customer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


# to substitute default User with CUstomer
'''
class CustomerSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()
 
    class Meta(object):
        model = Customer
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
'''