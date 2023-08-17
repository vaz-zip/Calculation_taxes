from django.contrib import admin
from .models import Document, Image


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'category', 'number', 'dateCreate']
    list_display = ['title', 'slug', 'category', 'number', 'dateCreate']
    list_filter = ['title', 'category', 'dateCreate']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'dateCreate'
    ordering = 'dateCreate', 'category'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['file']
    list_display = ['file']
  
    
    

# admin.site.register(Document, DocumentAdmin)
# admin.site.register(Image, ImageAdmin)
