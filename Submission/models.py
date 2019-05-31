from django.db import models

# Create your models here.
import Assignment

class Submission(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'