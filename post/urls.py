from django.urls import path
from .import views
urlpatterns = [
    path('post', views.postList.as_view(), name='post'),
    path('<int:pk>/postDetail', views.PostDetail.as_view(), name='postDetail'),

]