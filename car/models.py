from django.db import models

from aboutUsers.models import Users


class Road(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='道路id')
    name = models.CharField(max_length=100, verbose_name='道路名')
    information = models.TextField(verbose_name='道路信息')
    upload_url = models.URLField(default='',verbose_name='上传链接')
    lng = models.FloatField(default=0.0,verbose_name='经度')  # 经度
    lat = models.FloatField(default=0.0,verbose_name='纬度')  # 纬度
    main_road = models.IntegerField(default=0,verbose_name='所属大道')#
    current_red_time = models.IntegerField(default=0,verbose_name='当前红灯时间')
    current_green_time_1 = models.IntegerField(default=0,verbose_name='当前绿灯时间1')
    current_green_time_2 = models.IntegerField(default=0,verbose_name='当前绿灯时间2')
    video_url = models.URLField(default='',verbose_name='监控链接')#展示

    class Meta:
        verbose_name = '道路信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#交叉口表
class Intersection(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='交叉口id')
    TYPE_CHOICES = (
        ('cross', 'Crossroad'),
        ('t_junction', 'T-junction')
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    current_red_time = models.IntegerField(default=0,verbose_name='当前红灯时间')
    current_green_time_1 = models.IntegerField(default=0,verbose_name='当前绿灯时间1')
    current_green_time_2 = models.IntegerField(default=0,verbose_name='当前绿灯时间2')
    lng = models.FloatField(default=0.0, verbose_name='经度')  # 经度
    lat = models.FloatField(default=0.0, verbose_name='纬度')  # 纬度

    class Meta:
        verbose_name = '交叉口信息'
        verbose_name_plural = verbose_name



#道路交叉口关系表
class RoadIntersectionRelation(models.Model):
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE,verbose_name='交叉口id')
    road = models.ForeignKey(Road, on_delete=models.CASCADE,verbose_name='道路id')

    class Meta:
        verbose_name = '道路交叉口关系信息'
        verbose_name_plural = verbose_name



from datetime import time, datetime, timezone
from django.utils import timezone


def now_time():
    return time(datetime.now(timezone.utc).astimezone().hour,
                datetime.now(timezone.utc).astimezone().minute,
                datetime.now(timezone.utc).astimezone().second)


#5.车流量预测图表
class TrafficPrediction(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='查询记录id')
    road = models.ForeignKey(Road, on_delete=models.CASCADE,verbose_name='道路id')
    intersection = models.ForeignKey(Intersection, on_delete=models.CASCADE,verbose_name='交叉口id',blank=True,null=True)

    # 数据1-8
    data1 = models.FloatField(default=0.0)
    data2 = models.FloatField(default=0.0)
    data3 = models.FloatField(default=0.0)
    data4 = models.FloatField(default=0.0)
    data5 = models.FloatField(default=0.0)
    data6 = models.FloatField(default=0.0)
    data7 = models.FloatField(default=0.0)
    data8 = models.FloatField(default=0.0)
    date = models.DateField(default=timezone.now, verbose_name='日期',blank=True,null=True)
    time = models.CharField(max_length=100, verbose_name='时间',blank=True,null=True)


    class Meta:
        verbose_name = '车流量预测图表'
        verbose_name_plural = verbose_name



from django.utils import timezone

class RoadTraffic(models.Model):
    road = models.ForeignKey(Road, on_delete=models.CASCADE,verbose_name='道路id')
    lane = models.CharField(max_length=100,verbose_name='车道')
    collection_time = models.DateTimeField(default=timezone.now,verbose_name='采集时间')
    traffic_volume = models.IntegerField(default=0,verbose_name='车流量')
    time_ratio = models.FloatField(default=0.0,verbose_name='道路时间占有比')
    speed = models.IntegerField(default=0,verbose_name='速度')

    class Meta:
        verbose_name = '数据集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Road {self.road_id}, Lane {self.lane}, Time: {self.collection_time}, Traffic: {self.traffic_volume}, Ratio: {self.time_ratio}, Speed: {self.speed}"



class IntersectionRelationshipQWE(models.Model):
    id0 = models.ForeignKey(Intersection, on_delete=models.CASCADE, related_name='id0_relations')
    id1 = models.ForeignKey(Intersection, on_delete=models.CASCADE, related_name='id1_relations')
    id2 = models.ForeignKey(Intersection, on_delete=models.CASCADE, related_name='id2_relations')
    road1 =models.ForeignKey (Road, on_delete=models.CASCADE ,blank=True,max_length=255,null=True,related_name='road1')
    road2 = models.ForeignKey(Road, on_delete=models.CASCADE ,blank=True, max_length=255, null=True,related_name='road2')
    road3 = models.ForeignKey(Road, on_delete=models.CASCADE ,blank=True, max_length=255, null=True,related_name='road3')

    class Meta:
        verbose_name = '交叉口关系'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"({self.id.id}, {self.id1.id}, {self.id2.id})"


from datetime import time, datetime, timezone
from django.utils import timezone


def now_time():
    return time(datetime.now(timezone.utc).astimezone().hour,
                datetime.now(timezone.utc).astimezone().minute,
                datetime.now(timezone.utc).astimezone().second)
class TrafficLightPrediction(models.Model):
    road = models.ForeignKey(Road, on_delete=models.CASCADE,verbose_name='道路id')
    date = models.DateField(default=timezone.now, verbose_name='日期')
    timestamp = models.TimeField(default=now_time, verbose_name='时间')
    red_light_result = models.IntegerField(default=0,verbose_name='红灯结果')
    green_light_result1 = models.IntegerField(default=0,verbose_name='绿灯结果1')
    green_light_result2 = models.IntegerField(default=0,verbose_name='绿灯结果2')

    class Meta:
        verbose_name = '历史结果预测'
        verbose_name_plural = verbose_name

#反馈表
class Feedback(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='feedbacks', verbose_name='用户id') #反向关系
    road_id = models.ForeignKey(Road, on_delete=models.CASCADE, related_name='feedbacks', verbose_name='道路id')
    road= models.CharField(max_length=100, verbose_name='道路名')
    time = models.DateTimeField(default=timezone.now,verbose_name='时间')  # 使用当前时间作为默认值
    feedback = models.TextField(verbose_name='反馈内容')  # 存储用户的反馈内容

    class Meta:
        verbose_name = '反馈信息'
        verbose_name_plural = verbose_name

    # 你可以在这里添加其他方法，如__str__用于在Django admin中显示模型的字符串表示
    def __str__(self):
        return f"Feedback from {self.user} on {self.road} at {self.time}"

