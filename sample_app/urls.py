from django.urls import path
from sample_app.views import SampleAPIView

urlpatterns = [
    path('', SampleAPIView.as_view(), name='sample_api_view'),
]
