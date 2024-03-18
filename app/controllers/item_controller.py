from flask                              import redirect, render_template, request, url_for
from flask_restx                        import Resource
from typing                             import Any, Dict, List, Optional
from app.entities.item_entity           import Item
from app.services.item_service          import ItemService

class ItemController(Resource): # type: ignore
    
    def __init__(self, service: ItemService) -> None:
        self.service = service


    def post(self, item_data: Dict[str, Any]) -> Dict[str, Any]:
        if not item_data:
            return {"message": "Invalid request body", "response": 400}
        item = Item(
            name            =str(item_data.get('name')),
            price           =float(str(item_data.get('price'))),
            mac_address     =str(item_data.get('mac_address')),
            serial_number   =str(item_data.get('serial_number')),
            manufacturer    =str(item_data.get('manufacturer')),
            description     =str(item_data.get('description')),
            quantity        =int(str(item_data.get('quantity')))
        )
        created_item = self.service.create(item)
        return {
            "message": "Product successfully created",
            "data": {
                "id"            : created_item.id,
                "name"          : created_item.name,
                "price"         : created_item.price,
                "mac_address"   : created_item.mac_address,
                "serial_number" : created_item.serial_number,
                "manufacturer"  : created_item.manufacturer,
                "description"   : created_item.description,
                "quantity"      : created_item.quantity
                },
            "response": 201
        }

    def get(self, id: Optional[int] = None) -> Any:
        if id is not None:
            item = self.service.get_by_id(id)
            
            if item:
                item_dict = {
                    "id"            : int(item.id),   # type: ignore
                    "name"          : str(item.name),
                    "price"         : float(item.price),
                    "mac_address"   : str(item.mac_address),
                    "serial_number" : str(item.serial_number),
                    "manufacturer"  : str(item.manufacturer),
                    "description"   : str(item.description),
                    "quantity"      : int(item.quantity)
                }
                return item_dict
            else:
                return {"message": f"Item with id {id} not found"}, 404
        else:
            items = self.service.get_all()
            return {"items": [item.__dict__ for item in items]}, 200
        
    def get_all(self) -> List[Item]:
        return self.service.get_all()

    def put(self, id: int, item_data: Dict[str, Any]) -> Any:
        if not item_data:
            return "Empty form data submitted", 400
        item         = Item(**item_data)
        updated_item = self.service.update(id, item)
        if updated_item:
            # return dict({"message": "Item updated successfully", "item": updated_item.__dict__, "response": 200})
            return redirect(url_for('api.get_all_items'))       
        else:
            return "Item not found", 404


    def delete(self, id: int) -> Dict[str, Any]:
        deleted = self.service.delete(id)
        if deleted:
            return {"message": "Item deleted successfully", "response": 200}
        else:
            return {"message": f"Item with id {id} not found", "response": 404}