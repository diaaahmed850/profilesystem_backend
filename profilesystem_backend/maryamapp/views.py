from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import ASUmember
from .serializers import ASUmemberSerializer
# Create your views here.
@api_view(['GET','post'])
def ASUmemberReq(request):
	if request.method=='GET':
		ASUmembers=ASUmember.objects.all()
		serializer=ASUmemberSerializer(ASUmembers, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = ASUmemberSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors,status=400)