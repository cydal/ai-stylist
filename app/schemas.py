from pydantic import BaseModel
from typing import List, Optional

# Schema for user creation
class UserCreate(BaseModel):
    username: str
    style_preferences: Optional[str] = None

# Schema for outputting user data
class User(BaseModel):
    id: int
    username: str
    style_preferences: Optional[str] = None

    class Config:
        orm_mode = True

# Schema for creating a conversation entry
class ConversationCreate(BaseModel):
    user_id: int
    question: str
    answer: str

# Schema for outputting conversation data
class Conversation(BaseModel):
    id: int
    user_id: int
    question: str
    answer: str

    class Config:
        orm_mode = True

# Schema for creating an image entry
class ImageCreate(BaseModel):
    user_id: int
    image_path: str
    tags: Optional[List[str]] = []

# Schema for outputting image data
class Image(BaseModel):
    id: int
    user_id: int
    image_path: str
    tags: List[str]

    class Config:
        orm_mode = True
