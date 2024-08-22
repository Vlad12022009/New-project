from django import forms
from pizza.models import PizzaModel
from .models import OrderModel

PIZZAS = [
    (f'{p.id}', f'{p.name}') for p in PizzaModel.objects.all()
]

class CreateForm(forms.Form):
    address = forms.CharField()
    choice = forms.ChoiceField(choices=PIZZAS,
                               help_text='If you want some extra. Send us <a href="#">message</a>',
                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'pizzas'}))

class CreateOrderModelForm(forms.ModelForm):
    error_css_class = 'error-field-class'
    required_css_class = 'required-field-class'
    class Meta:
        model = OrderModel
        fields = ['addres', 'pizza_order']
        widgets = {
            'addres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address'
            }),
            'pizza_order': forms.CheckboxSelectMultiple()
            #'pizza_order': forms.Select(choices=PIZZAS)
        }