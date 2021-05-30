from django.urls import path
from .views import PostView, DetailView, CreateView, UpdateView, DeleteView, UserView
from . import views

urlpatterns = [
    path('', PostView.as_view(), name="BlogHome"),
    path('user/<str:username>/', UserView.as_view(), name="BlogUser"),
    path('post/<int:pk>/', DetailView.as_view(), name="BlogPost"),
    path('post/<int:pk>/update/', UpdateView.as_view(), name="BlogUpdate"),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name="BlogDelete"),
    path('create/', CreateView.as_view(), name="BlogCreate"),
    path('about/', views.About, name="BlogAbout")
]