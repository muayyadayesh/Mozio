
from rest_framework import serializers
from polygons.models import Provider, ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    service_area = ServiceAreaSerializer(required=True)

    class Meta:
        model = Provider
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        service_area_data = validated_data.pop('service_area')
        service_area = ServiceAreaSerializer.create(
            ServiceAreaSerializer(), validated_data=service_area_data)
        provider, created = Provider.objects.update_or_create(
            service_area=service_area,
            name=validated_data.pop('name'),
            email=validated_data.pop('email'),
            phone=validated_data.pop('phone'),
            language=validated_data.pop('language'),
            currency=validated_data.pop('currency')
        )
        return provider
