# Django Auth Boilerplate

Um projeto de autenticação robusto e pronto para uso, construído com **Django**, **Bootstrap**, **django-axes** (proteção contra brute-force), **Docker**, **PostgreSQL** e gerenciamento moderno de pacotes com **uv**. Ideal para aplicações que precisam de autenticação de usuários de forma rápida, segura e escalável.

---

## 🚀 **Principais Características**

- **Django**: Framework web Python maduro, seguro e altamente produtivo.
- **Bootstrap**: Interface moderna e responsiva pronta para customização.
- **django-axes**: Proteção automática contra ataques de força bruta em senhas.
- **Testes automatizados**: Cobertura básica pronta para garantir a qualidade do código.
- **Docker + PostgreSQL**: Ambiente isolado, portável e escalável para desenvolvimento e produção.
- **uv**: Gerenciador de pacotes ultrarrápido e moderno para Python.
- **Telas prontas**: Formulários de login, registro e mensagens de erro/sucesso já implementados.
- **Pronto para escalar**: Ideal para projetos que vão crescer e precisam de base sólida.

---

## 🛠️ **Pré-requisitos**

- [Docker](https://www.docker.com/get-started)
- [uv](https://github.com/astral-sh/uv) (instale com `pip install uv` ou veja instruções no repositório oficial)
- [Python 3.12](https://www.python.org/downloads/),

---

## ⚡ **Como rodar o projeto**

### 1. **Clone o repositório**
```bash
git clone https://github.com/VicVald/auth_django
cd auth_django
```

### 2. **Instale dependências com uv**
```bash
uv sync
```

### 3. **Suba o postgresql com Docker Compose**
```bash
docker-compose -f app/docker-compose.yml up --build
```
### 4. **Suba o Development enviroment do Django**
```bash
python3 app/manage.py runserver
```

- O Django estará disponível em `http://localhost:8000`
- O Adminer (interface para o banco) em `http://localhost:8080`

---

## 🧑‍💻 **Principais comandos do Django**

No Linux:
```bash
python3 app/manage.py migrate         # Aplica as migrações
python3 app/manage.py createsuperuser # Cria usuário admin
python3 app/manage.py test            # Roda os testes
```

uv pip install -r requirements.txt

---

## 🧪 **Testes**

O projeto já vem com testes automatizados para autenticação. Execute:

```bash
python3 app/manage.py test
```

---

## 🏆 **Por que usar este boilerplate?**

- **Economize tempo**: Telas e lógica de autenticação prontas para uso.
- **Segurança**: Proteção contra brute-force com django-axes.
- **Escalabilidade**: Docker e PostgreSQL prontos para produção.
- **Qualidade**: Testes automatizados e base para CI/CD.
- **Flexibilidade**: Fácil de customizar para qualquer aplicação Django.

---

## 🔒 **Próximos passos sugeridos**

- Adicionar linters para padronização do código.
- Implementar medidor de força de senha no frontend.
- Adicionar camadas extras de segurança (ex: reCAPTCHA).
- Configurar deploy automatizado (CI/CD).

---

## 📚 **Referências**

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [django-axes](https://django-axes.readthedocs.io/)
- [Docker Compose](https://docs.docker.com/compose/)
- [uv](https://github.com/astral-sh/uv)

