from django.urls import path
from car import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import RoadViewSet, FeedbackViewSet,IntersectionViewSet, RoadIntersectionRelationViewSet, TrafficPredictionViewSet,IntersectionRelationshipViewSet,RoadTrafficViewSet,TrafficLightPredictionViewSet

router = DefaultRouter()
router.register(r'roads', RoadViewSet)
router.register(r'intersections', IntersectionViewSet)
router.register(r'road_intersections', RoadIntersectionRelationViewSet)
router.register(r'traffic_predictions', TrafficPredictionViewSet)
router.register(r'road_traffic', RoadTrafficViewSet)
router.register(r'intersection_relationship', IntersectionRelationshipViewSet)
router.register(r'traffic_light_prediction', TrafficLightPredictionViewSet)
router.register(r'feedback', FeedbackViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
