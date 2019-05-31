from django.urls import path
from . import views

app_name = 'Submission'

urlpatterns = [
    path('<int:pk>/fail', views.fail, name="fail"),
    path('<int:pk>/success', views.success, name="success"),
    path('<int:pk>', views.detail, name="detail"),
]