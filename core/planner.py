class ExecutionPlan:

    def __init__(self, op_type, table, where=None, use_index=False, index_column=None):
        self.op_type = op_type
        self.table = table
        self.where = where
        self.use_index = use_index
        self.index_column = index_column

    def to_dict(self):
        return self.__dict__


from storage.schema import SCHEMA


class Planner:

    def create_plan(self, ast):

        op_type = "SELECT"
        if getattr(ast, "joins", []):
            op_type = "JOIN"

        use_index = False
        index_column = None

        if ast.where:

            col, val = ast.where

            # -------------------------
            # AUTO INDEX CHECK
            # -------------------------
            if col in SCHEMA[ast.table]["indexes"]:
                use_index = True
                index_column = col

        return ExecutionPlan(
            op_type=op_type,
            table=ast.table,
            where=ast.where,
            use_index=use_index,
            index_column=index_column
        )