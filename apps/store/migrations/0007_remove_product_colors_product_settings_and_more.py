# Generated by Django 4.0.6 on 2022-07-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.AddField(
            model_name='product',
            name='settings',
            field=models.JSONField(db_index=True, default=None),
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
    ]