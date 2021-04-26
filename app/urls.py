from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('^$',views.home,name='home'),
    path(r'^projects/(\d+)',views.projects,name='projects'),
    path(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    path('^uploads/',views.post_site,name='post_site'),
    path(r'^api/profiles/$', views.ProfileList.as_view(),name='profile_list'),
    path(r'^api/projects/$', views.ProjectsList.as_view(),name='projects_list'),
    path(r'^search/', views.search_results, name='search_results'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    