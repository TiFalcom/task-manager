# task-manager

Configure your .env file with the following variables:  
- POSTGRES_USER  
- POSTGRES_PASSWORD  
- POSTGRES_DB  
- DATABASE_URL  

task_manager/  
│  
├── app/  
│   ├── __init__.py  
│   ├── main.py                 # Entry point da FastAPI  
│   ├── config.py               # Configurações (ex: env vars, DB URL)  
│   │  
│   ├── models/                 # Modelos ORM (SQLAlchemy)  
│   │   ├── __init__.py  
│   │   └── task.py  
│   │   └── user.py  
│   │  
│   ├── schemas/                # Schemas Pydantic  
│   │   ├── __init__.py  
│   │   └── task.py  
│   │   └── user.py  
│   │  
│   ├── crud/                   # Operações de banco (CRUD)  
│   │   ├── __init__.py  
│   │   └── task.py  
│   │   └── user.py  
│   │  
│   ├── routers/                # Rotas organizadas  
│   │   ├── __init__.py  
│   │   └── task.py  
│   │   └── user.py  
│   │   └── auth.py  
│   │  
│   ├── database.py             # Configuração e conexão do banco  
│   └── auth.py                 # Lógica de autenticação (JWT)  
│  
├── Dockerfile                  # Dockerfile do app  
├── docker-compose.yml          # Orquestração com banco (ex: Postgres)  
├── requirements.txt            # Dependências do projeto  
└── .env                        # Variáveis de ambiente  
