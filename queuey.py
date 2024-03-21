class Queuey:
    """
    A simple implementation of a queue data structure. Implementations cannot make use of these functions/methods:
        * len
        * list.pop
        * list.remove
    """

    def __init__(self, data_type):
        self.q = []
        self.data_type = data_type
        self.size = 0

    def enqueue(self, item):
        """ Adds an item to the queue, raising a TypeError if the wrong type of item is provided """
        # Your code goes here
        if not isinstance(item, self.data_type):
            raise NotImplementedError("Something is wrong here...")
        self.q.append(item)
        self.size += 1
    def dequeue(self):
        """ Removes the next item in the queue and returns it """
        # Your code goes here
        if self.size == 0:
            raise IndexError("There is nothing but chickens!")
        item = self.q[0]
        del self.q[0]
        self.size -= 1
        return item

    def peek(self):
        """ Returns the next item in the queue, but does not remove it """
        # Your code goes here
        if self.size == 0:
            return None
        return self.q[0]


    def length(self) -> int:
        """ Returns the size of the queue """
        # Your code goes here
        return self.size

    def clear(self) -> None:
        """ Removes all items from the queue """
        # Your code goes here
        self.q.clear()

def main():
    q = Queuey(float)

    print(f"Expected: None, got: {q.peek()}")
    print(q.length()) # 0

    q.enqueue(3.14)
    print(f"Expected: 3.14, got: {q.peek()}")
    print(f"Expected: 1, got: {q.length()}")

    print(f"Expected: 3.14, got: {q.dequeue()}")

    print(f"Expected: None, got: {q.dequeue()}")
    print(f"Expected: 0, got: {q.length()}")

    try:
        q.enqueue(10)
        print(f"Should not reach this point, it means a TypeError wasn't thrown even though it should have been")
    except TypeError as e:
        print(e)

    q.enqueue(8.4)
    q.enqueue(12.1)
    q.enqueue(17.21)
    print(f"Expected: 3, got: {q.length()}")

    print(f"Expected: 8.4, got: {q.peek()}")
    print(f"Expected: 8.4, got: {q.dequeue()}")
    print(f"Expected: 2, got: {q.length()}")
    print(f"Expected: 12.1, got: {q.dequeue()}")
    print(f"Expected: 17.21, got: {q.dequeue()}")
    print(f"Expected: None, got: {q.dequeue()}")

    q.clear()
    print(f"Expected: 0, got: {q.length()}")

if __name__ == "__main__":
    main()