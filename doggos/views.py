from rest_framework import generics
from .models import Doggo
from .serializers import DoggoSerializer

class DoggoList(generics.ListCreateAPIView):
    queryset = Doggo.objects.all()
    serializer_class = DoggoSerializer

class DoggoDetail(generics.RetrieveDestroyAPIView):
    queryset = Doggo.objects.all()
    serializer_class = DoggoSerializer