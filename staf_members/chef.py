from staf_members.staff import Staff
class Chef(Staff):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.specialty="Italian"
    def cook_order(self,order):
        order="cooking"
        order="ready"
        super().work()
    def work(self):
        self.energy-=15
