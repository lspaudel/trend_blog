## Blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required


def index(request):
    # if request.user.is_authenticated:
    #     # Fetch blogs of the logged-in user
    #     user_blogs = Blog.objects.filter(user=request.user)
    # else:
    #     # Fetch all blogs for non-authenticated users
    #     user_blogs = Blog.objects.all()

    # Pass the blogs to the template
    user_blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'user_blogs': user_blogs})


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # Associate the blog with the logged-in user
            blog.save()
            return redirect('blog:profile')  # Redirect to the user's profile or another page
    else:
        form = BlogForm()

    return render(request, 'blog/create.html', {'form': form})

@login_required
def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.user != blog.user:
        return redirect('blog:blog-home')  # Redirect to home page if user is not the owner
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:profile')  # Redirect to profile page after update
    else:
        form = BlogForm(instance=blog)
    # return render(request, 'blog/blog_form.html', {'form': form})
    return render(request, 'blog/update.html', {'form': form})

@login_required
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.user == blog.user:
        blog.delete()
    return redirect('blog:profile')  

def profile(request):
    user_blogs = Blog.objects.filter(user=request.user)  # Fetch user's blogs
    return render(request, 'blog/profile.html', {'user_blogs': user_blogs})  # Pass blogs to the profile template


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})