from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView
from .models import Edition, Artist, TeamMember
from .forms import SignupForm

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin:index')

class EditionView(DetailView):
    template_name = 'edition.html'
    queryset = Edition.objects.exclude(slug=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edition = self.object
        participations = edition.participations.order_by('team_member__name')
        context.update({
            'edition': edition,
            'participations': participations
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

class TeamView(DetailView):
    template_name = 'team.html'
    queryset = TeamMember.objects.exclude(slug=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_member = self.object
        participations = team_member.participations.order_by('edition__date')
        context.update({
            'team_member': team_member,
            'participations': participations,
        })
        return context
