# Generated by Django 4.0.6 on 2022-07-28 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_colors_product_settings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='settings',
            field=models.JSONField(blank=True, db_index=True, default=None, null=True),
        ),
    ]
