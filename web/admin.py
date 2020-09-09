from django.contrib import admin

from web.models import Book


class AdminMode(admin.ModelAdmin):
    list_display = ['story_name', 'author', 'favorite']
    search_fields = ['story_name', 'author']


admin.site.register(Book, AdminMode)
