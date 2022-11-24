class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_save= price-deal_price
    def display_product_details(self):
        print("Product : {}".format(self.name))
        print("Price: {} Rs".format(self.price))
        print("Deal Price : {} Rs".format(self.deal_price))
        print("Ratings : {} stars".format(self.ratings))
        print("You Saved : {} Rs".format(self.you_save))

class ElectronicItem(Product):
    def __init__(self,name,price,deal_price,ratings,warranty):
        super().__init__(name,price,deal_price,ratings)
        self.warranty=warranty
        
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} months".format(self.warranty))

class GroceryItem(Product):
    def __init__(self,name,price,deal_price,ratings,expired_date):
        super().__init__(name,price,deal_price,ratings)
        self.expired_date=expired_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Expired by: {}".format(self.expired_date))

class Laptop(ElectronicItem):
    def __init__(self,name,price,deal_price,ratings,warranty,ram,storage):
        super().__init__(name,price,deal_price,ratings,warranty)
        self.ram=ram
        self.storage=storage
    def display_product_details(self):
        super().display_product_details()
        print("ram: {} GB".format(self.ram))
        print("Storage: {} GB SSD".format(self.storage))
        
    
    
class Order:
    delivery_carges={    ## As it is same for all users it declared as class attribute
        "Normal":0,
        "Prime delivey":100
    }
    def __init__(self,delivery_method,delivery_address):
        self.items_in_cart=[]
        self.delivery_address=delivery_address
        self.delivery_method=delivery_method
    
    def add_items(self,product,quantity):
        self.items_in_cart.append((product,quantity))
        
    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Products:")
        print()
        for product,qty in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(qty))
            print()
        total_bill=self.get_total_bill()    
        print("Total Bill: {} Rs".format(total_bill))
    
    def get_total_bill(self):
        total_bill=0
        for product,qty in self.items_in_cart:
            total_bill+=(product.deal_price*qty)
        total_bill+=(Order.delivery_carges[self.delivery_method])
        return total_bill
    
    @classmethod
    def update_delivery_charges(cls,delivery_method,charges):
        cls.delivery_carges[delivery_method]=charges
    
    
tv=ElectronicItem("Sony TV",40000,35000,4.2,12)
milk=GroceryItem("Heritage milk",35,31,4,"jan 2023")
laptop=Laptop("Lenovo Laptop",70000,63000,4.6,12,16,512)
my_order=Order("Normal","Vizag")
my_order.add_items(tv,1)
my_order.add_items(milk,3)
my_order.add_items(laptop,1)
my_order.update_delivery_charges("Normal",50)
my_order.display_order_details()