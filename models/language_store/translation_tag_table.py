from datetime import datetime

class TranslationTagTable:
    def __init__(self):
        self.id: int
        self.language_id: int
        self.tag_id: int
        self.text: str
        self.is_active: bool
        self.created_at: datetime
        self.updated_at: datetime
        self.deleted_at: str
