from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_task, name='delete-task'),
    path('detail/<int:pk>', views.task_content, name='task-content'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('accounts/profile/', views.profile, name='profile'),
]
