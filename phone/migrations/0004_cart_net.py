# Generated by Django 4.2.10 on 2024-03-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_cart_alter_itemdetails_itemsid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='net',
            field=models.FloatField(null=True),
        ),
    ]