import os, pickle

class DiskManager:
    def __init__(self, path="data/pages"):
        self.path = path
        os.makedirs(path, exist_ok=True)

    def write_page(self, page_id, data):
        with open(f"{self.path}/{page_id}.pg", "wb") as f:
            pickle.dump(data, f)

    def read_page(self, page_id):
        file = f"{self.path}/{page_id}.pg"
        if not os.path.exists(file):
            return None
        with open(file, "rb") as f:
            return pickle.load(f)
