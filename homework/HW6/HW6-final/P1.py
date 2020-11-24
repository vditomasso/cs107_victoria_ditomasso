#!/usr/bin/env python3
from enum import Enum
import numpy as np

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
        '''Should return a new tree, not modify self'''
        new_tree = self
        return new_tree._remove(new_tree, key)

    def _remove(self, node, key):
        '''Should be modifying self
        Reassign the node.key and node.val attributes of the node where key=key'''
        # TODO: Should return a subtree whose root is  but without
        #       the node whose key is
        
#        print('\n node, key at the start of _remove= \n',node,'\nkey = ',key)
#        print('\nnode at the start of _remove\n',node)
#        print('\nnode.size at start of _remove=',node.size)
#        print('\nkey',key)
        
        ### This code block handles removal of a leaf ###
        if isinstance(node, BSTNode):
#            print('\nnode is a BSTNode')
            # make a special case for when the child of the node is the key and that child has no children
            if isinstance(node.right, BSTNode):
                if node.right.key==key and node.right.size==1:
                    print('\nnode.right.key==key')
                    node.right = None
                    node.size = node.size - 1
                    return(self)
                  
            if isinstance(node.left, BSTNode):
                if node.left.key==key and node.left.size==1:
                    print('\nnode.left.key==key')
                    node.left = None
                    node.size = node.size - 1
                    return(self)
                        
            if node.key < key:
                print('\nnode.key < key')
                node.size = node.size - 1
                node = node.right
                return(self._remove(node, key))

            elif node.key > key:
                print('\nnode.key > key')
                node.size = node.size - 1
                node = node.left
                return(self._remove(node,key))
        ### End of code block that handles removing a leaf ###
                
        ### Replace a node (the current node) -- not a leaf ###
            elif node.key == key:

                # if it has one child, replace it with its child
                if node.size == 2:
                    print('\nnode.size == 2')
                    if node.right is not None:
                        node.key, node.val = node.right.key, node.right.val
                        node.right = None
                        node.size = node.size - 1
                        return(self)
                    elif node.left is not None:
                        node.key, node.val = node.left.key, node.left.val
                        node.left = None
                        node.size = node.size - 1
                        return(self)
                    else:
                        print('Neither node.left nor node.right are not None')

                # If there's no right subtree, find the highest value in the left subtree
                elif node.size > 2:
                    print('\n node.size>2')

                    if node.right is None:
                        # find the max in the node's left subtree
                        node_max = node.left
                        while node_max.right is not None:
                            node_max = node_max.right
                        # save info about node_max (on left subtree) to replace node with later
                        node_max_key, node_max_val = node_max.key, node_max.val
                        print('\nnode_max_key, node_max_val=',node_max_key, node_max_val)
                        # delete the maximum node in the current node's right subtree
                        self._remove(node,node_max_key)
                        # replace node with node_max's key and val
                        node.key, node.val = node_max_key, node_max_val
                        return(self)

                    # if the node has a right subtree, find the minimum node, delete it & replace the current node with that minimum node
                    else:
                        node_min = node.right
                        while node_min.left is not None:
                            node_min = node_min.left

                        # save info about node_min (on right subtree) to replace node with later
                        node_min_key, node_min_val = node_min.key, node_min.val
                        # delete the minimum node in the current node's right subtree
                        self._remove(node,node_min_key)
                        # replace node with node_min's key and val
                        node.key, node.val = node_min_key, node_min_val
                        return(self)

        else:
            raise TypeError('Either key does not exist in this tree or node is not a BSTNode.')
                        
    @staticmethod
    def _size(node):
        return node.size if node else 0
         
class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.bst = tree
        self.traversalType = traversalType
        self.returned = []
        self.node = self.bst._root
#        self.index = 0
#        self.visited = np.zeros(len(self.bst))

    def __iter__(self):
#        self.node = self.bst._root
#        print('\nself in __iter__\n',self)
#        print('\nself.node in __iter__\n',self.node)
        return self

    def __next__(self):
        if self.traversalType == DFSTraversalTypes.PREORDER:
            return(self.preorder(self.bst))
        elif self.traversalType == DFSTraversalTypes.INORDER:
            return(self.inorder(self.bst))
        elif self.traversalType == DFSTraversalTypes.POSTORDER:
            return(self.postorder(self.bst))
        else:
            raise AttributeError('self.traversalType must be a DFSTraversalType')
            
    def inorder(self, bst: BSTTable):
        
#        print(self.node at the start )
#        print('\nself.node at start of inorder\n', self.node)
        
        if len(self.returned) == len(self.bst):
            raise StopIteration

        if isinstance(self.node.left,BSTNode) and self.node.left.key not in self.returned:
#            print('left')
#            print(self.node)
#            current_node = self.node
            self.node = self.node.left
#            print(self.node)
            return(self.inorder(self.bst))
            
        elif self.node.key not in self.returned:
#            print('current')
            self.returned.append(self.node.key)
            return(self.node)
            
        elif isinstance(self.node.right,BSTNode) and self.node.right.key not in self.returned:
#            print('right')
            self.node = self.node.right
            return(self.inorder(self.bst))
            
        else:
#            print(self.returned)
            self.node = self.bst._root
            return(self.inorder(self.bst))
        
    def preorder(self, bst: BSTTable):

#        print('\nnode at start\n',self.node)

        if len(self.returned) == len(self.bst):
            raise StopIteration

        if self.node.key not in self.returned:
#            print('current')
            self.returned.append(self.node.key)
            return(self.node)

        elif isinstance(self.node.left,BSTNode) and self.node.left.key not in self.returned:
#            print('left')
            self.node = self.node.left
            return(self.preorder(self.bst))
            
        elif isinstance(self.node.right,BSTNode) and self.node.right.key not in self.returned:
#            print('right')
            self.node = self.node.right
            return(self.preorder(self.bst))
            
        else:
            self.node = self.bst._root.right
            return(self.preorder(self.bst))
            
    def postorder(self, bst: BSTTable):
    
        if len(self.returned) == len(self.bst):
            raise StopIteration
            
        if isinstance(self.node.left,BSTNode) and self.node.left.key not in self.returned:
            self.node = self.node.left
            return(self.postorder(self.bst))
            
        elif isinstance(self.node.right,BSTNode) and self.node.right.key not in self.returned:
#            print('right')
            self.node = self.node.right
            return(self.postorder(self.bst))

        elif self.node.key not in self.returned:
            self.returned.append(self.node.key)
            return(self.node)
            
        else:
            self.node = self.bst._root
            return(self.postorder(self.bst))

### Testing DFSTraversal ###

input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
bst = BSTTable()
for key, val in input_array:
    bst.put(key, val)
#print(bst)
traversal = DFSTraversal(bst, DFSTraversalTypes.PREORDER)
for node in traversal:
    print(str(node.key) + ', ' + node.val)

    
