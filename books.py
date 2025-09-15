from typing import Annotated, Optional, Self

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI() 

class Book :
    id: int 
    title:str 
    author:str 
    description:str
    rating:int 
    published_date:int
    def __init__(self , id :int , title:str, author:str , description:str  , rating :int , published_date:int) :
        self.id = id 
        self.title = title 
        self.author = author 
        self.description = description 
        self.rating = rating
        self.published_date = published_date
    @classmethod
    def from_dict( cls ,  data:dict[str, str | int]) ->Self :
        return Book(id=data['id'] ,title=data['title'] , author=data['author'] ,description=data['description'] ,rating=data['rating'] , published_date=date['published_date']) # type: ignore

class BookRequest(BaseModel) :
    id:Optional[int] = Field(description="not required on create" , default=None)
    title:str = Field(min_length=3 , max_length=200) 
    author:str = Field(min_length=3 , max_length=200) 
    description:str = Field(min_length=3 , max_length=200) 
    rating:int = Field(gt=0, le=5) 
    published_date:int = Field(gt=1999 , lt=2031)
    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title" : "A new book" , 
                "author" : "Eslam Kamel" , 
                "description" : "new book description"  , 
                "rating":3,
                "published_date" : 2025,
            }
        }
    }
        
books:list[Book] = [
    Book( 1, "The Silent Patient",  "Alex Michaelides" , 'description 1' , 3 , 1997),
    Book( 2, "Educated",  "Tara Westover" , 'description 2' , 4 , 2021),
    Book( 3, "Dune",  "Frank Herbert",  'description 3' , 2 , 2022),
    Book( 4, "Thinking, Fast and Slow",  "Daniel Kahneman" , 'description 4' , 3 , 2026),
    Book( 5, "The Hobbit",  "J.R.R. Tolkien" , 'description 5' , 3 , 2020),
    Book( 6, "Sapiens: A Brief History of Humankind",  "Yuval Noah Harari" , 'description 6' , 5 , 1997),
    Book( 7, "The Midnight Library",  "Matt Haig" , 'description 7' , 3 , 1998),
    Book( 8, "Atomic Habits",  "James Clear" , 'description 8' , 2 , 1993),
    Book( 9, "The Body: A Guide for Occupants",  "Bill Bryson" , 'description 9' , 1 , 1991),
    Book( 10 , "Pride and Prejudice",  "Jane Austen" , 'description 10' , 4 , 1994),
    Book( 11 , "The Seven Husbands of Evelyn Hugo",  "Taylor Jenkins Reid" , 'description 11' , 5 , 1995),
    Book( 12 , "Deep Work",  "Cal Newport" , 'description 12' , 5 , 1997),
]

@(app.get('/' , status_code=status.HTTP_200_OK))
async def  home():
    return {'message' : "Welcome to fastapi books api"}

@(app.get('/books' , response_model=list[BookRequest] , status_code=status.HTTP_200_OK))
async def books_index()->list[Book]:
    return books 

@(app.post('/books'))
async def create_books(book_request:BookRequest  ):
    book_dict = book_request.model_dump()
    book_dict['id'] = 1 if len(books) == 0 else books[-1].id+1
    book =  Book(**book_dict)
    books.append(book)
    return book

@app.get('/books/{id}' , response_model=BookRequest , summary="Fetch single book by it's id" , status_code=status.HTTP_200_OK)
async def get_book_by_id (id:Annotated[int , Path(description="Book id >= 1" , ge=1)]) :
    for book in books :
        if book.id == id :
            return book 
    raise HTTPException(status.HTTP_404_NOT_FOUND , f'There are no book with this id: {id}')

@app.get('/filter-books' , response_model=list[BookRequest] , status_code=status.HTTP_200_OK) 
async def filter_books(rating:Annotated[int , Query(description='Book rating [1..5]' , ge=1 , le=5 )]) :
    return [b for b in books if b.rating >= rating]

@app.get('/books-publish/' , status_code=status.HTTP_200_OK)
async def read_books_by_published_date(year:int):
    result: list[Book] = []
    for book in books :
        if book.published_date   == year :
            result.append(book)
    return result 

@app.put('/books/{id}' , response_model=BookRequest , status_code=status.HTTP_201_CREATED)
async def update_book(id:Annotated[int , Path(ge=1 , description="the book id must be >= 1")] , book : BookRequest) :
    for i ,b in enumerate(books) :
        if b.id == id :
            book_data = book.model_dump()
            book_data['id'] = id 
            books[i] = Book.from_dict(book_data)
            return books[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Book not found")

@app.delete('/books/{id}' , response_model=None , status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id : Annotated[int , Path(ge=1 , description="book id must be >= 1")]):
    for i , book in enumerate(books) : 
        if book.id == id :
            books.pop(i)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Book not found")