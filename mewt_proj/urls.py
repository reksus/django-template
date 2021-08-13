from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

	# this urls is for demonstration purpose only
    path('sample/', include('sample_app.urls')),
]
