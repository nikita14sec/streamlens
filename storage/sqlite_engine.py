import sqlite3
from storage.schema import SCHEMA


class SQLiteEngine:

    def __init__(self, index_manager):

        self.conn = sqlite3.connect(
            "data/streamlens.db",
            check_same_thread=False
        )
        self.cursor = self.conn.cursor()

        self.index_manager = index_manager

    # =====================================================
    # FULL TABLE SCAN
    # =====================================================
    def full_scan(self, table):

        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

    # =====================================================
    # BUILD ALL INDEXES FOR TABLE
    # =====================================================
    def build_all_indexes(self, table):

        schema = SCHEMA.get(table)

        if not schema:
            return

        indexes = schema.get("indexes", set())
        columns = schema["columns"]

        rows = self.full_scan(table)

        for col in indexes:

            self.index_manager.create_index(table, col)

            col_idx = columns[col]

            for row in rows:

                key = row[col_idx]
                self.index_manager.add(table, col, key, row)