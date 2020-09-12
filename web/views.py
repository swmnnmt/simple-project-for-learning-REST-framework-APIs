from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from web.models import Book
from web.serializers import BookModelSerializer
from web.serializers import BookSerializer

#Class Based GET ALL DATA
class GetAllData(APIView):
    def get(self, request):
        query = Book.objects.all()
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

#Function Based GET ALL DATA
@api_view(['GET'])
def getalldata(request):
    if request.method == 'GET':
        query = Book.objects.all()
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status= status.HTTP_200_OK)

class GetFavData(APIView):
    def get(self, request):
        query = Book.objects.filter(favorite=True)
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class PostModelData(APIView):
    # Model Serializer

    def post(self, request):
        serializers = BookModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PostData(APIView):
    # Custom Serializer
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
        serializers = BookModelSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class EditData(APIView):
    def get(self, request):
        try:
            query = Book.objects.get(pk=request.GET['id'])
            serializers = BookModelSerializer(query)
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
