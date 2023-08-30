from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


from .serializers import GradeSerializer, SchoolCardSerializer
from .models import Grade, SchoolCard


class SchoolCardListAPI(APIView):
    def get_object(self):
        try:
            return SchoolCard.objects.all()
        except SchoolCard.DoesNotExist:
            return Http404

    def get(self, request):
        queryset = self.get_object()
        if queryset == Http404:
            return Http404
        serializer = SchoolCardSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolCardDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return SchoolCard.objects.get(pk=pk)
        except SchoolCard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk=pk)
        if queryset == Http404:
            return Http404
        serializer = SchoolCardSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk=pk)
        if queryset == Http404:
            return Http404
        serializer = SchoolCardSerializer(queryset, data=request.data)
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


class GradeListAPI(APIView):

    def get(self, request):
        school_card_id = request.query_params.get('school_card')
        queryset = Grade.objects.all()
        if school_card_id:
            queryset = queryset.filter(school_card_id=school_card_id)
        serializer = GradeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GradeDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Grade.objects.get(pk=pk)
        except Grade.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        queryset = self.get_object(pk=pk)
        if queryset == Http404:
            return Http404
        serializer = GradeSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk=pk)
        if queryset == Http404:
            return Http404
        serializer = GradeSerializer(queryset, data=request.data)
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
