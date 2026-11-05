import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Filme, Serie


class FilmeCrudTests(TestCase):
    def setUp(self):
        self.filme = Filme.objects.create(
            titulo="O Sexto Sentido",
            diretor="M. Night Shyamalan",
            genero="Suspense",
            data_lancamento=datetime.date(1999, 10, 22),
        )

    def test_home_lista_o_filme_com_links(self):
        resposta = self.client.get(reverse("home"))
        self.assertContains(resposta, "O Sexto Sentido")
        self.assertContains(resposta, reverse("update_filme", args=[self.filme.id]))
        self.assertContains(resposta, reverse("delete_filme", args=[self.filme.id]))
        self.assertContains(resposta, reverse("create_filme"))

    def test_create(self):
        resposta = self.client.post(reverse("create_filme"), {
            "titulo": "Vingadores: Guerra Infinita",
            "diretor": "Irmãos Russo",
            "genero": "Ação",
            "data_lancamento": "2018-04-26",
        })
        self.assertRedirects(resposta, reverse("home"))
        self.assertTrue(Filme.objects.filter(titulo="Vingadores: Guerra Infinita").exists())

    def test_update_mostra_formulario_preenchido(self):
        resposta = self.client.get(reverse("update_filme", args=[self.filme.id]))
        self.assertContains(resposta, "Atualizar filme")
        self.assertContains(resposta, 'value="O Sexto Sentido"')
        self.assertContains(resposta, 'value="1999-10-22"')

    def test_update_salva(self):
        self.client.post(reverse("update_filme", args=[self.filme.id]), {
            "titulo": "Sexto Sentido",
            "diretor": "M. Night Shyamalan",
            "genero": "Drama",
            "data_lancamento": "1999-10-05",
        })
        self.filme.refresh_from_db()
        self.assertEqual(self.filme.titulo, "Sexto Sentido")
        self.assertEqual(self.filme.genero, "Drama")
        self.assertEqual(self.filme.data_lancamento, datetime.date(1999, 10, 5))

    def test_delete_pergunta_antes(self):
        resposta = self.client.get(reverse("delete_filme", args=[self.filme.id]))
        self.assertContains(resposta, "Você tem certeza que deseja remover o filme")

    def test_delete_nao_remove_quando_clica_nao(self):
        self.client.post(reverse("delete_filme", args=[self.filme.id]), {})
        self.assertTrue(Filme.objects.filter(id=self.filme.id).exists())

    def test_delete_remove_quando_clica_sim(self):
        self.client.post(reverse("delete_filme", args=[self.filme.id]), {"confirmar": "Sim"})
        self.assertFalse(Filme.objects.filter(id=self.filme.id).exists())

    def test_id_inexistente_da_404(self):
        self.assertEqual(self.client.get(reverse("update_filme", args=[999])).status_code, 404)


class SerieCrudTests(TestCase):
    def setUp(self):
        self.serie = Serie.objects.create(
            titulo="Dark", plataforma="Netflix", temporadas=3,
            data_estreia=datetime.date(2017, 12, 1),
        )

    def test_create(self):
        self.client.post(reverse("create_serie"), {
            "titulo": "The Office", "plataforma": "Prime Video",
            "temporadas": "9", "data_estreia": "2005-03-24",
        })
        self.assertTrue(Serie.objects.filter(titulo="The Office", temporadas=9).exists())

    def test_update(self):
        self.client.post(reverse("update_serie", args=[self.serie.id]), {
            "titulo": "Dark", "plataforma": "Netflix",
            "temporadas": "4", "data_estreia": "2017-12-01",
        })
        self.serie.refresh_from_db()
        self.assertEqual(self.serie.temporadas, 4)

    def test_delete(self):
        self.client.post(reverse("delete_serie", args=[self.serie.id]), {"confirmar": "Sim"})
        self.assertFalse(Serie.objects.filter(id=self.serie.id).exists())
