from exercise10_10 import Invoice
from decimal import Decimal 

def main():
    # initlizing the first invoice object for further testing 
    invoice_obj1 = Invoice(5542, "GeForce RTX 40 Series", 10, Decimal(1349.99))
    print("=" * 40)
    print("First Invoice Object:")
    print(invoice_obj1.__repr__())

    # part 2 invoice obj with negative quantity to display validation 
    print("=" * 40)
    print("Attempting to set a negative value for quantity:")
    try:
        negative_quan_invoice_obj = Invoice(5402, "NVIDIA GH200 Grace Hopper SuperChip", -40, Decimal(49999.99))
        print("=" * 40)
        print("Negative Quantity Object:")
        print(negative_quan_invoice_obj.__repr__())
    except ValueError as e:
        print(f"Value error at: {e}")
        
    # part 3 Invoice object with a negative price 
    print("=" * 40)
    print("Attempting to set a negative value for price:")
    try:
        negative_price_invoice_obj = Invoice(8534, "Intel Core i9-14900K", 25, Decimal(-38.99))
        print("=" * 40)
        print("Negative Price Object: ")
        print(negative_price_invoice_obj.__repr__())
    except ValueError as e:
        print(f"Value Error at: {e}")

    # part 4 Showing that you can set each of the attributes of an existing invoice 
    print("=" * 40)
    print("Result of using setters to change object attributes:")
    # using invoice_obj1 setter methods from the Invoice class to change values 
    invoice_obj1.part_num = 5555
    invoice_obj1.description = "GeForce RTX 50 Series"
    invoice_obj1.quantity = 50
    invoice_obj1.price_per_item = Decimal(424.44)
    print(invoice_obj1.__repr__())

# only having the dunder name main statement in this file. 
# This is because we do not need to actually run the file containing the Class.
if __name__ == "__main__":
    main() 