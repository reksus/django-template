from django.urls import reverse, resolve
from sample_app.views import SampleAPIView


def test_sample_app_home_url():
	url = reverse('sample_api_view')
	assert resolve(url).func.view_class == SampleAPIView

