class Our_Queue:

    # ----------------------------------------------------
    # Internal class _Node
    # Names starting with underscore are suggested not to be
    # used outside the class

    class _Node:
        
        def __init__(self, element, nxt):
            self._element = element 
            self._next = nxt              

    # ------------------------------------------

    def __init__(self):
        self._front = None
        self._rear = None
        self._len = 0

    def is_empty(self):
        "ALT: we could as well test whether self._front is None"
        return self._len == 0
 
    def __len__(self):
        return self._len

    def first(self):
        # Precondition: nonempty queue
        assert self._len > 0
        return (self._front)._element

    def enqueue(self, e):
        new = self._Node(e, None)   
        if self.is_empty():
            self._front = new
        else:
            self._rear._next = new
        self._rear = new
        self._len += 1

    def dequeue(self):
        # Precondition: nonempty queue
        assert self._len > 0
        r = self._front._element
        self._front = self._front._next
        self._len -= 1
        if self.is_empty():
            "the removed front was also the rear!"
            self._rear = None          
        return r

