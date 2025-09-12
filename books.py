from fastapi import FastAPI

app = FastAPI() 

@(app.get('/'))
async def  home():
    return {'message' : "Welcome to fastapi books api"}