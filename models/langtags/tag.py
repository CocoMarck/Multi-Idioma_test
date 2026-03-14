from .control_fields

class Tag(ControlFields):
    def __init__(self):
        super().__init__()

        self.tag_id: int = None
        self.tag_key: str = None
