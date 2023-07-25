class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):        
        new_node = Node(x)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.ref = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return
        elif self.front.ref is None:#Checks if there is any element after the front
            print(f"Popped element is {self.front.data}")
            self.front = None
            
        else:
            n = self.front
            print(f"Popped element is {self.front.data}")
            self.front = n.ref
            n = None
    
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        else:
            n = self.front
            while n is not None:
                print(n.data)
                n = n.ref
            print(f"Front of Queue is {self.front.data}")
            print(f"Rear of Queue is {self.rear.data}")

    def sort_queue(self):
        n = self.front
        queue_list = []
        while n is not None:
            queue_list.append(n.data)
            n = n.ref
        queue_list.sort()
        for element in queue_list:
            self.enqueue(element)
        

        
            
class SingleLinkedList:
    def __init__(self):
        self.head = None

# Operations in Linked List
    def add_beginning(self, data):
        #Using the node class you can create the node.
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    

    def add_between_after(self, data, x):#x is the node you want to add after
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("No node available in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        

    def add_between_before(self, data, x):#x is the node you want to add before
        if self.head == None:
            print("Linked List is Empty")
            return #come out of the method
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    
    def delete_beginning(self):
        if self.head == None:
            print("Linked List is empty. We can't delete any nodes")
        else:
            self.head = self.head.ref


    def delete_end(self):
        if self.head == None:
            print("Linked List is empty.We can't delete any nodes.")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    

    def delete_by_value(self, x):# This x is the input that the user will want to delete
        if self.head == None:
            print("Linked List is empty. We can't delete any nodes.")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref == None:
            print("Node doesn't exist.")
        else:
            n.ref = n.ref.ref
    
   
    def print_linked_list(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def maximum_number(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        else:
            n = self.head
            max = 0 
            while n.ref is not None:
                if n.data > max:
                    max = n.data
                n = n.ref
            print(max)
    

    def minimum_number(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        else:
            n = self.head
            min = n.data # Or you can use sys.maxsize
            while n.ref is not None:
                if n.data < min:
                    min = n.data
                n = n.ref
            print(min)

    



