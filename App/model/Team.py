from pydantic import BaseModel
from typing import Optional


class TeamModel(BaseModel):
    id: Optional[int] = None
    name: str


class Team:
    __id = None
    __name = None

    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.__id = kwargs.get("id")
        self.__name = kwargs.get("name")

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__str__()

    def set_id(self, id: int):
        self.__id = id

    def set_name(self, name: str):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
