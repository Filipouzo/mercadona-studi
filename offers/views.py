from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, CategoryFilterForm
from .models import Product
from django.contrib.auth.decorators import user_passes_test
from django.template.loader import render_to_string
from django.http import JsonResponse


def offers_list(request):
    form = CategoryFilterForm(request.GET)
    queryset = Product.objects.all()

    if form.is_valid():
        category = form.cleaned_data.get('category')
        if category:
            queryset = queryset.filter(category=category)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        # print("C'est une requête AJAX")  # Ajout du point de contrôle
        return render(request, 'offers/product_list_partial.html', {'products': queryset})

    # print("Ce n'est pas une requête AJAX")  # Ajout du point de contrôle
    return render(request, "offers/offers_list.html", {'form': form, 'products': queryset})


def est_admin(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(est_admin, login_url='/login/')
def page_admin(request):
    return HttpResponse("Bienvenue sur la page réservée aux administrateurs.")
