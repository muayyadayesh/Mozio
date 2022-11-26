import pytest
from rest_framework.test import APIClient
from polygons.models import Provider
from polygons.serializers import ProviderSerializer


@pytest.mark.django_db
def test_list_providers(client):
    response = client.get('/api/providers')

    providers = Provider.objects.all()
    expected_data = ProviderSerializer(providers, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_get_existing_provider(client):
    response = client.get('/api/providers/1')
    expected_data = ProviderSerializer(response, many=False, partial=True)
    assert expected_data


@pytest.mark.django_db
def test_get_areas_without_coordinates(client):
    response = client.get('/api/polygon')
    assert response.status_code != 200


@pytest.mark.django_db
def test_get_areas_with_false_coordinates(client):
    response = client.get('/api/polygon/abc/def')
    assert response.status_code != 200


@pytest.mark.django_db
def test_get_areas_with_correct_coordinates(client):
    response = client.get('/api/polygon/-69.9042034/46.914246')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_provider_that_success():
    client = APIClient()
    payload = {
        "name": "new_service",
        "email": "muayyadayesh@gmail.com",
        "phone": "+12125552368",
        "language": "EN",
        "currency": "USD",
        "service_area": {
            "name": "services",
            "price": "1123.00",
            "geo_info": [
                [
                    -69.9066067,
                    46.9172361
                ],
                [
                    -69.9014139,
                    46.9106402
                ],
                [
                    -69.9154902,
                    46.9072393
                ],
                [
                    -69.9187088,
                    46.914246
                ],
                [
                    -69.9069071,
                    46.9172361
                ]
            ]
        },

    }
    response = client.post('/api/providers', payload, format='json')
    assert response.status_code == 201
