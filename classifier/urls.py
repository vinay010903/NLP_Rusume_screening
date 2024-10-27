from django.urls import path
from .views import index, predict

urlpatterns = [
    path('', index, name='index'),  # Root URL for the index view
    path('predict/', predict, name='predict'),
]
