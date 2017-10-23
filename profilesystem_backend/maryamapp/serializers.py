from rest_framework import serializers
from .models import ASUmember

class ASUmemberSerializer(serializers.ModelSerializer):
	class Meta:
		model=ASUmember
		fields='__all__'

			