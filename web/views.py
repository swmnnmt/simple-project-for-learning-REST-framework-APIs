from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import Book
from web.serializers import BookModelSerializer
from web.serializers import BookSerializer


# Class Based API for GET ALL DATA
# Model Based  Serializer
class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all()
        serializers = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# Function Based Get All Data
# Model Based Serializer
@api_view(['GET'])
def get_all_data(request):
    if request.method == 'GET':
        query = Book.objects.all()
        serializers = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# Class Based Get Favorite Date
# Model Based Serializer
class GetFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(favorite=True)
        serializers = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


# Class Based API for Post Data
# Model Based Serializer
class PostModelData(APIView):
    def post(self, request):
        serializers = BookModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# Function Based API for Post Data
# Model Based Serializer
@api_view(['POST'])
def post_model_data(request):
    if request.method == 'POST':
        serializers = BookModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# Class Based API for Post Data
# Custom Serializer
class PostData(APIView):
    def post(self, request):
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            author = serializers.data.get('author')
            story_name = serializers.data.get('story_name')
            description = serializers.data.get('description')
            image = request.FILES['image']
            favorite = serializers.data.get('favorite')
            book = Book()
            book.author = author
            book.story_name = story_name
            book.description = description
            book.image = image
            book.favorite = favorite
            book.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchData(APIView):
    def get(self, request):
        query = Book.objects.filter(story_name__contains=request.GET['name'])
        serializers = BookModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class EditData(APIView):
    def get(self, request):
        try:
            query = Book.objects.get(pk=request.GET['id'])
            serializers = BookModelSerializer(query, context={'request': request})
            return Response(serializers.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            query = Book.objects.get(pk=request.GET['id'])
            serializers = BookModelSerializer(query, data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)

            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        try:
            query = Book.objects.get(pk=request.GET['id'])
            serializers = BookModelSerializer(query)
            query.delete()
            return Response(serializers.data, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
