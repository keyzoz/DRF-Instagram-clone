from rest_framework import serializers
from inst_app.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    about_me = serializers.CharField()
    
    class Meta:
        model = User
        fields = '__all__'
           
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()