from rest_framework import serializers
from .models import BMImodel

class BMIserializer(serializers.ModelSerializer):
	class Meta:
		model=BMImodel
		fields="__all__"

	