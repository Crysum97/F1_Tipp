import secrets
from App.util.Tools import hash_sha256
from pydantic import BaseModel


class UserModel(BaseModel):
    user_id: int | None = None
    name: str
    password: str
    salt: str


class User:
    __user_id = None
    __name = None
    __password = None
    __salt = None

    def __init__(self, **kwargs):
        self.__user_id = kwargs.get("id", None)
        self.__name = kwargs.get("name", "")
        self.__salt = kwargs.get("salt", secrets.token_hex(3)[:5])
        if "password" in kwargs:
            print((kwargs.get("password") + self.__salt))
            self.__password = hash_sha256((kwargs.get("password") + self.__salt))
        else:
            self.__password = kwargs.get("pass_hash")

    def __dict__(self):
        return {"ID": self.__user_id, "Name": self.__name, "Password": self.__password, "Salt": self.__salt}

    def __str__(self):
        return self.__dict__().__str__()

    def __repr__(self):
        return self.__str__()

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_pass_hash(self):
        return self.__password

    def get_salt(self):
        return self.__salt
