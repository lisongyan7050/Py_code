
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root
#先序便利
def preOrderBT(root):
    if not root:
        return None
    print(root.val, end='\t')
    preOrderBT(root.left)
    preOrderBT(root.right)


def rob(root):
    if root==None:
        return 0
    result=dfs(root)
    return max(result[0],result[1])
def dfs(root):
    if root==None:
        return [0,0]
    result = [0, 0]
    if root.left:
        left = dfs(root.left)
    else:
        left = [0, 0]
    if root.right:
        right = dfs(root.right)
    else:
        right = [0, 0]

    result[0]=root.val+left[1]+right[1]
    result[1]=max(left[0],left[1])+max(right[0],right[1])
    return result

if __name__ == '__main__':
    llist = [1, 2,3]
    root = listCreatTree(None, llist, 0)
    result=rob(root)
    print("结果是"+str(result))

