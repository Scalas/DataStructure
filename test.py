from myds import DoublyLinkedList, Heap, RBTree
import random


# 테스트
def test():
    t = RBTree()
    MAX_VAL = 10000
    test_set = random.sample(range(1, MAX_VAL), 500)
    for num in test_set:
        t.insert(num)
    print("삽입끝", len(t))

    sc = 0
    for num in test_set:
        if t.get(num):
            sc += 1
    print("탐색끝", sc)

    t.in_order()
    return 0


if __name__ == '__main__':
    test()
