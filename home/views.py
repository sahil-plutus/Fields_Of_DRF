from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response


class StudentAPI(ViewSet):

    def list(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

