from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from .. import schemas, crud

conversation_router = APIRouter()

@conversation_router.post("/", response_model=schemas.Conversation)
def add_conversation(user_id: int, question: str, db: Session = Depends(get_db)):
    try:
        # user style information
        user_style = crud.get_user_style(db, user_id=user_id)

        # last 10 conversations
        recent_conversations = crud.get_recent_conversations(db, user_id=user_id, limit=10)

        # Fetch image tags
        image_tags = crud.get_image_tags(db, user_id=user_id)

        # structured input for the language model
        prompt = {
            "question": question,
            "style_info": user_style,
            "recent_conversations": [conv.question + " " + conv.answer for conv in recent_conversations],
            "image_tags": image_tags
        }

        # Call language model
        answer = crud.ask_fashion_question(prompt)

        # Create the conversation in the database
        conversation_data = schemas.ConversationCreate(user_id=user_id, question=question, answer=answer)
        created_conversation = crud.create_conversation(db=db, conversation=conversation_data)

        return created_conversation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@conversation_router.get("/{user_id}")
def get_conversations(user_id: int, db: Session = Depends(get_db)):
    try:
        conversations = crud.get_conversations_by_user(db=db, user_id=user_id)
        return conversations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@conversation_router.get("/match-styles/")
def match_styles(user_id: int, db: Session = Depends(get_db)):
    user_style = crud.get_user_style(db, user_id=user_id)
    image_tags = crud.get_image_tags_with_paths(db, user_id=user_id)

    prompt = {"user_style": user_style, "image_tags": image_tags}
    
    suggested_outfits = crud.retrieve_style_matching(prompt)  # Implement this function to handle the request

    return suggested_outfits