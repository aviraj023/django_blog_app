from django.urls import path
from .views import PostsAPIView,PostDetailAPIView,TestAPIView

urlpatterns = [
    path("posts",PostsAPIView.as_view()),
    path("posts/<int:pk>",PostDetailAPIView.as_view()),
    path("testdb/<str:tb>",TestAPIView.as_view())
]