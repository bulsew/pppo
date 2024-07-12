# Generated by Django 5.0.6 on 2024-07-05 14:53

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='道路id')),
                ('name', models.CharField(max_length=100, verbose_name='道路名')),
                ('information', models.TextField(verbose_name='道路信息')),
                ('length', models.FloatField(verbose_name='道路长度')),
                ('connected_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='car.road', verbose_name='相连道路')),
            ],
            options={
                'verbose_name': '道路信息',
                'verbose_name_plural': '道路信息',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalPrediction',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='历史记录id')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('red_prediction', models.CharField(blank=True, help_text='历史预测结果（红灯）', max_length=10)),
                ('green_prediction', models.CharField(blank=True, help_text='历史预测结果（绿灯）', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_predictions', to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_predictions', to='car.road', verbose_name='道路id')),
            ],
            options={
                'verbose_name': '历史预测记录',
                'verbose_name_plural': '历史预测记录',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('feedback', models.TextField(verbose_name='反馈内容')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='car.road', verbose_name='道路id')),
            ],
            options={
                'verbose_name': '反馈信息',
                'verbose_name_plural': '反馈信息',
            },
        ),
        migrations.CreateModel(
            name='TrafficPredictionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='时间')),
                ('image_link', models.URLField(verbose_name='图像')),
                ('predicted_traffic_volume', models.IntegerField(verbose_name='预测结果')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traffic_predictions', to='car.road', verbose_name='道路id')),
            ],
            options={
                'verbose_name': '预测结果信息',
                'verbose_name_plural': '预测结果信息',
            },
        ),
    ]
