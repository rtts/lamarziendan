from django.views.generic import DetailView
from .models import Edition, Artist

class EditionView(DetailView):
    template_name = 'edition.html'
    queryset = Edition.objects.exclude(slug=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edition = self.object
        context.update({
            'edition': edition,
        })
        return context

class ArtistView(DetailView):
    template_name = 'artist.html'
    queryset = Artist.objects.exclude(slug=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = self.object
        performances = artist.performances.order_by('edition__date')
        context.update({
            'artist': artist,
            'performances': performances,
        })
        return context
