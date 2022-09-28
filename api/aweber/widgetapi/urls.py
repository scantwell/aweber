from django.urls import path, include
from rest_framework.routers import DefaultRouter
from aweber.widgetapi import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'widgets', views.WidgetViewSet, basename="widget")

urlpatterns = [
    path('', include(router.urls))
]