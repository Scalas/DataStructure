from myds import DoublyLinkedList


# 테스트
def test():
    # 연결 리스트 생성
    dlist = DoublyLinkedList()

    # 데이터 삽입
    dlist.insert(3)
    dlist.insert(1)
    dlist.insert(2)
    dlist.insert(4)
    dlist.insert(0)
    dlist.insert(6)
    dlist.insert(7)
    dlist.insert(9)

    # 데이터 4 삭제
    dlist.delete(4)

    # 첫 번째 데이터(3) 삭제
    dlist.delete_at(0)

    # 3 번째 데이터(6) 삭제
    dlist.delete_at(3)

    # Python 의 list 로 변환하여 출력
    print(list(dlist))


if __name__ == '__main__':
    test()
