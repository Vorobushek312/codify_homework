from django.db import models
from datetime import datetime
def article_directory_path(instance, filename):
    return 'blog/static/images/article/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'), filename)
# Create your models here.

class Create(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=2000)
    upload_image = models.ImageField(upload_to=article_directory_path, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
