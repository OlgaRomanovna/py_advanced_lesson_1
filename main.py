from fastapi import FastAPI, Response, status, HTTPException
from starlette.responses import JSONResponse

from models.login import ResponseLogin, LoginData
from models.users import ResponseModel

app = FastAPI()

url = "http://0.0.0.0:8000"


@app.get("/api/users/{user_id}", response_model=ResponseModel)
def get_user(user_id: int):
    users = {
        2: {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg",
        }
    }

    support_info = {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you.",
    }

    user = users.get(user_id)
    if not user:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="{}", media_type="application/json")

    return {
        "data": user,
        "support": support_info,
    }


@app.post("/api/login", response_model=ResponseLogin)
def login(data: LoginData):
    data_login = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    if data.password is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Missing password"}
        )

    if data.password != data_login["password"]:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "user not found"}
        )
    if data.email is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Missing email or username"}
        )

    if data.email == data_login["email"] and data.password == data_login["password"]:
        return {"id": 4, "token": "QpwL5tke4Pnpja7X4"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


