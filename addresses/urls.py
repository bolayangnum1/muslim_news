from django.urls import path
from .views import (
    CategoryMVC,
    MosqueMVC,
    MadrasahMVC,
    MosqueRoomMVC,
    MosqueCollegeMVC,
    MosqueUniversityMVC,
    MosqueLibraryMVC, MuslimCreateView,
    MuslimDeleteView,
    MuslimUpdateView,
    MuslimDetailView,
    MuslimListView
)


plural = {
    'get': 'list',
    'post': 'create'
}

single = {
    'get': 'retrieve',
    'delete': 'destroy'
}


urlpatterns = [
    path('categories/', CategoryMVC.as_view(plural)),
    path('categories/<int:id>/', CategoryMVC.as_view(single)),
    path('mosques/', MosqueMVC.as_view(plural)),
    path('mosques/<int:id>/', MosqueMVC.as_view(single)),
    path('mosque_rooms/', MosqueRoomMVC.as_view(plural)),
    path('mosque_rooms/<int:id>/', MosqueRoomMVC.as_view(single)),
    path('mosque_colleges/', MosqueCollegeMVC.as_view(plural)),
    path('mosque_colleges/<int:id>/', MosqueCollegeMVC.as_view(single)),
    path('mosque_universities/', MosqueUniversityMVC.as_view(plural)),
    path('mosque_universities/<int:id>/', MosqueUniversityMVC.as_view(single)),
    path('mosque_libraries/', MosqueLibraryMVC.as_view(plural)),
    path('mosque_libraries/<int:id>/', MosqueLibraryMVC.as_view(single)),
    path('mosque_madrasahs/', MadrasahMVC.as_view(plural)),
    path('mosque_madrasahs/<int:id>/', MadrasahMVC.as_view(single)),

    path('muslim-create/', MuslimCreateView.as_view()),
    path('muslim-list/', MuslimListView.as_view()),
    path('muslim-delete/<int:pk>/', MuslimDeleteView.as_view()),
    path('muslim-update/<int:pk>/', MuslimUpdateView.as_view()),
    path('muslim-detail/<int:pk>/', MuslimDetailView.as_view()),
]