from django.urls import path
from .views import DoggoListView, DoggoDetailView

urlpatterns = [
    path('', DoggoListView.as_view(), name="doggo_list"),
    path('<int:pk>/', DoggoDetailView.as_view(), name="doggo_detail"),
]