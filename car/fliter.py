import django_filters
from .models import *
class TrafficPredictionFilter(django_filters.FilterSet):
    class Meta:
        model = TrafficPrediction
        fields = '__all__'  # 使用 '__all__' 表示过滤所有字段

class RoadFliter(django_filters.FilterSet):
    class Meta:
        model = Road
        fields = '__all__'