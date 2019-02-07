from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.utils.text import Truncator
from django.utils.safestring import mark_safe
from .models import *

class PerformanceAdmin(admin.StackedInline):
    model = Performance
    extra = 0

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'concept', 'get_description']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PerformanceAdmin]
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    def get_description(self, obj):
        return mark_safe(Truncator(obj.description).words(50, html=True))
    get_description.short_description = 'beschrijving'

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [PerformanceAdmin]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['performances__edition', 'performances__genre']

@admin.register(TeamMember)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ['editions']

class InlineSectionAdmin(admin.StackedInline):
    model = Section
    extra = 0

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['position', 'title']
    list_display_links = ['title']
    inlines = [InlineSectionAdmin]

#@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    save_on_top = True
    list_filter = ['page']
    list_display = ['page', 'position', 'title', 'get_content']
    list_display_links = ['title']

    def get_content(self, obj):
        return mark_safe(Truncator(obj.content).words(50, html=True))
    get_content.short_description = 'inhoud'

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_content']
    exclude = ['parameter']

    def get_content(self, obj):
        return mark_safe(Truncator(obj.content).words(50, html=True))
    get_content.short_description = 'inhoud'
