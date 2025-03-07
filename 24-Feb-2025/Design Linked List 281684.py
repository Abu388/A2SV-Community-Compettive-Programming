# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None  
        self.size = 0      
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1  
        current = self.head
        for _ in range(index):  
            current = current.next
        return current.val
    
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head  
        self.head = new_node  
        self.size += 1  
    
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node 
        else:
            current = self.head
            while current.next:  
                current = current.next
            current.next = new_node  
        self.size += 1  
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return  
        if index == 0:
            self.addAtHead(val)  
            return
        
        new_node = Node(val)
        current = self.head
        for _ in range(index - 1):  
            current = current.next
        
        new_node.next = current.next  
        current.next = new_node  
        self.size += 1 
    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return  
        if index == 0:
            self.head = self.head.next  
        else:
            current = self.head
            for _ in range(index - 1):  
                current = current.next
            
            current.next = current.next.next  
        self.size -= 1 

# example usage:
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)  # linked list becomes 1 -> 2 -> 3
# print(obj.get(1))  # returns 2
# obj.deleteAtIndex(1)  # linked list becomes 1 -> 3
# print(obj.get(1))  # returns 3
