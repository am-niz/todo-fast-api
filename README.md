# todo-fast-api
It is a ToDo app created with fast API

# FastAPI Todo Application

This is a simple Todo application built with FastAPI, demonstrating the creation of RESTful APIs with basic CRUD (Create, Read, Update, Delete) operations. The application uses an in-memory list to store todo items, making it simple to understand and easy to run without the need for external databases.

## Features

- List all todos
- Get a specific todo by ID
- Create new todos
- Delete todos

## Requirements

- Python 3.6+
- FastAPI
- Uvicorn

## Installation & Running the App

First, clone this repository to your local machine:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd <project-directory>
```

It's recommended to create a virtual environment for Python projects. Run:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install fastapi uvicorn
```

To start the server, run:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables hot reloading during development.

## API Endpoints

Below are the available API endpoints and their descriptions:

- `GET /todos` - Retrieve a list of all todo items.
- `GET /todos/{id_}` - Retrieve a specific todo item by its `id`.
- `POST /todos` - Create a new todo item. The body should contain the `title` and optionally the `done` status.
- `DELETE /todos/{id_}` - Delete a specific todo item by its `id`.
