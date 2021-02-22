from django.urls import path

from . import views


urlpatterns = [
    path('profiles', views.ProfileListView.as_view(), name='profile_list'),
    path('profile/<slug:username>', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('resource', views.ResourceListView.as_view(), name='resource_list'),
    # FIXME: below should probably be a slug
    path('resources/<int:resource>', views.ResourceDetailView.as_view(), name='resource_detail'),
]