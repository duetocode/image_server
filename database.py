import contextlib
from pathlib import Path
import sqlite3
from typing import final


class Database:

    _db_file: Path

    def __init__(self, database_file: Path):
        self._db_file = database_file

    def get_image(self, md5_sum) -> bytes:

        conn, cursor = None, None
        try:
            conn = sqlite3.connect(str(self._db_file))
            cursor = conn.cursor()
            cursor.execute("SELECT data FROM image WHERE md5_sum = ?", (md5_sum,))
            row = cursor.fetchone()
            if row is None:
                return None

            return row[0]
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
