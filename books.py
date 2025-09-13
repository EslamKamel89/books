from typing import Annotated, Optional

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field

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

class BookRequest(BaseModel) :
    id:Optional[int] = Field(description="not required on create" , default=None)
    title:str = Field(min_length=3 , max_length=200) 
    author:str = Field(min_length=3 , max_length=200) 
    description:str = Field(min_length=3 , max_length=200) 
    rating:int = Field(gt=0, le=5) 
    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title" : "A new book" , 
                "author" : "Eslam Kamel" , 
                "description" : "new book description"  , 
                "rating":3,
            }
        }
    }
        
books:list[Book] = [
    Book( 1, "The Silent Patient",  "Alex Michaelides" , 'description 1' , 3),
    Book( 2, "Educated",  "Tara Westover" , 'description 2' , 4),
    Book( 3, "Dune",  "Frank Herbert",  'description 3' , 2),
    Book( 4, "Thinking, Fast and Slow",  "Daniel Kahneman" , 'description 4' , 3),
    Book( 5, "The Hobbit",  "J.R.R. Tolkien" , 'description 5' , 3),
    Book( 6, "Sapiens: A Brief History of Humankind",  "Yuval Noah Harari" , 'description 6' , 5),
    Book( 7, "The Midnight Library",  "Matt Haig" , 'description 7' , 3),
    Book( 8, "Atomic Habits",  "James Clear" , 'description 8' , 2),
    Book( 9, "The Body: A Guide for Occupants",  "Bill Bryson" , 'description 9' , 1),
    Book( 10 , "Pride and Prejudice",  "Jane Austen" , 'description 10' , 4),
    Book( 11 , "The Seven Husbands of Evelyn Hugo",  "Taylor Jenkins Reid" , 'description 11' , 5),
    Book( 12 , "Deep Work",  "Cal Newport" , 'description 12' , 5),
]

@(app.get('/'))
async def  home():
    return {'message' : "Welcome to fastapi books api"}

@(app.get('/books' , response_model=list[BookRequest]))
async def books_index()->list[Book]:
    return books 
@(app.post('/books'))
async def create_books(book_request:BookRequest  ):
    book_dict = book_request.model_dump()
    book_dict['id'] = 1 if len(books) == 0 else books[-1].id+1
    book =  Book(**book_dict)
    books.append(book)
    return book
@app.get('/books/{id}' , response_model=BookRequest , summary="Fetch single book by it's id")
async def get_book_by_id (id:Annotated[int , Path(description="Book id >= 1" , ge=1)]) :
    for book in books :
        if book.id == id :
            return book 
    raise HTTPException(404 , f'There are no book with this id: {id}')
@app.get('/filter-books' , response_model=list[BookRequest]) 

async def filter_books(rating:Annotated[int , Query(description='Book rating [1..5]' , ge=1 , le=5 )]) :
    return [b for b in books if b.rating >= rating]