from django.urls import path, include
from .views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView,
    ReviewViewSet,
    ProductWithReviewsAPIView,
    OwnerProductListAPIView,
)

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<int:id>/', ProductDetailAPIView.as_view()),
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),
    path('reviews/', ProductWithReviewsAPIView.as_view()),
    path('my_products/', OwnerProductListAPIView.as_view()),
]