from django.contrib import admin
from .models import *

class PerformanceAdmin(admin.StackedInline):
    model = Performance
    extra = 0

class ParticipationAdmin(admin.StackedInline):
    model = Participation
    extra = 0

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PerformanceAdmin, ParticipationAdmin]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [PerformanceAdmin]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['performances__edition', 'performances__genre']

@admin.register(TeamMember)
class TeamAdmin(admin.ModelAdmin):
    inlines = [ParticipationAdmin]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['participations__edition']
