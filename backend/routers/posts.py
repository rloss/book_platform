from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_posts():
    return {"message": "게시물 목록"}
