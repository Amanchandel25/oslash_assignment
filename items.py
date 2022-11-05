import vendor, messeges

# class for item
class item:

    def __init__(self, name, category, price, discount):
        self.name = name
        self.category = category
        self.price = price
        self.discount = discount
        self.max_quantity = vendor.ClothingMaxQuantity if category == vendor.Clothing else vendor.StationeryMaxQuantity

# class for items which will create a list of items in the inventory
class items(item):

    def __init__(self, inventoryList):
        self.itemsList = []
        self.createInventory(inventoryList)

    def createInventory(self, inventoryList):
        inventoryList = inventoryList.split(messeges.newLine)
        for object in inventoryList:
            name, category, price, discount = object.split()
            self.itemsList.append(item(name, category, int(price), int(discount)))

