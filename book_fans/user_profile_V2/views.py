from django.contrib import messages
from django.contrib.auth import get_user_model  
from bookclub.models import Review
from user_profile_V2.models import Comment
from .models import UserProfileV2
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.views import generic
from . import forms, models


class CommentListView(generic.ListView):
    model = models.Comment
    template_name = 'bookclub/comment_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Comment.objects.all()

def signup(request):
    if request.method == 'POST':
        user_form = forms.CreateUserForm(request.POST)
        profile_form = forms.ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            UserProfileV2.objects.create(
                user=new_user,
                picture=profile_form.cleaned_data['picture']
            )
            messages.success(request, _("Thank you! You can log in now with your credentials."))
            return redirect('login')
    else:
        user_form = forms.CreateUserForm()
        profile_form = forms.ProfileForm()
    return render(request, 'user_profile_V2/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def user_profile(request):
    profile, created = UserProfileV2.objects.get_or_create(user=request.user)
    return render(request, 'user_profile_V2/user_profile.html', {
        'user': request.user,
        'profile': profile,
        'user_reviews': Review.objects.filter(user=request.user),
        'user_comments': Comment.objects.filter(user=request.user)
    })

@login_required
def user_update(request):
    profile, created = UserProfileV2.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("user_profile")
    else:
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=profile)
    return render(request, "user_profile_V2/user_update.html", {
    "user_form": user_form,
    "profile_form": profile_form,
    "user_reviews": Review.objects.filter(user=request.user),
    "user_comments": Comment.objects.filter(user=request.user)
})

@login_required
def user_delete(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("index")  
    return render(request, "user_profile_V2/user_delete.html")

@login_required
def comment_create(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('review_detail', pk=review_id)
    else:
        form = forms.CommentForm()
    return render(request, "user_profile_V2/comment_create.html", {'form': form, 'review': review})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, _('Comment has been deleted.'))
        return redirect('kur_norite_nukreipti_po_istrynimo')
    return render(request, 'comment_confirm_delete.html', {'comment': comment})
