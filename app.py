# external modules import
import os
import json
import openai
from pathlib import Path
from datetime import date
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi import FastAPI, HTTPException

# internal modules import
from modules import User, Project, UserSkills, ProjectInfo


# app object creation
app = FastAPI()


# app startup operations
@app.on_event('startup')
async def startup_event():

    # environment variables loading and creation (for local execution, it requires a .env file in the main project folder)
    load_dotenv()

    # db connection creation
    client = MongoClient(os.getenv("MONGO_URI"))
    app.db = client['open-science-cafe']
    app.users =  app.db['users']
    app.projects = app.db['projects']

    # openai configuration
    openai.api_key = os.getenv("OPENAI_API_KEY")


# endpoints
@app.get("/get_user/{user_id}")
async def get_user(user_id: str) -> User | None:
    try:
        user_data = app.users.find_one({"_id": ObjectId(user_id)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
    if user_data is None:
            raise HTTPException(status_code=404, detail="User Not Found")

    return user_data

@app.get("/get_project/{project_id}")
async def get_project(project_id: str) -> Project | None:
    try:
        project_data = app.projects.find_one({"_id": ObjectId(project_id)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
    if project_data is None:
            raise HTTPException(status_code=404, detail="User Not Found")

    return project_data

@app.get('/get_users_skills')
async def get_users_skills() -> dict[str, UserSkills]:

    # initializing output dictionary
    users_skills = {}

    # conversation history retrival
    for user_record in app.users.find():
        current_user = User(**user_record)
        users_skills[current_user.nickname] = UserSkills(
             skills=current_user.interests_skills
             )

    return users_skills

@app.get('/get_projects_info')
async def get_projects_info() -> dict[str, ProjectInfo]:

    # initializing output dictionary
    projects_info = {}

    # conversation history retrival
    for project_record in app.projects.find():
        current_project = Project(**project_record)
        projects_info[current_project.title] = ProjectInfo(
             description=current_project.description, 
             keywords=current_project.keywords
             )

    return projects_info
