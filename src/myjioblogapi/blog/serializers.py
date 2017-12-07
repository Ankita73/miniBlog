from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from accounts.serializers import UserDetailSerializer
from comments.serializers import CommentSerializer

from blog.models import blog

from comments.models import Comment

blog_detail_url = HyperlinkedIdentityField(
        view_name='blog:detail',
        lookup_field = 'pk'
        )


class BlogListSerialiser(ModelSerializer):
    url = blog_detail_url
    class Meta:
        model = blog
        fields = [
            'url',
            'user',
            'blogId',
            'blogTitle',
            'blogContent',
            'bloggedDate',
        ]


class BlogDetailSerialiser(ModelSerializer):
    url = blog_detail_url
    comments = SerializerMethodField()
    class Meta:
        model = blog
        fields = [
            'url',
            'user',
            'blogId',
            'blogTitle',
            'blogContent',
            'bloggedDate',
            'comments'
        ]

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

class BlogCreateUpdateSerialiser(ModelSerializer):
    class Meta:
        model = blog
        fields = [
            'blogTitle',
            'blogContent',
            'bloggedDate',
        ]
