from storage.bplus_node import BPlusNode

class BPlusTree:
    def __init__(self, buffer_pool, root_page_id, order=3):
        self.buffer_pool = buffer_pool
        self.root_page_id = root_page_id
        self.order = order

    def search(self, page_id, key):
        node = self.buffer_pool.get_page(page_id)
        if not node:
            return None

        if node.is_leaf:
            for i, k in enumerate(node.keys):
                if k == key:
                    return node.values[i]
            return None

        for i, k in enumerate(node.keys):
            if key < k:
                return self.search(node.children[i], key)

        return self.search(node.children[-1], key)

    def insert(self, key, value):
        root = self.buffer_pool.get_page(self.root_page_id)
        new = self._insert(root, key, value)

        if new:
            new_root = BPlusNode(self._new_id(), False)
            new_root.keys = [new["key"]]
            new_root.children = [self.root_page_id, new["node"].page_id]
            self.root_page_id = new_root.page_id
            self.buffer_pool.write_page(new_root.page_id, new_root)

    def _insert(self, node, key, value):
        if node.is_leaf:
            node.keys.append(key)
            node.values.append(value)

            combined = sorted(zip(node.keys, node.values))
            node.keys, node.values = zip(*combined)
            node.keys, node.values = list(node.keys), list(node.values)

            self.buffer_pool.write_page(node.page_id, node)

            if len(node.keys) > self.order:
                return self._split_leaf(node)
            return None

        child = self.buffer_pool.get_page(node.children[-1])
        return self._insert(child, key, value)

    def _split_leaf(self, node):
        mid = len(node.keys)//2

        new = BPlusNode(self._new_id(), True)
        new.keys = node.keys[mid:]
        new.values = node.values[mid:]

        node.keys = node.keys[:mid]
        node.values = node.values[:mid]

        new.next = node.next
        node.next = new.page_id

        self.buffer_pool.write_page(node.page_id, node)
        self.buffer_pool.write_page(new.page_id, new)

        return {"key": new.keys[0], "node": new}

    def _new_id(self):
        import random
        return random.randint(1000, 9999)
