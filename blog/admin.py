from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('category', 'created_at', 'is_deleted')
    search_fields = ('title', 'content', 'user__username')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'title', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('content', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'is_deleted'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['soft_delete_selected', 'restore_selected']
    
    def soft_delete_selected(self, request, queryset):
        """Soft delete selected blogs"""
        for blog in queryset:
            blog.soft_delete()
        self.message_user(request, f'{queryset.count()} blog(s) soft deleted.')
    soft_delete_selected.short_description = 'Soft delete selected blogs'
    
    def restore_selected(self, request, queryset):
        """Restore selected blogs"""
        for blog in queryset:
            blog.restore()
        self.message_user(request, f'{queryset.count()} blog(s) restored.')
    restore_selected.short_description = 'Restore selected blogs'

