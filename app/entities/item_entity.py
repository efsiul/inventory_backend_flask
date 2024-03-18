
from typing import Any, Dict, Optional

class Item:
    def __init__(
                self,
                name            : str = "",
                price           : float = 0.0,
                mac_address     : str = "",
                serial_number   : str = "",
                manufacturer    : str = "",
                description     : str = "",
                quantity        : int = 0,
                id              : Optional[int] = None) -> None:
        
        self.id             = id
        self.name           = name
        self.price          = price
        self.mac_address    = mac_address
        self.serial_number  = serial_number
        self.manufacturer   = manufacturer
        self.description    = description
        self.quantity       = quantity

    def dict(self) -> Dict[str, Any]:
        return {
            "id"            : self.id,
            "name"          : self.name,
            "price"         : self.price,
            "mac_address"   : self.mac_address,
            "serial_number" : self.serial_number,
            "manufacturer"  : self.manufacturer,
            "description"   : self.description,
            "quantity"      : self.quantity
        }