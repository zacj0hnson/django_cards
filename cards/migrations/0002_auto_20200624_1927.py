# Generated by Django 3.0.7 on 2020-06-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='suit',
            field=models.CharField(choices=[('diamonds', 'Diamonds'), ('clubs', 'Clubs'), ('spades', 'Spades'), ('hearts', 'Hearts')], max_length=50),
        ),
    ]
