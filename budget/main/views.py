from django.shortcuts import render, redirect, reverse
from main.models import Transaction
from django.views import View
from .forms import AddForm

def index(request, *args, **kwargs):
    qs = Transaction.objects.all()
    return render(request, template_name="pages/home.html", context={"transactions": qs})


class AddView(View):
    template_name = 'pages/add.html'

    def post(self, request, *args, **kwargs):
        tr = Transaction(amount=request.POST.get("amount"),
        type=request.POST.get("type"))
        tr.save()
        return redirect("/")

    def get(self, request, *args, **kwargs):
        form = AddForm()
        return render(request, template_name="pages/add.html",
        context={"form": form})
