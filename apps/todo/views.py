from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.todo.models import Todo
from apps.todo.serializers import TodoSerializer

# Create your views here.
class TodoAPIView(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def perform_destroy(self, instance):
        Todo.objects.filter(user=self.request.user).delete()