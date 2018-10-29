from django.views.generic import DetailView
from .models import Edition

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
