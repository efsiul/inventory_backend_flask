from sqlalchemy        import Column, Integer, String, Float
from app.db            import Base

class ItemModel(Base):         

    id              = Column(Integer, primary_key=True, autoincrement=True)
    name            = Column(String(100), nullable=False)
    price           = Column(Float, default=0.0)
    mac_address     = Column(String(50))
    serial_number   = Column(String(50))
    manufacturer    = Column(String(100))
    description     = Column(String(200))
    quantity        = Column(Integer, default=0)

    def __repr__(self) -> str:
        return f"<ItemEntity {self.name}>"