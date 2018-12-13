from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.http import Http404
from .views import EditionView, ArtistView, TeamView, SignupView
from .models import Edition

def latest_edition(request):
    latest_edition = Edition.objects.exclude(slug=None, concept=True).last()
    if latest_edition:
        return redirect(latest_edition)
    else:
        raise Http404

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('', latest_edition),
    path('editie/<slug:slug>/', EditionView.as_view(), name='edition'),
    path('artiest/<slug:slug>/', ArtistView.as_view(), name='artist'),
    path('team/<slug:slug>/', TeamView.as_view(), name='team'),
    path('aanmelden/', SignupView.as_view(), name='signup'),
    path('admin/', admin.site.urls),
]
