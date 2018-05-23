
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    error_msg = ""

    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("email")
        pwd = request.POST.get("password")
        if username == "root" and pwd == "123":
            return redirect("/index")
        else:
            error_msg = "invalid user name or password"
    return render(request, "login.html",{"error_msg":error_msg})


def mainpage(request):
    return render(request, "mainpage.html")


USER_LIST = [
    {"password":"Alex","email":"Alex@qq.com"},
    {"password":"Dean","email":"Dean@163.com"},
    {"password":"Paul","email":"Paul@baidu.com"}
             ]
def userManager(request):
    if request.method == "POST":
        u = request.POST.get("email")
        e = request.POST.get("password")
        user = {"password":u,"email":e}
        USER_LIST.append(user)
    return render(request, "user.html", {"userlist": USER_LIST})