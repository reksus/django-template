from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SampleAPIView(APIView):
	def get(self, request):
		response_data = {
			'status' : "success",
			'sCode' : 200,
			'data': "sample data",
			'message' : "sample data successfully retrieved"
		}
		return Response(data=response_data, status=status.HTTP_200_OK)
