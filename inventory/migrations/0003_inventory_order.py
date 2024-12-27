# Generated by Django 5.1.4 on 2024-12-24 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_order_packaged_alter_product_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='inventory.order', verbose_name='Orden de compra'),
            preserve_default=False,
        ),
    ]
