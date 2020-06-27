from django.urls import path
from .  import views


urlpatterns = [
    path('api/diseaseupdates/', views.DiseaseupdatesListCreate.as_view() ),
]
