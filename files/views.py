from .serializers import FileSerializer
from rest_framework.viewsets import ModelViewSet
from .models import File

class FileViewSet(ModelViewSet):
    queryset= File.objects.all()
    serializer_class = FileSerializer
