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
#from typing import Optional
from importlib.resources import path
import os
import sys

ROOT_PATH = os.path.dirname(
    (os.sep).join(os.path.abspath(__file__).split(os.sep)))
sys.path.insert(1, ROOT_PATH)

import root

from fastapi import FastAPI
from typing import Optional
from starlette.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import pandas as pd
from budget_program import YnabImportProgram


import datetime
import json

class YNABProgram(BaseModel):
    path_data: str
    path_export: str

#create an app instance
app_ynab = FastAPI(title="My Budget Program for YNAB")

###---------------------------------------------------
## Loads the home for the api
## Params:
## None
## returns:
## Home land page
###---------------------------------------------------
@app_ynab.get("/")
async def read_root():
    return FileResponse('./resources/index.html')

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
@app_ynab.get("/structure_change/")
async def process_structure_change():
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    return(budget_obj.process_structure_change())

@app_ynab.get("/get-changed-file/{file_id}")
def verify_changed_by_file(file_id: str):
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    dict_transform = budget_obj.process_structure_change()
    return(dict_transform[file_id])

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------
@app_ynab.get("/encoding/")
async def process_encoding():
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS

    budget_obj = YnabImportProgram(root.DIR_DATA_RAW,root.DIR_DATA_ANALYTICS)
    return(budget_obj.process_encoding_by_file())

@app_ynab.get("/get-encoding/{file_id}")
def get_encoding_by_file(file_id: str):
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
@app_ynab.get("/path-data/")
async def get_path_data():
    #Unless user change the input path of data AND export path, it will be from root
    path_data= root.DIR_DATA_RAW
    path_export = root.DIR_DATA_ANALYTICS
    return({'INFO: Getting data from and exporting into': [path_data, path_export]})

###---------------------------------------------------
## Creating (POST) input path (raw data) and export path to execute YNAB Program
## Params:
## None
## returns:
## Home land page
###---------------------------------------------------
# @app_ynab.post("/create-paths/")
# async def create_paths(trial_path_data: str, trial_path_export: str):
#     #Unless user change the input path of data AND export path, it will be from root
#     if trial_path_data == root.DIR_DATA_RAW and trial_path_export == root.DIR_DATA_ANALYTICS:
#         return {"Error":"This input and export path have been used before"}
#     else:
#         path_data = trial_path_data
#         path_export = trial_path_export

#     return({'path_data': path_data, 'path_export':path_export})

###---------------------------------------------------
## XXX
## Params:
## XXX
## returns:
## XXX
###---------------------------------------------------

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

