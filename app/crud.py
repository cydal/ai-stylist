import os
import random
from pathlib import Path
from sqlalchemy.orm import Session
from . import gemini, models, schemas


IMAGE_DIR = Path(__file__).resolve().parent.parent / "uploaded_images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# User
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, style_preferences=user.style_preferences)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Conversation
def create_conversation(db: Session, conversation: schemas.ConversationCreate):
    db_conversation = models.Conversation(**conversation.dict())
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def get_conversations_by_user(db: Session, user_id: int):
    return db.query(models.Conversation).filter(models.Conversation.user_id == user_id).all()

# Image
def create_image(db: Session, user_id: int, image_path: str, tags: list):
    db_image = models.Image(user_id=user_id, image_path=image_path, tags=tags)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_images_by_user(db: Session, user_id: int):
    return db.query(models.Image).filter(models.Image.user_id == user_id).all()


def save_image_file(user_id: int, image_data: bytes, filename: str) -> str:
    """
    Save an image file to the disk and return the file path.
    """
    file_path = IMAGE_DIR / f"{user_id}_{filename}"
    with open(file_path, "wb") as image_file:
        image_file.write(image_data)
    return str(file_path)


def get_user_style(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        return user.style_preferences
    return None


def get_recent_conversations(db: Session, user_id: int, limit: int = 10):
    return db.query(models.Conversation).filter(models.Conversation.user_id == user_id).order_by(models.Conversation.created_at.desc()).limit(limit).all()


def get_image_tags(db: Session, user_id: int):
    images = db.query(models.Image).filter(models.Image.user_id == user_id).all()
    tags_list = [image.tags for image in images]
    return tags_list

def get_image_tags_with_paths(db: Session, user_id: int):
    images = db.query(models.Image).filter(models.Image.user_id == user_id).all()
    tags_and_paths = [{
        'tags': image.tags,
        'image_path': image.image_path
    } for image in images]
    return tags_and_paths

def ask_fashion_question(prompt: str) -> str:
    """
    Call to Language Model.
    """
    return(gemini.retrieve_response(prompt))


def extract_image_tags(image_path: str) -> dict:
    """
    image tag extraction by randomly selecting tags from predefined categories.
    """
    return(gemini.retrieve_tags(image_path))


def retrieve_style_matching(image_tags: dict) -> str:
    """
    Retrieve Style matching recommendation
    """
    return(gemini.style_matching(image_tags))