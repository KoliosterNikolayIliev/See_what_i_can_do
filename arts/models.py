from django.contrib.auth.models import User
from django.db import models

from accounts.models import UserProfile


class Art(models.Model):
    PIC = 'pic'
    MOD = 'mod'

    ART_TYPES = (
        (PIC, 'Picture'),
        (MOD, 'Model'),

    )

    type = models.CharField(max_length=7, choices=ART_TYPES, default=None)
    name = models.CharField(max_length=6, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='arts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.name}'


class Like(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
