from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_http_methods


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('anasayfa')
        messages.error(request, "Kullanıcı adı veya şifre yanlış!")
    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.warning(request, "Girdiğin şifreler uyuşmuyor!")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Bu kullanıcı adı zaten alınmış!")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Bu e-posta adresi zaten kullanılıyor!")
            return render(request, "register.html")

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.save()
        messages.success(request, "Kayıt başarılı! Giriş yapabilirsin.")
        return redirect("login")
    return render(request, "register.html")


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız.")
    return redirect('login')
