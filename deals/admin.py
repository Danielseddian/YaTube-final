from django.contrib import admin

from .models import Deal, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "text", "image", "creation_date", "author", "group",)
    search_fields = ("text",)
    list_filter = ("creation_date",)
    empty_value_display = "-пусто-"


admin.site.register(Deal, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk', 'title', 'description', 'slug',)
    search_fields = ("title",)
    empty_value_display = "-пусто-"


admin.site.register(Group, GroupAdmin)
