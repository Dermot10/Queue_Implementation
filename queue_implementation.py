from collections import deque

# Basic Implementation of the queue data structure

queue = deque()

# print(dir(queue))

# All of the elements appended to the left
# This is opposed to usually being appending to the right
queue.appendleft("cat")
queue.appendleft("dog")
queue.appendleft("fish")
queue.appendleft("rabbit")
queue.appendleft("bird")
queue.appendleft("snake")
queue.appendleft("horse")
print(queue)
print("")

# An exmple of the First In First Out principle
# The elements that were added in first are retrieved first
print(queue.pop())
print(queue.pop())
print("New queue with two elements removed")
print(queue)
print(" ")


# An implementation of queue data structure using OOP


class Queue:
    def __init__(self):
        self.buffer = deque()

    # function to add to elements to the end of the queue
    def enqueue(self, value):
        self.buffer.appendleft(value)

    # function to remove elements from the front of queue
    def dequeue(self):
        return self.buffer.pop()

    # function to determine the length of the queue
    def size(self):
        return len(self.buffer)


sports = Queue()
sports.enqueue({
    "Football": "Manchester United",
    "Country": "England",
    "Home kit": "Red",
    "Nickname": "Red Devils",
})

# printing the attribute of the sports object to console
print(sports.buffer)
print(" ")
print(" ")

sports.enqueue({
    "Football": "Real Madrid",
    "Country": "Spain",
    "Home kit": "White",
    "Nickname": "Los Blancos"
})

# second dictionary added to the queue utilising the enqueue function initialised in the class
print(sports.buffer)
print(" ")
print(" ")
sports.enqueue({
    "Football": "AC Milan",
    "Country": "Italy",
    "Home kit": "Red and Black",
    "Nickname": "Rossoneri"
})

# third dictionary added to the queue utilising the enqueue function initialised in the class
print(sports.buffer)
print(" ")
print(f"This is the current length of the queue is: {sports.size()}")
print(sports.dequeue())
print(" ")
# The first element in the queue was returned, This again follows the FIFO principle
print(
    f"Now we can check the length of our queue again which is: {sports.size()}")
