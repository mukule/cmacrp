from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'company')
    list_filter = ('company__business', 'company')
    search_fields = ('file', 'company__name', 'company__business__name')

admin.site.register(Document, DocumentAdmin)
