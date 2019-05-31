from django.db import models

# Create your models here.
import Assignment

def submission_image_path(instance, filename):
    return f'submission/{filename}'

class Submission(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = submission_image_path, null=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Coaching(models.Model):
    content = models.TextField()
    # writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(User, related_name='like_coachings', blank=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.submission.title} - {self.pk}] {self.content}'