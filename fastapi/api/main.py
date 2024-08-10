from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.middleware(CORSMiddleware,
               allow_origins=['http://localhost:3000'],
               allow_credentials=True,
               allow_methods=['*'],
               allow_headers=['*']
               )
@app.get("/")
def read():
    return 'hello world'