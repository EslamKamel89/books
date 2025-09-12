from fastapi import FastAPI

app = FastAPI() 

class Book :
    id: int 
    title:str 
    author:str
    description:str
    rating:int
    def __init__(self , id :int , title:str, author:str , description:str  , rating :int) :
        self.id = id 
        self.title = title 
        self.author = author 
        self.description = description 
        self.rating = rating 
books:list[Book] = []

@(app.get('/'))
async def  home():
    return {'message' : "Welcome to fastapi books api"}

@(app.get('/books'))
async def books_index():
    return books 