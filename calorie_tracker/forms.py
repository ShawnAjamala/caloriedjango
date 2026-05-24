from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calories']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'e.g., Apple'}),
            'calories': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Calories'}),
        }