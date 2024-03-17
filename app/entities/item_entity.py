

from typing import Any, Dict, Optional


class Item:
    def __init__(self, name: str, price: float, description: str, quantity: int, id: Optional[int] = None) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def dict(self) -> Dict[str, Any]:
        return {
            "id"            : self.id,
            "name"          : self.name,
            "price"         : self.price,
            "description"   : self.description,
            "quantity"      : self.quantity
        }