from rest_framework import serializers

from .models import Grade, SchoolCard



class GradeSerializer(serializers.ModelSerializer):
    subject_name = serializers.StringRelatedField(source='subject', read_only=True)

    def create(self, validated_data):
        return Grade.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.school_card = validated_data.get('school_card', instance.school_card)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance

    class Meta:
        model = Grade
        fields = '__all__'


class SchoolCardSerializer(serializers.ModelSerializer):
    student_name = serializers.StringRelatedField(source='student', read_only=True)
    grades = GradeSerializer(source='grade_set', read_only=True, many=True)

    def create(self, validated_data):
        return SchoolCard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.student = validated_data.get('student', instance.student)
        instance.save()
        return instance

    class Meta:
        model = SchoolCard
        fields = '__all__'
