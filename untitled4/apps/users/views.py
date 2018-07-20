from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username or username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
def login(request):
    if request.method == "POST":
        user_name = request.POST.get("Username","")
        pass_word = request.POST.get("Password","")
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/',{user:user})
            #return render(request,"index.html")
        else:
            return render(request,"login.html",{"msg":"用户名或密码错误"})

    elif request.method == "GET":
        return render(request,"login.html",{})