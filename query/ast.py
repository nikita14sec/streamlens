class Select:

    def __init__(self, table):
        self.type = "SELECT"
        self.table = table
        self.where = None
        self.joins = []

    def to_dict(self):
        return self.__dict__


class Join:

    def __init__(self, table, l, r):
        self.type = "JOIN"
        self.table = table
        self.left_key = l
        self.right_key = r