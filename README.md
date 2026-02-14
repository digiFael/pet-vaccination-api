# 🐶 Pet Vaccination API

API REST desenvolvida com Django e Django REST Framework para gerenciamento de cadastro de pets, vacinas e registros de vacinação, com autenticação baseada em JWT e controle de permissões por tipo de usuário.

---

## 📌 Visão Geral do Projeto

A aplicação permite:

- Cadastro de Pets
- Cadastro de Vacinas
- Registro de Vacinações
- Associação de pets aos seus responsáveis
- Controle de acesso com autenticação JWT
- Separação de permissões entre administrador e cliente

O sistema foi estruturado seguindo boas práticas de organização por apps no Django.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite (banco de dados padrão)

---

## 📁 Estrutura do Projeto

PROJETO_VACINA/
│
├── config/ # Configurações do projeto
├── accounts/ # Controle de usuários
├── pets/ # Cadastro de pets
├── vaccines/ # Cadastro de vacinas
├── vaccinations/ # Registros de vacinação
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md


---

## ⚙️ Como Executar o Projeto Localmente

### 1️⃣ Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd PROJETO_VACINA

2️⃣ Criar ambiente virtual
python -m venv .venv


Ativar no Windows:

.venv\Scripts\activate


Ativar no Linux/Mac:

source .venv/bin/activate

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Aplicar migrações
python manage.py migrate

5️⃣ Criar superusuário (Admin)
python manage.py createsuperuser

6️⃣ Executar servidor
python manage.py runserver


A API estará disponível em:

http://127.0.0.1:8000/

🔐 Autenticação

A API utiliza JWT (JSON Web Token).

Obter Token

Endpoint:

POST /api/auth/token/


Body:

{
  "username": "seu_usuario",
  "password": "sua_senha"
}


Resposta:

{
  "refresh": "token_refresh",
  "access": "token_access"
}


Utilize o token de acesso no header das requisições:

Authorization: Bearer <access_token>

📦 Endpoints Disponíveis
🐶 Pets

GET /api/pets/

POST /api/pets/

GET /api/pets/{id}/

PATCH /api/pets/{id}/

DELETE /api/pets/{id}/

💉 Vaccines

GET /api/vaccines/

POST /api/vaccines/ (Admin)

PATCH /api/vaccines/{id}/ (Admin)

DELETE /api/vaccines/{id}/ (Admin)

📋 Vaccinations

GET /api/vaccinations/

POST /api/vaccinations/ (Admin)

PATCH /api/vaccinations/{id}/ (Admin)

DELETE /api/vaccinations/{id}/ (Admin)

👥 Controle de Permissões

O sistema diferencia dois tipos de usuários:

🔹 Cliente

Pode visualizar apenas seus próprios pets

Pode visualizar apenas as vacinações relacionadas aos seus pets

Não pode criar ou excluir vacinas

Não pode criar registros de vacinação

🔹 Administrador

Pode cadastrar, editar e excluir vacinas

Pode registrar vacinações

Pode visualizar todos os dados do sistema

🧠 Decisões Técnicas Adotadas

Uso de JWT para autenticação stateless.

Separação da aplicação em múltiplas apps Django para melhor organização.

Uso de ViewSets do Django REST Framework para padronização da API.

Regra de unicidade (pet, vaccine, dose_number) para evitar duplicidade de dose.

Uso de on_delete=PROTECT para impedir exclusão de vacinas vinculadas a registros.

Controle de permissões customizado para diferenciar cliente e administrador.

Banco SQLite para simplificação do ambiente local.

🧪 Testes da API

A API pode ser testada utilizando:

Thunder Client (VS Code)

Postman

curl

📌 Considerações Finais

O projeto foi desenvolvido seguindo boas práticas de organização, separação de responsabilidades por app, controle de autenticação via JWT e implementação de regras de negócio relacionadas à vacinação de pets.

A arquitetura foi pensada para permitir futura escalabilidade, incluindo possível troca de banco de dados ou implantação em ambiente containerizado.


---

