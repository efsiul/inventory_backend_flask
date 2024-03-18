from sqlalchemy.orm             import Session
from app.entities.item_entity   import Item
from app.models.item_model      import ItemModel
from typing                     import List

class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, item: Item) -> ItemModel:
        item_model = ItemModel( 
            name            =item.name,         #type: ignore
            price           =item.price, 
            mac_address     =item.mac_address,
            serial_number   =item.serial_number,
            manufacturer    =item.manufacturer,
            description     =item.description, 
            quantity        =item.quantity
        )
        try:
            self.session.add(item_model)
            self.session.commit()
            return item_model
        except Exception as e:
            print(f"Error creating item: {e}")
            self.session.rollback()
            raise e

    def get_id(self, id: int) -> ItemModel:
        item_model = self.session.query(ItemModel).filter_by(id=id).first()
        if item_model is None:
            raise Exception(f"Item with id {id} not found")
        else:
            return item_model

    def get_all(self) -> List[ItemModel]:
        return self.session.query(ItemModel).all()

    def update(self, item: Item, id:int) -> ItemModel:
        item_model = self.session.query(ItemModel).filter(ItemModel.id == id).first()
        if item_model is not None:
            item_model.name         = item.name             #type: ignore
            item_model.price        = item.price            #type: ignore
            item_model.mac_address  = item.mac_address      #type: ignore
            item_model.serial_number= item.serial_number    #type: ignore
            item_model.manufacturer = item.manufacturer     #type: ignore
            item_model.description  = item.description      #type: ignore
            item_model.quantity     = item.quantity         #type: ignore
            self.session.commit()
            return item_model
        else:
            raise Exception(f"Item with id {item.id} not found")

    def delete(self, id: int) -> bool:
        try:
            item_model = self.session.query(ItemModel).filter(ItemModel.id == id).first()
            if item_model:
                self.session.delete(item_model)
                self.session.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al eliminar el elemento con ID {id}: {str(e)}")
            self.session.rollback()
            return False
