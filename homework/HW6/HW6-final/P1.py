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
#        if node.left is None:
##            node = None
#            node.key, node.val, node.size, node.right, node.left = None, None, None, None, None
#        else:
#            print('\n _removemin node.left= \n',node.left,)
#            return(self._removemin(node.left))
#        print('\nnode after=\n',node)
#        return(self)
        
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
        
        print('\n node, key at the start of _remove= \n',node,'\nkey = ',key)
        
        if isinstance(node, BSTNode):
        
            # make a special case for when the child of the node is the key and that child has no children
            if isinstance(node.right, BSTNode):
                if node.right.key==key and node.right.size==1:
                    node.right = None
                  
            if isinstance(node.left, BSTNode):
                if node.left.key==key and node.left.size==1:
                    node.left = None
        
            if node.key < key:
                node = node.right
                return(self._remove(node, key))

            elif node.key > key:
                node = node.left
                return(self._remove(node,key))
                
            elif node.key == key:

                # if it has no children, just remove it
#                if node.size == 1:
##                    node = None
#                    node.key, node.val, node.size, node.right, node.left = None, None, None, None, None

                # if it has one child, replace it with its child
                if node.size == 2:
                    if node.left is not None:
                        node.key, node.val = node.left.key, node.left.val
                    elif node.right is not None:
                        node.key, node.val = node.right.key, node.right.val
                    else:
                        print('Neither node.left nor node.right are not None')
                        
                # if it has two chidren, replace it with the minimum value in the right subtree, and delete that node
                elif node.size > 2:

                    print('\n node.size>2 \n')
#                    print('\n node= \n',node)

                    if node.right is None:
#                        print('\n node when node.right is None= \n',node)
                    
                        # save the info about the node's left child
                        node_left_key, node_left_val, node_left_size = node.left.key, node.left.val, node.left.size
                        
                        print('\n node_left info= \n',node_left_key, node_left_val, node_left_size)
#                        print('\n node before _remove in function \n',node)
                        # remove the node's left child by its key
                        self._remove(node,node_left_key)
                        # replace the node with its left child (now deleted)
                        node.key, node.val = node_left_key, node_left_val
                        node.size = node_left_size
                        
                    # if the node has a right subtree, find the minimum node, delete it & replace the current node with that minimum node
                    else:
                        node_min = node.right
                        while node_min.left is not None:
                            node_min = node_min.left

                        # save info about node_min (on right subtree) to replace node with later
                        node_min_key, node_min_val = node_min.key, node_min.val
                        print('\n node.right before deleting the minimum node in the current nodes right subtree \n',node.right)
                        # delete the minimum node in the current node's right subtree
                        self._remove(node,node_min_key)
                        # replace node with node_min's key and val
                        node.key, node.val = node_min.key, node_min.val
                                    
            else:
                raise KeyError

        else:
            pass


#    def _remove(self, node, key):
#        '''Should be modifying self
#        Reassign the node.key and node.val attributes of the node where key=key'''
#        # TODO: Should return a subtree whose root is  but without
#        #       the node whose key is
##        print('starting node=\n',node)
##        print('starting node key=\n',node.key)
#
##        if new_tree is None:
##            new_tree = BSTTable()
#
#        if node.key < key:
##            new_tree = BSTTable()
##            new_tree.put(node.key,node.val)
#            node = node.left
#            return(self._remove(node, key))
#
#        elif node.key > key:
##            new_tree.put(node.key,node.val)
#            node = node.right
#            return(self._remove(node,key))
#
#        elif node.key == key:
#
##            print('\n node with key?\n',node)
##            print(node.size)
#            # if it has no children, just remove it
#            if node.size == 1:
#                node.key, node.val, node.size, node.right, node.left = None, None, None, None, None
##                print('\n node.size==1 \n')
#                # just don't put it in the tree
##                pass
##                node = None
##                new_tree.put(None)
#            # if it has one child, replace it with its child
#            elif node.size == 2:
##                print('\n node.size==2 \n')
#
#                if node.left is not None:
##                    new_tree.put(node.left.key,node.left.val)
#                    node.key, node.val = node.left.key, node.left.val
#                elif node.right is not None:
#                    new_tree.put(node.right.key,node.right.val)
#                    node.key, node.val = node.right.key, node.right.val
#                else:
#                    print('Neither node.left nor node.right are not None')
#            # if it has two chidren, replace it with the maximum value in the left subtree, and delete that node
#            elif node.size > 2:
##                print('\n node.size>2 \n')
#                print('node with key before=\n',node)
#                if node.right is None:
##                    print('node with key right is None')
#                    # save the info about the node's left child
#                    node_left_key, node_left_val, node_left_size = node.left.key, node.left.val, node.left.size
#                    # remove the node's left child by its key
#                    self._remove(node,node_left_key)
#                    # replace the node with its left child (now deleted)
#                    node.key, node.val = node_left_key, node_left_val
#                    node.size = node_left_size
##                    new_tree.put(node.left.key,node.left.val)
#                ## ACTUALLY WANT TO FIND MINIMUM VALUE IN RIGHT SUBTREE
#                # find maximum value in left subtree
##                print('node=\n',node)
##                print('node.right=\n',node.right)
#            # start traversing the left subtree
#                else:
##                    if node.left is not None:
##                    new_tree.put(node.left.key,node.left.val)
##                    # need to add everything left of the node to new_tree
##                    node_traversing_left = node.left
##                        while node_traversing.left is not None:
##                            new_tree.put(node_traversing.left.key,node_traversing.left.val)
##                            new_tree.put(node_traversing.right.key, node_traversing.right.val)
#
#                    node_min = node.right
##                print('node_max=\n',node_max)
##                try:
##                    while node_max.right is not None:
##                        node_max = node_max.right
##                except AttributeError:
##                print('\n node with key again 1?\n',node)
##                print('\n node_max \n',node_max)
#                    while node_min.left is not None:
##                        while node_min.right is not None:
##                            new_tree.put(node_min.right.val,node_min.right.key)
#                        node_min = node_min.left
##                        print('\n node _max \n',node_max)
#
#                    # save info about node_min (on right subtree) to replace node with later
#                    node_min_key, node_min_val = node_min.key, node_min.val
#                    # delete the minimum node in the current node's right subtree
#                    self._removemin(node.right)
#                    # replace node with node_min's key and val
#                    node.key, node.val = node_min.key, node_min.val
#
#                    # replace node with node_min
##                    new_tree.put(node_min.key,node_min.val)
#                    # delete node_min -- minimum node on the right subtree
##                    new_tree._removemin(node_min)
#
#                # once you have the max node, replace the current node with it
##                print('\n node with key again 2?\n',node)
##                    node = node_min
##                print('\n node with key again 2?\n',node)
#                # if that max node had a child on the left, replace it with that
##                if node_max.left is not None:
##                    node_max = node_max.left
##                # if not, replace the max node with none
##                else:
##                    node_max = None
##            else:
##                print('node.size is {}'.format(node.left.size))
##            print('node reassigned=\n',node)
##            return(new_tree)
#
#        else:
#            raise KeyError


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
#print('\n t._root=\n',t._root)
#print('t._removemin(t._root)=\n',t._removemin(t._root))

#### Testing for remove ###

#t = BSTTable()
#t.put(5, 'a')
#t.put(1, 'b')
#t.put(2, 'c')
#t.put(0, 'd')
#
#print('\n t._root=\n',t._root)
#
##print(t._root.size)
#
##print('t=\n',t)
#
#print('\n t._remove(t._root, 5)=\n',t._remove(t._root, 5))
#
##print('t._remove(t._remove(t._root, 5), 1)=\n',t._remove(t._remove(t._root, 5), 1))
##
##print('t._remove(t._root, 10)=\n',t._remove(t._root, 10))

### my own testing for remove ###

