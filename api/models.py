from django.db import models

# Create your models here.

class Player(models.Model):
    """This class represents the bucketlist model."""
    timestamp = models.BigIntegerField(db_index=True)
    player_type = models.IntegerField()
    player_id = models.IntegerField(db_index=True)

