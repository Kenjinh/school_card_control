from django.utils.translation import ugettext as _
from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_email(self, value):
        if '@' not in value or ('.com' not in value and '.br' not in value):
            raise serializers.ValidationError(_("The e-mail address is invalid."))

        return value

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance
