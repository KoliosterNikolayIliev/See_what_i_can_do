from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile


class Item(models.Model):

    ITEM_TYPES = (
        ('pic', 'Picture'),
        ('mod', 'Hand-made model'),

    )

    CATEGORY_TYPES = (
        ('nat', 'Nature'),
        ('fam', 'Family'),
        ('ani', 'Animals'),
        ('christ', 'Christmas'),
        ('east', 'Easter'),
        ('city', 'City'),
        ('fun', 'Fun'),
        ('other', 'Other'),

    )

    type = models.CharField(max_length=7, choices=ITEM_TYPES, default=None)
    category = models.CharField(max_length=20, choices=CATEGORY_TYPES, default='other', null=True)
    name = models.CharField(max_length=6, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='items')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    #TODO rating here and in the user profile.

    def __str__(self):
        return f'{self.id}; {self.name}; {self.date_created};'


class Like(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=2)


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)






