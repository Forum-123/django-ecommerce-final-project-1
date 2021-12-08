# Generated by Django 4.0 on 2021-12-07 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_basket'),
        ('communities', '0004_merge_0002_initial_0003_alter_product_sold_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='basket_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.basket'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name=''),
        ),
    ]
