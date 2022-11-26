from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Service areas models


class ServiceArea(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    geo_info = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

# Provider models


class Provider(models.Model):
    # Language choices
    LANGUAGES = [
        ('EN', 'EN'),
        ('FR', 'FR'),
        ('ES', 'ES')
    ]
    # Currency choices
    CURRENCIES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    language = models.CharField(choices=LANGUAGES,
                                default='EN', max_length=5)
    currency = models.CharField(choices=CURRENCIES,
                                default='EN', max_length=5)
    service_area = models.OneToOneField(
        ServiceArea, related_name='provider', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
