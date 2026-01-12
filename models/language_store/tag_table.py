from datetime import datetime

class TagTable:
    def __init__(self):
        self.id: int
        self.tag: str
        self.is_active: bool
        self.created_at: datetime
        self.updated_at: datetime
        self.deleted_at: str
