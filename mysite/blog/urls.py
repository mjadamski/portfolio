from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),

#    path('post/', views.post, name='post'),
    #path('post_list', views.post_list, name='post_list'),

    path('post_new/', views.post_new, name='post_new'),

    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),


]
