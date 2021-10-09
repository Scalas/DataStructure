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
        return self.__arr.__iter__()

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


class RBTree:
    class __Node:
        def __init__(self, key, color):
            self.__key = key

            # 노드의 색
            # 0: 검정, 1: 빨강
            self.__color = color
            self.__parent = None
            self.__left = None
            self.__right = None

        def __cmp__(self, other):
            if self.__key < other.__key:
                return -1
            elif self.__key > other.__key:
                return 1
            else:
                return 0

        def set_parent(self, node):
            self.__parent = node

        def set_left(self, node):
            self.__left = node

        def set_right(self, node):
            self.__right = node

        def set_color(self, color):
            self.__color = color

        def set_key(self, key):
            self.__key = key

        def get_key(self):
            return self.__key

        def get_color(self):
            return self.__color

        def get_parent(self):
            return self.__parent

        def get_left(self):
            return self.__left

        def get_right(self):
            return self.__right

    def __init__(self):
        self.__root = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def insert(self, e):
        # 삽입할 노드를 생성
        # 색은 기본적으로 붉은색
        new_node = self.__Node(e, 1)
        pos = self.__root

        # 삽입한 노드가 루트노드인 경우
        if not pos:
            # 노드의 색을 검은색으로 변경하여 삽입
            new_node.set_color(0)
            self.__root = new_node
            self.__size += 1
        else:
            while pos:
                if pos.get_key() < new_node.get_key():
                    if not pos.get_right():
                        pos.set_right(new_node)
                        new_node.set_parent(pos)
                        self.__size += 1
                        break
                    pos = pos.get_right()
                elif pos.get_key() > new_node.get_key():
                    if not pos.get_left():
                        pos.set_left(new_node)
                        new_node.set_parent(pos)
                        self.__size += 1
                        break
                    pos = pos.get_left()
                else:
                    break
            self.__insertion_fix_tree(new_node)

    def search(self, e):
        pos = self.__root
        while pos:
            key = pos.get_key()
            if key > e:
                pos = pos.get_left()
            elif key < e:
                pos = pos.get_right()
            else:
                break
        return pos

    def __insertion_fix_tree(self, node):
        # 삽입된 노드의 부모노드
        parent = node.get_parent()

        # 부모노드가 존재하고 붉은색인 동안 반복
        while parent and parent.get_color() == 1:
            # 삽입된 노드의 조부모노드
            # 부모노드가 붉은색인 시점에서 루트노드가 아니기 때문에 조부모노드 는 반드시 존재한다
            grand_parent = parent.get_parent()

            # 부모 노드가 어느쪽 자식인지의 정보
            # true 라면 좌측 자식노드, false 라면 우측 자식노드가 된다;
            parent_direction = (grand_parent.get_left() == parent)

            # 회전 대상 노드가 어느쪽 자식인지의 정보
            # true 라면 좌측 자식노드, false 라면 우측 자식노드가 된다;
            node_direction = (parent.get_left() == node)

            # 삽입된 노드의 삼촌 노드
            uncle_node = grand_parent.get_right() if parent_direction else grand_parent.get_left()

            # 삼촌 노드의 색
            u_color = 0 if (not uncle_node or uncle_node.get_color() == 0) else 1

            # 케이스 1. 삼촌 노드가 붉은색이라면
            # Recoloring 을 수행
            if u_color == 1:
                # 부모노드와 삼촌노드의 색을 검은색으로, 조부모노드의 색을 붉은색으로 바꾼다
                parent.set_color(0)
                uncle_node.set_color(0)
                grand_parent.set_color(1)

                # 삽입노드를 조부모 노드로, 부모노드를 조부모노드의 부모노드로 변경한다
                node = grand_parent
                parent = node.get_parent()

            # 케이스 2. 삼촌 노드가 검은색이라면
            # Restructuring 을 수행
            else:
                # 회전 대상 노드와 부모노드가 서로 다른방향의 자식 노드인 경우 (LR 또는 RL 상태)
                if node_direction != parent_direction:
                    # 부모 노드가 좌측 자식노드라면 부모노드에 대해 LL 회전을 수행
                    # 부모 노드가 우측 자식노드라면 부모노드에 대해 RR 회전을 수행
                    self.__left_rotation(parent) if parent_direction else self.__right_rotation(parent)

                    # 회전으로 부모자식 관계가 역전되었기 때문에 부모노드를 회전 대상 노드로 설정
                    parent = node

                # 회전을 통해 LL 혹은 RR 상태가 되었기 때문에 원래 회전 대상 노드였던 parent 가 최종적으로 부모노드가 되고
                # 기존의 parent 와 grand_parent 가 자식노드가 된다. 부모노드가 되는 노드는 검은색, 나머진 붉은색을 칠한다.
                # 기존의 parent 의 경우 이미 붉은색이기 때문에 칠할필요가 없다
                parent.set_color(0)
                grand_parent.set_color(1)

                # LL 상태라면 grand_parent 대상으로 LL 회전, 즉 __right_rotation 을 수행한다
                if parent_direction:
                    self.__right_rotation(grand_parent)

                # RR 상태라면 grand_parent 대상으로 RR 회전, 즉 __left_rotation 을 수행한다
                else:
                    self.__left_rotation(grand_parent)

                # Restructuring 의 경우 서브트리에 영향을 주지 않기 때문에 더이상 작업이 불필요하다.
                break

        # 루트의 색은 항상 검은색을 유지해야한다
        self.__root.set_color(0)

    # 좌측 회전 함수
    def __left_rotation(self, node):
        # 회전 대상 노드 또는 회전 대상 노드의 우측 자식노드가 존재하지 않을 경우 종료
        if not node or not node.get_right():
            return

        # 회전 대상노드의 부모노드
        parent = node.get_parent()

        # 우측 자식노드를 임시변수에 저장
        right_temp = node.get_right()

        # 회전 대상노드의 우측 자식노드를 우측 자식노드의 좌측 자식노드로 설정
        node.set_right(node.get_right().get_left())

        # 새로 설정된 우측 자식노드가 존재한다면 부모노드를 회전 대상노드로 설정
        if node.get_right():
            node.get_right().set_parent(node)

        # 임시변수에 저장해둔 원래 우측 자식노드의 좌측 자식노드를 회전 대상노드로 설정
        right_temp.set_left(node)

        # 원래 우측 자식노드의 부모노드를 회전 대상노드의 부모노드로 설정
        right_temp.set_parent(parent)

        # 회전 대상노드의 부모노드가 존재한다면
        # 회전 대상노드의 부모노드의 자식노드를 원래 우측 자식노드로 설정
        if parent:
            # 회전 대상 노드가 좌측 자식노드였을 경우
            if node == parent.get_left():
                parent.set_left(right_temp)
            else:
                parent.set_right(right_temp)

        # 회전 대상노드의 부모노드를 원래 우측 자식노드로 설정
        node.set_parent(right_temp)

        # 만약 회전 대상 노드가 루트노드였다면
        if node == self.__root:
            self.__root = right_temp

    # 우측 회전 함수
    def __right_rotation(self, node):
        # 회전 대상 노드 또는 회전 대상 노드의 좌측 자식노드가 존재하지 않을 경우 종료
        if not node or not node.get_left():
            return

        # 회전 대상노드의 부모노드
        parent = node.get_parent()

        # 좌측 자식노드를 임시변수에 저장
        left_temp = node.get_left()

        # 회전 대상노드의 좌측 자식노드를 좌측 자식노드의 우측 자식노드로 설정
        node.set_left(node.get_left().get_right())

        # 새로 설정된 좌측 자식노드가 존재한다면 부모노드를 회전 대상노드로 설정
        if node.get_left():
            node.get_left().set_parent(node)

        # 임시변수에 저장해둔 원래 좌측 자식노드의 우측 자식노드를 회전 대상노드로 설정
        left_temp.set_right(node)

        # 원래 좌측 자식노드의 부모노드를 회전 대상노드의 부모노드로 설정
        left_temp.set_parent(parent)

        # 회전 대상노드의 부모노드가 존재한다면
        # 회전 대상노드의 부모노드의 자식노드를 원래 우측 자식노드로 설정
        if parent:
            # 회전 대상 노드가 좌측 자식노드였을 경우
            if node == parent.get_left():
                parent.set_left(left_temp)
            else:
                parent.set_right(left_temp)

        # 회전 대상노드의 부모노드를 원래 우측 자식노드로 설정
        node.set_parent(left_temp)

        # 만약 회전 대상 노드가 루트노드였다면
        if node == self.__root:
            self.__root = left_temp

    def in_order(self):
        self._dfs(self.__root, 0, 0)

    def _dfs(self, node, bcnt, pre):
        if node.get_color() == 0:
            bcnt += 1
        if node.get_left():
            self._dfs(node.get_left(), bcnt, node.get_color())
        print(node.get_key(), ':', bcnt, ':color=', node.get_color(), "invalid" if pre==node.get_color()==1 else "valid")
        if node.get_right():
            self._dfs(node.get_right(), bcnt, node.get_color())
