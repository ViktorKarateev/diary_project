from django.contrib import admin
from .models import Entry, Tag, Mood


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "mood")
    list_filter = ("mood", "created_at")
    search_fields = ("title", "text")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ("emoji", "name")
    search_fields = ("name",)
