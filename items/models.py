from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile


class Item(models.Model):
    PIC = 'pic'
    MOD = 'mod'

    ITEM_TYPES = (
        (PIC, 'Picture'),
        (MOD, 'Model'),

    )

    type = models.CharField(max_length=7, choices=ITEM_TYPES, default=None)
    name = models.CharField(max_length=6, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='items')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    #TODO rating here and in the user profile.

    def __str__(self):
        return f'{self.id}; {self.name}'


class Like(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=2)


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)






