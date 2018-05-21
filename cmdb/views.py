
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


USER_LIST = [
    {"name":"Alex","email":"Alex@qq.com"},
    {"name":"Dean","email":"Dean@163.com"},
    {"name":"Paul","email":"Paul@baidu.com"}
             ]
def userManager(request):
    if request.method == "POST":
        u = request.POST.get("username")
        e = request.POST.get("email")
        user = {"name":u,"email":e}
        USER_LIST.append(user)
    return render(request, "user.html", {"userlist": USER_LIST})