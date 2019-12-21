from rest_framework.viewsets import ModelViewSet #brings in generic PUT, POST, etc for API

from .serializers import ListSerializer, CardSerializer
from .models import Card, List


class ListViewSet(ModelViewSet):
    queryset = List.objects.all() # gets data from query, getting all rows
    serializer_class = ListSerializer # Convert to JSON with this or the serilizer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer