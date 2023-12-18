from rest_framework.routers import DefaultRouter

from apps.todo.views import TodoAPIView

router = DefaultRouter()
router.register('', TodoAPIView, "api_todo")

urlpatterns = router.urls