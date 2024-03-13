import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from hashlib import sha256

from Database.DBController import *
from App.model.User import User, UserModel
from fastapi.encoders import jsonable_encoder
from typing import Union

app = FastAPI()
app.mount("/static", StaticFiles(directory="../Web"), name="static")


@app.get("/")
def get_root():
    return FileResponse("../Web/login.html")


@app.get("/bets")
def get_betting_page():
    return FileResponse("../Web/index.html")


@app.get("/auth")
def auth_user(name: str, sha256_hash: str):
    print(name + " " + sha256_hash)
    c_user = read_user_by_name(name)
    if c_user is not None and c_user.get_pass_hash() == sha256_hash:
        c_user.reauth()
        reauth_user(c_user)
        key = sha256((c_user.get_pass_hash() + str(c_user.get_last_login())).encode('utf-8')).hexdigest()
        return JSONResponse(content={'key': key})
    else:
        return 500


@app.get("/user")
def get_all_user_entries():
    return jsonable_encoder(read_all_users())


@app.get("/user/{user_info}")
def get_user_entry(user_info: Union[int, str]):
    if user_info.isdigit():
        result = read_user(user_info)
        if result is not None:
            return result.__dict__()
        else:
            return {}
    else:
        result = read_user_by_name(user_info)
        if result is not None:
            return result.__dict__()
        else:
            return {}


@app.post("/user")
def post_user_entry(user_model: UserModel):
    insert_user(User(name=user_model.name, password=user_model.password, salt=user_model.salt))
    return JSONResponse(content=read_user_by_name(user_model.name).__dict__())


@app.delete("/user/{user_id}")
def delete_user_entry(user_id):
    return delete_user(user_id)


@app.get("/team")
def get_all_teams():
    return {"teams": read_teams()}


if __name__ == '__main__':
    create_database()
    user = User(name="Admin", password="admin", salt="0ec62")
    insert_user(user)
    uvicorn.run(app, host="0.0.0.0", port=80)
