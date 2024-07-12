from rest_framework import viewsets
from .models import Road, Intersection, RoadIntersectionRelation, TrafficPrediction,RoadTraffic,IntersectionRelationship,TrafficLightPrediction
from .serializers import RoadSerializer, IntersectionSerializer, RoadIntersectionRelationSerializer, TrafficPredictionSerializer,RoadTrafficSerializer,IntersectionRelationshipSerializer,TrafficLightPredictionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class RoadViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class IntersectionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Intersection.objects.all()
    serializer_class = IntersectionSerializer

class RoadIntersectionRelationViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = RoadIntersectionRelation.objects.all()
    serializer_class = RoadIntersectionRelationSerializer

class TrafficPredictionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TrafficPrediction.objects.all()
    serializer_class = TrafficPredictionSerializer


class RoadTrafficViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = RoadTraffic.objects.all()
    serializer_class = RoadTrafficSerializer


class IntersectionRelationshipViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IntersectionRelationship.objects.all()
    serializer_class = IntersectionRelationshipSerializer


class TrafficLightPredictionViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TrafficLightPrediction.objects.all()
    serializer_class = TrafficLightPredictionSerializer

