from django.contrib import messages
from django.contrib.auth import get_user_model  
from bookclub.models import Review
from user_profile_V2.models import Comment
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


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Thank you! You can log in now with your credentials."))
            return redirect("login")
    else:
        form = forms.CreateUserForm()
    return render(request, 'user_profile_V2/signup.html', {
        'form': form,
    })

@login_required
def user_detail(request: HttpRequest, username: str | None = None) -> HttpResponse:
    user = request.user if not username else get_object_or_404(get_user_model(), username=username)  
    return render(request, 'user_profileV_2/user_detail.html', {
        'object': user,
    })

@login_required
def user_update(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST, instance=request.user.userprofilev2)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("user_detail")
    else:
        form = forms.ProfileForm(instance=request.user.userprofilev2)
    return render(request, "user_profile_V2/user_update.html", {"form": form})

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
