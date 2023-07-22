from django.urls import path
from .views import IndexPageView, menuView, registerView, loginView, logout_view, add_view,listar_vehiculos


urlpatterns = [
    path('', IndexPageView.as_view(), name="index"),
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logout_view, name="logout"),
    path('vehiculo/add', add_view, name="add"),
    path('vehiculo/list', listar_vehiculos, name="list")
    

]
