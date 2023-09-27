class Item:
    def __init__(self,category, img, title, price):
        self.img = img
        self.title = title
        self.price = price
        self.category = category
    
    def show(self):
        print(self.category)
        print(self.img)
        print(self.title)
        print(self.price)
