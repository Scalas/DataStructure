# 양방향 연결리스트 클래스
class DoublyLinkedList:
    # 노드 클래스
    class __Node:
        # 노드 생성자
        def __init__(self, e):
            # 데이터
            self.data = e

            # 다음 노드
            self.next = None

            # 이전 노드
            self.prev = None

    # 리스트 생성자
    def __init__(self):
        # head
        self.__head = None

        # tail
        self.__tail = None

        # 현재 노드 (iterator 구현을 위한 필드)
        self.__it = self.__Node(0)

        # 리스트 크기
        self.__size = 0

    # 삽입 메소드
    def insert(self, e, i=-1):
        # 삽입할 노드 생성
        new_node = self.__Node(e)

        # 인덱스가 생략됐거나 마지막 인덱스인 경우 맨 끝에 삽입
        if i < 0 or i == self.__size:
            # 리스트가 비어있다면 head = tail = new_node
            if not self.__head:
                self.__head = self.__tail = new_node

            # 리스트가 비어있지 않다면 마지막 노드 뒤에 삽입
            else:
                self.__tail.next = new_node
                new_node.prev = self.__tail
                self.__tail = new_node

        # 마지막 노드가 아닌 인덱스가 주어졌을 경우
        else:
            # 유효하지 않은 인덱스라면 IndexError 발생
            if i > self.__size:
                raise IndexError

            # 인덱스가 0이라면 첫 노드의 앞 부분에 삽입
            if i == 0:
                self.__head.prev = new_node
                new_node.next = self.__head
                self.__head = new_node

            # 그렇지 않다면 해당 인덱스의 노드 앞 부분에 삽입
            else:
                cur = self.__head
                for _ in range(i):
                    cur = cur.next
                cur.prev.next = new_node
                new_node.prev = cur.prev
                cur.prev = new_node
                new_node.next = cur

        # 리스트의 크기 1 증가
        self.__size += 1

    # 탐색 메소드 - 인덱스
    def search_at(self, i):
        # 유효하지 않은 인덱스라면 IndexError 발생
        if i < 0 or i >= self.__size:
            raise IndexError

        # head 부터 i만큼 다음 노드로 이동
        cur = self.__head
        for _ in range(i):
            cur = cur.next

        # 노드의 데이터 반환
        return cur.data

    # 탐색 메소드 - 데이터
    def search(self, e):
        cur = self.__head
        idx = 0
        # 데이터 값이 e인 노드가 나올 때 까지 탐색
        while cur and cur.data != e:
            cur = cur.next
            idx += 1

        # 데이터 값이 e인 노드가 없을 경우 ValueError 발생
        if not cur:
            raise ValueError

        # 데이터 값이 e인 노드가 처음으로 나타난 인덱스 반환
        return idx

    # i 번째 노드 삭제 메소드
    def delete_at(self, i):
        # 유효하지 않은 인덱스라면 IndexError 발생
        if i < 0 or i >= self.__size:
            raise IndexError

        # head 부터 i 만큼 다음 노드로 이동
        cur = self.__head
        for _ in range(i):
            cur = cur.next

        # 반환할 노드의 데이터를 저장
        res = cur.data

        # 앞, 뒤 노드가 서로 연결되도록 조정
        # head, tail 을 삭제한 경우 head, tail 재지정
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.__head = cur.next

        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.__tail = cur.prev

        # 리스트 크기 1 감소
        self.__size -= 1

        # 삭제한 데이터 반환
        return res

    # 처음으로 나타나는 데이터 e 삭제 메소드
    def delete(self, e):
        # 데이터 삭제 시도
        try:
            # search 메소드를 호출하여 데이터의 인덱스를 구함
            idx = self.search(e)

            # delete_at 메소드를 호출하여 데이터 삭제
            self.delete_at(idx)

            # 삭제성공. True 반환
            return True

        # 존재하지 않는 데이터라면 삭제에 실패. False 반환
        except ValueError:
            return False

    # len 함수의 결과로 sef.__size 반환
    def __len__(self):
        return self.__size

    # 이터레이터 구현
    def __iter__(self):
        # 이터레이션을 위한 self.__it 객체의 next 를 self.__head 로 하고 self 를 반환
        self.__it.next = self.__head
        return self

    def __next__(self):
        # 다음 노드가 있다면 self.__it = self.__it.next 후 self.__it 의 데이터값 반환
        if self.__it.next:
            self.__it = self.__it.next
            return self.__it.data
        # 없다면 이터레이션 종료
        else:
            raise StopIteration


# 힙 클래스
class Heap:
    def __init__(self, arr=[]):
        if arr:
            for i in range(len(arr) // 2 - 1, -1, -1):
                self.__heapify(arr, i)
        self.__arr = arr
        self.__size = len(arr)

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.__arr)

    def __iter__(self):
        return self.__arr

    def push(self, e):
        arr = self.__arr
        arr.append(e)
        self.__size += 1
        idx = self.__size-1
        while idx > 0:
            parent = (idx - 1) // 2
            if arr[parent] > arr[idx]:
                arr[parent], arr[idx] = arr[idx], arr[parent]
                idx = parent
            else:
                break

    def pop(self):
        arr = self.__arr
        if arr:
            res = arr[0]
            self.__size -= 1
            if len(arr) == 1:
                arr.pop()
            else:
                arr[0] = arr.pop()
                idx = 0
                while idx < self.__size:
                    left, right = idx * 2 + 1, idx * 2 + 2
                    target = idx
                    if left < self.__size and arr[left] < arr[target]:
                        target = left
                    if right < self.__size and arr[right] < arr[target]:
                        target = right
                    if idx != target:
                        arr[idx], arr[target] = arr[target], arr[idx]
                    else:
                        break
            return res
        return -1

    @staticmethod
    def __heapify(arr, cur):
        left, right = cur * 2 + 1, cur * 2 + 2
        target = cur
        if left < len(arr) and arr[left] < arr[target]:
            target = left
        if right < len(arr) and arr[right] < arr[target]:
            target = right
        if cur != target:
            arr[cur], arr[target] = arr[target], arr[cur]
            Heap.__heapify(arr, target)


