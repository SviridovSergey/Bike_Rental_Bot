from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Application:
    user_id: int
    full_name: str
    phone: str
    location: str
    service: str
    date: str
    created_at: datetime
    status: str = "new"

    def to_dict(self):
        return{
            "user_id":self.user_id,
            "full_name":self.full_name,
            "phone":self.phone,
            "location":self.location,
            "service":self.service,
            "date":self.date,
            "created_at":self.created_at.isoformat(),
            "status":self.status
        }