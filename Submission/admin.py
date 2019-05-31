from django.contrib import admin

from .models import Submission, Coaching

class SubmissionAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'content', 'status', 'created_at', 'updated_at']

class CoachingAdmin(admin.ModelAdmin):
    fields = ['content', 'submission', 'created_at', 'updated_at']

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Coaching, CoachingAdmin)
