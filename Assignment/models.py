from django.db import models
from django.conf import settings

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    pay_coin = models.IntegerField(default = 0)
    status = models.BooleanField(default=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

class AssignmentUser(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
