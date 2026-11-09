from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class ServerModel(Base):
    # Nome da tabela gerada lá no PostgreSQL
    __tablename__ = "servers"

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)      # Ex: "Servidor Ubuntu Lab"
    ip_address = Column(String, unique=True, nullable=False)            # Ex: "192.168.1.50"
    is_online = Column(Boolean, default=True)                           # Status atual (True/False)
    created_at = Column(DateTime, default=datetime.utcnow)              # Data de cadastro
