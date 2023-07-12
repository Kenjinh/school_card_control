from django.utils.translation import ugettext as _
from rest_framework import serializers

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.hourly_load = validated_data.get('hourly_load', instance.hourly_load)
        instance.save()
        return instance