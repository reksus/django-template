from django.urls import path
from sample_app.views import SampleAPIView, SampleBgTaskAPIView

urlpatterns = [
    path('', SampleAPIView.as_view(), name='sample_api_view'),
    path('bgtask', SampleBgTaskAPIView.as_view(), name='sample_bg_task_api_view'),
]
