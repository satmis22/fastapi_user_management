# FastAPI User Management Project

## Step 1: Project Setup and Environment Configuration

### 1.1. Setting up the Project Directory:

   - **Description**: Create a new directory for the FastAPI project and navigate into it.
   
   - **Commands**:
     ```
     mkdir fastapi_user_management
     cd fastapi_user_management
     ```

### 1.2. Installing Dependencies:

   - **Description**: Install necessary dependencies including FastAPI, SQLAlchemy, SQLModel, and Alembic.
   
   - **Command**:
     ```
     pip install fastapi[all] sqlalchemy sqlmodel alembic
     ```

### 1.3. Configuring Database Connection:

   - **Description**: Configure a SQLite database connection for the project.
   
   - **File**: `database.py`
   
   - **Content**:
     ```python
     from sqlalchemy import create_engine
     from sqlalchemy.ext.declarative import declarative_base
     from sqlalchemy.orm import sessionmaker

     SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

     engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

     Base = declarative_base()
     ```

### 1.4. Setting up the FastAPI App:

   - **Description**: Create a FastAPI application file and define the basic structure of the application.
   
   - **File**: `main.py`
   
   - **Content**:
     ```python
     from fastapi import FastAPI
     from database import engine

     app = FastAPI()

     @app.get("/")
     async def root():
         return {"message": "Hello World"}
     ```

### 1.5. Running the FastAPI App:

   - **Description**: Run the FastAPI application using Uvicorn server.
   
   - **Command**:
     ```
     uvicorn main:app --reload
     ```

   - **Access the Application**: Open a web browser and go to `http://127.0.0.1:8000/` to see the "Hello World" message, indicating that the FastAPI application is running successfully.
