from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),  # HTML-интерфейс
    path('auth/', include('django.contrib.auth.urls')),  # login/logout
    path('api/', include('diary.api_urls')),  # API перенесем сюда
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
