from rest_framework import serializers

from web.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=50)
    story_name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    image = serializers.ImageField(default='', use_url=True)
    favorite = serializers.BooleanField(default=False)


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
