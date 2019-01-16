from django.contrib import admin
from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    search_fields = ['title']

    class Meta:
        model = models.Post


admin.site.register(models.Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', "date"]
    search_fields = ['author', 'text', 'date']

    class Meta:
        model = models.Comment


admin.site.register(models.Comment, CommentAdmin)
