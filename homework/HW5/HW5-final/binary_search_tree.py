#!/bin/usr python3

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
    # self is the BSTTable, ie the BST itself
    # node is the root of the subtree that you want the key:value pair inserted -> is going to be self._root
    # should return the new root of this subtree
        if node is None:
            node = BSTNode(key, val)
        else:
            try: # check to see if key is already in the tree
                if node.left.key == key:
                    node.left.val = val
                if node.right.key == key:
                    node.right.val = val
            except:
                if node.key>key:
                    node.left = BSTNode(key, val)
                    node.size += 1
                else:
                    node.right = BSTNode(key, val)
                    node.size += 1
        return(node)

    def _get(self, node, key):
    # node is the root of the subtree that you're searching -> self._root
    # return the value associated with key in that subtree
    # raise a KeyError is no such not is found
        if node.left.key == key:
            return(node.left.val)
        elif node.right.key == key:
            return(node.right.val)
        else:
            raise KeyError('There is no value with key: {} in the subtree with root: {}, {}'.format(key, node.key, node.val))

    @staticmethod
    def _size(node):
        return node.size if node else 0

### Testing ###

greektoroman = BSTTable()
greektoroman.put('Athena',    'Minerva')
greektoroman.put('Eros',      'Cupid')
greektoroman.put('Aphrodite', 'Venus')
#greektoroman.put('Eros',      'Stupid new thing')
#print(greektoroman.get('Eros'))
#print(greektoroman._size())
## Should print 'Cupid'
print(greektoroman)
