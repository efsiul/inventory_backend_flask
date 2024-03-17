from typing import Any
from flask                              import Blueprint, Flask
from app.controllers.item_controller    import ItemController
from app.services.item_service          import ItemService
from app.repositories.item_repository   import ItemRepository
from app.config                         import Config
from app.db                             import get_db,  Base, engine


api             = Blueprint('api', __name__)

item_repository = ItemRepository(next(get_db()))
item_service    = ItemService(item_repository)
item_controller = ItemController(item_service)


@api.route('/products', methods=['POST'])
def create_item() -> dict[str, Any]:
    return item_controller.post()

@api.route('/products/<int:id>', methods=['GET'])
def get_item(id: int) -> str:
    return str(item_controller.get(id))

@api.route('/products', methods=['GET'])
def get_all_items() -> Any:
    return item_controller.get_all()

@api.route('/products/<int:id>', methods=['PUT'])
def update_item(id: int) -> str:
    return str(item_controller.put(id))

@api.route('/products/<int:id>', methods=['DELETE'])
def delete_item(id: int) -> str:
    return str(item_controller.delete(id))

# app  = Flask(__name__)
# app.config.from_object(Config)
# app.register_blueprint(api, url_prefix='/api') 



# def create_tables() -> None:
#     Base.metadata.create_all(bind=engine)   # type: ignore


# if __name__ == "__main__":
#     create_tables()
#     app.run(debug=True)
    