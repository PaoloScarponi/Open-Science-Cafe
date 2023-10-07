# external modules import
from pydantic import BaseModel, confloat

# internal modules import
from ..enumerates import UserRole, UserStatus, CommType

# class definition
class User(BaseModel):
    
    # editable mandatory fields
    nickname: str                       
    password: str                       
    name: str                           
    surname: str                        
    email: str                          
    phone_number: str                   
    role: list[UserRole | None] = [UserRole.SURFER, None]                           
    newsletter_subscription: bool = False

    # editable non-mandatory fields
    photo: str | None = None 
    video_presentation: str | None = None      
    spoken_languages: list[str] | None = None  
    curriculum_vitae: str | None = None        
    linkedin_profile: str | None = None              
    preferred_communication: CommType | None = None
    interests_skills: list[str] | None = None


    # non-editable fields
    date_of_registration: str                            
    registration_status: UserStatus = UserStatus.PENDING
    contributed_projects: list[dict] | None = None            
    created_projects: list[str] | None = None                 
    contributor_level: confloat(ge=0.0, le=5.0) | None = None  
    creator_level: confloat(ge=0.0, le=5.0)     | None = None  
