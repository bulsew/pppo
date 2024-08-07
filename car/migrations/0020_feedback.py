# Generated by Django 5.0.6 on 2024-07-12 17:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0019_trafficprediction_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road', models.CharField(max_length=100, verbose_name='道路名')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('feedback', models.TextField(verbose_name='反馈内容')),
                ('road_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='car.road', verbose_name='道路id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
            ],
            options={
                'verbose_name': '反馈信息',
                'verbose_name_plural': '反馈信息',
            },
        ),
    ]
