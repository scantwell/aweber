from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from aweber.widgetapi import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'widgets', views.WidgetViewSet, basename="widget")

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', include([
        path('', SpectacularAPIView.as_view(), name='schema'),
        path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ])),
]