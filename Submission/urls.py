from django.urls import path
from . import views

app_name = 'Submission'

urlpatterns = [
    path('<int:submission_pk>/coaching/', views.create_coaching, name="create_coaching"),
    path('<int:pk>/fail/', views.fail, name="fail"),
    path('<int:pk>/success/', views.success, name="success"),
    path('<int:pk>/', views.detail, name="detail"),
]