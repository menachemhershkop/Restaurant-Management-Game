class Customer:
    def __init__(self,name):
        self.name=name
        self.satisfaction=50
    def increase_satisfaction(self,amount):
        self.satisfaction+=amount
        if self.satisfaction>100:
            self.satisfaction=100
    def decrease_satisfaction(self,amount):
        self.satisfaction-=amount
        if self.satisfaction<0:
            self.satisfaction=0
    def is_happy(self):
        return self.satisfaction>70
    def get_info(self):
        return f'customer name : {self.name}, satisfaction level {self.satisfaction}'
