from rest_framework import serializers
from .models import ExamModel

class ExamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = '__all__'
