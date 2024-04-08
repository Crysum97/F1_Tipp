import secrets

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from hashlib import sha256

from Database.DBController import *
from App.model.User import User, UserModel
from App.model.Bet import Bet, BetModel
from fastapi.encoders import jsonable_encoder
from typing import Union

app = FastAPI()
app.mount("/static", StaticFiles(directory="../Web"), name="static")


@app.get("/")
def get_root():
    return FileResponse("../Web/login/login.html")


@app.get("/bets")
def get_betting_page():
    return FileResponse("../Web/index/index.html")


@app.get("/register")
def get_register_page():
    return FileResponse("../Web/Register/registration_form.html")


@app.get("/usersetting")
def get_settings_page():
    return FileResponse("../Web/settings/settings.html")


@app.get("/auth")
def auth_user(name: str, sha256_hash: str):
    c_user = read_user_by_name(name)
    if c_user is not None and c_user.get_pass_hash() == sha256_hash:
        c_user.reauth()
        reauth_user(c_user)
        key = sha256((c_user.get_pass_hash() + str(c_user.get_last_login())).encode('utf-8')).hexdigest()
        return JSONResponse(content={'key': key})
    else:
        return 500


@app.get("/auth/{username}")
def check_auth_key(username: str, auth_key: str):
    c_user = read_user_by_name(username)
    key = sha256((c_user.get_pass_hash() + str(c_user.get_last_login())).encode('utf-8')).hexdigest()
    if key == auth_key:
        return JSONResponse(status_code=200, content={"auth": "OK"})
    else:
        return JSONResponse(status_code=404, content={"auth": "FAIL"})


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
            raise HTTPException(status_code=404, detail="user not found")
    else:
        result = read_user_by_name(user_info)
        if result is not None:
            return result.__dict__()
        else:
            raise HTTPException(status_code=404, detail="user not found")


@app.post("/user")
def post_user_entry(user_model: UserModel):
    insert_user(User(name=user_model.name, pass_hash=user_model.pass_hash, salt=user_model.salt))
    return JSONResponse(content=read_user_by_name(user_model.name).__dict__())


@app.get("/salt")
def generate_salt():
    salt = secrets.token_hex(3)[:5]
    return {"salt": salt}


@app.delete("/user/{user_id}")
def delete_user_entry(user_id):
    return delete_user(user_id)


@app.get("/team")
def get_all_teams():
    return {"teams": read_teams()}


@app.get("/driver/{team_id}")
def get_drivers(team_id: int):
    return {"drivers": read_driver_by_team_id(team_id)}


@app.get("/bet")
def get_bets():
    return {"bets": read_bets()}


@app.post("/insertbet")
def inser_bet(bet_model: BetModel):
    user_id = read_user_by_name(bet_model.user).get_id()
    team_id = read_team_by_name(bet_model.team).get_id()
    number_of_driver = count_drivers()
    first = int(bet_model.first_pl)
    second = int(bet_model.second_pl)
    len_first = len(str(bet_model.first_pl))
    len_second = len(str(bet_model.second_pl))
    if (len_first <= 2 and len_second <= 2) and (first <= number_of_driver and second <= number_of_driver):
        insert_bet(Bet(user_id=user_id, team_id=team_id, first_driver=bet_model.first_driver, first_pl=bet_model.first_pl,
                    second_driver=bet_model.second_driver, second_pl=bet_model.second_pl))
    else:
        print("false input")



if __name__ == '__main__':
    create_database()
    user = User(name="Admin", password="admin")
    #bet = Bet(user_id=1, team_id=3, first_driver="Charles Sainz", second_driver="Carlos Leclerc", first_pl=1, second_pl=4)
    insert_user(user)
    #insert_bet(bet)
    uvicorn.run(app, host="0.0.0.0", port=80)
