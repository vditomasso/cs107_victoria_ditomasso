#!/bin/usr python3

class LinkedList:

    def __init__(self, head, tail):
        assert isinstance(tail, LinkedList) or isinstance(tail, Nil), TypeError(
            'tail should either be a LinkedList or a Nil')
        self._head, self._tail = head, tail

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        return str(self._head) + ' -> ' + str(self._tail)

    def __repr__(self):
        return f'LinkedList({repr(self._head)}, {repr(self._tail)})'

    def __len__(self):
        return 1 + len(self._tail)

    def __getitem__(self, i):
        return self._head if i == 0 else self._tail[i-1]

    def prepend(self, val):
        pass # TODO

    def append(self, val):
        # Make a new node with the value as the head and Nil as the tail, since it will be the new end of the linked list
        new_node = Nil().append(val)
        for i in reversed(range(len(self))):
            new_node = LinkedList(self[i],new_node)
        return(new_node)

    def for_each(self, fun):
        pass # TODO

    def summation(self):
        return self._head + self._tail.summation() if self._tail else self._head

    def minimum(self):
        def smaller(a, b):
            return a if a < b else b
        return smaller(self._head, self._tail.minimum()) if self._tail else self._head

    def reduce_right(self, fun):
        pass # TODO

class Nil():

    def __str__(self):
        return 'Nil'

    def __repr__(self):
        return 'Nil()'

    def __len__(self):
        return 0

    def __getitem__(self, i):
        raise IndexError('index out of range')

    def __bool__(self):
        return False

    def prepend(self, val):
        pass # TODO

    def append(self, val):
        return LinkedList(val, Nil())

    def for_each(self, fun):
        pass # TODO

### Testing ###
ll = LinkedList(1,LinkedList('a',Nil()))
print(ll)
ll2 = ll.append(2)
print(ll2)
#ll2 = LinkedList(1,LinkedList(2,Nil()))
ll3 = ll2.append(3)
print(ll3)

