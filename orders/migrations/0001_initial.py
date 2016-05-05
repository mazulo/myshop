# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='primeiro nome', max_length=50)),
                ('last_name', models.CharField(verbose_name='ultimo nome', max_length=50)),
                ('email', models.EmailField(verbose_name='email', max_length=254)),
                ('address', models.CharField(verbose_name='endereço', max_length=250)),
                ('postal_code', models.CharField(verbose_name='código postal', max_length=50)),
                ('city', models.CharField(verbose_name='cidade', max_length=100)),
                ('created', models.DateField(auto_now_add=True, verbose_name='criado em')),
                ('update', models.DateField(auto_now=True, verbose_name='atualizado em')),
                ('paid', models.BooleanField(verbose_name='está pago?', default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('price', models.DecimalField(max_digits=10, verbose_name='preço', decimal_places=2)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantidade', default=1)),
                ('order', models.ForeignKey(to='orders.Order', verbose_name='pedido', related_name='items')),
                ('product', models.ForeignKey(to='shop.Product', verbose_name='produto', related_name='order_items')),
            ],
        ),
    ]
