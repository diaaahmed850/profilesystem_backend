from rest_framework import serializers
from rest_framework import seriali
from .models import ASUmember

class ASUmemberSerializer(serializers.ModelSerializer):
	class Meta:
		model=ASUmember
		fields=(__all__)

			