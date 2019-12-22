from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #Django specific class, has a lot of functionality. Just want to expose as little as possible
        fields = ('id', 'username')