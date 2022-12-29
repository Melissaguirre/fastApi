#Python 
from typing import Optional, List #tipado estático
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

#subir archivos - imágenes y traer la info de la misma
@app.post(
    path = "/post-image"
    )
def post_image(
    image : UploadFile = File(...)
):
    return {
        "FileName" : image.filename, 
        "Format" : image.content_type,
        "Size(kb)" : round(len(image.file.read())/1024, ndigits = 2)  
        #read-> función nativa de python para leer el contenido de un archivo. 
        #len -> envolver todo para contener la cantidad de bytes del archivo
    }
    
    
#Multiples archivos
@app.post(
    path='/post-image2'
)
def post_image(
    images: List[UploadFile] = File(...)
):
    info_images = [{
        "filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    } for image in images]

    return info_images


#Files y forms juntos

@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }