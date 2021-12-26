class GraphNode(object):

    def __init__(self, id_=""):

        self.id = id_

    def __str__(self):
        return self.id.__str__()


class TreeNode(object):
    def __init__(self, id_=""):
        self.id = id_
        self.left = TreeNode()
        self.right = TreeNode()

    def __str__(self):
        return self.id.__str__()