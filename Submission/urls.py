from django.urls import path
from . import views

app_name = 'Submission'

urlpatterns = [
    path('detail/<int:pk>', views.detail, name="detail"),
]