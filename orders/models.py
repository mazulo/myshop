from django.db import models

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(
        'primeiro nome',
        max_length=50
    )
    last_name = models.CharField(
        'ultimo nome',
        max_length=50
    )
    email = models.EmailField('email')
    address = models.CharField(
        'endereço',
        max_length=250
    )
    postal_code = models.CharField(
        'código postal',
        max_length=50
    )
    city = models.CharField('cidade', max_length=100)
    created = models.DateField(
        'criado em',
        auto_now_add=True
    )
    updated = models.DateField(
        'atualizado em',
        auto_now=True
    )
    paid = models.BooleanField(
        'está pago?',
        default=False
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        verbose_name='pedido'
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        verbose_name='produto'
    )
    price = models.DecimalField(
        'preço',
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        'quantidade',
        default=1
    )

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
