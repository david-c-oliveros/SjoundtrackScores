from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('podcast', views.podcast, name="podcast"),
    path('issue/<str:pk>/', views.issue, name="issue"),
    path('episode/<str:pk>/', views.episode, name="episode"),
    path('create_issue/', views.createIssue, name="create_issue"),
    path('edit_issue/<str:pk>/', views.editIssue, name="edit_issue"),
    path('delete_issue/<str:pk>/', views.deleteIssue, name="delete_issue"),
]
