  Esse projeto se baseia em um simples CRUD utilizando o framework Django como backend de site. Trata-se de um CRUD, sem API, que é capaz de criar categorias e
produtos com chave estrangeira para organizar cada produto em sua determinada categoria criada pelo próprio usuário. É utilizado também biblioteca Pillow do
python, para permitir a renderização das imagens.

  O models, classe que vai servir para definir as tabelas de produtos e de categorias, possui seus próprios atributos, sendo separado em categorias, que possui
as seguintes colunas:
  id -> Que é definido automáticamente pelo django, sem necessidade de código específico;
  user -> Guardando qual usuário que criou aquele objeto;
  image -> Imagem que irá definir a categoria
  categoria -> Define o nome da categoria da classe Categoria

  Já de produtos, está separado da seguinte maneira:
  id -> Definido automaticamente pelo Django
  user -> Guarda o usuário que criou o objeto
  categoria -> Chave estrangeira que se refere a categoria de Categoria
  nome -> Guarda o nome do produto
  descrição -> Descreve o que é o produto
  preco -> Define o preço do produto

  O admin do Django também foi definido, tendo todas as tabelas e colunas das duas classes podendo filtrar os produtos por nome, preco e categoria. O admin pode
ser acessado ao colocar "admin/" na URL e logando com a conta do superuser criado pelo terminal.

  Nas views, arquivo responsável pela renderização e redirecionamento das páginas, além da manipulação do banco de dados via frontend, é possivel criar, editar
e deletar cada produto e categoria, tendo sua respectiva página responsável pela adição e edição das duas classes.

  Ademais, há a criação, login e logout de usuário no frontend, tendo o seu próprio inventário no ambiente de trabalho.

  Há também um arquivo .txt contendo todas as dependências necessárias do python para rodar o projeto.

  Para rodar o projeto!!!
  git clone https://github.com/MatheusSarmento316/django-product-crud
  cd django-product-crud
  python -m venv .venv
  .\.venv\Scripts\activate
  pip install django
  pip install pillow
  python manage.py migrate
  python manage.py runserver
