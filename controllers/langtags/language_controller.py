from repositories.langtags.language_repository import LanguageRepository
from models.langtags.language import Language

class LanguageController:
    def __init__(self, repository:LanguageRepository, model:Language):
        self.repository = repository
        self.model = model

    # Funciones genericas
    def get_columns(self):
        return self.repository.table.get_columns()

    def get_column_values(self):
        return self.repository.table.get_column_values()

    # Especificas
    def get_row(self, code_id) -> bool:
        row = self.repository.get_row( code_id )
        if len(row) > 0:
            self.model.language_id = row[0]
            self.model.code = row[1]
            self.model.created_at = row[2]
            self.model.updated_at = row[3]
            self.model.deleted_at = row[4]
            return True
        else:
            return False

    def get_code_row(self, code:str) -> bool:
        code_id = self.repository.get_code_id( code )
        return self.get_row( code_id )

    def update(self, language_id, code) -> bool:
        if self.repository.update_code( language_id, code ):
            self.get_row( language_id )
            return True
        return False

    def insert(self, code) -> bool:
        if isinstance(code, str):
            if self.repository.insert_code( code ):
                self.get_code_row( code )
                return True
        return False

    def save(self, language_id, code):
        if self.repository.exists( language_id ):
            return self.update( language_id, code)
        return self.insert( code )

    def is_deleted(self, language_id):
        return self.repository.is_deleted( language_id )

    def is_model_deleted(self):
        return self.repository.is_deleted( self.model.language_id )
