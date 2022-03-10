from django.shortcuts import redirect
from posts.models import Post
from django.http import HttpResponse
import csv
from django.contrib import messages

# Create your views here.
def export(request) :
    
    #Check if method is POST
    if request.method == 'POST':
        data = ''
        if request.POST['orders'] == 'asc' :
            data = 'timestamp'
        elif request.POST['orders'] == 'desc' :
            data = '-timestamp'

        if data :
            response = HttpResponse(content='text/csv')
            response['Content-Disposition'] = 'attachment; filename=posts.csv'
            writer = csv.writer(response)
            writer.writerow(['Title', 'Content', 'Timestamp', 'View Count'])
            posts = Post.objects.all().order_by(data).values_list('title','content', 'timestamp', 'view_count')

            for post in posts:
                writer.writerow(post)
            return response
        else :
            messages.error(request, 'Fail')
            return redirect(request.META['HTTP_REFERER'])

#Check if method is POST
def redirectAdmin(request):
    response = redirect('/admin/')
    return response

def bulkCreatePost(request):
    for x in range(4, 100):
        Post.objects.bulk_create([
            Post(title='title' + str(x), content='content' + str(x))
        ])
    return redirect(request.META['HTTP_REFERER'])
    

    