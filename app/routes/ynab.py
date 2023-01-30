from importlib.resources import path
import os
import sys
import shutil

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
from fastapi import HTTPException
from fastapi import Path, Form, UploadFile, File
from fastapi import APIRouter
from fastapi.responses import FileResponse

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
    tags=["Home"]
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
    tags=["files_structure_change"]
    )
async def make_structure_change():
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
    return(budget_obj.process_files_structure_change())

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
    tags=["files_structure_change"]
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
    dict_transform = budget_obj.process_files_structure_change()
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
    tags=["files_encoding"]
    )
async def run_encoding():
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
    tags=["files_encoding"]
    )
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
@router.get(
    path="/path/data",
    status_code=status.HTTP_200_OK,
    tags=["files_path"]
    )
async def get_data_path():
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
    status_code=status.HTTP_200_OK,
    tags=["test_login"])
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
## Making get_upload file to copy file into raw and verify content
## Using File, UploadFile and HTTPException when the content is not right
###---------------------------------------------------
@router.post(
    path="/get-uploadfile",
    status_code=status.HTTP_200_OK,
    tags=["upload_file"]
    )
async def get_uploadfile(
    upload_file: UploadFile = File(...)
    ):
    # Adding verification of file
    if upload_file.content_type not in ["text/plain"]:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Invalid document type, the format correct is .csv from bank")
    else:
        try:
            upload_file_name = upload_file.filename
            upload_file_format = upload_file.content_type
            upload_file_size = round(len(upload_file.file.read())/1024)
        except Exception:
            return {"message": "There was an error uploading the file"}

    return {
        "Filename" : upload_file_name,
        "Format" : upload_file_format,
        "Size (kb)": upload_file_size
    }

###---------------------------------------------------
## File, UploadFile and HTTPException
## Making get_upload file to copy file into raw and verify content
## Using File, UploadFile and HTTPException when the content is not right
###---------------------------------------------------
@router.post(
    path="/process-uploadfile",
    status_code=status.HTTP_200_OK,
    tags=["upload_file"]
    )
async def process_uploadfile(
    upload_file: UploadFile = File(...)
    ):

    # Adding verification of file
    if upload_file.content_type not in ["text/plain"]:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="Invalid document type, the format correct is .csv from bank")
    else:
        try:
            #Getting file
            file_destination = root.DIR_DATA_TEST_RAW + upload_file.filename
            with open(file_destination, "wb") as file_object:
                shutil.copyfileobj(upload_file.file,file_object)
                print(f"Copying was correct file '{upload_file.filename}' saved at '{file_destination}")

            ## Process from file
            df_load = pd.read_csv(
                file_destination,
                sep="\t",
                encoding="ISO-8859-1")
            #print(df_load.info())

            #//TODO Fix Adding structural change for a single file

            filename=str(upload_file.filename.split(".")[0])+"_change.csv"
            df_load.to_csv(root.DIR_DATA_TEST_ANALYTICS+filename)

        except Exception:
            return{"Exception":"File in data/test/raw could not be processed"}

    return FileResponse(
        path=root.DIR_DATA_TEST_ANALYTICS+filename,
        filename=filename,
        media_type="text/csv")
