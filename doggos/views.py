from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Doggo
from .serializers import DoggoSerializer
from .permissions import IsOwnerOrReadOnly

class DoggoListView(ListCreateAPIView):
    queryset = Doggo.objects.all()
    serializer_class = DoggoSerializer
    permission_classes = [IsAuthenticated]

class DoggoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doggo.objects.all()
    serializer_class = DoggoSerializer
    permission_classes = [IsOwnerOrReadOnly]