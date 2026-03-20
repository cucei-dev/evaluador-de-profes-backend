from fastapi import APIRouter

from app.api.schemas import Info
from app.modules.auth.api.routes import router as auth_router
from app.modules.users.api.routes import router as users_router

router = APIRouter()


@router.get("/", response_model=Info)
async def get_info():
    return Info()

router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(users_router, prefix="/users", tags=["Users"])
