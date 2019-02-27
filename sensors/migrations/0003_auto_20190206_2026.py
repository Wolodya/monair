# Generated by Django 2.1.4 on 2019-02-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_sensor_pm1'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=11.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=122.2, max_digits=11),
            preserve_default=False,
        ),
    ]