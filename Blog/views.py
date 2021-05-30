from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import POST

posts = [
    {
        "author" : "Rushil Desai",
        "title" : "Blog Post 1",
        "content" : "First Post Content",
        "date" : "September 17, 2004"
    },
    {
        "author" : "Jefe Ese",
        "title" : "Blog Post 2",
        "content" : "Second Post Content",
        "date" : "January 1, 2000"
    }
]

def Home(request):
    context = {
        "posts" : POST.objects.all()
    }
    return render(request, "Blog/home.html", context)

class PostView(ListView):
    model = POST
    template_name = 'Blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2

class UserView(ListView):
    model = POST
    template_name = 'Blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return POST.objects.filter(author=user).order_by('-date')

class DetailView(DetailView):
    model = POST

class CreateView(LoginRequiredMixin, CreateView):
    model = POST
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = POST
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = POST
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def About(request):
    return render(request, "Blog/about.html")
