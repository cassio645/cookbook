from django.urls import path
from . import views


app_name = "receitas"
urlpatterns = [ 
    path("", views.IndexView.as_view(), name="home"),
    path("categoria/<slug:slug>", views.IndexView.as_view(), name="lista_categoria"),
    path("<int:pk>/", views.DetalheView.as_view(), name="detalhe"),
]