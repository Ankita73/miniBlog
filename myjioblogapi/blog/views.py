from django.shortcuts import render

# Create your views here.
from django.db.models import Q

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )


from blog.models import blog
from blog.serializers import (
    BlogListSerialiser,
    BlogDetailSerialiser,
    BlogCreateUpdateSerialiser,
    )

from .permissions import IsOwnerOrReadOnly

class BlogListAPIView(ListAPIView):
    #queryset = blog.objects.all()
    serializer_class = BlogListSerialiser
    permission_classes = [AllowAny]
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = blog.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list


class BlogDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = blog.objects.all()
    serializer_class = BlogDetailSerialiser

class BlogUpdateAPIView(RetrieveUpdateAPIView):
    queryset = blog.objects.all()
    serializer_class = BlogCreateUpdateSerialiser
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class BlogDestroyAPIView(DestroyAPIView):
    queryset = blog.objects.all()
    serializer_class = BlogDetailSerialiser
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #permission_classes = [IsAuthenticatedOrReadOnly]


class BlogCreateAPIView(CreateAPIView):
    queryset = blog.objects.all()
    serializer_class = BlogCreateUpdateSerialiser
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        