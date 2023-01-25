""""
Step 2: create a FastAPI "instance"
Step 3: create a path operation
Step 4: define the path operation function
Step 5: return the content
"""

"""
Import FastAPI.
Create an app instance.
Write a path operation decorator (like @app.get("/")).
Write a path operation function (like def root(): ... above).
Run the development server (like uvicorn main:app --reload).
"""
from importlib.resources import path
import os
import sys

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)))
sys.path.insert(1, ROOT_PATH)

#From Python
from starlette.responses import FileResponse, HTMLResponse
from typing import Optional

# From Pydantic
from pydantic import BaseModel
from pydantic import Field

# From FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Path, Body, Form
from fastapi import APIRouter

import pandas as pd
import datetime
import json
import root
from utils.budget_import import YnabImportProgram

## Space for possible models and make testing
# Model to use later
# class FileRestructure(BaseModel):
#     file_id = str = Field(
#         ...,
#         min_length=1,
#         max_length=50,
#         example="640-212335-18_76.txt"
#     )

class LoginOut(BaseModel):
    username: str = Field(...,max_length=20,example="ynab_kamy")
    message: str = Field(default="Login succesfully!")

router = APIRouter()

#create an app instance
app_ynab = FastAPI(title="My Budget Program for YNAB")

###---------------------------------------------------
## Loads the home for the api
## Params:
## None
## returns:
## Home land page
###---------------------------------------------------
#@app_ynab.get("/")
@router.get(
    path="/",
    status_code=status.HTTP_200_OK
    )
async def home():
    return FileResponse('./resources/index.html')

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
#@app_ynab.get("/structure_change/")
@router.get(
    path="/structure_change/run",
    status_code=status.HTTP_200_OK
    )
async def make_structure_change():
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    return(budget_obj.process_structure_change())

#@app_ynab.get("/get-changed-file/{file_id}")
@router.get(
    path="/structure_change/detail/{file_id}",
    status_code=status.HTTP_200_OK
    )
def verify_changed_by_file(
    file_id: str = Path(
    ...,
    title="File name when donwloaded from bank.",
    description="This is the name of the file when downloaded from bank and with extension .txt.",
    example="640-212335-18_76.txt"
    )
):
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(
        root.DIR_DATA_RAW,
        root.DIR_DATA_ANALYTICS)
    dict_transform = budget_obj.process_structure_change()
    return(dict_transform[file_id])

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
#@app_ynab.get("/encoding/")
@router.get(
    path="/encoding/run",
    status_code=status.HTTP_200_OK
    )
async def run_encoding():
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    return(budget_obj.process_encoding_by_file())

#@app_ynab.get("/get-encoding/{file_id}")
@router.get(
    path="/enconding/detail/{file_id}",
    status_code=status.HTTP_200_OK)
def get_encoding_by_file(file_id: str = Path(
    ...,
    title="File name when donwloaded from bank.",
    description="This is the name of the file when downloaded from bank and with extension .txt.",
    example="640-212335-18_76.txt"
    )
):
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    dict_encoding = budget_obj.process_encoding_by_file()
    return(dict_encoding[file_id])


###---------------------------------------------------
## Reading input path (raw data) to execute YNAB Program
## Params:
## None
## returns:
## Home land page
###---------------------------------------------------
#@app_ynab.get("/path-data/")
@router.get(
    path="/path/data",
    status_code=status.HTTP_200_OK)
async def get_data_path():
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS
    return({'INFO: Getting data from and exporting into': [path_data, path_export]})

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------

# Making login to test if works and project a vision for it in my app
# Testing Forms

@router.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK)
def login(
    username: str = Form(...,example="ynab_kamy"),
    password: str = Form(...,example="hisoykamy")
    ):
    print(f"Printing type of LoginOut")
    print(type(LoginOut))

    print(f"\nPrinting type of LoginOut(username=username)")
    print(type(LoginOut(username=username)))

    return LoginOut(username=username)

"""
When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.

So, in OpenAPI, each of the HTTP methods is called an "operation".
We are going to call them "operations" too.
"""

# I should make a BaseModel of importing file

# #write a path decorator, according to operations
# @app_ynab.get("/")
# #write a path operation function
# async def root():
# #write return content
#   return {'message':'Hello World'}

