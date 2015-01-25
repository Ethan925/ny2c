from django.db import models

# Create your models here.

class Order(models.Model):

    table = models.CharField(max_length=50, default='counter')
    order_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s." %(str(self.order_time))

class Pizza(models.Model):
    NEW_YORK = 'New York'
    CHICAGO = 'CH'
    BRAVO = 'BR'
    SICILIAN = 'SC'
    CRUST_CHOICES = (
        (NEW_YORK, 'New York'),
        (CHICAGO, 'Chicago'),
        (BRAVO, 'Bravo'),
        (SICILIAN, 'Sicilian'),
    )

    Pepperoni = 'Pepperoni'
    Sausage = 'Sausage'
    Onion = 'Onion'

    TOPPING_CHOICES = (
        (Pepperoni, 'Pepperoni'),
        (Sausage, 'Sausage'),
        (Onion, 'Onion'),
    )

    order = models.ForeignKey(Order)

    toppings = models.CharField(max_length=500,
                                      choices=TOPPING_CHOICES,
                                      default=Pepperoni)
    crust = models.CharField(max_length=8,
                                      choices=CRUST_CHOICES,
                                      default=NEW_YORK)

    def __unicode__(self):
        return "Make a %s with %s." %(self.crust, str(self.toppings))