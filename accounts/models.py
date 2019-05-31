from django.db import models
from django.conf import settings
# form.profile.user
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=3)
    
    def __str__(self):
        return f'{self.user}님 - 포인트는  : {self.points} '
