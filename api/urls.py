from django.urls import path

from .views import AQChildViewSet, PersonViewSet

app_name = 'api'


urlpatterns = [
    path('aq10/child', AQChildViewSet.as_view({'get': 'list', 'post': 'create'}), name='aqchild_view_set'),
    path('person', PersonViewSet.as_view({'get': 'list', 'post': 'create'}), name='person_view_set'),
]
