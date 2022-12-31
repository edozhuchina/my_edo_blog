from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用！")

def adduser(request):
    return HttpResponse("增加用户！")

def user_list(request):
    # 1.优先去项目的根目录的templates中寻找（提前配置）
    # 2.再去blog应用目录下的templates目录寻找“user_list.html”(根据app的注册顺序，逐一去它们的templates目录中找)
    return render(request, "user_list.html")