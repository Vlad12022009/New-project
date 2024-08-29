from django.shortcuts import render

from .models import PizzaModel
# Create your views here.

def pizza_detail_view(request, *args, **kwargs):
    pizza_object = PizzaModel.objects.get(name_slug=kwargs.get('slug'))
    contex = {
        'pizza_object': pizza_object,
              }
    return render(request, 'pizza/pizza_detail.html', context=contex)