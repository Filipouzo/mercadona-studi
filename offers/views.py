from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryFilterForm, PromotionForm
from .models import Product, Promotion
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
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


def add_promotion(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    existing_promotion = Promotion.objects.filter(product=product).first()

    if existing_promotion:
        messages.error(request, "Une promotion existe déjà pour ce produit.")
        return redirect('offers_list')

    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            if start_date >= end_date:
                messages.error(request, "La date de début doit être antérieure à la date de fin.")
                return render(request, 'offers/add_promotion.html', {'form': form, 'product': product})

            promotion = form.save(commit=False)
            promotion.product = product
            promotion.save()
            return redirect('offers_list')
    else:
        form = PromotionForm()

    return render(request, 'offers/add_promotion.html', {'form': form, 'product': product})


def est_admin(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(est_admin, login_url='/login/')
def page_admin(request):
    return HttpResponse("Bienvenue sur la page réservée aux administrateurs.")
