from collections import Counter, OrderedDict



class OrderedCounter(Counter, OrderedDict):

    pass



x = OrderedCounter(input() for i in range(int(input())))

print(len(x))

print(*x.values())
