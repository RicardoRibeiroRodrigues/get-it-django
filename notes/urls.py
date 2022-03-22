from django.urls import include, path
from notes import views

urlpatterns = [
    path("", views.index, name="index"),
    path('put', views.update, name='PUT'),
    path('delete/<int:id>', views.delete, name="DELETE")
]
