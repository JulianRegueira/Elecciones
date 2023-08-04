from django.urls import path
from . import views

app_name = "candidatos"

urlpatterns = [
    path('', views.index, name='index'),
    path("votar/<int:candidato_id>", views.votar, name="votar")
]