from django.urls import path, include
from bike.views import BikeListView


urlpatterns = [
    path('list/',BikeListView.as_view(),name='BikeList'),
]