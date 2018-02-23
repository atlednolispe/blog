from rest_framework import serializers, viewsets

from .models import Post, Category, Tag


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'url', 'title', 'owner', 'desc',
            'category', 'tags', 'created_time'
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url', 'name', 'created_time'
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
