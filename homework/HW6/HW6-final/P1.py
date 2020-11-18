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
        '''I think it's ok that this can't handle when node.left.left does not exist, because that would mean the tree only has 1 node & what would it mean to remove the minimum node from a tree with only one node?'''
        if node.left.left is not None:
            node.size = node.size-1
            return(self._removemin(node.left))
        else:
            node.left = None
            node.size = node.size-1
        return(self)
    
    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        '''CANNOT HANDLE IF THE CURRENT NODE IS THE NODE THAT NEEDS TO BE DELETED
        WOULD IT BE EASIER TO CREATE A SECOND METHOD THAT CAN FIND THE MAXIMUM VALUE IN THE LEFT SUBTREE?'''
        # TODO: Should return a subtree whose root is  but without
        #       the node whose key is
        
        if node.key < key:
            node = node.left
            return(self._remove(node, key))

        elif node.key > key:
            node = node.right
            return(self._remove(node,key))
            
        elif node.key == key:
            # if it has no children, just remove it
            if node.size == 1:
                node = None
            # if it has one child, replace it with its child
            elif node.size == 2:
                if node.left is not None:
                    node = node.left
                elif node.right is not None:
                    node = node.right
                else:
                    print('Neither node.left nor node.right are not None')
            # if it has two chidren, replace it with the maximum value in the left subtree, and delete that node
            elif node.size > 2:
                # find maximum value in left subtree
                node_max = node.right
                while node_max.right is not None:
                    node_max = node.max.right
                # once you have the max node, replace the current node with it
                node = node_max
                # if that max node had a child on the left, replace it with that
                if node_max.left is not None:
                    node_max = node_max.left
                # if not, replace the max node with none
                else:
                    node_max = None
            else:
                print('node.size is {}'.format(node.left.size))
            return(self)
            
        else:
            raise KeyError


#########################################################
### Not sure why I can't just write this for the current node. Why do I need to write it for the current node's children? ###
#        # we want to remove the current node's left child
#        try:
#            if node.left.key==key:
#                # if it has no children, just remove it
#                if node.left.size == 1:
#                    node.left = None
#                # if it has one child, replace it with its child
#                elif node.left.size == 2:
#                    if node.left.left is not None:
#                        node.left = node.left.left
#                    elif node.left.right is not None:
#                        node.left = node.left.right
#                    else:
#                        print('Neither node.left.left nor node.left.right are not None')
#                # if it has two chidren, replace it with the maximum value in the left subtree, and delete that node
#                elif node.left.size > 2:
#                    # find maximum value in left subtree
#                    node_max = node.left.right
#                    while node_max.right is not None:
#                        node_max = node.max.right
#                    # once you have the max node, replace the current node's left child with it
#                    node.left = node_max
#                    # if that max node had a child on the left, replace it with that
#                    if node_max.left is not None:
#                        node_max = node_max.left
#                    # if not, replace the max node with none
#                    else:
#                        node_max = None
#                else:
#                    print('node.left.size is {}'.format(node.left.size))
#                return(self)
#        except:
#            pass
#
#        # we want to remove the current node's right child
#        try:
#            if node.right.key==key:
#                # if it has no children, just remove it
#                if node.right.size == 1:
#                    node.right = None
#                # if it has one child, replace it with its child
#                elif node.right.size == 2:
#                    if node.right.left is not None:
#                        node.right = node.right.left
#                    elif node.right.right is not None:
#                        node.right = node.right.right
#                    else:
#                        print('Neither node.right.left nor node.right.right are not None')
#                # if it has two chidren, replace it with the maximum value in the left subtree, and delete that node
#                elif node.right.size > 2:
#                    # find maximum value in left subtree
#                    node_max = node.right.right
#                    while node_max.right is not None:
#                        node_max = node.max.right
#                    # once you have the max node, replace the current node's left child with it
#                    node.right = node_max
#                    # if that max node had a child on the left, replace it with that
#                    if node_max.left is not None:
#                        node_max = node_max.left
#                    # if not, replace the max node with none
#                    else:
#                        node_max = None
#                else:
#                    print('node.right.size is {}'.format(node.left.size))
#
#        except:
#            pass
#
#        # if we don't want to remove the current node's right or left child, then we need to keep looking for the key
#        if node.key < key:
#            node = node.left
#            return(self._remove(node, key))
#
#        elif node.key > key:
#            node = node.right
#            return(self._remove(node,key))
#
#        else:
#            raise KeyError
            
#######################################################

#        # the current node is the node we want to remove
#        if node.key == key:
#        # if it has no children, just remove it
#            if node.left is not None:
                


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
#t = BSTTable()
#t.put(5, 'a')
#t.put(1, 'b')
#t.put(2, 'c')
#t.put(0, 'd')
#print('t._root=\n',t._root)
#print('t._removemin(t._root)=\n',t._removemin(t._root))

#### Testing for remove ###

t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')

print(t._root.size)

print('t=\n',t)

print('t._remove(t._root, 5)=\n',t._remove(t._root, 5))

print('t._remove(t._remove(t._root, 5), 1)=\n',t._remove(t._remove(t._root, 5), 1))

print('t._remove(t._root, 10)=\n',t._remove(t._root, 10))
