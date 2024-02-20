from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Doggo
from .serializers import DoggoSerializer

class DoggoListView(ListCreateAPIView):
    queryset = Doggo.objects.all()
    serializer_class = DoggoSerializer

class DoggoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doggo.objects.all()
    serializer_class = DoggoSerializer