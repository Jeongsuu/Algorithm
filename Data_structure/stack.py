#-*- coding: utf-8 -*-
from DoublyLinkedLists import Node
from DoublyLinkedLists import DoublyLinkedList

#배열로 구현한 스택
class ArrayStack:

    def __init__(self):             # constructor method
        self.data = []              # 빈 리스트 초기화
    
    def size(self):                 # 스택의 크기를 반환
        return len(self.data)       
    
    def isEmpty(self):              # 스택이 비어있는지 확인
        return self.size() == 0 

    def push(self, item):           # 데이터 원소를 추가
        self.data.append(item)  
    
    def pop(self):                  # 데이터 원소를 삭제 및 반환
        return self.data.pop()      

    def peek(self):                 # 스택 최상단 원소 반환
        return self.data[-1]    

# 양방향 연결리스트로 구현한 스택

class LinkedListsStack:

    def __init__(self):             # constructor method
        self.data = DoublyLinkedList()      # 비어있는 양방향 연결리스트로 초기화
    
    def size(self):
        return self.data.getLength()
    
    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())
    
    def peek(self):
        return self.data.getAt(self.size()).data

# 괄호짝 검사
def solution(expr):
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    s = ArrayStack()
    for c in expr:
        if c in '([{':
            s.push(c)
        elif c in match:
            if s.isEmpty():
                return False
            else:
                t = s.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()

