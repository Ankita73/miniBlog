from django.db import models
from django.conf import settings

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

# Create your models here.
class blog(models.Model):
    blogId = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    blogTitle = models.CharField(max_length=60)
    blogContent = models.CharField(max_length=140)
    bloggedDate = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'blog'


    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type