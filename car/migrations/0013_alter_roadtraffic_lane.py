# Generated by Django 5.0.6 on 2024-07-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_alter_roadtraffic_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadtraffic',
            name='lane',
            field=models.CharField(max_length=100, verbose_name='车道'),
        ),
    ]
