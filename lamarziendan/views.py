from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, TemplateView
from .models import Edition, Artist, TeamMember, Page, Config
from .forms import SignupForm

def get_config(parameter):
    if parameter not in [t[0] for t in Config.TYPES]:
        raise ValueError('Invalid configuration parameter requested')
    (c, created) = Config.objects.get_or_create(parameter=parameter)
    return c.content

class MenuMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pages = Page.objects.filter(menu=True).exclude(slug='')
        footer = get_config(20)
        context.update({
            'pages': pages,
            'footer': footer,
        })
        return context

class Thanks(MenuMixin, TemplateView):
    template_name = 'thanks.html'

class PageView(MenuMixin, DetailView):
    model = Page
    template_name = 'page.html'

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin:index')

class EditionView(MenuMixin, DetailView):
    template_name = 'edition.html'
    queryset = Edition.objects.exclude(slug=None).exclude(concept=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edition = self.object
        context.update({
            'edition': edition,
        })
        return context

class ArtistView(MenuMixin, DetailView):
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

class TeamView(MenuMixin, DetailView):
    template_name = 'team.html'
    queryset = TeamMember.objects.exclude(slug=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_member = self.object
        context.update({
            'team_member': team_member,
        })
        return context
