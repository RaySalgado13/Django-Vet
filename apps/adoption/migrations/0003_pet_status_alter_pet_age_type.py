# Generated by Django 4.0.6 on 2022-07-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_pet_age_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.CharField(choices=[('type', 'in adoption'), ('type', 'adopted')], default='not specified', max_length=15),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age_type',
            field=models.CharField(choices=[('type', 'years'), ('type', 'months')], default='', max_length=10),
        ),
    ]
