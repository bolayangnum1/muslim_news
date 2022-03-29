from django.urls import path
from .views import CategoryMVC, CafesMVC, RestaurantMVC, MagazineMVC, FastFoodMVC, MosqueCafeDetailView, MosqueCafeListView, MosqueCafeCreateView, MosqueCafeUpdateView, MosqueCafeDeleteView

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
    path('cafes/', CafesMVC.as_view(plural)),
    path('cafes/<int:id>/', CafesMVC.as_view(single)),
    path('restaurants/', RestaurantMVC.as_view(plural)),
    path('restaurants/<int:id>/', RestaurantMVC.as_view(single)),
    path('magazines/', MagazineMVC.as_view(plural)),
    path('magazines/<int:id>/', MagazineMVC.as_view(single)),
    path('fastfoods/', FastFoodMVC.as_view(plural)),
    path('fastfoods/<int:id>/', FastFoodMVC.as_view(single)),

    path('mosquecafe-detail/<int:pk>/', MosqueCafeDetailView.as_view()),
    path('mosquecafe-update/<int:pk>/', MosqueCafeUpdateView.as_view()),
    path('mosquecafe-delete/<int:pk>/', MosqueCafeDeleteView.as_view()),
    path('mosquecafe-create/', MosqueCafeCreateView.as_view()),
    path('mosquecafe-list/', MosqueCafeListView.as_view()),
]
