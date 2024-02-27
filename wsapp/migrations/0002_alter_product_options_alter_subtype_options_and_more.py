# Generated by Django 5.0.1 on 2024-02-23 17:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Тур'},
        ),
        migrations.AlterModelOptions(
            name='subtype',
            options={'verbose_name': 'Направление тура', 'verbose_name_plural': 'Направления туров'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип тура', 'verbose_name_plural': 'Типы тура'},
        ),
        migrations.AddField(
            model_name='product',
            name='date_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата тура'),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount_pr',
            field=models.PositiveIntegerField(verbose_name='Количество мест'),
        ),
        migrations.AlterField(
            model_name='subtype',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wsapp.type', verbose_name='Тип тура'),
        ),
    ]