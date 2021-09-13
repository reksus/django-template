from django.urls import reverse, resolve
from sample_app.views import SampleAPIView


def test_sample_app_home_url(client):
	url = reverse('sample_api_view')
	response = client.get(url)
	assert response.status_code == 200

