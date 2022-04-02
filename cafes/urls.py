from django.urls import path
from .views import CafeCreateView, CafeListView, CafeDeleteView, CafeUpdateView, CafeDetailView,\
    RestaurantCreateView, RestaurantDeleteView, RestaurantListView, RestaurantUpdateView, RestaurantDetailView,\
    MagazineCreateView, MagazineDeleteView, MagazineDetailView, MagazineUpdateView, MagazinListView,\
    FastFoodDeleteView, FastFoodDetailView, FastFoodCreateView, FastFoodUpdateView, FastFoodListView,\
    CategoryCreateView, CategoryDeleteView, CategoryListView, CategoryUpdateView, CategoryDetailView


urlpatterns = [
    path('magazine-create/', MagazineCreateView.as_view()),
    path('magazine-list/', MagazinListView.as_view()),
    path('magazine-detail/<int:pk>/', MagazineDetailView.as_view()),
    path('magazine-update/<int:pk>/', MagazineUpdateView.as_view()),
    path('magazine-delete/<int:pk>/', MagazineDeleteView.as_view()),


    path('cafe-update/<int:pk>/', CafeUpdateView.as_view()),
    path('cafe-delete/<int:pk>/', CafeDeleteView.as_view()),
    path('cafe-detail/<int:pk>/', CafeDetailView.as_view()),
    path('cafe-create/', CafeCreateView.as_view()),
    path('cafe-list/', CafeListView.as_view()),

    path('restaurant-create/', RestaurantCreateView.as_view()),
    path('restaurant-detail/<int:pk>/', RestaurantDetailView.as_view()),
    path('restaurant-update/<int:pk>/', RestaurantUpdateView.as_view()),
    path('restaurant-delete/<int:pk>/', RestaurantDeleteView.as_view()),
    path('restaurant-list/', RestaurantListView.as_view()),

    path('fastfood-create/', FastFoodCreateView.as_view()),
    path('fastfood-list/', FastFoodListView.as_view()),
    path('fastfood-update/<int:pk>/', FastFoodUpdateView.as_view()),
    path('fastfood-detail/<int:pk>/', FastFoodDetailView.as_view()),
    path('fastfood-delete/<int:pk>/', FastFoodDeleteView.as_view()),

    path('category-create', CategoryCreateView.as_view()),
    path('category-list', CategoryListView.as_view()),
    path('category-detail', CategoryDetailView.as_view()),
    path('category-update', CategoryUpdateView.as_view()),
    path('category-delete', CategoryDeleteView.as_view()),
]


