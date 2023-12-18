from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, write_only=True
    )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли не совпадают'})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({'phone_number': 'НАПИШИТЕ НОМЕР С +996'})
        return attrs 
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User 
        fields = ('username', 'password', 'confirm_password')