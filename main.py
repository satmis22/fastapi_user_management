from fastapi import FastAPI
from models import User
from database import engine
from typing import Optional
app = FastAPI()

#Endpoints to create a new user

@app.post("/users/")
async def create_user(user: User):

    # Logic to save the user data to the database can be added here.
    # For simplicity, let's assume it's implemented elsewhere.
    # Return the created user data as a response.

    return user



#Endpoint to retrieve user details by user ID

@app.get("/users{user_id}")
async def get_user(user_id: int):
    
    # Logic to fetch the user data to the database based on the user ID can be added here.
    # For simplicity, let's assume it's implemented elsewhere.
    # Return the created user data as a response.

    return {"user_id": user_id, "user_data": "Sample user data"}


#Endpoint to update user details by user ID

@app.patch("/users{user_id}")
async def update_user(user_id: int, user_update: User):
    
    # Logic to fetch the user data to the database based on the user ID can be added here.
    # For simplicity, let's assume it's implemented elsewhere.
    # Return the created user data as a response.

     return {"message": f"User with ID {user_id} updated succesfully", "updated_data": user_update}


#Endpoint to delete a user by user ID

@app.delete("/users{user_id}")
async def delete_user(user_id: int):
    
    # Logic to fetch the user data to the database based on the user ID can be added here.
    # For simplicity, let's assume it's implemented elsewhere.
    # Return the created user data as a response.

    return {"message": f"User with ID {user_id} deleted succesfully"}
