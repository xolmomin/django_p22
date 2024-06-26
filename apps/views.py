from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from apps.models import Product


# CRUD - Create, Read, Update, Delete
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'apps/product-list.html'
    context_object_name = 'products'


#
# def product_list(request):  # Read
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'apps/product-list.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'apps/product-detail.html'
    context_object_name = 'product'


def product_detail(request, pk):  # Read
    product = get_object_or_404(Product.objects.all(), pk=pk)
    context = {
        'product': product
    }
    return render(request, 'apps/product-detail.html', context)


def product_delete(request, pk):  # Delete
    product = get_object_or_404(Product.objects.all(), pk=pk)
    product.delete()
    return redirect('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'title', 'price', 'discount_price'
    template_name = 'apps/product-update.html'
    success_url = reverse_lazy('product_list')


def product_update(request, pk):  # Delete
    product = get_object_or_404(Product.objects.all(), pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        discount_price = request.POST.get('discount_price')
        product.title = title
        product.price = price
        product.discount_price = discount_price
        product.save()
        return redirect('product_list')

    context = {
        'product': product
    }
    return render(request, 'apps/product-update.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = 'title', 'price', 'discount_price', 'image'
    template_name = 'apps/product-create.html'
    success_url = reverse_lazy('product_list')

def product_create(request):  # Delete
    if request.method == 'POST':
        title = request.POST.get('title')
        price = int(request.POST.get('price'))
        discount_price = int(request.POST.get('discount_price'))
        image = request.FILES.get('image')
        Product(title=title, price=price, discount_price=discount_price, image=image).save()
        # Product.objects.create(title=title, price=price, discount_price=discount_price)
        # data = dict(request.POST)
        # data.pop('csrfmiddlewaretoken')
        # Product(**data).save()
        return redirect('product_list')

    return render(request, 'apps/product-create.html')
