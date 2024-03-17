from flask                              import jsonify, request
from flask_restx                        import Resource
from typing                             import Any, Dict, Optional
from app.entities.item_entity           import Item
from app.services.item_service          import ItemService

class ItemController(Resource): # type: ignore
    
    def __init__(self, service: ItemService) -> None:
        self.service = service


    def post(self) -> Dict[str, Any]:
        item_data: Optional[Dict[str, Any]] = request.json
        if item_data is None:
            return {"message": "Invalid request body", "response": 400}
        item = Item(**item_data)
        created_item = self.service.create(item)
        
        return {
            "message": "Product successfully created",
            "data": {
                "id"            : created_item.id,
                "name"          : created_item.name,
                "price"         : created_item.price,
                "description"   : created_item.description,
                "quantity"      : created_item.quantity
                },
            "response": 201
        }

    
    def get(self, id: Optional[int] = None) -> Any:
        if id is not None:
            item = self.service.get_by_id(id)
            if item:
                return {"item": item.__dict__}, 200
            else:
                return {"message": f"Item with id {id} not found"}, 404
        else:
            items = self.service.get_all()
            return {"items": [item.__dict__ for item in items]}, 200
        
    def get_all(self) -> Any:
        items = self.service.get_all()
        return jsonify([item.dict() for item in items]), 200

    def put(self, id: int) -> Dict[str, Any]:
        item_data: Dict[str, Any] = request.json if request.json is not None else {}
        item            = Item(**item_data)
        updated_item    = self.service.update(id, item)
        if updated_item:
            return dict({"message": "Item updated successfully", "item": updated_item.__dict__, "response": 200})
        else:
            return {"message": f"Item with id {id} not found", "response": 404}


    def delete(self, id: int) -> Dict[str, Any]:
        deleted = self.service.delete(id)
        if deleted:
            return {"message": "Item deleted successfully", "response": 200}
        else:
            return {"message": f"Item with id {id} not found", "response": 404}