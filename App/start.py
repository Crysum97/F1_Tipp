import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from Database.DBController import *
from App.model.User import User, UserModel
from fastapi.encoders import jsonable_encoder
from typing import Union

app = FastAPI()
app.mount("/static", StaticFiles(directory="../Web"), name="static")


@app.get("/")
def get_root():
    return FileResponse("../Web/login.html")


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


if __name__ == '__main__':
    create_database()
    user = User(name="Hannes", password="HalloWelt", salt="0ec62")
    print(user)
    insert_user(user)
    inserted = read_user(1)
    print(inserted)
    uvicorn.run(app, host="0.0.0.0", port=80)
