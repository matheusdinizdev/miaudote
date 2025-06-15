from django.contrib import admin
from django.urls import path
from core import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('cadastrar_animal/', views.cadastrar_animal_view, name='cadastrar_animal'),
    path('excluir-animal/<int:animal_id>/', views.excluir_animal_view, name='excluir_animal'),
]
