# Corey Sokol

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

# This is the function that handles mathematical expressions that
# do not have spaces between every character.

def listAdjust(alist):
    brokenList = list(alist)
    
    # Setting the counters
    i = 0
    count = len(brokenList)
    
    while i < count:
        # Checks if i and the item in the next index are both numerical digits
        # If so combine them and pop the next item in the list
        if brokenList[i].isdigit() and brokenList[i + 1].isdigit():
            brokenList[i] = brokenList[i] + brokenList[i + 1]
            brokenList.pop(i + 1)
            count = count - 1
        i = i + 1
    return brokenList
    

def buildParseTree(fpexp):
    breakList = listAdjust(fpexp)
    #fplist = breakList.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in breakList:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("((10+5)*3)")
pt.postorder()
