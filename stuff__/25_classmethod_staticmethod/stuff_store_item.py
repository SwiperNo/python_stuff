class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = sum(item['price'] for item in self.items)
        return total
    

store = Store("Amazon")
store.add_item("TV", 500)
store.add_item("GoPro", 700)


print(f"The total stock price: {store.stock_price()}")