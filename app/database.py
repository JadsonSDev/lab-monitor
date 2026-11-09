import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Pega a URL do banco que definimos lá no docker-compose.yml
# Se não achar, usa um valor padrão local para testes
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://jadson:753951@db:5432/labdb"
)

# 1. Cria o "Engine" do SQLAlchemy, que gerencia as conexões físicas com o PostgreSQL
engine = create_engine(DATABASE_URL)

# 2. Cria uma fábrica de sessões (SessionLocal). Cada requisição web abrirá sua própria sessão com o banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base declarativa: classe mãe da qual todos os nossos modelos (tabelas) vão herdar
Base = declarative_base()

# Função utilitária para injetar a sessão do banco nas rotas do FastAPI e fechar após o uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
