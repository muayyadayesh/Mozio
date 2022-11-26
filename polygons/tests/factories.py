import factory
from polygons.models import Provider


class ProviderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Provider

    name = factory.Faker("sentence")
    email = factory.Faker("name")
    phone = factory.Faker("text")
    language = factory.Faker("name")
    currency = factory.Faker("name")
