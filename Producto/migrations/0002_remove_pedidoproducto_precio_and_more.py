# Generated by Django 4.1.2 on 2022-11-13 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='pedidoproducto',
            name='tipo_de_producto',
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='blog_post',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pedidoproducto',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
