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
        context = {"action": "created"}
        return render(request, "success.html", context)
    return render(request, "create.html")


def detail(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        context = {"action": "deleted"}
        return render(request, "success.html", context)
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "detail.html", context)