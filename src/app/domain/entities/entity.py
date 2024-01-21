from datetime import datetime

class Entity():
    id: int
    created_at: datetime
    
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at