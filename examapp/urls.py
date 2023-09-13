from . import views
from django.urls import path

app_name = 'examapp'
urlpatterns = [
    path('', views.index, name='index'),    
    path('home', views.home, name='home'),
    path('login_user', views.login_user, name='login_user'),
    path('register_user', views.register_user, name='register_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add_question', views.add_question, name='add_question'),
    path('exam', views.exam, name='exam'),
    path('result', views.result, name='result'),
]
