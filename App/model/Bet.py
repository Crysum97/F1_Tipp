from pydantic import BaseModel
from typing import Optional


class BetModel(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    user: str
    team: Optional[str] = None
    team_id: Optional[int] = None
    first_driver: str
    first_pl: int
    second_driver: str
    second_pl: int
    event: Optional[str] = None


class Bet:
    __id = None
    __user_id = None
    __user = None
    __team = None
    __team_id = None
    __first_driver = None
    __first_pl = None
    __second_driver = None
    __second_pl = None
    __event = None

    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.__id = kwargs.get("id")
        if "user_id" in kwargs:
            self.__user_id = kwargs.get("user_id")
        self.__user = kwargs.get("user")
        if "team" in kwargs:
            self.__team = kwargs.get("team")
        if "team_id" in kwargs:
            self.__team_id = kwargs.get("team_id")
        self.__first_driver = kwargs.get("first_driver")
        self.__first_pl = kwargs.get("first_pl")
        self.__second_driver = kwargs.get("second_driver")
        self.__second_pl = kwargs.get("second_pl")
        if "event" in kwargs:
            self.__event = kwargs.get("event")

    def get_event(self):
        return self.__event

    def get_team(self):
        return self.__team

    def get_user_id(self):
        return self.__user_id

    def get_user(self):
        return self.__user

    def get_team_id(self):
        return self.__team_id

    def get_first_driver(self):
        return self.__first_driver

    def get_first_pl(self):
        return self.__first_pl

    def get_second_driver(self):
        return self.__second_driver

    def get_second_pl(self):
        return self.__second_pl
