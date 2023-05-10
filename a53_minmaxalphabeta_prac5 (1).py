class TreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def CreateTreeFromList(arr):

    n = len(arr)
    tree = []

    if(n == 0):
        return None

    root = TreeNode(arr[1])
    tree.append(root)

    for i in range(1, n):

        currIndex = i
        parIndex = (i-1)//2

        isLeft = True

        if(i % 2 == 0):
            isLeft = False

        currNode = TreeNode(arr[currIndex])
        parNode = tree[parIndex]

        tree.append(currNode)

        if(isLeft):
            parNode.left = currNode
        else:
            parNode.right = currNode

    return tree


def inOrderTraversal(root, arr):

    if(root == None):
        return

    inOrderTraversal(root.left, arr)
    arr.append(root.data)
    inOrderTraversal(root.right, arr)


def MinMax(root, isMaxLevel):

    if(root == None):
        return 0

    if(root.left == None and root.right == None):
        return root.data

    if(isMaxLevel == True):

        leftval = MinMax(root.left, False)
        rightval = MinMax(root.right, False)

        ans = max(leftval, rightval)
        root.data = ans

        return ans

    else:

        leftval = MinMax(root.left, True)
        rightval = MinMax(root.right, True)

        ans = min(leftval, rightval)
        root.data = ans

        return ans


def alphaBetaPruning(root, isMaxLevel, alpha, beta):

    if(root == None):
        return 0

    if(root.left == None and root.right == None):
        return root.data

    if(isMaxLevel == True):

        leftval = alphaBetaPruning(root.left, False, alpha, beta)

        alpha = max(alpha, leftval)

        if(beta <= alpha):
            return alpha

        rightval = alphaBetaPruning(root.right, False, alpha, beta)

        ans = max(leftval, rightval)
        root.data = ans

        alpha = max(alpha, rightval)

        if(beta <= alpha):
            return ans

        return ans

    else:

        leftval = alphaBetaPruning(root.left, True, alpha, beta)

        beta = min(beta, leftval)

        if(beta <= alpha):
            return beta

        rightval = alphaBetaPruning(root.right, True, alpha, beta)

        ans = min(leftval, rightval)
        root.data = ans

        beta = min(beta, ans)

        if(beta <= alpha):
            return ans

        return ans


arr = [80, 30, 25, 35, 55, 20, 5, 65, 40, 10, 70, 15, 50, 45, 60, 75]


for i in range(15):
    arr.insert(0, 0)

print(arr)

treeList = CreateTreeFromList(arr)
root = treeList[0]

traversal = []
inOrderTraversal(root, traversal)
print(traversal)

print("Tree Constructed : ", end=" ")
for i in treeList:
    print(i.data, end=", ")

answer = MinMax(root, True)

print(f'Value from Min-Max Algorithm : {answer}')

print("Tree Constructed : ", end=" ")
for i in treeList:
    print(i.data, end=", ")


arr = [80, 30, 25, 35, 55, 20, 5, 65, 40, 10, 70, 15, 50, 45, 60, 75]


for i in range(15):
    arr.insert(0, 0)

print(arr)

treeList = CreateTreeFromList(arr)
root = treeList[0]

traversal = []
inOrderTraversal(root, traversal)
print(traversal)

print("Tree Constructed : ", end=" ")
for i in treeList:
    print(i.data, end=", ")

answer = alphaBetaPruning(root, True, -99999, 99999)

print(f'Value from Min-Max Algorithm : {answer}')

print("Tree Constructed : ", end=" ")
for i in treeList:
    print(i.data, end=", ")
