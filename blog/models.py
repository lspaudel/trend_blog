# blog/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import logging

logger = logging.getLogger(__name__)


class BlogManager(models.Manager):
    """Custom manager to filter out soft-deleted blogs by default"""
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('tech', 'Tech'),
        ('life', 'Life'),
        ('news', 'News'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=275, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete
    
    # Managers
    objects = BlogManager()  # Default manager excludes deleted blogs
    all_objects = models.Manager()  # Manager that includes deleted blogs
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['category']),
            models.Index(fields=['user', '-created_at']),
        ]
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<Blog: {self.title} by {self.user.username}>'
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from title if not provided"""
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Ensure unique slug
            while Blog.all_objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        
        logger.info(f'Saving blog: {self.title} (ID: {self.pk or "new"})')
        super().save(*args, **kwargs)
    
    def soft_delete(self):
        """Soft delete the blog post"""
        self.is_deleted = True
        self.save()
        logger.info(f'Soft deleted blog: {self.title} (ID: {self.pk})')
    
    def restore(self):
        """Restore a soft-deleted blog post"""
        self.is_deleted = False
        self.save()
        logger.info(f'Restored blog: {self.title} (ID: {self.pk})')
    