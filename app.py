# external modules import
import os
import json
import openai
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

# app shutdown operations
@app.on_event('shutdown')
async def shutdown_event():

    # db connection closing
    app.db.client.close()


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
        users_skills[current_user.name] = UserSkills(
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

@app.post('/find_contributors')
async def find_contributors(project_description: str) -> dict[str, list[str]]:

    # user skills fetching
    users_skills = await get_users_skills()

    # prompt construction
    prompt = [
        {
            'role': 'user', 
            'content': f"These are the users of our platform: {users_skills}. \
                         Which one among them has the best skills for this project: {project_description}? \
                         Return just names and skills of the the three best entries in the same json format."
        }
    ]

    # invoke openapi endpoint
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=prompt)

    # response post-processing
    response = response.choices[0].message.content
    response = json.loads(response[response.find('{'):])
    # response = {k: UserSkills(**v) for k, v in response.items()}
    response = {'recommended_contributors': [name for name in response.keys()]}


    # return the response
    return response
