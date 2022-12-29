#Python 
from typing import Optional #tipado estático
from enum import Enum

#FastApi
from fastapi import FastAPI
from fastapi import status
from fastapi import Form, Header, Cookie, File, UploadFile
from fastapi import Body
from fastapi import Query
from fastapi import Path

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr 


app = FastAPI()


@app.post(
    path = "/post-image"
    )
def post_image(
    image : UploadFile = File(...)
):
    return {
        "FileName" : image.filename, 
        "Format" : image.content_type,
        "Size(kb)" : len(image.file.read())  
        #read-> función nativa de python para leer el contenido de un archivo. 
        #len -> envolver todo para contener la cantidad de bytes del archivo
    }