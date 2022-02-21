
from django.urls import path
from project import views

app_name = 'project'


urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
]