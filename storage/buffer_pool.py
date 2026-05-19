class BufferPool:
    def __init__(self, disk, capacity=50):
        self.disk = disk
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get_page(self, page_id):
        if page_id in self.cache:
            self.lru.remove(page_id)
            self.lru.append(page_id)
            return self.cache[page_id]

        page = self.disk.read_page(page_id)
        if page is None:
            return None

        self._put(page_id, page)
        return page

    def write_page(self, page_id, page):
        self._put(page_id, page)
        self.disk.write_page(page_id, page)

    def _put(self, page_id, page):
        if page_id in self.cache:
            self.cache[page_id] = page
            return

        if len(self.cache) >= self.capacity:
            old = self.lru.pop(0)
            self.cache.pop(old, None)

        self.cache[page_id] = page
        self.lru.append(page_id)
