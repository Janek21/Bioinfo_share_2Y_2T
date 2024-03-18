class Our_Stack:

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
        self._top = None
        self._len = 0

    def is_empty(self):
        "ALT: we could as well test whether self._top is None"
        return self._len == 0
 
    def __len__(self):
        return self._len

    def push(self, e):
        self._top = self._Node(e, self._top)
        self._len += 1

    def top(self):
        # Precondition: nonempty stack
        assert self._len > 0
        return self._top._element

    def pop(self):
        # Precondition: nonempty stack
        assert self._len > 0
        r = self._top._element
        self._top = (self._top)._next 
        self._len -= 1
        return r

