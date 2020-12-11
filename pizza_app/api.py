from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Pizza
from .serializers import PizzaSerializer
from .permissions import IsEmployeeOrNoAccess


class PizzaList(generics.ListCreateAPIView):
   queryset = Pizza.objects.all()
   serializer_class = PizzaSerializer

#    def get_queryset(self):
#       queryset = Pizza.objects.filter(user=self.request.user)
#       return queryset


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
   permission_classes = (IsEmployeeOrNoAccess,)
   queryset = Pizza.objects.all()
   serializer_class = PizzaSerializer