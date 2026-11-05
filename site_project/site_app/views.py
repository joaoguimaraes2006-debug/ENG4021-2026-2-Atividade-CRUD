from django.shortcuts import get_object_or_404, redirect, render

from .models import Filme, Serie


# READ: a home lista todos os filmes e todas as séries do banco de dados
def home(request):
    contexto = {
        "filmes": Filme.objects.all().order_by("titulo"),
        "series": Serie.objects.all().order_by("titulo"),
    }
    return render(request, "home.html", contexto)


# ---------------------------------------------------------------- Filmes

# CREATE: abre o formulário vazio (GET) e cria o filme quando ele é enviado (POST)
def create_filme(request):
    if request.method == "POST":
        Filme.objects.create(
            titulo=request.POST["titulo"],
            diretor=request.POST["diretor"],
            genero=request.POST["genero"],
            data_lancamento=request.POST["data_lancamento"],
        )
        return redirect("home")

    contexto = {"acao": "Adicionar", "generos": Filme.GENEROS}
    return render(request, "form_filme.html", contexto)


# UPDATE: o mesmo formulário, já preenchido com os dados do filme escolhido pelo id
def update_filme(request, id):
    filme = get_object_or_404(Filme, id=id)

    if request.method == "POST":
        filme.titulo = request.POST["titulo"]
        filme.diretor = request.POST["diretor"]
        filme.genero = request.POST["genero"]
        filme.data_lancamento = request.POST["data_lancamento"]
        filme.save()
        return redirect("home")

    contexto = {"filme": filme, "acao": "Atualizar", "generos": Filme.GENEROS}
    return render(request, "form_filme.html", contexto)


# DELETE: pergunta "tem certeza?" e só remove se a pessoa clicar em "Sim"
def delete_filme(request, id):
    filme = get_object_or_404(Filme, id=id)

    if request.method == "POST":
        if "confirmar" in request.POST:
            filme.delete()
        return redirect("home")

    contexto = {"item": filme, "tipo": "o filme"}
    return render(request, "confirmar_remocao.html", contexto)


# ---------------------------------------------------------------- Séries

def create_serie(request):
    if request.method == "POST":
        Serie.objects.create(
            titulo=request.POST["titulo"],
            plataforma=request.POST["plataforma"],
            temporadas=request.POST["temporadas"],
            data_estreia=request.POST["data_estreia"],
        )
        return redirect("home")

    contexto = {"acao": "Adicionar", "plataformas": Serie.PLATAFORMAS}
    return render(request, "form_serie.html", contexto)


def update_serie(request, id):
    serie = get_object_or_404(Serie, id=id)

    if request.method == "POST":
        serie.titulo = request.POST["titulo"]
        serie.plataforma = request.POST["plataforma"]
        serie.temporadas = request.POST["temporadas"]
        serie.data_estreia = request.POST["data_estreia"]
        serie.save()
        return redirect("home")

    contexto = {"serie": serie, "acao": "Atualizar", "plataformas": Serie.PLATAFORMAS}
    return render(request, "form_serie.html", contexto)


def delete_serie(request, id):
    serie = get_object_or_404(Serie, id=id)

    if request.method == "POST":
        if "confirmar" in request.POST:
            serie.delete()
        return redirect("home")

    contexto = {"item": serie, "tipo": "a série"}
    return render(request, "confirmar_remocao.html", contexto)
