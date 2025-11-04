from costomers_and_orders.customer import Customer


class Order:
    def __init__(self,customer:Customer,order_number):
        self.customer=customer
        self.order_number=order_number
        self.items=[]
        self.status="pendig"
        self.total_price=0
    def add_item(self,menu_item):
        self.items.append(menu_item)
        self.total_price+=1
    def remove_item(self,menu_item):
        self.items.remove(menu_item)
        self.total_price-=1
    def get_total(self):
        return self.total_price
    def set_status(self,new_status):
        self.status=new_status
    def display_order(self):
        print(f'Order number: {self.order_number}; customer: {self.customer.name}; total items : {self.items}; total prise : {self.total_price}; status order : {self.status}')
    def is_complete(self):
        return self.status == "delivered"
