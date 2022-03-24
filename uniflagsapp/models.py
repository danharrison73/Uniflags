from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Flag(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_coords(self):
        return self.lat, self.lng

    def get_owner(self):
        return self.owner

# class PlatformUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
