from myds import DoublyLinkedList
from myds import Heap


# 테스트
def test():
    # 힙 생성
    heap = Heap()

    # 힙에 삽입
    heap.push(5)
    heap.push(1)
    heap.push(2)
    heap.push(0)
    heap.push(7)
    heap.push(3)

    # 힙 출력
    print(heap)

    # 작은 순서대로 출력
    for _ in range(6):
        print(heap.pop())

    # 배열을 인자로 전달하여 힙 생성
    heap = Heap([5, 2, 3, 0, 7, 1])

    # 힙 출력
    print(heap)

    # 작은 순서대로 출력
    for _ in range(6):
        print(heap.pop())


if __name__ == '__main__':
    test()
