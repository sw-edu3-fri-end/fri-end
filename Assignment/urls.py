from django.urls import path
from . import views

app_name = 'Assignment'

urlpatterns = [
    path('<int:pk>/submit/',views.submit,name="submit"),
    path('<int:pk>/',views.detail,name="detail"),
    path('new/',views.new,name="new"),
    path('',views.index,name="index"),
    ]