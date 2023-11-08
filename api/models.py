from django.db import models
from django.core.exceptions import ValidationError


def validate_positive_health(value):
    if value <= 0 or value > 100:
        raise ValidationError("player health can`t be negative or greater than 100",
            params={"value": value},
        )

# Create your models here.
class Player(models.Model):
    player_x = models.FloatField(null=False)
    player_y = models.FloatField(null=False)
    player_scene = models.TextField(null=False)
    player_health = models.PositiveIntegerField(validators=[validate_positive_health])
    player_laser_bullets = models.IntegerField(null=False)
    player_grenade_bullets = models.IntegerField(null=False)
    player_max_score = models.IntegerField(null=False)

