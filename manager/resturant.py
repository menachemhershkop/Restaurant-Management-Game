from costomers_and_orders.order import Order
from menu_item.menu import Menu
import random


class Restaurant:
    def __init__(self,name):
        self.name=name
        self.menu=Menu()
        self.staff=[]
        self.order=[]
        self.money=1000
    def hire_staff(self,stadf_member):
        self.staff.append(stadf_member)
    def fire_staff(self,staff_name):
        self.staff.remove(staff_name)
    def create_order(self,order:Order):
        order_number=random.randint(1500,5000)



