
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    error_msg = ""

    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if username == "root" and pwd == "123":
            return redirect("/index")
        else:
            error_msg = "invalid user name or password"
    return render(request, "login.html",{"error_msg":error_msg})


def index(request):
    return render(request, "index.html")