from Setup import Item, Container, CreateItems, CreateContainer, CalculateLoad

items = CreateItems(500, 100, 300, 50, 100)
container = CreateContainer(2000)

items.sort(key=lambda x: x.profit/x.weight, reverse=True)

for i in items:
    if (i.weight + container.load <= container.capacity):
        i.chosen = True
        container.items.append(i)
        container.load = CalculateLoad(container)

for i in container.items:
    print(i.id)

print('Loaded items: ', len(container.items))
print('Container load: ', container.load)