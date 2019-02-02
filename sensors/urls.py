from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from sensors import views
from django.urls.conf import path

# Create a router and register our viewsets with it.
router = DefaultRouter()

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('sensors/', views.SensorList.as_view(), name='sensors-list'),
    path('sensors/<int:pk>/', views.SensorDetail.as_view(), name='sensors-detail'),
    path('sensors/sensor_id_list/', views.SensorIdList.as_view(), name='sensors-id-list'),
]
