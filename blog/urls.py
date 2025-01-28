from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Home page URL that uses the index view
    path('', views.index, name='blog-home'),
    path('profile/', views.profile, name='profile'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]