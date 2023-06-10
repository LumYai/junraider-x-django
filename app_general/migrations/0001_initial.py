# Generated by Django 4.2.2 on 2023-06-07 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('status', models.CharField(choices=[('unapproved', 'Unapproved'), ('approved', 'Approved'), ('banned', 'Banned')], default='unapproved', max_length=15)),
                ('register', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
