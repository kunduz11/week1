# map(), filter(), reduce()

def add(x):
    return x + 7
lists = [3, 5, 8,12]
add_to = list(map(add, lists))
print(add_to)
