# Generated by Django 4.2.2 on 2023-06-07 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0002_food_description_food_special_price_and_more'),
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='food',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_foods.food'),
        ),
    ]
