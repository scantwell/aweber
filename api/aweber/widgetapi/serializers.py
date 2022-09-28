from rest_framework import serializers
from aweber.widgetapi.models import Widget


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = ['id', 'name', 'number_of_parts', 'created_at', 'updated_at']
