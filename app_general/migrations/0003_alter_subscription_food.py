# Generated by Django 4.2.2 on 2023-06-07 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0002_food_description_food_special_price_and_more'),
        ('app_general', '0002_subscription_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_foods.food'),
        ),
    ]
