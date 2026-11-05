from django.contrib import admin
from django.urls import path

from site_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),

    # Filmes
    path("filmes", views.create_filme, name="create_filme"),
    path("filmes/update/<int:id>", views.update_filme, name="update_filme"),
    path("filmes/delete/<int:id>", views.delete_filme, name="delete_filme"),

    # Séries
    path("series", views.create_serie, name="create_serie"),
    path("series/update/<int:id>", views.update_serie, name="update_serie"),
    path("series/delete/<int:id>", views.delete_serie, name="delete_serie"),
]
