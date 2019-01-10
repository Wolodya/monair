from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from sensors import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^sensors/$', views.SensorList.as_view(),
        name='sensors-list'),
    url(r'^sensors/(?P<pk>\d+)/$', views.SensorDetail.as_view(),
        name='sensors-detail'),
    url(r'^sensors/sensor_id_list/$', views.SensorIdList.as_view(),
        name='sensors-id-list'),


]
