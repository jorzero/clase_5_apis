from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="APIs en clase de Mlops 5",
    version="0.0.1"
)

users = {
    "hola43443": {
        "username": "napster",
        "name": "gabo"
    },
    "ide-67": {
        "username": "andrey",
        "name": "gabo"
    }
}


@app.post("/api/v1//users/")
async def create_user(username: str, name: str):
    return {
        "username": username,
        "name": name,
        "id": str(uuid.uuid4()),
        "message": "The user was created successfully",
        "status_code": 201
    }


@app.get("/api/v1//{user_ID}")
async def get_user(user_id: str):
    if user_id in users:
        user = users[user_id]
        return JSONResponse(
            content=user,
            status_code= status.HTTP_200_OK
        )
    else:
        return JSONResponse(
        content="no existe el usuario",
        status_code=status.HTTP_404_NOT_FOUND
        )