
#  Miaudote

Sistema de adoção de animais desenvolvido com Django + Django REST Framework (backend) e React (frontend).

## Requisitos

- Python 3.10+
- Node.js (para o frontend React)
- Git

##  Como rodar o projeto 

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/miaudote.git
cd miaudote
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute as migrações do banco

```bash
python manage.py migrate
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000`

---

## API Endpoints

- `GET /api/animais/` — Lista animais
- `POST /api/animais/` — Cria novo animal
- `GET /api/ongs/`
- `GET /api/pessoas/`

---

##  Frontend React (em construção)



---

## Equipe
- Leonardo Elias Rodrigues
- Matheus 
- Samuel 

