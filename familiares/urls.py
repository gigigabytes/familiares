from django.urls import path
from . import views
from .views import FamiliarListView


app_name = 'familiares'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('familiares/', FamiliarListView.as_view(), name='familiar-list'),
]