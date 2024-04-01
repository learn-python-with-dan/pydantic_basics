from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Role(Enum):
    READER = 'r'
    EDITOR = 'e'
    ADMIN = 'a'


class Location(BaseModel):
    city: str
    country: str


class User(BaseModel):
    id: int
    name: str
    created_at: datetime
    role: Role
    team_member_ids: list[int]
    location: Location = None


User(
    id=1,
    name='Dan',
    created_at=datetime.now(),
    role=Role.ADMIN,
    team_member_ids=[2, 3, 4],
    location=Location(
        city='some city',
        country='some country',
    )
)
