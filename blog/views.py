## Blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


def index(request):
    """Display all non-deleted blogs"""
    # Blog.objects uses BlogManager which automatically filters out deleted blogs
    user_blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'user_blogs': user_blogs})


@login_required
def create_blog(request):
    """Create a new blog post (login required)"""
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                blog = form.save(commit=False)
                blog.user = request.user
                blog.save()
                messages.success(request, 'Blog post created successfully!')
                logger.info(f'User {request.user.username} created blog: {blog.title}')
                return redirect('blog:profile')
            except Exception as e:
                logger.error(f'Error creating blog: {str(e)}')
                messages.error(request, 'Error creating blog post. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogForm()

    return render(request, 'blog/create.html', {'form': form})


@login_required
def update_blog(request, blog_id):
    """Update a blog post (only by owner)"""
    blog = get_object_or_404(Blog, id=blog_id)
    
    # Permission check: only owner can update
    if request.user != blog.user:
        messages.error(request, 'You do not have permission to edit this blog post.')
        logger.warning(f'User {request.user.username} attempted to edit blog {blog_id} owned by {blog.user.username}')
        return redirect('blog:blog-home')
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Blog post updated successfully!')
                logger.info(f'User {request.user.username} updated blog: {blog.title}')
                return redirect('blog:profile')
            except Exception as e:
                logger.error(f'Error updating blog {blog_id}: {str(e)}')
                messages.error(request, 'Error updating blog post. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'blog/update.html', {'form': form})


@login_required
def delete_blog(request, blog_id):
    """Soft delete a blog post (only by owner)"""
    blog = get_object_or_404(Blog, id=blog_id)
    
    # Permission check: only owner can delete
    if request.user == blog.user:
        blog.soft_delete()
        messages.success(request, 'Blog post deleted successfully!')
        logger.info(f'User {request.user.username} deleted blog: {blog.title} (ID: {blog_id})')
    else:
        messages.error(request, 'You do not have permission to delete this blog post.')
        logger.warning(f'User {request.user.username} attempted to delete blog {blog_id} owned by {blog.user.username}')
    
    return redirect('blog:profile')


@login_required
def profile(request):
    """Display user's own blog posts"""
    user_blogs = Blog.objects.filter(user=request.user)
    return render(request, 'blog/profile.html', {'user_blogs': user_blogs})


def blog_detail(request, blog_id):
    """Display a single blog post"""
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})