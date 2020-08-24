from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/', views.PostRedirectDetailView.as_view(), name='redirect'),
    path('<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]
