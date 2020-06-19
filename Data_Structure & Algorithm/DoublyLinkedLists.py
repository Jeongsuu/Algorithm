 '''
    양방향 연결 리스트 ( Doubly Linked Lists )
    -   한 쪽으로만 링크를 연결하지 말고, 앞뒤로 링크를 연결한다.
    -   앞으로도 (다음 Node) 뒤로도 (이전 Node) 로도 진행이 가능해진다.

    Node의 구조를 확장시킨다.
    -   리스트의 처음과 끝에 dummy node를 둔다.
    -   이러면 데이터를 가지고 있는 노드들은 모두 같은 모양을 갖게 된다. 앞뒤로 링크를 걸게됨.
 '''




class Node:
    def __init__(self, item):   # constructor method
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):         # constructor method
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):         
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result
    
    def reverse_traverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:     # Index bound check
            raise Indexrror

        if pos > (self.nodeCount // 2):     # if pos is close with tail
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:                               # if pos is close with head
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        target = prev.next
        prev.next = target.next
        target.next.prev = prev
        self.nodeCount -= 1
        return target.data


    def popBefore(self, next):
        target = next.prev
        next.prev = target.prev
        target.prev.next = next
        self.nodeCount -= 1
        return target.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        prev = self.getAt(self.nodeCount)
        if L.nodeCount is 0:
            prev.next = L.tail
            L.tail.prev = prev
        else:
            next = L.getAt(1)
            prev.next = next
            next.prev = prev
            L.getAt(L.nodeCount).next = self.tail
            self.tail.prev = L.getAt(L.nodeCount)
            self.nodeCount = self.nodeCount + L.nodeCount

def solution(x):
    return 0
