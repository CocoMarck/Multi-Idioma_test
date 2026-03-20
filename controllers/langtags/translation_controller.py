from .base_controller import BaseController

class TranslationController(BaseController):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, attributes={ "id": "translation_id", "value": "value" }, **kwargs)

    def get_row(self, value_id) -> bool:
        row = self.repository.get_row( value_id )
        if len(row) > 0:
            setattr(self.model, self._ATTRIBUTES['id'], row[0])
            self.model.tag_id = row[1]
            self.model.language_id = row[2]
            setattr(self.model, self._ATTRIBUTES['value'], row[3])
            self.model.created_at = row[4]
            self.model.updated_at = row[5]
            self.model.deleted_at = row[6]
            return True
        else:
            return False

    def get_translation_row(self, tag_name, language_code) -> bool:
        value_id = self.repository.get_translation_id( tag_name, language_code )
        return self.get_row( value_id )

    def save(self, value_id, tag_id, language_id, value, is_deleted):
        save = self.repository.save( value_id, tag_id, langauge_id, value, is_deleted )
        if self.repository.exists( value_id ):
            self.get_row( value_id )
        else:
            self.get_value_row( value )
        return save

    def save_value(self, tag_name, language_code, value, is_deleted=False ):
        save = self.repository.save_value( tag_name, language_code, value, is_deleted )
        if save:
            self.get_translation_row( tag_name, language_code )
        return save
