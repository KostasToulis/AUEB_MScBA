from Setup import Item, Stock
import random

random.seed(1)
items = []
stock = []



for i in range(5):
    items.append(Item(i,random.randint(3,14), random.randint(4,10)))

