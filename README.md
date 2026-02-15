# Pet Vaccination API

API REST para gestao de pets, vacinas e registros de vacinacao, com autenticacao JWT.

## Visao Geral

O projeto foi construido com Django + Django REST Framework e organizado por dominio:

- `pets`: cadastro e consulta de pets
- `vaccines`: catalogo de vacinas
- `vaccinations`: registros de aplicacao de vacinas
- `accounts`: modelo auxiliar de funcionario (`Employee`)

Autenticacao e documentacao:

- JWT com SimpleJWT
- OpenAPI com drf-spectacular
- Swagger UI para teste dos endpoints

## Stack

- Python 3.x
- Django 6.0.2
- Django REST Framework 3.16.1
- djangorestframework-simplejwt 5.5.1
- drf-spectacular 0.29.0
- SQLite (padrao atual)

## Estrutura do Projeto

```text
progeto_vacina/
|-- manage.py
|-- requirements.txt
|-- config/
|   |-- settings.py
|   `-- urls.py
|-- accounts/
|-- pets/
|-- vaccines/
`-- vaccinations/
```

## Arquitetura (por app)

Cada app segue o mesmo padrao principal:

1. `models.py`: define entidades e regras de persistencia
2. `serializers.py`: valida e serializa dados de entrada/saida
3. `permissions.py` (quando aplicavel): regras de acesso
4. `views.py`: `ModelViewSet` com regras de consulta/criacao
5. `urls.py`: roteamento via `DefaultRouter`

### Relacoes de dados

- `Pet.owner -> auth.User`
- `VaccinationRecord.pet -> Pet`
- `VaccinationRecord.vaccine -> Vaccine`
- `VaccinationRecord.applied_by -> auth.User`
- `accounts.Employee.user -> auth.User` (OneToOne)

### Regras importantes de dominio

- `VaccinationRecord` possui unicidade por `(pet, vaccine, dose_number)`
- `applied_by` em vacinacao e definido automaticamente com o usuario autenticado no `create`

## Instalacao e Execucao

1. Criar ambiente virtual:

```bash
python -m venv .venv
```

2. Ativar ambiente virtual (PowerShell):

```bash
.\.venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Rodar migracoes:

```bash
python manage.py migrate
```

5. Criar superusuario:

```bash
python manage.py createsuperuser
```

6. Subir servidor:

```bash
python manage.py runserver
```

Base local padrao: `http://127.0.0.1:8000`

## Endpoints

### Autenticacao

- `POST /api/auth/token/` -> gera `access` e `refresh`
- `POST /api/auth/token/refresh/` -> renova token `access`

### Documentacao

- `GET /api/schema/` -> schema OpenAPI (JSON)
- `GET /api/docs/` -> Swagger UI

### Pets

- `GET /api/pets/`
- `POST /api/pets/`
- `GET /api/pets/{id}/`
- `PUT /api/pets/{id}/`
- `PATCH /api/pets/{id}/`
- `DELETE /api/pets/{id}/`

Campos do recurso:

- `id`
- `name`
- `species` (`dog`, `cat`, `other`)
- `breed` (opcional)
- `birth_date` (opcional)
- `owner` (somente leitura na API)

### Vaccines

- `GET /api/vaccines/`
- `POST /api/vaccines/`
- `GET /api/vaccines/{id}/`
- `PUT /api/vaccines/{id}/`
- `PATCH /api/vaccines/{id}/`
- `DELETE /api/vaccines/{id}/`

Campos do recurso:

- `id`
- `name`
- `manufacturer` (opcional)
- `species_target` (`dog`, `cat`, `both`)
- `doses_required`
- `days_between_doses` (opcional)

### Vaccinations

- `GET /api/vaccinations/`
- `POST /api/vaccinations/`
- `GET /api/vaccinations/{id}/`
- `PUT /api/vaccinations/{id}/`
- `PATCH /api/vaccinations/{id}/`
- `DELETE /api/vaccinations/{id}/`

Campos do recurso:

- `id`
- `pet`
- `vaccine`
- `applied_at`
- `dose_number`
- `notes` (opcional)
- `applied_by` (somente leitura na API)

## Permissoes

Configuracao global (`REST_FRAMEWORK`):

- autenticacao: JWT (`JWTAuthentication`)
- permissao padrao: `IsAuthenticated`

Regras por recurso:

- `pets`:
  - autenticado obrigatorio
  - staff/superuser visualiza todos os pets
  - usuario comum visualiza apenas pets onde `owner == request.user`
  - ao criar pet, usuario comum recebe `owner` automatico

- `vaccines`:
  - leitura (`GET`, `HEAD`, `OPTIONS`) para qualquer usuario autenticado
  - escrita (`POST`, `PUT`, `PATCH`, `DELETE`) apenas staff/superuser

- `vaccinations`:
  - leitura para autenticados; no nivel de objeto, usuario comum so acessa vacinacoes de pets proprios
  - escrita apenas staff/superuser
  - `applied_by` definido automaticamente com usuario autenticado no create

## Exemplos rapidos

Gerar token:

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"SUA_SENHA"}'
```

Listar vacinas com token:

```bash
curl http://127.0.0.1:8000/api/vaccines/ \
  -H "Authorization: Bearer SEU_ACCESS_TOKEN"
```


