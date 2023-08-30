from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .serializers import SubjectSerializer
from .models import Subject


class SubjectListAPI(APIView):
    def get_object(self):
        try:
            return Subject.objects.all()
        except Subject.DoesNotExist:
            return Http404

    def get(self, request):
        queryset = self.get_object()
        if queryset == Http404:
            return Http404
        serializer = SubjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk=pk)
        if queryset == Http404:
            return Http404
        serializer = SubjectSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            queryset = self.get_object(pk=pk)
        except Http404:
            return Response("Objeto não encontrado.", status=status.HTTP_404_NOT_FOUND)
        serializer = SubjectSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk=pk)
        if queryset == Http404:
            return Http404
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)