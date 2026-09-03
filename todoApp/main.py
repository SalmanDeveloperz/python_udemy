from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, SessionLocal

app= FastAPI()

models.Base.metadata.create_all(bind=engine) # this only run if todos.db not exist

def get_db():
    db=SessionLocal()
    try:
        yield db #yield means the code prior to and including yield statement will executed before sending response

    finally:
        db.close() #this only executed after response has been delivered, make fastAPI quicker, very safe ,close connection in the end

db_dependency= Annotated[Session, Depends(get_db)] #depends is dependency injection really need before we execute behind scenes

@app.get("/")
async def read_all(db:db_dependency):
    return db.query(Todos).all()
