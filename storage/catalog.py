from storage.schema import SCHEMA


class Catalog:

    def get_tables(self):
        return list(SCHEMA.keys())

    def get_indexes(self, table):
        return SCHEMA[table].get("indexes", set())

    def get_columns(self, table):
        return SCHEMA[table]["columns"]
