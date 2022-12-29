#Python 
from typing import Optional #tipado estático
from enum import Enum

#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Form, Header, Cookie
from fastapi import Body
from fastapi import Query
from fastapi import Path

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr 

app = FastAPI()

#Modelos
class loginOut(BaseModel):
    username : str = Field(
        ...,
        max_length = 20,
        example = "Juelita2021")
    message : str = Field(default = "Login Successfully!")


#cookies and headers parameters
@app.post(
    path = "/contact",
    status_code = status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length = 20,
        min_length = 1
    ), 
    email : EmailStr = Form(...),
    message : str = Form(
        ...,
        min_length = 20
    ),
    #parametros de header y cookies
    user_agent : Optional[str] = Header(default=None),
    ads : Optional[str] = Cookie(default = None)
):
    return user_agent