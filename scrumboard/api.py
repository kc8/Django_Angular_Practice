from rest_framework.viewsets import ModelViewSet #brings in generic PUT, POST, etc for API
from rest_framework import permissions

from .serializers import ListSerializer, CardSerializer
from .models import Card, List


class ListViewSet(ModelViewSet):
    queryset = List.objects.all() # gets data from query, getting all rows
    serializer_class = ListSerializer # Convert to JSON with this or the serilizer
    permission_classes = (permissions.IsAuthenticated,) #Tuple with 1 element


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)