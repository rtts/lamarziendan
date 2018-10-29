from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from numberedmodel.models import NumberedModel

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
    description = RichTextField('beschrijving', blank=True)
    image = models.ImageField('afbeelding', blank=True)
    photolink = models.URLField('link naar het fotoalbum', blank=True)

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

class Participation(NumberedModel):
    number = models.PositiveIntegerField('nummer', blank=True)
    team_member = models.ForeignKey(TeamMember, verbose_name='teamlid', on_delete=models.CASCADE, related_name='participations')
    edition = models.ForeignKey(Edition, verbose_name='editie', on_delete=models.CASCADE, related_name='participations')

    def __str__(self):
        return '{} hielp mee bij {}'.format(self.team_member, self.edition)

    def number_with_respect_to(self):
        return self.edition.participations.all()

    class Meta:
        verbose_name = 'Participatie'
        verbose_name_plural = 'Participaties'
        ordering = ['number']
