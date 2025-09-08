from collections import namedtuple
from collections import deque
from collections import Counter

def namedtuple_test():
    Point = namedtuple('Point', ('x', 'y'))
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    print(p1.x, p1.y, p2.x, p2.y)

    Circle = namedtuple('Circle', ('x', 'y', 'r'))
    circle1 = Circle(0, 0, 1)
    print(f'x:{circle1.x}, y:{circle1.y}, r:{circle1.r}')

def deque_test():
    dq = deque(list(i for i in 'abcd'))
    print(dq)
    dq.appendleft('0')
    print(dq)

def counter_test():
    c = Counter('python programming')
    print(c)
    # for ch in 'python programming':
    #     c[ch] += 1
    # print(c)

    b = Counter()
    b.update('python programming')
    print(b)

if __name__ == '__main__':
    # namedtuple_test()
    # deque_test()
    counter_test()