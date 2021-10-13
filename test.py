from myds import DoublyLinkedList, Heap, RBTree
import random


# 테스트
def test():
    t = RBTree()
    numset = range(1, 1000000)
    delset = random.sample(numset, 300000)
    i = 0
    for num in numset:
        t.insert(num)
        print("삽입완료", i)
        i += 1

    i = 0
    for num in delset:
        t.delete(num)
        print("삭제완료", i)
        i += 1

    t.in_order()

    print("정상종료")


if __name__ == '__main__':
    test()
