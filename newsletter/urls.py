from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('podcast', views.podcast, name="podcast"),
    path('issue/<str:pk>/', views.issue, name="issue"),
    path('episode/<str:pk>/', views.episode, name="episode")
]
