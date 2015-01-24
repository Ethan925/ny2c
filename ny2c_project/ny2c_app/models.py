from django.db import models

# Create your models here.
class Pizza(models.Model):
    NEW_YORK = 'NY'
    CHICAGO = 'CH'
    BRAVO = 'BR'
    SICILIAN = 'SC'
    CRUST_CHOICES = (
        (NEW_YORK, 'New York'),
        (CHICAGO, 'Chicago'),
        (BRAVO, 'Bravo'),
        (SICILIAN, 'Sicilian'),
    )
    crust = models.CharField(max_length=2,
                                      choices=CRUST_CHOICES,
                                      default=NEW_YORK)