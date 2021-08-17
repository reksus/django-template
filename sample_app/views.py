from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import sample_heavy_task

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


class SampleBgTaskAPIView(APIView):
	def get(self, request):

		# shift this heavy task to a task queue and continue with the request/response cycle
		sample_heavy_task.send()

		return Response("Your heavy task has been initiated.")
