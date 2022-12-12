from fastapi import FastAPI
import uvicorn
from routes import images


#iniciamos FastApi
app = FastAPI()
app.include_router(router=images.router)


if __name__=="__main__":

    #Reload para que el servidor actualice los cambios
    uvicorn.run("main:app",port=8000,reload=True)
