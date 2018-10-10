from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Product, SubCategory, Category
from django.urls import reverse_lazy



# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'category', 'subcategory')
    success_url = reverse_lazy('product_changelist')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name','category','subcategory')
    success_url = reverse_lazy('product_changelist')

def load_product(request):
    category_id = request.GET.get('category')
    subcategory = SubCategory.objects.filter(category_id=category_id).order_by('name')
    return render(request,'app/subcategory_dropdown_list.html',{'subcategory':subcategory})
