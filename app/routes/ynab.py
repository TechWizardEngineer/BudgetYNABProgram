from importlib.resources import path
import os
import sys

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)))
sys.path.insert(1, ROOT_PATH)

#From Python
from starlette.responses import FileResponse, HTMLResponse
from typing import List,Dict, Optional

# From Pydantic
from pydantic import BaseModel
from pydantic import Field

# From FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Path, Form
from fastapi import APIRouter

import pandas as pd
import datetime
import json
import root
from utils.budget_import import YnabImportProgram


###---------------------------------------------------
## Models
## Space for possible models and make testing
###---------------------------------------------------
class LoginOut(BaseModel):
    username: str = Field(...,max_length=20,example="ynab_kamy")
    message: str = Field(default="Login succesfully!")

###---------------------------------------------------
## Using router to organize app better and run Docker easier
## If router is not used, you can use standard @app.get("/path/")
###---------------------------------------------------
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
@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["default"]
    )
async def home():
    """
    Home

    This path operation shows home

    Parameters:
        -None

    Returns a .html with key info
    """
    return FileResponse('./resources/index.html')

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
@router.get(
    path="/structure_change/run",
    status_code=status.HTTP_200_OK,
    tags=["schema_for_ynab"]
    )
async def make_structure_change() -> Dict[str, str]:
    """
    Structure change of file

    This path operation realize structure change of imported file

    Parameters:
        -None

    Returns a json with the i
        -key (file_name from bank) : value (file_name after structure changed)
    """

    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    return(budget_obj.process_structure_change())

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
@router.get(
    path="/structure_change/detail/{file_id}",
    status_code=status.HTTP_200_OK,
    tags=['schema_for_ynab']
    )
def verify_changed_by_file(
    file_id: str = Path(
    ...,
    title="File name when donwloaded from bank.",
    description="This is the name of the file when downloaded from bank and with extension .txt.",
    example="640-212335-18_76.txt"
    )
) -> str :
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
@router.get(
    path="/encoding/run",
    status_code=status.HTTP_200_OK,
    tags=['files_details']
    )
async def run_encoding() -> Dict[str, str]:
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    return(budget_obj.process_encoding_by_file())

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
@router.get(
    path="/enconding/detail/{file_id}",
    status_code=status.HTTP_200_OK,
    tags=['files_details']
    )
def get_encoding_by_file(file_id: str = Path(
    ...,
    title="File name when donwloaded from bank.",
    description="This is the name of the file when downloaded from bank and with extension .txt.",
    example="640-212335-18_76.txt"
    )
) -> str:
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
@router.get(
    path="/path/data",
    status_code=status.HTTP_200_OK,
    tags=['data_details']
    )
async def get_data_path() -> Dict[str, List[str]]:
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS
    return({'INFO: Getting data from and exporting into': [path_data, path_export]})

###---------------------------------------------------
## Forms
## Making login to test if works and project a vision for it in my app
## Testing Forms
###---------------------------------------------------
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


###---------------------------------------------------
## File, UploadFile and HTTPException
## Making
## Testing File, UploadFile and HTTPException
###---------------------------------------------------

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
