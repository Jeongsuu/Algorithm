# 노드 = 데이터 + 링크

class Node:
    def __init__(self, item):
        self.data = item    # 데이터
        self.next = None    # 링크

class LinkedList:
    def __init__(self):
        self.nodeCount = 0  # 연결된 노드의 개수
        self.head = None    # 최전방 노드
        self.tail = None    # 최후방 노드
        
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount: # pos가 1보다 작거나 연결된 노드가 없는 경우
            return None
        i = 1
        curr = self.head    # 현재 노드를 최전방 노드로 초기화
        while i < pos:  # 계속 순회하겠다
            curr = curr.next    #현재 노드가 다음 노드를 가리키도록 한다.
            i += 1      # 인덱스값 1 증가
        return curr
    
    def traverse(self):
        answer = []
        curr = self.head        # curr은 Node 클래스의 인스턴스
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
        return answer
        
    
            
        
            