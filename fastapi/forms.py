#Python 
from typing import Optional #tipado estático
from enum import Enum
#FastApi
from fastapi import FastAPI, status, Form
    

from fastapi import Body, Query, Path
#Pydantic
from pydantic import BaseModel , Field 

app = FastAPI()

#Modelos
class loginOut(BaseModel):
    username : str = Field(
        ...,
        max_length = 20,
        example = "Juelita2021")
    message : str = Field(default = "Login Successfully!")


#Tipo formulario
@app.post(
    path = "/login",
    response_model= loginOut,
    status_code = status.HTTP_200_OK
    )
def login(username: str = Form(...), password : str = Form(...)):
    return loginOut(username = username) #instanciar la clase para poder que se convierta en formato JSON