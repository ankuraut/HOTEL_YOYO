# Generated by Django 3.1.1 on 2020-09-12 17:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yoyo', '0005_auto_20200912_1852'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookings',
            new_name='Booking',
        ),
        migrations.AlterField(
            model_name='room',
            name='meals',
            field=models.CharField(choices=[('LUC', 'LUNCH'), ('BKFST', 'BREAKFAST'), ('DIN', 'DINNER'), ('NA', 'NOTHING')], default='none', max_length=5),
        ),
        migrations.AlterField(
            model_name='room',
            name='types',
            field=models.CharField(choices=[('QUE', 'QUEEN'), ('XYX', 'COUPLE-FRIENDLY'), ('KIG', 'KING'), ('ACC', 'AC'), ('NAC', 'NON-AC'), ('NOR', 'NORMAL')], max_length=3),
        ),
    ]
