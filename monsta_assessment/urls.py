from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'index'),
    path('export/', views.export,name = 'export'),
    path('bulk/', views.bulkCreatePost,name = 'bulk'),
    path('', views.redirectAdmin,name = 'redirect'),
]
