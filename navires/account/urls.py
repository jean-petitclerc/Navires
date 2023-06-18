from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register_account, name='register_account'),
    path('logout/', views.logout_account, name='logout'),
    path('login/', views.login_account, name='login'),
]
