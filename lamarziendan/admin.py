from django.contrib import admin
from django.forms import CheckboxSelectMultiple
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
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PerformanceAdmin]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [PerformanceAdmin]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['performances__edition', 'performances__genre']

@admin.register(TeamMember)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['editions']
