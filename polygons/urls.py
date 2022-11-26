from django.urls import path
from .views import (ProviderDetailApiView, ProvidersListApiView)

# globally define app name
appname = 'polygons'

urlpatterns = [
    path('providers', ProvidersListApiView.as_view(), name='providers'),
    path('providers/<int:provider_id>', ProviderDetailApiView.as_view()),
]
