from django.urls import path
from .views import (ProvidersListApiView)

# globally define app name
appname = 'polygons'

urlpatterns = [
    path('providers/', ProvidersListApiView.as_view(), name='providers'),
]
