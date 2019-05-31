from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=3)
    
    def __str__(self):
        return f'{self.user}님 - 포인트는  : {self.points} '
