

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< Updated upstream
    path('submission/',include('Submission.urls')),
    path('assignment/',include('Assignment.urls')),
=======
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('Assignment/', include('Assignment.urls')),
>>>>>>> Stashed changes
    path('admin/', admin.site.urls),
]
