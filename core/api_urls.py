from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api_views import AnimalViewSet, PessoaFisicaViewSet, ONGViewSet  # use esse arquivo novo

router = DefaultRouter()
router.register(r'animais', AnimalViewSet)
router.register(r'pessoas', PessoaFisicaViewSet)
router.register(r'ongs', ONGViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

    # 👇 Nova rota da API
    path('api/', include(router.urls)),
]
