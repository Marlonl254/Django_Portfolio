from django.urls import path
from . import views

app_name = "Main_App"
urlpatterns = [
    path('', views.portfolio, name = "portfolio"),
    path('portfolio', views.portfolio)
]
