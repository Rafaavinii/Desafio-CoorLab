from django.db import models

class Transport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price_confort = models.FloatField()
    price_econ = models.FloatField()
    city = models.CharField(max_length=50)
    duration = models.IntegerField()
    seat = models.CharField(max_length=5)
    bed = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name
