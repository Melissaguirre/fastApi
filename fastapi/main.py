#Python 
from typing import Optional #tipado estático
from enum import Enum
#FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path
#Pydantic
from pydantic import BaseModel , Field 


app = FastAPI()    #instancia que permite que todo el framework funcione, con el constructor se crea un objeto de tipo fastAPI y se guarda dentro de app -> es esta variable la que nos permite correr un proyecto

#Models

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
    

class Person(BaseModel): 
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
    password: str = Field(..., 
        min_length=8)
    
    
    
class PersonOut(BaseModel):
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
    
class Config:
        schema_extra = {
            "example" : {
                "first_name" : "Melissa",
                "last_name" : "Aguirre G",
                "age" : 18,
                "hair_color" : "Castaño claro",
                "is_married" : False
            }
        }
    
#si traemos datos del servidor al cliente utilizamos get
@app.get("/")  #path operation decorator, nos dice que estamos utilizando la operation get en el path "/", es decir el método http get en el endpoint "/"
def home():     #path operation function
    return {"Hello": "World"}   #retorna en formato json

#Request and Response Body

@app.post("/person/new", response_model=PersonOut)   #tipo post ya que vamos a enviar datos desde el cliente al servidor
#este post permitirá crear personas
def create_person(person : Person = Body(...)):  #path operation function
    return person

#validaciones: Query Parameters con parametros automáticos

@app.get("/person/detail")
def show_person(
    name : Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,    #es una validación para que la persona no pueda mandar menos de un caracter, ni más de 50 caracteres
        title ="Person Name",
        description = "This is the person name. It's between 1 and 50 characters",
        example = "Rocío"
        ),
    age : str = Query(
        ...,
        title = "Person age",
        description = "This is the person age. It's required",
        example = 25
        ) #en caso de que esa variable sea obligatoria
):
    return {name: age}  #retorno de un JSON

#Validaciones : Path Parameters con parametros automáticos

@app.get("/person/detail/{person_id}")
def show_person(
    person_id : int = Path(
        ..., 
        gt=0,
        example = 123
        )
): 
    return {person_id: "It exist"}


#Validationes: Request Body con parametros automáticos

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title = "Person ID",
        description = "This is the person ID",
        gt = 0,
        example = "123"
    ),
    person : Person = Body(...), #el body es obligatorio, es lo que nos envía la persona
  #  location : Location = Body(...)
):
  #  return person.dict() | location.dict()
    return person