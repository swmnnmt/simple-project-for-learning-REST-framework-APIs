from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import Book
from web.serializers import BookModelSerializer, BookSerializer


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


class PostModelData(APIView):
    # Model Serializer

    def post(self, request):
        serializers = BookModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    #Custom Serializer
    def post(self, request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            author = serializers.data.get('author')
            story_name = serializers.data.get('story_name')
            description = serializers.data.get('description')
            image = request.FILES['image']
            favorite = serializers.data.get('favorite')
            book = Book()
            book.author= author
            book.story_name=story_name
            book.description=description
            book.image=image
            book.favorite=favorite
            book.save()
            return Response (serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        query = Book.objects.filter(story_name__contains=request.GET['name'])
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
