from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @validator('account_id')
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f'account_id must be positive: {value}')
        return value


user = User(name='Fatma', email='fatmasliti289@gmail.com', account_id='123')

print(user)

####################################
#Pydantic VS Dataclasses
#Dataclasses: python built in model that solves a similar problem (create a class with fields)

#python already has some data modeling and type hinting capabilities on its own

#Type hinting
x: int = 0
y: str = 'hello'

#Data classes
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int
