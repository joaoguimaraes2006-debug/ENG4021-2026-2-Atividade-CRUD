from django.db import models


class Filme(models.Model):
    GENEROS = [
        ("Ação", "Ação"),
        ("Aventura", "Aventura"),
        ("Animação", "Animação"),
        ("Comédia", "Comédia"),
        ("Drama", "Drama"),
        ("Ficção científica", "Ficção científica"),
        ("Romance", "Romance"),
        ("Suspense", "Suspense"),
        ("Terror", "Terror"),
    ]

    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=30, choices=GENEROS)
    data_lancamento = models.DateField()

    def __str__(self):
        return self.titulo


class Serie(models.Model):
    PLATAFORMAS = [
        ("Netflix", "Netflix"),
        ("Prime Video", "Prime Video"),
        ("Disney+", "Disney+"),
        ("Max", "Max"),
        ("Globoplay", "Globoplay"),
        ("Apple TV+", "Apple TV+"),
        ("Outra", "Outra"),
    ]

    titulo = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=30, choices=PLATAFORMAS)
    temporadas = models.PositiveIntegerField()
    data_estreia = models.DateField()

    def __str__(self):
        return self.titulo
