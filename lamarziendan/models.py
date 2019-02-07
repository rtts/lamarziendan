from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from numberedmodel.models import NumberedModel
from embed_video.fields import EmbedVideoField

class Genre(models.Model):
    name = models.CharField('naam', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']

class Artist(models.Model):
    name = models.CharField('naam', max_length=255)
    slug = models.SlugField('URL', unique=True, null=True)
    description = RichTextField('beschrijving', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    links = models.TextField('social media links', help_text='Plak hier per regel één hyperlink', blank=True)

    def get_absolute_url(self):
        if self.slug:
            return reverse('artist', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artiest'
        verbose_name_plural = 'Artiesten'
        ordering = ['name']

class TeamMember(models.Model):
    name = models.CharField('naam', max_length=255)
    slug = models.SlugField('URL', unique=True, null=True)
    description = RichTextField('beschrijving', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    links = models.TextField('social media links', help_text='Plak hier per regel één hyperlink', blank=True)

    def get_absolute_url(self):
        if self.slug:
            return reverse('team', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teamlid'
        verbose_name_plural = 'Teamleden'
        ordering = ['name']

class Edition(models.Model):
    date = models.DateField()
    title = models.CharField('titel', max_length=255)
    slug = models.SlugField('URL', unique=True, null=True)
    concept = models.BooleanField('concept', default=False)
    description = RichTextField('beschrijving', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    photolink = models.URLField('link naar het fotoalbum', blank=True)
    participations = models.ManyToManyField(TeamMember, verbose_name='teamleden', related_name='editions', blank=True)

    def get_absolute_url(self):
        if self.slug:
            return reverse('edition', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Editie'
        verbose_name_plural = 'Edities'
        ordering = ['date']

class Performance(NumberedModel):
    number = models.PositiveIntegerField('nummer', blank=True)
    artist = models.ForeignKey(Artist, verbose_name='artiest', on_delete=models.CASCADE, related_name='performances')
    edition = models.ForeignKey(Edition, verbose_name='editie', on_delete=models.CASCADE, related_name='performances')
    genre = models.ForeignKey(Genre, verbose_name='genre', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)

    def __str__(self):
        return '{} op {}'.format(self.artist, self.edition)

    def number_with_respect_to(self):
        return self.edition.performances.all()

    class Meta:
        verbose_name = 'Optreden'
        verbose_name_plural = 'Optredens'
        ordering = ['number']

class Page(NumberedModel):
    position = models.PositiveIntegerField('positie', blank=True)
    title = models.CharField('titel', max_length=255)
    tagline = models.TextField('tagline', blank=True)
    slug = models.SlugField('URL', help_text='Dit is een korte identifier om te gebruiken in URL’s. Deze moet uniek zijn. Gebruik bij voorkeur alleen kleine letters.', blank=True, unique=True)
    menu = models.BooleanField('zichtbaar in het menu', default=True)

    changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.position, self.title)

    def get_absolute_url(self):
        if self.slug:
            return reverse('page', args=[self.slug])
        else:
            return reverse('homepage')

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Pagina’s'
        ordering = ['position']

SECTION_TYPES = [
    ('normal', 'Normaal'),
    ('banner', 'Banner'),
    ('contact', 'Contactformulier'),
]
class Section(NumberedModel):
    page = models.ForeignKey(Page, verbose_name='pagina', related_name='sections', on_delete=models.CASCADE)
    position = models.PositiveIntegerField('positie', blank=True)
    type = models.CharField('soort sectie', help_text='Het soort sectie bepaalt hoe de sectie wordt weergegeven. Sommige soorten hebben extra functionaliteiten!', max_length=16, default='normal', choices=SECTION_TYPES)
    title = models.CharField('titel', max_length=255)
    content = RichTextField('inhoud', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    video = EmbedVideoField(blank=True, help_text='Plak hier een YouTube, Vimeo, of SoundCloud link')
    button = models.CharField('button', max_length=255, blank=True)
    hyperlink = models.CharField(max_length=255, blank=True)

    def number_with_respect_to(self):
        return self.page.sections.all()

    def __str__(self):
        return '{}. {}'.format(self.position, self.title)

    def get_absolute_url(self):
        return self.page.get_absolute_url()

    class Meta:
        verbose_name = 'sectie'
        ordering = ['page', 'position']

class Config(models.Model):
    TYPES = [
        (20, 'Footer'),
    ]

    parameter = models.PositiveIntegerField(choices=TYPES, unique=True)
    content = RichTextField('Inhoud', blank=True)

    def __str__(self):
        return "{}. {}".format(self.parameter, self.get_parameter_display())

    class Meta:
        verbose_name = 'configuratieparameter'
        ordering = ['parameter']
