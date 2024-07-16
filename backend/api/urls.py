from django.urls import path
from . import views
from .views import GenerateTeamView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('support/', views.support_view, name='support'),
    path('contact/', views.contact_view, name='contact'),
    path('generate-team/', GenerateTeamView.as_view(), name='generate_team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)