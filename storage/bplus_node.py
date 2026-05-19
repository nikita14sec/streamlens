class BPlusNode:
    def __init__(self, page_id, is_leaf=False):
        self.page_id = page_id
        self.is_leaf = is_leaf
        self.keys = []
        self.values = []
        self.children = []
        self.next = None
