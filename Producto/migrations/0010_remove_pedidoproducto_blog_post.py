# Generated by Django 4.1.2 on 2022-11-14 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0009_pedidoproducto_resumen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='blog_post',
        ),
    ]
