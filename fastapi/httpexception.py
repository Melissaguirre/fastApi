#Python 
from typing import Optional #tipado estático
from enum import Enum

#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Form, Header, Cookie, HTTPException
from fastapi import Body
from fastapi import Query
from fastapi import Path

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr 

app = FastAPI()

persons = [1,2,3,4,5]

#Excepciones sobre status code
@app.get("/person/detail/{person_id}")
def show_person(
    person_id : int = Path(
        ..., 
        gt=0,
        example = 123
        )
): 
    if person_id not in persons:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "This person doesn't exist!"
        )
    #palabra clave de retorno raise
    return {person_id: "It exist"}

