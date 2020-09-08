from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import Book
from web.serializers import BookModelSerializer


class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all()
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class GetFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(favorite=True)
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class UpdateStoryData(APIView):
    def get(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookModelSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = Book.objects.get(pk=pk)
        serializers = BookModelSerializer(query, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
