# blog/models.py
from django.db import models
from django.contrib.auth import get_user_model

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('tech', 'Tech'),
        ('life', 'Life'),
        ('news', 'News'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # Add the profile_picture field
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')  # Add the category field
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    