# Generated by Django 5.0.1 on 2024-02-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wsapp', '0003_alter_product_description_pr_alter_product_title_pr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title_pr',
            field=models.CharField(max_length=70, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]