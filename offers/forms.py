from django import forms
from .models import Product, Category, Promotion


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


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['start_date', 'end_date', 'discount_percentage']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }