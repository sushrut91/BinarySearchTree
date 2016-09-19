#Check submodule
from PythonNode import Node
from PythonNode import Tree

def main():
    bst = Tree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(16)
    print "PreOrder"
    bst.preorder()
    print "Post Order"
    bst.postorder()
if __name__ == '__main__':
    main()
