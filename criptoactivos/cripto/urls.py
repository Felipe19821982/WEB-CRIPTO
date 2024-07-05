from django.urls import path
from . import views
from .views import logout_view, exit

urlpatterns = [
    path('index/', views.index, name='index'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('criptoactivos/', views.criptoactivos, name='criptoactivos'),
    path('comprar/', views.comprar, name='comprar'),
    path('vender/', views.vender, name='vender'),
    path('registro/', views.registro_view, name='registro'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/', exit, name='exit'),
    path('mis_compras/', views.mis_compras, name='mis_compras'), 
]