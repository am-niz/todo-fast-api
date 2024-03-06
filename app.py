from fastapi import FastAPI, HTTPException
from pydantic import BaseModel #for creating a model (its an agrement btw user and server which data is acceptable)
from typing import List

app = FastAPI()

# Define your data model using Pydantic
class Todo(BaseModel):
    id: int    
    title: str
    done: bool = False

# Initialize your in-memory database
todos = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Learn Python", "done": False},
    {"id": 3, "title": "elon musk at aluva", "done": True},
]

# List all todos
@app.get("/todos", response_model=List[Todo])
async def todos_get():
    return todos

# Delete a todo by id
@app.delete("/todos/{id_}", status_code=204)
async def todos_id_delete(id_: int):
    global todos
    todos = [todo for todo in todos if todo['id'] != id_]
    return {"message": "Todo deleted"}

# Get a todo by id
@app.get("/todos/{id_}", response_model=Todo)
async def todos_id_get(id_: int):
    todo = next((todo for todo in todos if todo['id'] == id_), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Create a new todo
@app.post("/todos", response_model=Todo, status_code=201)
async def todos_post(todo: Todo):
    new_id = max([todo['id'] for todo in todos]) + 1 if todos else 1
    todo_dict = todo.model_dump()
    todo_dict['id'] = new_id
    todos.append(todo_dict)
    return todo_dict
