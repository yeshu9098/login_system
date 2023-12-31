from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('update/', views.update, name="update"),
    path('logout/', views.log_out, name='logout'),
]