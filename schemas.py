from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    residence_country: str
    email: str

class Country(BaseModel):
    country_name: str
    country_code: str
    additional_info: Optional[str] = None

