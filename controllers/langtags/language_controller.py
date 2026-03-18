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

    def activate_model(self):
        return self.repository.activate( self.model.language_id )

    def deactivate_model(self):
        return self.repository.deactivate( self.model.language_id )

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

    def update(self, language_id, code, is_deleted) -> bool:
        if self.repository.update_code( language_id, code, is_deleted ):
            self.get_row( language_id )
            return True
        return False

    def insert(self, code) -> bool:
        if isinstance(code, str):
            if self.repository.insert_code( code, is_deleted ):
                self.get_code_row( code )
                return True
        return False

    def save(self, language_id, code, is_deleted):
        save = self.repository.save( language_id, code, is_deleted )
        if self.repository.exists( language_id ):
            self.get_row( language_id )
        else:
            self.get_code_row( code )
        return save

    def is_deleted(self, language_id):
        return self.repository.is_deleted( language_id )

    def is_model_deleted(self):
        return self.repository.is_deleted( self.model.language_id )

    def toggle_model_state(self):
        return self.repository.toggle_row_state( self.model.language_id )
