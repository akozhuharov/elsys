from django.shortcuts import render

from home.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


def create(request):
    data = request.POST
    obj = Post(data)
    obj.save()
    return obj