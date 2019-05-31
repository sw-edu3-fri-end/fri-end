from django.contrib import admin

from .models import Submission

class SubmissionAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'status', 'created_at', 'updated_at']

admin.site.register(Submission, SubmissionAdmin)
