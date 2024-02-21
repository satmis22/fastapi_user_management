from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):

    # User model representing user data

    id: Optional[int] = Field(default=None, primary_key=True)                    # Unique identifier for the user

    first_name: str                        #first name of the user.

    last_name: str                        #Last name of the user

    phone_number: str
    residence_country: str
    email: str