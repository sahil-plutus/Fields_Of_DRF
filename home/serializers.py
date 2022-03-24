from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    # this is a serializer method fields
    result = serializers.SerializerMethodField()

    def get_result(self, obj):
        if obj.marks >= 50:
            return "pass"
        else:
            return "fail"

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'url', 'gender', 'marks', 'result']
