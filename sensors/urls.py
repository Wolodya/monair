from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from sensors import views
from django.urls.conf import path
from sensors.views import SensorViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('sensors', views.SensorViewSet)
# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('sensors/sensor_id_list/', views.SensorIdList.as_view(), name='sensors-id-list'),
]
