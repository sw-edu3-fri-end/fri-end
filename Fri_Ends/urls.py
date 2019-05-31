

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('submission/',include('Submission.urls')),
    path('assignment/',include('Assignment.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
