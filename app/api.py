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
from fastapi import FastAPI
from starlette.responses import FileResponse, HTMLResponse
import pandas as pd
#import Model

import datetime
import json

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

