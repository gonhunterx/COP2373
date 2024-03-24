# Assignment 10.10 Create a class called 'Invoice' for a hardware store to represent an invoice for an item sold. 
# import Decimal class to use for the price attribute 
from decimal import Decimal

class Invoice:
    # initlize Invoice class 
    def __init__(self, part_num:str, description:str, quantity:int, price_per_item:Decimal):
        # parameters for the class 
        self.part_num = part_num
        self.description = description
        self.quantity = quantity 
        self.price_per_item = price_per_item

    # propertities for setting values to attributes of the Invoice class 
    # PART NUM METHODS 
    @property
    def part_num(self):
        return self._part_num
            
    @part_num.setter
    def part_num(self, num:int):
        if not isinstance(num, int):
            # raising type error for incorrect instance of the object passed 
            raise TypeError("Part number must be an integer")
        # checking if it was passed nothing 
        elif not num:
            raise ValueError("Part number can not be empty.")
        # not allowing the value to be below 0 
        elif num < 0:
            raise ValueError("Part number can not be less than 0.")
        else:
            self._part_num = num

    # DESCRIPTION METHODS 
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, desc):
        if not isinstance(desc, str):
            raise TypeError("Descripiton must be a string")
        elif not desc:
            raise ValueError("Description can not be empty.")
        else:
            self._description = desc 
    
    # QUANTITY METHODS 
    @property 
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        elif quantity <= 0:
            raise ValueError("Quantity can not be less than 0.")
        else:
            self._quantity = quantity
            
    # PRICE PER ITEM METHODS 
    @property 
    def price_per_item(self):
        return self._price_per_item

    @price_per_item.setter
    def price_per_item(self, price):
        if not isinstance(price, Decimal):
            raise TypeError("Price must be a number (integer or float)")
        elif not price:
            raise ValueError("Price can not be empty")
        elif price < 0:
            raise ValueError("Price must be above $0.00")
        else:
            self._price_per_item = price 
    # using __repr__ to pring the string object values with formatting 
    def __repr__(self) -> str:
        return (f"1. Part Number: {self.part_num}\n2. Description: {self.description}\n3. Quantity: {self.quantity}\n4. Price per item: ${self.price_per_item:.2f}")    


        