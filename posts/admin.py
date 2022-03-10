from email.headerregistry import Group
from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'content', 'timestamp', 'view_count')
    exclude = ('view_count',)
    list_filter = ('timestamp', )
    list_per_page = 10
    change_list_template = "admin/posts/post/export.html"

    

admin.site.register(Post, PostAdmin)
admin.site.site_header = 'Admin Panel'

