#Python 
from typing import Optional #tipado estático
from enum import Enum
#FastApi
from fastapi import FastAPI, status
from fastapi import Body, Query, Path
#Pydantic
from pydantic import BaseModel , Field 

app = FastAPI()


#MODELS
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    yellow = "yellow"
    blonde = "blode"
    red = "red"
    

class Location(BaseModel):
    city : str
    state : str
    country : str
    
class Personbase(BaseModel):
    first_name : str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example = "Julieta"
        )
    last_name : str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example = "Torres"
    )
    age : int = Field(
        ...,
        gt = 0,
        le = 115,
        example = 25
    )
    
    hair_color : Optional[HairColor]  = Field(default = None, example = "black") #esto nos asegura que se ingrese los colores que si o sí estén en la clase
    is_married : Optional[bool] = Field(default = None, example = False)

class Person(Personbase): 
    password: str = Field(..., 
        min_length=8)
  
class PersonOut(Personbase):
    pass

@app.get(
    path = "/", 
    status_code = status.HTTP_200_OK)
def home(): 
    return {"Hello": "World"}  


@app.post(
    path = "/person/new", 
    response_model=PersonOut, 
    status_code = status.HTTP_201_CREATED,  # 201 de que ha sido creado
    tags = ["Persons"] #ordenar las path correspondientes
    )
def create_person(person : Person = Body(...)): 
    return person


@app.get(
    path = "/person/detail",
    status_code = status.HTTP_200_OK,    # 200 de que sale OK
    tags = ["Persons"]
    )
def show_person(
    name : Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50, 
        title ="Person Name",
        description = "This is the person name. It's between 1 and 50 characters",
        example = "Rocío"
        ),
    age : str = Query(
        ...,
        title = "Person age",
        description = "This is the person age. It's required",
        example = 25
        )
):
    return {name: age}  


#---------------------------------------------------------
#Validaciones : Path Parameters con parametros automáticos

@app.get(
    path = "/person/detail/{person_id}", 
    status_code = status.HTTP_200_OK,
    tags = ["Persons"]
    )
def show_person(
    person_id : int = Path(
        ..., 
        gt=0,
        example = 123
        )
): 
    return {person_id: "It exist"}


#-----------------------------------------------------------
#Validationes: Request Body con parametros automáticos

@app.put(
    path = "/person/{person_id}",
    status_code = status.HTTP_202_ACCEPTED,
    tags = ["Persons"]
    )
def update_person(
    person_id: int = Path(
        ...,
        title = "Person ID",
        description = "This is the person ID",
        gt = 0,
        example = "123"
    ),
    person : Person = Body(...), 
):
    return person