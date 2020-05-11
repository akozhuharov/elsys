from django.shortcuts import get_object_or_404, render

from home.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        obj = Post(title=request.POST.get("title"),
                   text=request.POST.get("text"))
        obj.save()
        return render(request, "success.html")
    return render(request, "create.html")


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "detail.html", context)