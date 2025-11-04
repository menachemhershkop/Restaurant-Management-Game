from menu_item.menuitem import MenuItem


class Menu:
    def __init__(self):
        self.item_list=[]
    def add_item(self, menu_item:MenuItem):
        print(menu_item.name)
        self.item_list.append(menu_item)
    def remove_item(self,item_name):
        self.item_list.remove(item_name)
    def get_item_by_name(self,name):
        for i in self.item_list:
            if name == i.name:
                return f'{name} in stuck'
            else:
                return "Item not found"
    def get_item_by_category(self,category):
        items=[]
        for i in self.item_list:
            if category in i.category:
                items.append(i.name)
        return items
    def dispaly_nenu(self):
        for i in self.item_list:
            if i.available:
                print(i.name)
    def get_totle_items(self):
        print(self.item_list[0].get_info())
        return len(self.item_list)