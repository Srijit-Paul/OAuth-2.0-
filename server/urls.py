from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root_view),
    path('login/', views.login),
    path('signup/', views.signup),
    path('test_token/', views.test_token),
    path('api/', include('api.urls')),

    # JWT Token obtain and refresh endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
