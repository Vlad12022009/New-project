from django import forms
from pizza.models import PizzaModel
from .models import OrderModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button, ButtonHolder, Field


PIZZAS = [
    (f'{p.id}', f'{p.name}') for p in PizzaModel.objects.all()
]
DEL_STATUS = [('PEN','Pending'), ('DEL', 'Delivered')]
class CreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('address'),
            Field('choice'),
            Field('delivery_status'),
            ButtonHolder(
                Submit('order', 'Order', css_class='btn btn-danger')
            )
        )
    
    address = forms.CharField(required=True)
    choice = forms.ChoiceField(choices=PIZZAS,
                               help_text='If you want some extra. Send us <a href="#">message</a>',
                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'pizzas'}))
    delivery_status = forms.ChoiceField(
        choices=DEL_STATUS
    )

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