from django.contrib import admin
from .models import SiteContent

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('section', 'key', 'content_type', 'value', 'image')
    search_fields = ('section', 'key', 'content_type')
    list_filter = ('section', 'content_type')
