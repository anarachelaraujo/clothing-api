from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    is_active: bool  # Renamed the field from 'not' to 'is_active'
