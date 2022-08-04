# Generated by Django 4.0.6 on 2022-07-28 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='static/assets/media/adoption/PetBreed')),
            ],
        ),
        migrations.CreateModel(
            name='PetKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='static/assets/media/adoption/PetKind')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('pet_breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adoption.petbreed')),
                ('pet_kind', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adoption.petkind')),
            ],
        ),
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.customer')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adoption.pet')),
            ],
        ),
    ]