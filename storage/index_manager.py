from storage.bplustree import BPlusTree
from storage.bplus_node import BPlusNode

class IndexManager:
    def __init__(self, buffer_pool):
        self.buffer_pool = buffer_pool
        self.indexes = {}

    def create_index(self, table, col):
        if table not in self.indexes:
            self.indexes[table] = {}

        root_id = abs(hash(table+col)) % 10000
        root = BPlusNode(root_id, True)

        self.buffer_pool.write_page(root_id, root)

        self.indexes[table][col] = BPlusTree(self.buffer_pool, root_id)

    def add(self, table, col, key, row):
        self.indexes[table][col].insert(key, row)

    def search(self, table, col, key):
        return self.indexes[table][col].search(
            self.indexes[table][col].root_page_id,
            key
        )
