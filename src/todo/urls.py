from django.conf.urls import include, url
from django.urls import path
from todo import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
