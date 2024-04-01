from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


# create a user instance
User(id=1, name='Dan')

# pydantic raises validation error
User(id='Dan', name=1)
