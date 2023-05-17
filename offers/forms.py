from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']


class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Catégorie"
    )
