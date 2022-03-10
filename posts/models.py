from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    content = models.TextField(db_column='content', max_length=1000, blank=False)
    timestamp = models.DateTimeField(auto_now_add= True)
    view_count = models.IntegerField(db_column='view_count', default=0)
    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return self.title