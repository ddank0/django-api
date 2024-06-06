from django.shortcuts import render
from .models import Usuario
# Create your views here.

def home(request):
	return render(request, 'usuarios/home.html')

def usuarios(request):
	#salva da dos da tela no banco
	novo_usuario = Usuario()

	novo_usuario.nome  = request.POST.get('nome')
	novo_usuario.idade = request.POST.get('idade')

	# print(f"\n{novo_usuario.nome}\n")
	
	if not (Usuario.objects.filter(nome=novo_usuario.nome).exists()):
		novo_usuario.save()

	#recupera os dados do banco
	usuarios = {
		'usuarios': Usuario.objects.all()
	}

	#retorna a lista de usuarios
	return render(request, 'usuarios/usuarios.html', usuarios)