# Implement queue using stack
class Queue:
    def __init__(self): # runs automatically when we create an object 
        self.s1 = [] # 2 empty stacks
        self.s2 = []

    def enqueue(self, x): #enqueue function to add element
        self.s1.append(x) #add x to stack 1

    def dequeue(self): #to remove element from queue
        while self.s1: #runs while s1 still has element 
            self.s2.append(self.s1.pop()) #last element from s1 and put it to s2

        x = self.s2.pop() #removes element from s2 and stores it in x

        while self.s2: #runs while s2 has elements
            self.s1.append(self.s2.pop()) #moves elements back to s1 from s2

        return x #returns deleted/removed element 

q = Queue() #creates queue object named q

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Inserted:", q.s1)
print("Deleted:", q.dequeue())
print("Deleted:", q.dequeue())
