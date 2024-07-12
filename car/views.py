from rest_framework import viewsets
from .models import Road, Intersection, RoadIntersectionRelation, TrafficPrediction,RoadTraffic,IntersectionRelationship,TrafficLightPrediction,Feedback
from .serializers import RoadSerializer, IntersectionSerializer, RoadIntersectionRelationSerializer,FeedbackSerializer, TrafficPredictionSerializer,RoadTrafficSerializer,IntersectionRelationshipSerializer,TrafficLightPredictionSerializer
from .fliter import *
from django_filters.rest_framework import DjangoFilterBackend
class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoadFliter

class IntersectionViewSet(viewsets.ModelViewSet):
    queryset = Intersection.objects.all()
    serializer_class = IntersectionSerializer

class RoadIntersectionRelationViewSet(viewsets.ModelViewSet):
    queryset = RoadIntersectionRelation.objects.all()
    serializer_class = RoadIntersectionRelationSerializer

class TrafficPredictionViewSet(viewsets.ModelViewSet):
    queryset = TrafficPrediction.objects.all()
    serializer_class = TrafficPredictionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TrafficPredictionFilter

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
class RoadTrafficViewSet(viewsets.ModelViewSet):
    queryset = RoadTraffic.objects.all()
    serializer_class = RoadTrafficSerializer


class IntersectionRelationshipViewSet(viewsets.ModelViewSet):
    queryset = IntersectionRelationship.objects.all()
    serializer_class = IntersectionRelationshipSerializer


class TrafficLightPredictionViewSet(viewsets.ModelViewSet):
    queryset = TrafficLightPrediction.objects.all()
    serializer_class = TrafficLightPredictionSerializer

