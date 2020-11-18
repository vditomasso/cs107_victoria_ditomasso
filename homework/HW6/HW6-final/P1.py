#!/usr/bin/env python3

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
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
        if not node:
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val
            
    def _removemin(self, node):
        
        if node.left.left is not None:
            node.size = node.size-1
            return(self._removemin(node.left))
        else:
            node.left = None
            node.size = node.size-1
        return(self)
    
#    def remove(self, key):
#        self._root = self._remove(self._root, key)
#
#    def _remove(self, node, key)
#        # TODO: Should return a subtree whose root is  but without
#        #       the node whose key is
#        tree = BSTTable()
#
#        # the root is the node we want to remove
#        if self._root.key == key:
#            left_node = self._root.left
            
        
        
#        current_node = self._root
#
#        while current_node is not None:
#            if current_node.key == key:
#                delete_node = current_node
#                break
#            else:
#                if current_node.val>val:
#                    if current_node.left is not None:
#                        direction='left'
#                        current_node=current_node.left
#                    else:
#                        raise KeyError('There is no node with key: {}'.format(key))
#                else:
#                    if point.right is not None:
#                        direction='right'
#                        current_node = current_node.right
#                    else:
#                        raise KeyError('There is no node with key: {}'.format(key))
#            if delete_node.left is None:
#                if delete_node
                        
    @staticmethod
    def _size(node):
        return node.size if node else 0
        
### Testing for removemin ###
t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')
print('t._root=\n',t._root)
print('t._removemin(t._root)=\n',t._removemin(t._root))

#### Testing for remove ###
#
#t = BSTTable()
#t.put(5, 'a')
#t.put(1, 'b')
#t.put(2, 'c')
#t.put(0, 'd')
#
#print(t)
#
#print(t._remove(t._root, 5))
#
#print(t._remove(t._remove(t._root, 5), 1))
