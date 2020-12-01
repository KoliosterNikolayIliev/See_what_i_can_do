from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, UserProfileForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    items = user.item_set.all()
    form = UserProfileForm()
    if request.method == 'GET':
        context = {'profile_user': user, 'items': items, 'form': form, }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')
        return redirect('current user profile')


def signup_user(request):
    form = SignUpForm()
    if request.method == 'GET':
        context = {'form': form}

        return render(request, 'registration/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user, )
            profile.save()
            login(request, user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'registration/signup.html', context)
