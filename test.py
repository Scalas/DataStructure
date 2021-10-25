from myds import DoublyLinkedList, Heap, RBTree, Trie
import random


# 테스트
def test():
    trie = Trie()
    trie.insert('bee')
    trie.insert('bean')
    trie.insert('be')
    trie.insert('apple')
    trie.insert('apart')
    trie.insert('app')
    trie.insert('be')

    print(trie.find('application'))
    print(trie.find('apple'))
    print(trie.find('bea'))
    print(trie.find('be'))
    print(len(trie))


if __name__ == '__main__':
    test()
