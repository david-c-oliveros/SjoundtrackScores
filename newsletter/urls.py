from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user_page"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('newsletter_admin', views.newsletterAdmin, name="newsletter_admin"),
    path('podcast', views.podcast, name="podcast"),
    path('issue/<str:pk>/', views.issue, name="issue"),
    path('issue_admin/<str:pk>/', views.issueAdmin, name="issue_admin"),
    path('episode/<str:pk>/', views.episode, name="episode"),
    path('create_issue/', views.createIssue, name="create_issue"),
    path('edit_issue/<str:pk>/', views.editIssue, name="edit_issue"),
    path('delete_issue/<str:pk>/', views.deleteIssue, name="delete_issue"),

    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
]
