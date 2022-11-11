# Generated by Django 4.0.6 on 2022-11-09 21:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/assets/media/home/HomeSlide')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='static/assets/media/home/Logos')),
                ('whatsapp_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('facebook_url', models.URLField(blank=True, max_length=250)),
                ('products_image', models.ImageField(upload_to='static/assets/media/home/HomeImages')),
                ('services_image', models.ImageField(upload_to='static/assets/media/home/HomeImages')),
                ('adoption_image', models.ImageField(upload_to='static/assets/media/home/HomeImages')),
                ('slides', models.ManyToManyField(to='home.homeslide')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
