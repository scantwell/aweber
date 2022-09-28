from rest_framework import viewsets
from aweber.widgetapi.models import Widget
from aweber.widgetapi.serializers import WidgetSerializer


class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer