
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def login(request):
    error_msg = ""
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        user = models.User.objects.filter(email=email,password=pwd).first()
        if user is not None:
            return redirect("/mainpage")
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


from cmdb import models
def register(request):
    msg = ""
    if request.method == "POST":
        e = request.POST.get("email")
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = {"email":e,"password":p,"username":u}
        models.User.objects.create(**user)
        msg = "Success"
    else:
        msg = "Fail"
    return render(request, "register.html", {"msg":"Success"})