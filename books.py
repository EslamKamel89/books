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

@(app.get('/books'))
async def books_index():
    return books 