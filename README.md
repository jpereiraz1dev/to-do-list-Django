# 📝 Django To-Do List

Um sistema de gerenciamento de tarefas desenvolvido com Django.

O projeto permite criar, visualizar e gerenciar tarefas com data de validade, status público e controle de conclusão.

---

## 🚀 Funcionalidades

- ✅ Criar nova tarefa
- 📅 Definir data de validade
- 🌍 Definir se a tarefa é pública
- 👀 Visualizar tarefas públicas
- 📌 Visualizar detalhes de cada tarefa
- 🗂 Sistema preparado para expansão (multiusuário, clonagem de tarefas etc.)

---

## 🛠 Tecnologias utilizadas

- Python 3
- Django
- SQLite
- HTML5
- CSS3

---

## 📂 Estrutura do Projeto

tarefas/
│
├── models.py
├── views.py
├── forms.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── tarefa.html
│ └── nova_tarefa.html
│
└── static/
└── css/

yaml
Copiar código

---

## ⚙️ Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
Entre na pasta do projeto:

bash
Copiar código
cd seurepositorio
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente:

Windows:

bash
Copiar código
venv\Scripts\activate
Linux/Mac:

bash
Copiar código
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Rode as migrations:

bash
Copiar código
python manage.py migrate
Inicie o servidor:

bash
Copiar código
python manage.py runserver
🔐 Segurança
A SECRET_KEY é armazenada via variável de ambiente e não é versionada no repositório.

📌 Próximas melhorias
🔑 Sistema de autenticação

👤 Tarefas por usuário

🔁 Sistema de clonagem (fork) de tarefas públicas

🎨 Melhorias de UI/UX

🚀 Deploy em produção

👨‍💻 Autor
Desenvolvido por João Pedro.

yaml
Copiar código

---

# 🔥 Extra (recomendado)

Depois cria um `requirements.txt`:

```bash
pip freeze > requirements.txt