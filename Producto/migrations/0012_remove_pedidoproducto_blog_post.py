# Generated by Django 4.1.2 on 2022-11-14 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0011_pedidoproducto_blog_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='blog_post',
        ),
    ]