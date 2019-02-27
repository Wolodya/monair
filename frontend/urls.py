from django.views.generic.base import TemplateView
from django.urls.conf import path


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"))
]
