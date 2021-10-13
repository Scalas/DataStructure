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


# 삽입, 삭제 모두 구현할 레드블랙트리
class RBTree:
    class __Node:
        def __init__(self, p=None):
            # 키값은 None, 색은 0(검은색)
            self.key = None
            self.color = 0

            # 부모노드
            self.parent = p

            # 좌측 자식노드, 우측 자식노드는 None
            self.left = None
            self.right = None

            # NIL 여부 True
            self.IS_NIL = True

    def __init__(self):
        # 루트노드에 NIL 노드 세팅
        self.__root = self.__Node()

        # 트리의 크기 0으로 초기화
        self.__size = 0

    def __len__(self):
        # 트리의 크기 반환
        return self.__size

    # 데이터 삽입 함수
    def insert(self, key):
        # 삽입할 위치 탐색
        cursor = self.__root
        while not cursor.IS_NIL:
            # 현재 노드보다 키 값이 크다면 우측 자식노드로 이동
            if cursor.key < key:
                cursor = cursor.right
            # 현재 노드보다 키 값이 작다면 좌측 자식노드로 이동
            elif cursor.key > key:
                cursor = cursor.left
            # 이미 키 값이 존재할 경우 삽입 종료(삽입안함)
            else:
                return False

        # 삽입 위치의 NIL 노드에 key, color, 좌측 자식노드, 우측 자식노드를 세팅하고 NIL 여부를 False 로 한다
        cursor.key = key
        cursor.color = 1
        cursor.left = self.__Node(cursor)
        cursor.right = self.__Node(cursor)
        cursor.IS_NIL = False

        # 트리 크기 1 증가
        self.__size += 1

        # 루트노드의 색은 검은색
        self.__root.color = 0

        # insert_fix 를 수행하여 RB 트리의 규칙을 유지
        self.__insert_fix(cursor)

    # 삽입 이후 규칙에 맞게 트리를 수정하는 함수
    def __insert_fix(self, node):
        parent = node.parent
        # 부모노드가 존재하고 붉은색인 동안 반복
        # 루트노드는 검은색이기 떄문에 부모노드가 붉은색이면 반드시 조부모 노드가 존재
        while parent and parent.color == 1:
            # 조부모노드
            grand_parent = parent.parent

            # 부모노드와 노드가 어느쪽 자식노드인지 확인
            # True: 좌측 / False: 우측
            parent_direction = (grand_parent.left == parent)
            node_direction = (parent.left == node)

            # 삼촌노드
            uncle_node = grand_parent.right if parent_direction else grand_parent.left

            # 케이스 1. Recoloring
            # 삼촌 노드가 붉은색인 경우
            if uncle_node.color == 1:
                # 삼촌노드와 부모노드를 모두 검은색으로 변경
                uncle_node.color = parent.color = 0

                # 조부모노드를 붉은색으로 변경
                grand_parent.color = 1

                # 조부모노드를 삽입노드로 하여 fix 를 다시 수행
                node = grand_parent
                parent = node.parent
                continue

            # 케이스 2. Restructuring
            # 삼촌 노드가 검은색인 경우
            else:
                # 부모노드와 노드가 서로 다른 방향의 자식노드인 경우(LR, RL 형태)
                if node_direction != parent_direction:
                    # LR 형태인 경우 LL 형태로 변형
                    if parent_direction:
                        self.__left_rotation(parent)

                    # RL 형태인 경우 RR 형태로 변형
                    else:
                        self.__right_rotation(parent)

                    # 회전에 의해 parent 와 node 가 뒤바뀜
                    node, parent = parent, node

                # LL 형태인 경우 조부모노드에 대해 right_rotation
                if parent_direction:
                    self.__right_rotation(grand_parent)
                # RR 형태인 경우 조부모노드에 대해 left_rotation
                else:
                    self.__left_rotation(grand_parent)

                # 부모노드가 된 parent 노드의 색을 검은색으로, 나머지 두 노드는 붉은색으로 한다
                parent.color = 0
                grand_parent.color = 1
                node.color = 1

                # Restructuring 은 추가작업을 필요로하지 않음
                break

        # 루트노드는 항상 검은색
        self.__root.color = 0

    def __left_rotation(self, node):
        if node.IS_NIL or node.right.IS_NIL:
            return

        parent = node.parent
        right_tmp = node.right

        node.right = right_tmp.left
        right_tmp.left.parent = node

        right_tmp.left = node
        node.parent = right_tmp

        right_tmp.parent = parent
        if parent:
            if node == parent.left:
                parent.left = right_tmp
            else:
                parent.right = right_tmp
        else:
            self.__root = right_tmp

    def __right_rotation(self, node):
        if node.IS_NIL or node.left.IS_NIL:
            return

        parent = node.parent
        left_tmp = node.left

        node.left = left_tmp.right
        left_tmp.right.parent = node

        left_tmp.right = node
        node.parent = left_tmp

        left_tmp.parent = parent
        if parent:
            if node == parent.left:
                parent.left = left_tmp
            else:
                parent.right = left_tmp
        else:
            self.__root = left_tmp

    # 데이터 삭제 함수
    def delete(self, key):
        # 삭제할 노드 탐색
        target = self.__search(key)

        # 삭제할 노드를 찾지 못한 경우
        if not target:
            return False

        # 삭제 후 fix 를 위한 변수
        child, s_color = None, None

        # target 이 리프노드인 경우
        if target.left.IS_NIL and target.right.IS_NIL:
            child, s_color = target, target.color
            target.key = None
            target.left = target.right = None
            target.IS_NIL = True
            target.color = 0

        # 좌측 자식노드를 가진 경우
        elif not target.left.IS_NIL:
            # 좌측 서브트리중 가장 오른쪽의 노드를 구한다
            successor = target.left

            while not successor.right.IS_NIL:
                successor = successor.right

            # successor 의 좌측 자식노드와 색상 저장
            child, s_color = successor.left, successor.color

            # 삭제할 노드의 키값을 successor 의 키값으로 변경
            target.key = successor.key

            # successor 가 target 의 좌측 자식노드인 경우
            if successor == target.left:
                # successor 의 부모노드의 좌측 자식노드를 successor 의 좌측 자식노드로 설정
                successor.parent.left = successor.left

            # successor 가 target 의 좌측 자식노드가 아닌 경우
            else:
                # successor 의 부모노드의 우측 자식노드를 successor 의 좌측 자식노드로 설정
                successor.parent.right = successor.left

            # successor 의 좌측 자식노드의 부모노드를 successor 의 부모노드로 설정
            successor.left.parent = successor.parent

        # 우측 자식노드만 가진 경우
        else:
            # 우측 서브트리중 가장 왼쪽의 노드를 구한다
            successor = target.right
            while not successor.left.IS_NIL:
                successor = successor.left

            # successor 의 우측 자식노드와 색상 저장
            child, color = successor.right, successor.color

            # 삭제할 노드의 키값을 successor 의 키값으로 변경
            target.key = successor.key

            # successor 가 target 의 우측 자식노드인 경우
            if successor == target.right:
                # successor 의 부모노드의 우측 자식노드를 successor 의 우측 자식노드로 설정
                successor.parent.right = successor.right

            # successor 가 target 의 우측 자식노드가 아닌 경우
            else:
                # successor 의 부모노드의 좌측 자식노드를 successor 의 우측 자식노드로 설정
                successor.parent.left = successor.right

            # successor 의 우측 자식노드의 부모노드를 successor 의 부모노드로 설정
            successor.right.parent = successor.parent

        # 트리 크기 1 감소
        self.__size -= 1

        # 삭제이후 fix 과정
        # 트리가 비어있지 않은 경우
        if child.parent:
            # successor 가 검은색이었던 경우
            if s_color == 0:
                # child 는 붉은색인 경우
                if child.color == 1:
                    child.color = 0

                # child 도 검은색인 경우
                else:
                    self.__delete_fix(child)
        return True

    # 삭제 이후 규칙에 맞게 트리를 수정하는 함수
    def __delete_fix(self, child):
        # child 의 부모 노드
        parent = child.parent

        while parent:
            # True 일 경우 child 는 parent 의 좌측 자식노드 False 일 경우 우측 자식노드
            child_direction = (child == parent.left)

            # 형제노드
            sibling = parent.right if child_direction else parent.left

            # 조카노드
            n1, n2 = sibling.left, sibling.right

            # parent 가 붉은색인 경우
            if parent.color == 1:
                # 케이스 1. sibling, n1, n2 가 모두 검은색인 경우
                if sibling.color == n1.color == n2.color == 0:
                    # parent 와 sibling 의 색을 교환하고 종료
                    parent.color, sibling.color = sibling.color, parent.color
                    break

            # parent 가 검은색인 경우
            else:
                # 케이스 2. sibling, n1, n2도 모두 검은색인 경우
                if sibling.color == n1.color == n2.color == 0:
                    # sibling 의 색을 붉은색으로 바꾼 뒤 child 를 parent 로,
                    # parent 를 parent 의 부모노드로 하여 continue
                    sibling.color = 1
                    child, parent = parent, parent.parent
                    continue

                # 케이스 3. sibling 은 붉은색, n1, n2는 검은색인 경우
                elif sibling.color == 1 and n1.color == n2.color == 0:
                    # parent 와 sibling 의 색을 교환
                    parent.color, sibling.color = sibling.color, parent.color

                    # child 노드의 방향에 따라 회전 수행
                    if child_direction:
                        self.__left_rotation(parent)
                    else:
                        self.__right_rotation(parent)
                    continue

            # parent 의 색에 무관한 경우
            # sibling 의 색이 검은색인 경우
            if sibling.color == 0:
                # 가까운 조카노드가 n1, 먼 조카노드가 n2가 되도록 한다
                if not child_direction:
                    n1, n2 = n2, n1

                # 케이스 4. 먼 조카노드 n2가 붉은색인 경우
                if n2.color == 1:
                    # parent 와 sibling 의 색을 교환하고 n2의 색을 검은색으로 변경
                    parent.color, sibling.color = sibling.color, parent.color
                    n2.color = 0

                    # child 노드의 방향에 따라 회전 수행
                    if child_direction:
                        self.__left_rotation(parent)
                    else:
                        self.__right_rotation(parent)
                    break

                # 케이스 5. 가까운 조카노드 n1이 붉은색이고 먼 조카노드 n2가 검은색인 경우
                if n1.color == 1 and n2.color == 0:
                    # sibling 과 n1의 색을 교환
                    sibling.color, n1.color = n1.color, sibling.color

                    # child 노드의 방향에 따라 회전 수행
                    if child_direction:
                        self.__right_rotation(sibling)
                    else:
                        self.__left_rotation(sibling)
                    continue

        # 루트노드의 색은 항상 검은색
        self.__root.color = 0

    # 특정 데이터 찾는 함수
    # 여기서 노드에는 데이터 값이 따로 없기 때문에 키 값을 반환
    def get(self, key):
        target = self.__search(key)
        if target:
            return target.key
        else:
            return None

    def __search(self, key):
        # 루트 노드부터 탐색 시작
        cursor = self.__root
        while not cursor.IS_NIL:
            # 현재 노드의 키값보다 key 가 더 크다면 우측 자식노드로 이동
            if cursor.key < key:
                cursor = cursor.right
            # 현재 노드의 키값보다 key 가 더 작다면 좌측 자식노드로 이동
            elif cursor.key > key:
                cursor = cursor.left
            # key 에 해당하는 노드를 찾았다면 노드반환
            else:
                return cursor

        # 찾지 못했을 경우 None 반환
        return None

    def in_order(self):
        self._dfs(self.__root, 0, 0)

    def _dfs(self, node, bcnt, pre):
        if node.color == 0:
            bcnt += 1
        if not node.left.IS_NIL:
            self._dfs(node.left, bcnt, node.color)
        print(node.key, ':', bcnt, ':color=', node.color, "invalid" if pre == node.color == 1 else "valid")
        if not node.right.IS_NIL:
            self._dfs(node.right, bcnt, node.color)
