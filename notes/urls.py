from django.urls import path
from . import views

# Notes app k pages k urls
urlpatterns = [
    path('', views.note_list, name='note_list'),           # Notes ki list
    path('new/', views.note_create, name='note_create'),   # Naya note
    path('<int:id>/edit/', views.note_edit, name='note_edit'),   # Note edit
    path('<int:id>/delete/', views.note_delete, name='note_delete'),  # Note delete
]