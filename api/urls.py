from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemList,ItemDetail,LocationList,LocationDetail,ProductViewSet, LocationViewSet
from .views import CustomTokenObtainPairView
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('product/',ItemList.as_view()),
    path('product/<int:pk>/',ItemDetail.as_view()),
    path('location/',LocationList.as_view()),
    path('location/<int:pk>',LocationDetail.as_view()),
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('api/', include(router.urls)), 
]
