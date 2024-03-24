# Generated by Django 3.2.12 on 2024-03-10 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metro_station', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=120)),
                ('building_number', models.CharField(max_length=120)),
                ('floors_in_house', models.PositiveSmallIntegerField()),
                ('floor', models.PositiveSmallIntegerField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('area_of_premise', models.PositiveSmallIntegerField()),
                ('type_of_deal', models.CharField(choices=[('rent', 'rent'), ('sale', 'sale')], default='sale', max_length=100)),
                ('bathroom', models.CharField(choices=[('combined', 'combined'), ('separate', 'separate'), ('several', 'several')], default='combined', max_length=100)),
                ('balcony', models.BooleanField(default=False)),
                ('title_photo', models.ImageField(null=True, upload_to='media/photos')),
                ('city_district', models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='real_estate.citydistrict')),
                ('metro', models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='real_estate.metro')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/photos')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate.realestate')),
            ],
        ),
        migrations.CreateModel(
            name='DealRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggest_text', models.TextField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate.realestate')),
            ],
        ),
    ]
