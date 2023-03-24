from django.contrib import admin
from .models import Document, Image


class DocumentAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'number', 'dateCreate']
    list_display = ['title', 'category', 'number', 'dateCreate']


class ImageAdmin(admin.ModelAdmin):
    fields = ['file']
    list_display = ['file']
  
    
    

admin.site.register(Document, DocumentAdmin)
admin.site.register(Image, ImageAdmin)
