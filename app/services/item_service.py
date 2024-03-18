from typing                             import Any, List
from app.entities.item_entity           import Item
from app.models.item_model              import ItemModel
from app.repositories.item_repository   import ItemRepository
from typing import Dict

class ItemService:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def create(self, item: Item) -> ItemModel:
        item_dict: Dict[str, Any] = vars(item)
        item_model = ItemModel(**item_dict)
        self.item_repository.create(item_model)  #type: ignore
        return item_model

    def get_by_id(self, id: int) -> Item:
        item_model = self.item_repository.get_id(id)
        
        if item_model is None:
            return None 
        return Item(
                id              = int(item_model.id),             
                name            = str(item_model.name),
                price           = float(item_model.price),
                mac_address     = str(item_model.mac_address),
                serial_number   = str(item_model.serial_number),
                manufacturer    = str(item_model.manufacturer),
                description     = str(item_model.description),
                quantity        = int(item_model.quantity),
            )

    def get_all(self) -> List[Item]:
        item_repository = self.item_repository.get_all()
        return [
            Item(
                id              = int(item_model.id),             
                name            = str(item_model.name),
                price           = float(item_model.price),
                mac_address     = str(item_model.mac_address),
                serial_number   = str(item_model.serial_number),
                manufacturer    = str(item_model.manufacturer),
                description     = str(item_model.description),
                quantity        = int(item_model.quantity),
                )
            for item_model in item_repository
            ]

    def update(self, id: int, item: Item) -> Item:
        updated_item = self.item_repository.update(item, id)
        if updated_item is None:
            return None
        return Item(
            id              = int(updated_item.id),             
            name            = str(updated_item.name),
            price           = float(updated_item.price),
            mac_address     = str(updated_item.mac_address),
            serial_number   = str(updated_item.serial_number),
            manufacturer    = str(updated_item.manufacturer),
            description     = str(updated_item.description),
            quantity        = int(updated_item.quantity),
        )

    def delete(self, id: int) -> bool:
        return self.item_repository.delete(id)