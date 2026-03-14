import sqlite3
import pathlib

class StandardDatabase():
    def __init__(self, directory: pathlib.Path, name: str  ):
        self.directory = directory
        self.name = name

    def get_path(self):
        path = self.directory.joinpath( self.name )
        return path

    def _connect(self):
        return sqlite3.connect( self.get_path() )

    def execute( self, statement:str, commit: bool, params: tuple=() ):
        '''
        Devuelve un cursor
        '''
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION") # Iniciar transacción Para que jale el rollback
            cursor.execute(statement, params)

            if commit:
                conn.commit()
            else:
                conn.rollback()

            return cursor

    def create_file(self):
        if self.get_path().exists():
            return False
        conn = self._connect()
        conn.close()
        return True

    def delete(self):
        path = self.get_path()
        if not path.exists():
            return False
        return pathlib.Path.unlink( path )

    def get_tables(self):
        cursor = self.execute(
            statement=(
                "SELECT name FROM sqlite_master WHERE type='table';"
            ), commit=False
        )
        return cursor.fetchall()

    def get_table_names(self):
        tables = []
        for name, _ in self.get_tables():
            tables.append( name )
        return tables

    def table_exists(self, table: str) -> bool:
        return table in self.get_table_names()

    def drop_table(self, table: str) -> bool:
        exists = self.table_exists(table)
        if exists:
            cursor = self.execute(
                statement=f"DROP TABLE {table};",
                commit=True
            )

        return not exists

    def drop_all_tables(self):
        tables = self.get_table_names()
        for name in tables:
            self.delete_table(name)
        return len(tables) > 0
