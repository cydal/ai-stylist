from fastapi import APIRouter
from .user import user_router
from .conversation import conversation_router
from .image import image_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(conversation_router, prefix="/conversations", tags=["Conversations"])
router.include_router(image_router, prefix="/images", tags=["Images"])
