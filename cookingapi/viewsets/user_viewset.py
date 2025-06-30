from rest_framework import viewsets
from cookingapi.models import CookingAPIUser
from cookingapi.serializers import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CookingAPIUser.objects.all()
    serializer_class = UserSerializer
