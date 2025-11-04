from costomers_and_orders.customer import Customer
from costomers_and_orders.order import Order
from menu_item.menu import Menu
from staf_members.staff import Staff


class Waiter(Staff):
    def __init__(self, name,salary):
        super().__init__(name,salary)
        self.tips=0
    def take_order(self,customer:Customer, menu:Menu):
        new_order=Order(customer.name,13)
        while True:
            menu.disaply_menu()
            choice = input("Choice one item from the menu or press Q to exit: ")
            if menu.get_item_by_name(choice):
                    new_order.add_item(choice)
                    continue
            if choice == "Q":
                break
        return new_order
    def serve_order(self,order: Order):
        order.status="delivered"
    def receive_tip(self,amount):
        self.tips+=amount
    def get_total_earnings(self):
        return self.salary + self.tips
