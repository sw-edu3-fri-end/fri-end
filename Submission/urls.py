from django.urls import path
from . import views

app_name = 'Submission'

urlpatterns = [
    path('',views.index,name="index"),
    ]