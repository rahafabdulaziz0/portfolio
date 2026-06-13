from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from accounts.models import CustomUser


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirmPassword", "")
        first_name = request.POST.get("firstName", "").strip()
        last_name = request.POST.get("lastName", "").strip()

        if password != confirm_password:
            return render(request, "accounts/signup.html", {"error": "Passwords do not match"})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, "accounts/signup.html", {"error": "Username already taken"})

        if CustomUser.objects.filter(email=email).exists():
            return render(request, "accounts/signup.html", {"error": "Email already registered"})

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        login(request, user)
        return redirect('homepage')

    return render(request, "accounts/signup.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        identifier = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=identifier, password=password)
        if user is None:
            try:
                matched = CustomUser.objects.get(email=identifier)
                user = authenticate(request, username=matched.username, password=password)
            except CustomUser.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'homepage'
            return redirect(next_url)

        return render(request, "accounts/login.html", {"error": "Invalid username/email or password"})

    return render(request, "accounts/login.html", {"next": request.GET.get('next', '')})


def logout_view(request):
    logout(request)
    return redirect('homepage')


# ── Fetch endpoints ──────────────────────────────────────────────────────────

@require_GET
def check_username(request):
    username = request.GET.get("username", "").strip()
    taken = CustomUser.objects.filter(username=username).exists()
    return JsonResponse({"taken": taken})


@require_GET
def check_email(request):
    email = request.GET.get("email", "").strip()
    taken = CustomUser.objects.filter(email=email).exists()
    return JsonResponse({"taken": taken})


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


@login_required
def profile_api(request):
    u = request.user

    if request.method == "GET":
        return JsonResponse({
            "username": u.username,
            "email": u.email,
            "first_name": u.first_name,
            "last_name": u.last_name,
        })

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        password = request.POST.get("password", "")

        if username and username != u.username:
            if CustomUser.objects.filter(username=username).exclude(pk=u.pk).exists():
                return JsonResponse({"error": "Username already taken"}, status=400)
            u.username = username

        if email and email != u.email:
            if CustomUser.objects.filter(email=email).exclude(pk=u.pk).exists():
                return JsonResponse({"error": "Email already registered"}, status=400)
            u.email = email

        u.first_name = first_name
        u.last_name = last_name

        if password:
            u.set_password(password)
            u.save()
            # Keep user logged in after password change
            update_session_auth_hash(request, u)
        else:
            u.save()

        return JsonResponse({"success": True})
