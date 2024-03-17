# Carga la configuración de la base de datos
from typing                     import Any, Generator
from app.config                 import Config
from sqlalchemy                 import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm             import sessionmaker, as_declarative, declared_attr

print(Config.DATABASE_URI)
engine                  = create_engine(Config.DATABASE_URI)
SessionLocal            = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base: DeclarativeMeta = declarative_base()
@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr               # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


def get_db() -> Generator:      # type: ignore
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()