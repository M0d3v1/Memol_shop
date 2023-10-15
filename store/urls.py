from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]
