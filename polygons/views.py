from django.shortcuts import get_object_or_404
from rest_framework import (authentication, generics, parsers, permissions,
                            status, viewsets)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from polygons.models import Provider
from polygons.serializers import ProviderSerializer
from polygons.utils.coordinates_check import check_coordinates


class ProvidersListApiView(APIView):
    """
    View to list all polygons in the system.
    * Requires token authentication.
    * All users are able to access this view.
    """
    # authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # List all providers
    def get(self, request, format=None):
        '''
        List all the providers in system
        '''
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create new provider with service area
    def post(self, request, *args, **kwargs):
        '''
        Create new provider with the payload
        '''
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderDetailApiView(APIView):
    # permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, provider_id):
        '''
        Helper get method to fetch specific provider obejct with given provider_id
        '''
        try:
            return Provider.objects.get(id=provider_id)
        except Provider.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, provider_id, *args, **kwargs):
        '''
        Retrieves a provider with a given provider_id
        '''
        provider_instance = self.get_object(provider_id)
        if not provider_instance:
            return Response(
                {f"message": "provider with the id:{provider_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProviderSerializer(provider_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, provider_id, *args, **kwargs):
        '''
        Updates provider with the provider_id if exists
        '''
        provider_instance = self.get_object(provider_id)
        if not provider_instance:
            return Response(
                {f"message": "provider with the id:{provider_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProviderSerializer(
            instance=provider_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, provider_id, *args, **kwargs):
        '''
        Deletes provider object if provided id exists
        '''
        provider_instance = self.get_object(provider_id)
        if not provider_instance:
            return Response(
                {f"message": "provider with the id:{provider_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        provider_instance.delete()
        return Response(
            status=status.HTTP_200_OK
        )


# TODO: complete polygon request
    # def get(self, request, format=None):
    #     """
    #     Takes latitude, longitude and returns a list
    #     of available polygons inside.
    #     """
    #     longitude = self.request.query_params.get('longitude')
    #     latitude = self.request.query_params.get('latitude')
    #     # we can also lookup by radius, but disabled for now
    #     # radius = self.request.query_params.get('radius')

    #     polygons = Provider.objects.all()
    #     results = [item for item in polygons if check_coordinates(long=float(
    #         longitude), lat=float(latitude), coordinates=item.service_area.geo_info)]

    #     serializer = ProviderSerializer(results, many=True)
    #     return Response({'polygons': serializer.data},
    #                     status=status.HTTP_200_OK)
