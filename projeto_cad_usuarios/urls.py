
# from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views 

urlpatterns = [
	#path('admin/', admin.site.urls),
	#rota, view responsável, nome de referencia
	path('', views.home, name='home'),
	path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
