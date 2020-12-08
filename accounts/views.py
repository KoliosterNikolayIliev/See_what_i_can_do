from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.forms import SignUpForm, UserProfileForm, ChangeForm
from accounts.models import UserProfile
from items.tools.clean_up import clean_up_files


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

@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    if user != request.user:
        # TODO (404 page)
        return HttpResponse('FORBIDDEN !')
    if request.method == 'GET':
        user = request.user
        form = ChangeForm(instance=user, initial={'user': user})

        context = {
            'form': form,
            'user': user,
        }

        return render(request, 'accounts/edit_user.html', context)
    else:
        user = request.user
        form = ChangeForm(request.POST, request.FILES, instance=user, initial={'user': user})
        if form.is_valid():
            form.save()
            return redirect('user profile', user.pk)

        context = {
            'form': form,
            'user': user,
        }

        return render(request, f'accounts/edit_user.html', context)


@login_required
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    if user != request.user:
        # TODO (404 page)
        return HttpResponse('FORBIDDEN !')
    if request.method == 'GET':
        context = {
            'user': user,
        }

        return render(request, 'accounts/delete_user.html', context)
    else:
        user_image = user.userprofile.profile_picture
        items_images = user.item_set.all()
        if items_images:
            [clean_up_files(x.image.path) for x in items_images]
        if user_image:
            clean_up_files(user_image.path)
        user.delete()
        return redirect('index')
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            pk = user.pk
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user profile', pk)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })