
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_note', views.add_note, name='add_note'),
    path('search_note', views.search_note, name='search_note'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
