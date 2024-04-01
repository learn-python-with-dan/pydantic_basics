from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


user = User(id=1, name='Dan')

# serialization
user.model_dump()

# deserialization
User(**{'id': 1, 'name': 'Dan'})
