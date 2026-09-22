from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, products

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
def read_root():
    return {"message": "Hello, Raj!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": "This is your first API route"}


