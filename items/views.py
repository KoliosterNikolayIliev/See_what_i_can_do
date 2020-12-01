from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from items.forms import CommentForm, ItemForm
from items.tools.clean_up import clean_up_files

from items.models import Item, Like, Comment


def index(request):
    return render(request, 'index.html')

def list_items(request):
    return render(request, 'item_list.html')


def list_pics(request):
    pics = Item.objects.filter(type='pic')
    context = {
        'pics': pics,
    }

    return render(request, 'pic_list.html', context)


def list_mods(request):
    mods = Item.objects.filter(type='mod')
    context = {
        'mods': mods,
    }

    return render(request, 'mod_list.html', context)


def details_or_comment_art(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'item': item,
            'form': CommentForm(),
            'can_delete': request.user == item.user,
            'can_edit': request.user == item.user,
            'can_like': request.user != item.user,
            'can_comment': request.user != item.user,
            'has_liked': item.like_set.filter(user_id=request.user.id).exists(),
        }

        return render(request, 'detail.html', context)
    else:
        if item.user == request.user:
            #TODO (404 page)
            return HttpResponse('FORBIDDEN !')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.user = request.user
            comment.item = item
            comment.save()
            return redirect('details or comment', pk)
        context = {
            'item': item,
            'form': form,

        }

        return render(request, 'detail.html', context)


def influence_item(request, item, template_name):
    if request.method == 'GET':
        user = request.user
        form = ItemForm(instance=item, initial={'user': user})
        form.fields['user'].widget = forms.HiddenInput()

        context = {
            'form': form,
            'item': item,
        }

        return render(request, f'{template_name}.html', context)
    else:
        old_image = item.image
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            likes = Like.objects.filter(item_id=item.pk)
            likes.delete()
            if old_image:
                clean_up_files(old_image.path)
            return redirect('details or comment', item.pk)

        context = {
            'form': form,
            'item': item,
        }

        return render(request, f'{template_name}.html', context)


# @user_required(Item, methods=['GET'])
def edit(request, pk):
    item = Item.objects.get(pk=pk)
    if item.user != request.user:
        # TODO (404 page)
        return HttpResponse('FORBIDDEN !')
    return influence_item(request, item, 'edit')


@login_required
def create(request):
    item = Item()
    return influence_item(request, item, 'create')


@login_required
def delete(request, pk):
    item = Item.objects.get(pk=pk)
    if item.user != request.user:
        # TODO (404 page)
        return HttpResponse('FORBIDDEN !')
    if request.method == 'GET':
        context = {
            'item': item,
        }

        return render(request, 'delete.html', context)
    else:
        item.delete()
        return redirect('list items')


@login_required
def like_item(request, pk):
    item = Item.objects.get(pk=pk)
    likes = item.like_set.filter(user_id=request.user.id)
    like = Like(value=str(pk))
    if likes.exists():
        likes.delete()
    else:
        like.item = item
        like.user = request.user
        like.save()
    return redirect('details or comment', pk)

