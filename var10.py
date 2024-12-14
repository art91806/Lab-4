TOM = 10

class Item:
    def __init__(self, weight, value, name):
        self.weight = weight
        self.value = value
        self.name = name


def knapsack(items, capacity):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)

        return node_value
    

    def branch_bound(i, weight, value):
        nonlocal max_value, best
        if weight <= capacity and value > max_value:
            max_value = value
            best = now[:]
        if i == len(items):
            return 0
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i+1, weight, value)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            now.append(items[i])
            branch_bound(i+1, weight + items[i].weight, value + items[i].value)
            now.pop()


    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    now = []
    best = []
    branch_bound(0, 0, 0)
    return max_value, best


if __name__ == '__main__':
    items = [
        Item(3, 25, 'r'), 
        Item(2, 15, 'p'), 
        Item(2, 15, 'a'),
        Item(2, 20, 'm'),
        Item(1, 5, 'i'), 
        Item(1, 15, 'k'),
        Item(3, 20, 'x'),
        Item(1, 25,'t'),
        Item(1, 15, 'f'),
        Item(1, 10, 'd'),
        Item(2, 20, 's'),
        Item(2,20,'c')
        ]
    capacity = 9
    max_value, best = knapsack(items, capacity)


    for thing in items:
        if thing not in best:
            max_value -= thing.value


    final = []
    for it in best:
        final += [it.name]*it.weight


    backpack = [[_ for _ in range(3)] for _ in range(3)]
    line = 0
    col=0

    for i in range(capacity):
        backpack[line][col] = final[i]
        col +=1

        if (i+1)%3==0:
            line +=1
            col=0

    for _ in backpack:
        print(_)
    print(max_value + TOM)