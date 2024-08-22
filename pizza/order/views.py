from django.shortcuts import render, redirect
from pizza.models import PizzaModel
from .forms import CreateForm, CreateOrderModelForm
from .models import OrderModel
from django.forms import modelformset_factory

def create_order(request, *args, **kwargs):
    all_pizza = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)
    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data)['choice']
        new_order = OrderModel.objects.create(addres=address)
        for i in order:
            pizza = PizzaModel.objects.get(pk=i)
            new_order.pizza_order.add(pizza)
        new_order.save()
        return redirect('createorder')
        #pizza_objects = [PizzaModel.objects.get(id-i) for i in order]
        #new_order = OrderModel.objects.create(addres=address)
        #new_order.pizza_order.add(*pizza_objects)
        #new_order.save()

    context = {
        'all_pizza': all_pizza,
        'order_form': order_form,
        }
    return render(request, 'order/create_order.html', context=context)

def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()

    OrderFormSet = modelformset_factory(
        OrderModel,
        form=CreateOrderModelForm,
        extra=2)
    model_form = OrderFormSet(
        request.POST or None,
        queryset=OrderModel.objects.none(),
        initial=[{
            'addres': 'modelformset street',
           
       }])
    #if model_form.is_valid():
    #    model_form.save()
    #    return redirect('createmodelorder')
    #
    context = {
        'pizzas': pizzas,
        'modelform': model_form
    }
    return render(request, 'order/create_model_order.html', context=context)