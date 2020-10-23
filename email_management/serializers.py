from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class SenderEmailSerializer(serializers.ModelSerializer):
	class Meta:
		model = SenderEmail
		exclude = ('created_at', 'updated_at')

		
class SendEmailSerializer(serializers.ModelSerializer):
	class Meta:
		model = SendEmail
		exclude = ('created_at', 'updated_at')