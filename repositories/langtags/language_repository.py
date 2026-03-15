from core.sqlite.standard_table import StandardTable
from core.sqlite.standard_database import StandardDatabase
from utils.datetime_util import get_datetime_now, set_datetime_formatted

class LanguageRepository:
    def __init__(self, table: StandardTable):
        self.table = table
        self.database = self.table.database

    def update_code(self, language_id:int, code: str):
        try:
            cursor = self.database.execute(
                statement=f"UPDATE {self.table.name} SET code=?, updated_at=? WHERE language_id=?;", commit=True, params=(code,get_datetime_now(),language_id)
            )
            return True
        except:
            return False

    def insert_code(self, code:str):
        try:
            cursor = self.database.execute(
                statement=(
                    f"INSERT INTO {self.table.name} (code,created_at) VALUES(?, ?);"
                ),
                commit=True, params=(code,get_datetime_now())
            )
            return True
        except:
            return False

    def code_exists(self, language_id:int, code: str) -> bool:
        try:
            cursor = self.database.execute(
                statement=f'SELECT 1 FROM {self.table.name} WHERE language_id=? AND code=? LIMIT 1;',
                commit=False, params=(language_id,code)
            )
            return cursor.fetchone() is not None
        except:
            return False

    def get_code_id(self, code:str) -> int | None:
        try:
            cursor = self.database.execute(
                statement=f"SELECT language_id FROM {self.table.name} WHERE code=? LIMIT 1;",
                commit=False, params=(code,)
            )
            row = cursor.fetchone()
            return row[0] if row else None
        except:
            return None

    def save_code(self, code:str):
        language_id = self.get_code_id(code)
        updated = False
        inserted = False
        if language_id is not None:
            updated = self.update_code( language_id, code )
        if updated == False:
            inserted = self.insert_code( code )
        return updated or inserted


    def deactivate(self, language_id: int):
        try:
            cursor = self.database.execute(
                statement=f"UPDATE {self.table.name} SET deleted_at=? WHERE language_id=?;",
                commit=True, params=(get_datetime_now(), language_id)
            )
            return True
        except:
            return False

    def activate(self, language_id: int):
        try:
            cursor = self.database.execute(
                statement=f"UPDATE {self.table.name} SET deleted_at=? WHERE language_id=?;",
                commit=True, params=(None, language_id)
            )
            return True
        except:
            return False

    def is_deleted(self, language_id:str) -> bool:
        try:
            cursor = self.database.execute(
                statement=f"SELECT deleted_at FROM {self.table.name} WHERE language_id=? LIMIT 1;",
                commit=False, params=(language_id,)
            )
            row = cursor.fetchone()
            return row[0] is not None
        except:
            return False

    def toggle_code_state(self, code: str):
        language_id = self.get_code_id(code)
        if language_id is not None:
            deleted = self.is_deleted( language_id )
            if deleted:
                return self.activate( language_id )
            else:
                return self.deactivate( language_id )
        return False
