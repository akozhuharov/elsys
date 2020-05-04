from django.shortcuts import render

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