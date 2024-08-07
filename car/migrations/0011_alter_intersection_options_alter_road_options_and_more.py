# Generated by Django 5.0.6 on 2024-07-11 10:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0010_intersection_remove_historicalprediction_road_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intersection',
            options={'verbose_name': '交叉口信息', 'verbose_name_plural': '交叉口信息'},
        ),
        migrations.AlterModelOptions(
            name='road',
            options={'verbose_name': '道路信息', 'verbose_name_plural': '道路信息'},
        ),
        migrations.AlterModelOptions(
            name='trafficprediction',
            options={'verbose_name': '车流量预测图表', 'verbose_name_plural': '车流量预测图表'},
        ),
        migrations.CreateModel(
            name='IntersectionRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id0_relations', to='car.intersection')),
                ('id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id1_relations', to='car.intersection')),
                ('id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id2_relations', to='car.intersection')),
            ],
            options={
                'verbose_name': '交叉口关系',
                'verbose_name_plural': '交叉口关系',
            },
        ),
        migrations.CreateModel(
            name='RoadTraffic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='记录id')),
                ('lane', models.IntegerField(default=0, verbose_name='车道')),
                ('collection_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='采集时间')),
                ('traffic_volume', models.IntegerField(default=0, verbose_name='车流量')),
                ('time_ratio', models.FloatField(default=0.0, verbose_name='道路时间占有比')),
                ('speed', models.IntegerField(default=0, verbose_name='速度')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.road', verbose_name='道路id')),
            ],
            options={
                'verbose_name': '数据集',
                'verbose_name_plural': '数据集',
            },
        ),
    ]
