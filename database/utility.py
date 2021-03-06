from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

BASE_API_URL = 'http://localhost:8000/database/'

def ApiGetResponse(serializer, queryset=[], many=True):
	serializer = serializer(queryset, many=many)
	return Response(serializer.data)

def ApiUpdateResponse(serializer, request, instance):
	serializer = serializer(instance=instance, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

def ApiPostResponse(serializer, request):
	serializer = serializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)