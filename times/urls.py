from django.urls import path
from .views import LocationMVC, TimeMVC


plural = {
    'get': 'list',
    'post': 'create'
}

single = {
    'get': 'retrieve',
    'delete': 'destroy'
}

urlpatterns = [
    path('locations/', LocationMVC.as_view(plural)),
    path('locations/<int:id>/', LocationMVC.as_view(single)),
    path('times/', TimeMVC.as_view(plural)),
    path('times/<slug:date>/', TimeMVC.as_view(single))
]
