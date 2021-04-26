from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home,name='home'),
    path('projects/(\d+)', projects,name='projects'),
    path('profile/(?P<username>\w+)', profile, name='profile'),
    path('uploads/', post_site,name='post_site'),
    path('api/profiles/', ProfileList.as_view(),name='profile_list'),
    path('api/projects/', ProjectsList.as_view(),name='projects_list'),
    path('search/', search_results, name='search_results'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    