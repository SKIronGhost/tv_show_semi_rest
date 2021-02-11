from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new_template),
    path('create', views.add_new),
    path('<show_id>', views.show),
    path('<show_id>/edit', views.edit),
    path('<show_id>/update', views.update_show),
    path('<show_id>/delete', views.delete),
]