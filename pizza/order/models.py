from django.db import models
from pizza.models import PizzaModel
from django.utils.translation import gettext_lazy as _
# Create your models here.

class OrderModel(models.Model):
    class DeliveryStatus(models.TextChoices):
        PENDING = 'PEN', _('Pending')
        DELIVERED = 'DEL', _('Delivered')
    addres = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)
    delivery_status = models.CharField(
        max_length=3,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING
    )
    
    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'ORDER'

    def all_orders(self):
        return "\n".join([o.name for o in self.pizza_order.all()])

    def __str__(self):
        order_pizza = [i.name for i in self.pizza_order.all()]
        return f'Address: {self.addres}, Order: {", ".join(order_pizza)}'
    
class OrderProxy(OrderModel.pizza_order.through):
    class Meta:
        proxy = True
     
    def __str__(self):
        return str(self.ordermodel)