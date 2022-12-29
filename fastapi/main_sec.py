#Python 
from typing import Optional #tipado estático
from enum import Enum
#FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path
#Pydantic
from pydantic import BaseModel , Field 


app = FastAPI()


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
    
    
#RESPONSE MODEL         
#con el response_model_exclude, permite que no se vea lo que contiene password para tener seguridad en cuanto a esta  
@app.post("/person/new", response_model=Person, response_model_exclude={'password'}) 
def create_person(person : Person = Body(...)):  #path operation function
    return person

@app.post("/person2/new", response_model=PersonOut) 
def create_person(person : Person = Body(...)):  #path operation function
    return person

