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
        pass
 
    def __len__(self):
        pass

    def first(self):
        pass

    def enqueue(self, e):
        pass

    def dequeue(self):
        pass

