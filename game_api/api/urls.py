from django.urls import path, include
from .models import Player
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id','player_x', 'player_y', 'player_scene',
                  'player_health', 'player_health','player_laser_bullets',
                  'player_grenade_bullets','player_max_score']


# ViewSets define the view behavior.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet)


urlpatterns = [
   path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
