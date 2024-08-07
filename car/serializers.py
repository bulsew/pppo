from rest_framework import serializers
from .models import Road, Intersection, RoadIntersectionRelation, TrafficPrediction,RoadTraffic,IntersectionRelationshipQWE,TrafficLightPrediction,Feedback

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = '__all__'

class IntersectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intersection
        fields = '__all__'

class RoadIntersectionRelationSerializer(serializers.ModelSerializer):
    road_name = serializers.ReadOnlyField(source='road.name')
    intersection_name = serializers.ReadOnlyField(source='intersection.name')

    class Meta:
        model = RoadIntersectionRelation
        fields = '__all__'

class TrafficPredictionSerializer(serializers.ModelSerializer):
    road_name = serializers.ReadOnlyField(source='road.name')
    intersection_name = serializers.ReadOnlyField(source='intersection.name')


    class Meta:
        model = TrafficPrediction
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.name')  # 外键字段
    road_name = serializers.ReadOnlyField(source='road.name')


    class Meta:
        model = Feedback
        fields = '__all__'
class RoadTrafficSerializer(serializers.ModelSerializer):
    road_name = serializers.ReadOnlyField(source='road.name')

    class Meta:
        model = RoadTraffic
        fields = '__all__'


class IntersectionRelationshipSerializer(serializers.ModelSerializer):
    id0 = IntersectionSerializer(read_only=True)
    id1 = IntersectionSerializer(read_only=True)
    id2 = IntersectionSerializer(read_only=True)
    road1 = RoadSerializer(read_only=True)
    road2 = RoadSerializer(read_only=True)
    road3 = RoadSerializer(read_only=True)

    class Meta:
        model = IntersectionRelationshipQWE
        fields = '__all__'

class TrafficLightPredictionSerializer(serializers.ModelSerializer):
    road_name = serializers.ReadOnlyField(source='road.name')
    class Meta:
        model = TrafficLightPrediction
        fields = '__all__'
