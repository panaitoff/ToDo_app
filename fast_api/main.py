from fastapi import FastAPI, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from comments import models, views

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the comments API"}

@app.get("/comments/")
def get_comments(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return views.get_all_comments()
