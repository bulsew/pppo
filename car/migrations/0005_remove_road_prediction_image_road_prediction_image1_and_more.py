# Generated by Django 5.0.6 on 2024-07-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_remove_road_connected_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='road',
            name='prediction_image',
        ),
        migrations.AddField(
            model_name='road',
            name='prediction_image1',
            field=models.ImageField(blank=True, null=True, upload_to='results/', verbose_name='预测图片1'),
        ),
        migrations.AddField(
            model_name='road',
            name='prediction_image2',
            field=models.ImageField(blank=True, null=True, upload_to='results/', verbose_name='预测图片2'),
        ),
    ]
