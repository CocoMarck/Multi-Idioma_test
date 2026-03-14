import sqlite3
from models.langtags import Translation

class TranslationRepository:
    def __init__(self, conn):
        self.conn = conn
