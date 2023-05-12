from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, CategoryFilterForm
from .models import Product
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


# A supprimer ?
# def base(request):
#     return render(request, "offers/base.html")


def offers_list(request):
    form = CategoryFilterForm(request.GET)
    queryset = Product.objects.all()

    if form.is_valid():
        category = form.cleaned_data.get('category')
        if category:
            queryset = queryset.filter(category=category)

    return render(request, "offers/offers_list.html", {'form': form, 'products': queryset})


def est_admin(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(est_admin, login_url='/login/')
def page_admin(request):
    return HttpResponse("Bienvenue sur la page réservée aux administrateurs.")


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('offers_list')
    else:
        form = ProductForm()
    return render(request, 'offers/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('offers_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'offers/product_form.html', {'form': form})
