# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .forms import BootstrapAuthenticationForm
from cookbook.models import Post, Comment
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.models import User
from django.utils import timezone



class LineChartJSONView(BaseLineChartView):
   
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return  ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь" ]

    def get_providers(self):
        """Return names of datasets."""
        return ["Регистраций", "Постов", "Комментов"]

    def get_data(self):
        t = timezone.localtime(timezone.now())
        i = 1
        regs = []
        posts = []
        comments = []
        while i <= 12:
            regs.append([User.objects.filter(date_joined__month= i).filter(date_joined__year = t.year).count(),])
            posts.append([Post.objects.filter(created_on__month= i).filter(created_on__year = t.year).count()])
            comments.append([Comment.objects.filter(created_on__month= i).filter(created_on__year = t.year).count()])
            i += 1
            # return regs, posts, comments
        """Return 3 datasets to plot."""
        
        
        return regs, posts, comments

line_chart = TemplateView.as_view(template_name='index.html')
# line_chart_json = LineChartJSONView.as_view()

# @login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('lk/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

from .forms import UserAccountCreationForm, ProfileForm, EditUserForm
from .models import Profile


def sign_in(request):
    form = BootstrapAuthenticationForm()
    if request.method == 'POST':
        form = BootstrapAuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse("home")  # TODO: go to profile
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserAccountCreationForm()
    if request.method == 'POST':
        form = UserAccountCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse("home"))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_up_l(request):
    form = UserAccountCreationForm()
    if request.method == 'POST':
        form = UserAccountCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse("home"))  # TODO: go to profile
    return render(request, 'accounts/sign_up_l.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse("home"))


@login_required(login_url="/lk/sign_in/")
def profile(request):
    user = request.user
    posts_count = Post.objects.filter(author=user).count()
    posts = Post.objects.filter(author=user)
    comments = Comment.objects.filter(name=user).count()
    try:
        profile = Profile.objects.get(id=user.id)
    except Profile.DoesNotExist:
        messages.info(request, "Provide more detail about yourself...")
        return HttpResponseRedirect(
            reverse("new_profile")
        )
    return render(request, 'accounts/profile.html', {'profile': profile, 'posts_count': posts_count, 'posts':posts, 'comments': comments})


@login_required(login_url="/accounts/sign_in/")
def new_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data.update(user=user)
            Profile.objects.create(**form.cleaned_data, id=user.id)
            return HttpResponseRedirect(
                reverse("profile")
            )
    else:
        form = ProfileForm()
    return render(request, 'accounts/create_profile.html', {'form': form, 'user': user})


@login_required(login_url="/accounts/sign_in/")
def edit_profile(request):
    user = request.user
    user_data = model_to_dict(
        user,
        fields=['username', 'first_name', 'last_name', 'email', 'verify_email']
    )
    current_profile = Profile.objects.get(user=user)
    profile_data = model_to_dict(
        current_profile, fields=['birth', 'bio', 'avatar']
    )
    if request.method == "POST":
        user_form = EditUserForm(
            request.POST, initial=user_data, instance=user
        )
        profile_form = ProfileForm(
            request.POST, request.FILES,
            initial=profile_data, instance=current_profile
        )
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            if any(data.has_changed() for data in [profile_form, user_form]):
                messages.success(request, "Your profile is updated!")
            else:
                messages.success(request, "No profile changes applied...")
            return HttpResponseRedirect(
                reverse("profile")
            )
    else:
        profile_form = ProfileForm(initial=profile_data)
        user_form = EditUserForm(initial=user_data)
    return render(
        request, 'accounts/edit_profile.html',
        {'profile_form': profile_form,
            'user_form': user_form,
            'username': user}
    )


@login_required(login_url="/accounts/sign_in")
def change_password(request):
    # import pdb; pdb.set_trace()
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            updated_password = form.cleaned_data['new_password2']
            user_identity = [user.first_name, user.last_name, user.username]
            alternative_identities = [name.title() if name.islower() else name.lower() for name in user_identity]
            user_identity.extend(list(alternative_identities))

            if (any(name in updated_password
                    for name in user_identity)):
                messages.info(
                    request,
                    "Password cannot contain: Username; First Name; Last Name"
                )
                return HttpResponseRedirect(
                    reverse(
                        "change_password"
                    )
                )
            else:
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Your password is updated!")
                return HttpResponseRedirect(reverse("home"))
    else:
        form = PasswordChangeForm(user)
    return render(request, 'accounts/change_password.html', {'form': form})