from enum import Enum
from typing import List
from pydantic import BaseModel

class PydanticEnum(Enum):
    @classmethod
    def __get_validators__(cls):
        cls.lookup = {v: k.value for v, k in cls.__members__.items()}
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return cls.lookup[v]
        except KeyError:
            raise ValueError(f'{v} is not a valid option for {cls.__name__}')

class Action(PydanticEnum):
    accept = 1
    drop = 2

class Device(BaseModel):
    '''A class that represents a device on the network'''
    name: str
    mac_address: str    

class Group(BaseModel):
    name: str
    members: List[Device]

class Rule(BaseModel):
    priority: int
    name: str
    action: Action
