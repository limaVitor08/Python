# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Vítor Papini de Lima
- Turma: 3B1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
As classes ficam na pasta models. Aula12 - Alunos/models/

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
streamflix.db. A configuração está em app.py

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
1 - ModeloBase - models/base.py
2 - FilmeFavorito - models/filme_favrito.py
3 - HistoricoBusca - models/historico_busca.py

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
As duas herdam de ModeloBase. Ganham id, data_cricao e data_atualizacao

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
o __tablename__ é filmes_favoritos. Usamos pois sem ele o SQLAlchemy criaria a tabela com o nome da classe em minusculo. com __tablename__ podemos escolher o nome exato.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
tmdb_id. nullable=False e unique=True

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
Não sei

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
Em models/historico_busca.py, HistoricoBusca, Ultimas(limite=8)

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
Só alguns campos espelhados. tmdb_id, titulo, poster_path, nota e ano

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
db, ModeloBase, FilmeFavorito e HistoricoBusca. É mais organizado

---

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
dashboard_bp  (nome: "dashboard") — sem url_prefix, cuida da rota /
filmes_bp     (nome: "filmes")    — url_prefix: /filmes
favoritos_bp  (nome: "favoritos") — url_prefix: /favoritos

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
controllers/filmes_controller.py. A função se chama populares()

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
1. Chama api.filmes_populares() — busca os filmes populares na API TMDB.
2. Chama FilmeFavorito.listar() — busca os favoritos salvos no banco para saber quais filmes já estão marcados como favorito na listagem.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
O controller filmes_controller.py, função buscar(). Usa o model HistoricoBusca, chamando HistoricoBusca.registrar(termo, len(filmes)) logo após a busca na API

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
Método POST. URL completa: /favoritos/adicionar/550

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
O controller redireciona o usuário para a página de filmes populares: return redirect(url_for("filmes.populares"))

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
São registrados em app.py, dentro da função criar_app():
app.register_blueprint(dashboard_bp)    
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)

**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
O dashboard_controller.py, função index(). Envia populares, melhores, total_favoritos, historico e modo_demo.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
É um Service (serviço) — não é nenhum dos três do MVC. É uma camada auxiliar que o Controller usa para se comunicar com a API externa TMDB. O Controller
chama a TmdbApi e repassa os dados para a View.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
Não sei

---

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
Aula12 - Alunos/views/templates/

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
 O template base é layout.html. Os outros usam com o comando Jinja: {% extends "layout.html" %}

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
"StreamFlix" (logo/brand) - url_for('dashboard.index')
"Populares"               - url_for('filmes.populares')
"Melhores"                - url_for('filmes.melhores')
"Buscar"                  - url_for('filmes.buscar')
"Favoritos"               - url_for('favoritos.listar')

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
O arquivo views/templates/filmes/detalhe.html. A variável streaming vem do controller filmes_controller.py, função detalhe(), que chama api.streaming(filme_id) e passa o resultado para o template

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
É um pedaço reutilizado (partial/fragmento). Os arquivos index.html, filmes/lista.html e filmes/buscar.html incluem ele usando a tag Jinja: {% include "filmes/_card.html" %}

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
A variável favorito controla o botão. Se ela não for None (filme já salvo), mostra o botão Remover dos favoritos. Se for None, mostra o botão Salvar favorito

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
O CSS está em views/static/css/style.css. O layout.html carrega com: <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
Loop: {% for fav in favoritos %} Campos exibidos na tabela: fav.titulo, fav.nota e fav.ano (também exibe fav.data_criacao formatada com strftime)

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
Quando modo_demo é verdadeiro, exibe um aviso dizendo que a chave da API TMDB não está configurada. A variável é disponibilizada para TODOS os templates pelocontext_processor em 
app.py — a função inject_globals() retorna {"modo_demo": TmdbApi().usando_demo} automaticamente em toda requisição

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.
Não sei

---

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
