from django.urls import path

from .views import AQChildViewSet

app_name = 'api'


urlpatterns = [
    path('aq10/child', AQChildViewSet.as_view({'get': 'list', 'post': 'create'}), name='aqchild_view_set'),
]
