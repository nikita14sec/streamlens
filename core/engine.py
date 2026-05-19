import time
from storage.disk_manager import DiskManager
from storage.buffer_pool import BufferPool
from storage.index_manager import IndexManager

class Engine:
    def __init__(self):
        self.disk = DiskManager()
        self.buffer_pool = BufferPool(self.disk)
        self.index_manager = IndexManager(self.buffer_pool)

        self._seed()

    def _seed(self):
        self.index_manager.create_index("users", "id")
        for i, name in [(1,"alice"),(2,"bob"),(3,"charlie")]:
            self.index_manager.add("users","id",i,[i,name])

    def run(self, sql):
        start = time.time()

        if "WHERE id =" in sql:
            key = int(sql.split("=")[-1])
            res = self.index_manager.search("users","id",key)
            return {
                "path":"INDEX_SCAN",
                "data":res,
                "latency":round((time.time()-start)*1000,2)
            }

        return {
            "path":"FULL_SCAN",
            "data":[[1,"alice"],[2,"bob"],[3,"charlie"]],
            "latency":round((time.time()-start)*1000,2)
        }
