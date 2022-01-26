def ex1():
    for i in range(0,10):
        print(i)
def ex2():
    print(list(range(2, 11)))
    print(list(range(2, 12, 2)))
    print(list(range(10, 1,-2)))

def ex3():
    a = [i for i in range(0, 14, 2)]
    b = [i for i in "abcdef"]
    c = reverse(a)
    d = [(i, j) for i, j in zip(b, c)]
    return a, b, c, d

def reverse(a):
    return list(reversed(a))