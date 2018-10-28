from django.contrib import admin
from .models import *

class PerformanceAdmin(admin.StackedInline):
    model = Performance
    extra = 0

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    inlines = [PerformanceAdmin]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [PerformanceAdmin]
