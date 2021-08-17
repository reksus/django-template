from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
	# url for the admin panel
    path('admin/', admin.site.urls),

	# jwt authentication
    path('getjwttoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshjwttoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifyjwttoken/', TokenVerifyView.as_view(), name='token_verify'),

	# this urls is for demonstration purpose only
    path('api/sample/', include('sample_app.urls')),

	# write your urls for other applications here.

]
