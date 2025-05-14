# core/serializers.py
from rest_framework import serializers
from .models import SiteContent

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Add display names for 'section' and 'content_type' fields
        data['section'] = instance.get_section_display()
        data['content_type'] = instance.get_content_type_display()
        return data
