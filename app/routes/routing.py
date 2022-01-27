from fastapi import APIRouter


router = APIRouter()


@router.get("/check", tags=["Testing"])
def check():
    return {"message": "router running properly"}
    