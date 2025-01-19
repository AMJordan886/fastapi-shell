project/
├── auth-service/
│   ├── app/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── main.py
├── inventory-service/
│   ├── app/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── main.py
├── payment-service/
│   ├── app/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── main.py
├── docker-compose.yml
└── integration-shell/
    ├── app/
    ├── app/main.py
    ├── alembic/
    ├── alembic.ini
    └── requirements.txt




├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Configuración general
│   │   ├── security.py        # Seguridad (OAuth2, JWT, etc.)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── item.py            # Modelos SQLAlchemy
│   │   ├── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── item.py            # Esquemas de Pydantic
│   │   ├── user.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── item.py            # Operaciones CRUD para "item"
│   │   ├── user.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py            # Dependencias comunes
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │           ├── __init__.py
│   │           ├── items.py   # Rutas relacionadas con "item"
│   │           ├── users.py   # Rutas relacionadas con "user"
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py            # Base SQLAlchemy
│   │   ├── session.py         # Conexión y configuración de la base de datos
│   ├── tests/
│       ├── __init__.py
│       ├── test_items.py      # Pruebas unitarias
│       ├── test_users.py
├── .env                       # Variables de entorno
├── .gitignore
├── requirements.txt           # Dependencias del proyecto
├── alembic/                   # Migraciones (si usas Alembic)
│   ├── env.py
│   ├── versions/
└── docker-compose.yml         # Configuración Docker (opcional)




