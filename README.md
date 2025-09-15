# 📚 FastAPI Books API: Where Books Go to Die (or Get Updated)

> _“I didn’t choose the FastAPI life. The FastAPI life chose me… after I accidentally deleted my entire bookshelf with a DELETE request.”_

Welcome to **FastAPI Books API** — the only RESTful service where your favorite novels are stored in memory (aka “the cloud” if you squint really hard) and can be manipulated like digital puppets.

No database? No problem.  
Just pure Python, a list of books, and the unshakable belief that 12 books is a _massive_ library.

---

## 🧠 What Is This?

A **FastAPI** playground built by someone who:

- Thought `Book` should be a class (not a dict)
- Refused to use an ORM because “I want to feel the pain”
- Wrote `published_date=1991` for a book about quantum physics and called it “historical accuracy”

This API lets you:

- ✅ List all books (even the ones with 1-star ratings)
- ✅ Create new books (with fictional dates like 2030 — time travel is real here)
- ✅ Read single books (because sometimes you just need to know if _The Hobbit_ is still alive)
- ✅ Filter by rating (only show books rated ≥4… because we’re elitist)
- ✅ Update books (turn “The Silent Patient” into “The Loud Patient” — your call)
- ✅ Delete books (RIP _Atomic Habits_, you were too good for this world)

---

## 📖 Sample Books in Our “Database”

| ID  | Title                             | Author              | Rating | Published Date | Why It’s Still Here                                            |
| --- | --------------------------------- | ------------------- | ------ | -------------- | -------------------------------------------------------------- |
| 1   | The Silent Patient                | Alex Michaelides    | 3      | 1997           | Still waiting for its sequel                                   |
| 2   | Educated                          | Tara Westover       | 4      | 2021           | We cried. We read it twice.                                    |
| 3   | Dune                              | Frank Herbert       | 2      | 2022           | Someone thought this was a romance novel                       |
| 4   | Thinking, Fast and Slow           | Daniel Kahneman     | 3      | 2026           | Time-traveling psychology                                      |
| 5   | The Hobbit                        | J.R.R. Tolkien      | 3      | 2020           | Still better than the movie                                    |
| 6   | Sapiens                           | Yuval Noah Harari   | 5      | 1997           | We all became philosophers after this                          |
| 7   | The Midnight Library              | Matt Haig           | 3      | 1998           | “What if I’d chosen differently?” — same question as my career |
| 8   | Atomic Habits                     | James Clear         | 2      | 1993           | We all tried. We failed.                                       |
| 9   | The Body: A Guide for Occupants   | Bill Bryson         | 1      | 1991           | We’re not sure what this even is                               |
| 10  | Pride and Prejudice               | Jane Austen         | 4      | 1994           | Still the OG dating app                                        |
| 11  | The Seven Husbands of Evelyn Hugo | Taylor Jenkins Reid | 5      | 1995           | We all shipped her with #HusbandNumberFour                     |
| 12  | Deep Work                         | Cal Newport         | 5      | 1997           | We pretend we do deep work                                     |

> 💡 Pro Tip: All dates are fictional except the one where you realize you’ve been reading for 3 hours straight.

---

## 🚀 How to Use

### Prerequisites

- Python 3.9+
- A heart full of hope
- A soul ready for `pip install fastapi uvicorn`

### Run It

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then go to:  
👉 [http://localhost:8000](http://localhost:8000)  
_(Yes, it says “Welcome to fastapi books api”. We didn’t write poetry.)_

### Swagger UI (Because We Like Pretty Things)

Go to:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)  
You’ll see beautiful interactive docs.  
We even added examples so you don’t have to guess what `rating=6` does.  
_(Spoiler: It doesn’t. We made it 1–5. You’re not special.)_

---

## 🛠️ Endpoints (AKA The Real Magic)

| Method | Endpoint                    | What It Does                                                        |
| ------ | --------------------------- | ------------------------------------------------------------------- |
| GET    | `/`                         | Says hi. Very politely.                                             |
| GET    | `/books`                    | Lists all books. Even the bad ones.                                 |
| POST   | `/books`                    | Adds a new book. Auto-generates ID. No ID? No problem.              |
| GET    | `/books/{id}`               | Fetches a single book. If it exists. Otherwise: 404 sadness.        |
| GET    | `/filter-books?rating=4`    | Shows only books rated ≥ your standards.                            |
| GET    | `/books-publish/?year=2020` | Finds books published in a year. Yes, even 1991.                    |
| PUT    | `/books/{id}`               | Updates a book. Change the title? Sure. Change the author? Go wild. |
| DELETE | `/books/{id}`               | Deletes a book. Forever. No undo. No mercy.                         |

> ⚠️ Warning: Deleting a book is permanent. Unless you have a backup. Or a conscience.

---

## 🤖 Why This Project Exists

1. To learn FastAPI without using a database (and lie to myself that it’s “lightweight”).
2. To prove that `Pydantic` is the real MVP.
3. To make `@app.get('/books-publish/')` exist because I thought it sounded cool.
4. To test whether anyone notices that `published_date=1991` for _The Body: A Guide for Occupants_ is actually correct.  
   _(It is. Bill Bryson wrote it in 1991. We’re not lying.)_

---

## 🐞 Known Issues / “Features”

- ❌ No persistence. Restart the server? Your 1-star review of _The Hobbit_ vanishes.
- ❌ No authentication. Anyone can delete your favorite book. Welcome to the wild west.
- ❌ `Book.from_dict()` has a typo: `date['published_date']` → should be `data`.  
  _(But hey, it works because we never use it. So… feature?)_
- ✅ But the Swagger UI looks _so good_. That counts for something, right?

---

## 🏆 Awards Won

- 🥇 **Most Likely to Be Used Once and Never Again**
- 🥈 **Best Use of `Annotated[int, Path(...)]` in a Personal Project**
- 🥉 **Most Dramatic 404 Error Message**:
  > _“There are no book with this id: 999”_  
  > _(Grammar? Who needs it when you’re emotionally invested in a fictional bookshelf?)_

---

## 🙏 Acknowledgements

- FastAPI — for making APIs feel like magic instead of trauma.
- Pydantic — for being the reason I stopped writing raw JSON.
- My cat — for sitting on my keyboard while I debugged `Book.from_dict`.
- My future self — for wondering why I didn’t just use PostgreSQL.

---

## 📣 Final Words

This isn’t production-grade.  
This isn’t scalable.  
This might crash if you add 13 books.  
_(We haven’t tested that.)_

But it’s **mine**.  
And it runs.  
And it has _The Seven Husbands of Evelyn Hugo_.  
So… mission accomplished.

🚀 **Star this repo if you also believe that books should be APIs.**

---

_Made with ❤️, caffeine, and zero databases._  
— Eslam Kamel (author of this README, not any of the books... yet)

---
