from django.db import models

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
    phone = models.PhoneNumberField()
    language = models.CharField(choices=LANGUAGES, default='EN')
    currency = models.CharField(choices=CURRENCIES, default='EN')

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    geo_info = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
