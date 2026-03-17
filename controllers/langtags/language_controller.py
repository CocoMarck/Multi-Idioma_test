from repositories.langtags.language_repository import LanguageRepository
from models.langtags.language import Language

class LanguageController:
    def __init__(self, repository:LanguageRepository, table:Language):
        self.repository = repository
        self.table = table

    # Funciones genericas
    def get_columns(self):
        return self.repository.table.get_columns()

    def get_column_values(self):
        return self.repository.table.get_column_values()

    # Especificas
    def get_row(self, code_id) -> bool:
        row = self.repository.get_row( code_id )
        if len(row) > 0:
            self.table.language_id = row[0]
            self.table.code = row[1]
            self.table.created_at = row[2]
            self.table.updated_at = row[3]
            self.table.deleted_at = row[4]
            return True
        else:
            return False

    def get_code_row(self, code:str) -> bool:
        code_id = self.repository.get_code_id( code )
        return self.get_row( code_id )

    def update(self) -> bool:
        return self.repository.update_code( self.table.language_id, self.table.code )

    def insert(self) -> bool:
        if isinstance(self.table.code, str):
            return self.repository.insert_code( self.table.code )
        return False

    def save(self):
        if self.repository.exists( self.table.language_id ):
            return self.update()
        return self.insert()

    def is_deleted(self):
        return self.repository.is_deleted( self.table.language_id )
