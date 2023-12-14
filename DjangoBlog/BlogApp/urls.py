from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # path('post/<int:pk>/', detail_view, name='detail'),
]