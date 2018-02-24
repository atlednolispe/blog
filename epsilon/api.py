from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from .models import Post, Category, Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = (
            'url', 'id', 'title', 'owner',
            'category', 'tags', 'desc', 'pv',
            'uv', 'created_time'
        )


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = (
            'url', 'id', 'title', 'owner',
            'category', 'tags', 'desc', 'pv',
            'uv', 'status', 'is_markdown', 'created_time',
            'update_time', 'content_html'
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url', 'id', 'name', 'created_time'
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'created_time',
            'post_set',
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'url', 'id', 'name', 'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Tag
        fields = (
            'id', 'name', 'created_time',
            'post_set',
        )


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = TagDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'date_joined',
        )


class UserDetailSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'date_joined',
            'post_set',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UserDetailSerializer
        return super().retrieve(request, *args, **kwargs)
