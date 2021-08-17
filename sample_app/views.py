"""samples view to test the functionalities of external services added to the project."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import sample_heavy_task


# Create your views here.
class SampleAPIView(APIView):
	"""sample class to test the working project settings."""

	def get(self, request):
		"""Sample get request which return a sample json response."""
		response_data = {
			'status': "success",
			'sCode': 200,
			'data': "sample data",
			'message': "sample data successfully retrieved"
		}
		return Response(data=response_data, status=status.HTTP_200_OK)


class SampleBgTaskAPIView(APIView):
	"""sample class to test task queue project settings."""

	def get(self, request):
		"""Sample get request which enqueues a sample background task."""
		# shift this heavy task to a task queue and continue with the request/response cycle
		sample_heavy_task.send()

		return Response("Your heavy task has been initiated.")
