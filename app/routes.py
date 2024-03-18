import traceback
from typing                             import Any
from flask                              import Blueprint, request
from app.controllers.item_controller    import ItemController
from app.services.item_service          import ItemService
from app.repositories.item_repository   import ItemRepository
from app.db                             import get_db
from flask                              import render_template

api             = Blueprint('api', __name__)

item_repository = ItemRepository(next(get_db()))
item_service    = ItemService(item_repository)
item_controller = ItemController(item_service)


@api.route('add', methods=['GET', 'POST'])
def create_item()-> Any:                    
    if request.method == 'POST':
        return item_controller.post(request.form)
    else:
        return render_template('add_item.html')

@api.route('get/<int:id>', methods=['GET'])
def get_item(id: int) -> Any:
    item = item_controller.get(id)
    return render_template('detail_item.html', item=item)


@api.route('/', methods=['GET'])
def get_all_items() -> Any:
    items = item_controller.get_all()
    return render_template('index.html', items=items)



@api.route('edit/<int:id>', methods=['GET', 'POST', 'PUT'])
def update_item(id: int) -> Any:                            

    if request.method == 'GET':
        try:
            item_ = item_controller.get(id)
            
            if item_ is None:
                return "Item not found", 404
            
            return render_template('edit_item.html', item=item_, item_id=id)
        
        except Exception as e:
            print(f"Error retrieving item: {str(e)}")
            traceback.print_exc() 
            return "Error retrieving item", 500 
    
    elif request.method in ['POST', 'PUT']:
        item_data = dict(request.form.items()) 
        
        if not item_data:
            return "Empty form data submitted", 400

        return item_controller.put(id, item_data)

    else:
        return "Method Not Allowed", 405


@api.route('delete/<int:id>', methods=['DELETE'])
def delete_item(id: int) -> Any:
    return item_controller.delete(id)
