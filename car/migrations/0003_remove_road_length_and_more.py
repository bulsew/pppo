# Generated by Django 5.0.6 on 2024-07-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_remove_trafficpredictionresult_image_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='road',
            name='length',
        ),
        migrations.RemoveField(
            model_name='trafficpredictionresult',
            name='image',
        ),
        migrations.RemoveField(
            model_name='trafficpredictionresult',
            name='predicted_traffic_volume',
        ),
        migrations.RemoveField(
            model_name='trafficpredictionresult',
            name='time',
        ),
        migrations.AddField(
            model_name='road',
            name='latitude',
            field=models.FloatField(default=0.0, verbose_name='纬度'),
        ),
        migrations.AddField(
            model_name='road',
            name='longitude',
            field=models.FloatField(default=0.0, verbose_name='经度'),
        ),
        migrations.AddField(
            model_name='road',
            name='prediction_image',
            field=models.ImageField(blank=True, null=True, upload_to='results/', verbose_name='预测图片'),
        ),
        migrations.AddField(
            model_name='trafficpredictionresult',
            name='green_light',
            field=models.IntegerField(default=0, verbose_name='绿灯时间'),
        ),
        migrations.AddField(
            model_name='trafficpredictionresult',
            name='red_light',
            field=models.IntegerField(default=0, verbose_name='红灯时间'),
        ),
        migrations.AddField(
            model_name='trafficpredictionresult',
            name='traffic_flow_prediction',
            field=models.FloatField(default=0.0, verbose_name='预测结果'),
        ),
    ]