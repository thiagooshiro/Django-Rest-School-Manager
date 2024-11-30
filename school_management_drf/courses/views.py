from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes=[AllowAny]
