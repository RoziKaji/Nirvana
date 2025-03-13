from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'phone_number', 'is_subscribed', 'subscribed_at', 'subscription_end', 'minutes_listened']
