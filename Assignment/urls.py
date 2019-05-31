from django.urls import path
from . import views

app_name = 'Assignment'

urlpatterns = [
    path('',views.index,name="index"),
    ]