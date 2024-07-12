from rest_framework import viewsets
from .models import Road, Intersection, RoadIntersectionRelation, TrafficPrediction,RoadTraffic,IntersectionRelationship,TrafficLightPrediction
from .serializers import RoadSerializer, IntersectionSerializer, RoadIntersectionRelationSerializer, TrafficPredictionSerializer,RoadTrafficSerializer,IntersectionRelationshipSerializer,TrafficLightPredictionSerializer

class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class IntersectionViewSet(viewsets.ModelViewSet):
    queryset = Intersection.objects.all()
    serializer_class = IntersectionSerializer

class RoadIntersectionRelationViewSet(viewsets.ModelViewSet):
    queryset = RoadIntersectionRelation.objects.all()
    serializer_class = RoadIntersectionRelationSerializer

class TrafficPredictionViewSet(viewsets.ModelViewSet):
    queryset = TrafficPrediction.objects.all()
    serializer_class = TrafficPredictionSerializer


class RoadTrafficViewSet(viewsets.ModelViewSet):
    queryset = RoadTraffic.objects.all()
    serializer_class = RoadTrafficSerializer


class IntersectionRelationshipViewSet(viewsets.ModelViewSet):
    queryset = IntersectionRelationship.objects.all()
    serializer_class = IntersectionRelationshipSerializer


class TrafficLightPredictionViewSet(viewsets.ModelViewSet):
    queryset = TrafficLightPrediction.objects.all()
    serializer_class = TrafficLightPredictionSerializer

