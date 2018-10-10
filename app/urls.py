from django.urls import path
from . import views

urlpatterns=[
    path('', views.ProductListView.as_view(), name='product_changelist'),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('ajax/load-product/', views.load_product, name='ajax_load_product'),
    path('<int:pk>/',views.ProductUpdateView.as_view(), name='product_change'),
    # path('caty/products/', views.CategoryProducts.as_view(), name='category-products'),

]