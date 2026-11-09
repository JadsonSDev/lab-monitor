from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.models import ServerModel

# Cria as tabelas no banco de dados automaticamente ao subir
Base.metadata.create_all(bind=engine)

app = FastAPI(title="LabMonitor API", version="1.0.0")

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {
        "status": "sucesso",
        "message": "Laboratório LabMonitor (Porta 8001) está rodando e conectado ao PostgreSQL com sucesso!"
    }

# teste 2