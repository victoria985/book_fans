from django.contrib import messages
from django.contrib.auth import get_user_model  # Pakeičiame User į get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from . import forms

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you! You can log in now with your credentials."))
            return redirect("login")
    else:
        form = forms.CreateUserForm()
    return render(request, 'user_profile/signup.html', {
        'form': form,
    })

@login_required
def user_detail(request: HttpRequest, username: str | None = None) -> HttpResponse:
    user = request.user if not username else get_object_or_404(get_user_model(), username=username)  # Pakeičiame User į get_user_model()
    return render(request, 'user_profile/user_detail.html', {
        'object': user,
    })

@login_required
def user_update(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("user_detail")
    else:
        form = forms.ProfileForm(instance=request.user.userprofile)
    return render(request, "user_profile/user_update.html", {"form": form})

@login_required
def user_delete(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("index")  # Redirect to the homepage after deletion
    return render(request, "user_profile/user_delete.html")

