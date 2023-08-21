from fastapi import APIRouter
from app.core.usecases.options_usecase import get_options

router = APIRouter()

@router.get("/options")
async def get_options_controller():
    return await get_options()
