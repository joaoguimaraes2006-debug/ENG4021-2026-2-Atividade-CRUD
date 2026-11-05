# ENG4021 - Atividade CRUD (Formulários Django)

Site em Django com **CRUD** (Create, Read, Update, Delete) para dois modelos: **Filmes** e **Séries**.

## O que tem

- **Read:** a página inicial lista os filmes (`ul`) e as séries (`ol`) do banco de dados.
- **Create:** links "Adicionar novo filme" e "Adicionar nova série" abrem um formulário (método `POST`, com `csrf_token`).
- **Update:** cada item da lista tem o link **Atualizar**, que abre o mesmo formulário já preenchido com os dados do item (`/filmes/update/<id>`).
- **Delete:** cada item tem o link **Remover**, que abre a página "Você tem certeza que deseja remover...?" com os botões **Sim** e **Não** (`/filmes/delete/<id>`).

## Rotas

| Rota | O que faz |
|---|---|
| `/` | Home com as duas listas |
| `/filmes` | Adicionar filme |
| `/filmes/update/<id>` | Atualizar filme |
| `/filmes/delete/<id>` | Remover filme |
| `/series` | Adicionar série |
| `/series/update/<id>` | Atualizar série |
| `/series/delete/<id>` | Remover série |

## Como rodar

```bash
pip install -r requirements.txt
cd site_project
python manage.py migrate
python manage.py runserver
```

## Estrutura

- `site_project/site_app/models.py` - modelos `Filme` e `Serie`
- `site_project/site_app/views.py` - uma view para cada operação (create, update e delete) de cada modelo
- `site_project/site_project/urls.py` - as rotas
- `template/` - `home.html`, `form_filme.html`, `form_serie.html` e `confirmar_remocao.html`
- `static/style.css` - estilo
